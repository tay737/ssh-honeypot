# SSH Honeypot — Daily Threat Reports

![status: archived](https://img.shields.io/badge/status-archived-8B949E?style=flat-square)
![reports: 11 days](https://img.shields.io/badge/reports-11%20days-7AA2F7?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=flat-square&logo=influxdb&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

> [!WARNING]
> **Archived — the project has ended.** This repository is a frozen record of the first honeypot deployment (15–25 September 2026) and is read-only. A rebuilt honeypot is in progress; this one is kept as-is for its data and its pipeline design.

A chronological archive of SSH brute-force activity observed by an internet-facing honeypot, published as one Markdown report per UTC day.

---

## Contents

- [What this is](#what-this-is)
- [Why it existed](#why-it-existed)
- [Results](#results)
- [Architecture](#architecture)
- [Components](#components)
- [Data model](#data-model)
- [Report anatomy](#report-anatomy)
- [Running it yourself](#running-it-yourself)
- [Limitations](#limitations)
- [Repository layout](#repository-layout)
- [Disclaimer](#disclaimer)

---

## What this is

An SSH service exposed to the internet collects failed authentication attempts. Each attempt is enriched with geolocation and network-ownership data, stored as a time series, visualised in Grafana, and once a day transformed into a Markdown report that is committed here.

Two things are produced:

1. **A pipeline** — rsyslog → Node collector → InfluxDB → Grafana, plus a Python report generator driven by cron.
2. **A dataset** — 11 days of dated reports under `2026/09/`, each a self-contained summary of that day's activity.

The repository is not a honeypot you can run with one command. It is the reporting half of a deployment: the collector entry point, the report generator, the rsyslog rule, the renderer config and a sanitised `docker-compose.yml` are included as reference. See [Limitations](#limitations) for exactly what is missing.

---

## Why it existed

Because the volume is the point. An SSH port on a public IP receives constant, automated authentication traffic — the same handful of botnets cycling through the same usernames. Individually those events are noise; collected over days they show real structure: which networks re-appear, which accounts are targeted, which hours are busiest, and how much of each day's traffic comes from infrastructure never seen before.

The design goal was therefore **longevity over immediacy**: a permanent, version-controlled, human-readable record that anyone can read without standing up the stack, with Grafana kept for interactive drilling and the Markdown kept as the record.

---

## Results

| Metric | Value |
| --- | --- |
| Reporting window | 2026-09-15 → 2026-09-25 (11 UTC days) |
| Total recorded attempts | **11,184** |
| Sum of daily unique source IPs | 521 |
| Busiest day | 2026-09-20 — 1,527 attempts from 70 IPs across 24 countries |
| Largest single-day reach | 2026-09-25 — 89 IPs across 25 countries |
| Most targeted account | `root` — ranked first on **all 11 days** |
| Quietest day | 2026-09-17 — 12 attempts from 2 IPs |

> Daily unique-IP counts are per day and are **not** de-duplicated across days; 521 is the sum of the daily figures, not a count of distinct attackers over the whole window.

The headline pattern is the concentration: in the final report, `root` absorbed 53% of all attempts, and the top network (`AS48090 TECHOFF SRV LIMITED`) accounted for 210 of 1,402. Traffic arrives in coordinated bursts from small clusters of addresses inside a few hosting providers rather than evenly across the internet.

---

## Architecture

Three stages, deliberately separated: **collection**, **storage and visualisation**, **publication**.

```text
                    Internet SSH scanners
                             │
                             ▼
            ┌────────────────────────────────┐
            │  Exposed host · real sshd      │
            │  no valuable accounts,         │
            │  nothing reachable past auth   │
            └───────────────┬────────────────┘
                            │ failed auth in syslog
                            ▼
            ┌────────────────────────────────┐
            │  rsyslog                       │
            │  30-ssh-geohash.conf           │
            │  Failed password /             │
            │  Invalid user / Disconnected   │
            │  → omfwd TCP 127.0.0.1:7070    │
            └───────────────┬────────────────┘
                            ▼
            ┌────────────────────────────────┐
            │  collector (Node)              │
            │  parse ip / port / username    │
            │  ip-api.com geolocation        │
            │  ngeohash encode               │
            └───────────────┬────────────────┘
                            ▼
            ┌────────────────────────────────┐
            │  InfluxDB — db `ssh_logs`      │
            │  measurement `geossh`          │
            └───────┬────────────────┬───────┘
                    │                │
                    ▼                ▼
        ┌───────────────────┐  ┌──────────────────────┐
        │  Grafana          │  │  daily-report.py     │
        │  geomap + queries │  │  InfluxQL over HTTP  │
        └───────────────────┘  └──────────┬───────────┘
                                          ▼
                              Markdown report + map PNG
                                          │
                                   cron · 00:05 UTC
                                          ▼
                                git commit && git push
                                          ▼
                            GitHub — 2026/09/ssh-threats-*.md
```

The important property is that no stage blocks another. If the renderer fails, the report still generates with a note that the map is missing — which is what happened on 2026-09-25, where the archived report records `No route to host` and carries on with its tables.

---

## Components

### 1. The exposed host

There is no emulated SSH server and no fake banner. A real `sshd` is exposed on a public address, and the host is treated as the honeypot: no accounts of value, nothing reachable past authentication. Every attempt is therefore an ordinary authentication failure in the system log, which is what the rest of the pipeline consumes.

This choice keeps the attack surface honest — attackers interact with real SSH, so the usernames and passwords they try are genuine — but it does mean the "honeypot" is really a **log-fed sensor**, and its fidelity depends on the host being correctly isolated.

### 2. rsyslog forwarding

`rsyslog/30-ssh-geohash.conf` is a drop-in rule that selects authentication failures and ships them over TCP:

```text
if $programname == 'sshd' and ($msg contains 'Failed password'
   or $msg contains 'Invalid user'
   or $msg contains 'Disconnected from authenticating user') then {
  action(
    type="omfwd" target="127.0.0.1" port="7070" protocol="tcp"
    template="SshAttemptMessage"
    action.resumeRetryCount="-1"
    queue.type="linkedList" queue.filename="ssh-geohash"
  )
}
```

Three deliberate details:

| Detail | Reason |
| --- | --- |
| `template="SshAttemptMessage"` with `drop-last-lf` | Sends one clean line per event, no newline framing to worry about on the receiver. |
| `queue.type="linkedList"` + `queue.filename` | Disk-assisted queue: if the collector is down, events spill to disk instead of being dropped. |
| `action.resumeRetryCount="-1"` | Retry forever rather than give up on a temporarily unreachable collector. |

`Invalid user` covers attempts against non-existent accounts, `Failed password` covers bad credentials for real ones. `Disconnected from authenticating user` is a looser signal — clients that drop the connection mid-authentication — and is the one pattern here that is a proxy for an attempt rather than proof of one.

### 3. The collector

`collector/index.js` runs a TCP server on `PORT` (default `7070`). For each connection it:

1. Ends the socket immediately after the first packet — one alert line per connection.
2. Parses the line into `ip`, `port` and `username`.
3. Looks the IP up against `ip-api.com` and **aborts the event if no location comes back**.
4. Encodes `lat`/`lon` into an ngeohash, strips `lat`/`lon` from the tag set, and writes one point to `geossh` with `value: 1`.

Configuration is entirely environment-driven:

| Variable | Default | Purpose |
| --- | --- | --- |
| `PORT` | `7070` | TCP listener for rsyslog |
| `INFLUX_DB` | — | Target database (expects `ssh_logs`) |
| `INFLUX_HOST` / `INFLUX_URL` | — | InfluxDB host |
| `INFLUX_PORT` | `8086` | InfluxDB port |
| `INFLUX_PROTOCOL` | `http` | `http` or `https` |
| `INFLUX_USER` / `INFLUX_PWD` | placeholders | Credentials |
| `DEBUG_LEVEL` | `info` | `log4js` level |

The geohash exists so Grafana's geomap can cluster points cheaply: adjacent cells share a prefix, so it doubles as a spatial aggregation key.

### 4. InfluxDB

Time-series store for every enriched event, in database `ssh_logs`, measurement `geossh`. Reports address it as container `ssh-influxdb` and query the HTTP API on `http://localhost:8086/query` through `docker exec`, which avoids exposing the database beyond the host and keeps credentials out of the script.

See [Data model](#data-model) for the point shape.

### 5. Grafana

The interactive layer: dashboard **Security → “SSH Login Attempts — Geohash”**, whose geomap panel (id `3`) is also the source of each report's map image. The report generator calls Grafana's `/render/d-solo/...` endpoint with the day's `from`/`to` window in epoch milliseconds, Basic auth, `width=1000`, `height=620`, `scale=2` and `tz=UTC+00:00`, then verifies the response actually starts with the PNG magic bytes before writing it.

Rendering is done by the remote **grafana-image-renderer**, whose settings live in `renderer/config.json`: Chromium launched with `--no-sandbox --disable-gpu --disable-dev-shm-usage`, timezone forced to UTC, and ArcGIS *World Light Gray Base* raster tiles as the basemap.

Grafana and InfluxDB are complementary rather than duplicated: one is for asking questions now, the other for what was true on a given day.

### 6. The report generator

`daily-report.py` builds one Markdown file per UTC day. It is the most substantial piece of the project, and its behaviour is worth knowing precisely.

**Time windows.** Days are UTC calendar days, constructed with timezone-aware datetimes and queried as `time >= START AND time < END`, so an event can never land in two reports. If the requested day is still in progress, the report says so and the numbers are partial.

**Reported statistics**, and the shape of each query:

| Statistic | InfluxQL |
| --- | --- |
| Total attempts | `SELECT count("value") FROM "geossh" WHERE <window>` |
| Per-IP attempts | `... GROUP BY "ip"` |
| Per-IP first / last seen | `SELECT first("value")` / `last("value") ... GROUP BY "ip"` |
| Country, city, ISP, ASN, username tallies | `... GROUP BY "<tag>"` |
| Hourly activity | `... GROUP BY time(1h) fill(0)` |
| First-time attackers | today's IPs **minus** every IP seen with `time < START` |

The overall window (`time < END`) is applied only where relevant; the "seen before" query deliberately has no lower bound, which is what makes the first-time-attacker set meaningful. Each query runs through `docker exec ... curl` with a 60-second timeout, and any InfluxDB error aborts rather than producing a silently empty report.

**CLI** — implemented directly in the script:

```bash
python3 daily-report.py                                  # yesterday, UTC
python3 daily-report.py --date 2026-09-25                # one day
python3 daily-report.py --from 2026-09-15 --to 2026-09-18  # one file per day
python3 daily-report.py --date 2026-09-25 --stdout       # also print it
python3 daily-report.py --date 2026-09-25 --no-front-matter
python3 daily-report.py --date 2026-09-25 --no-image     # skip the map capture
```

`--out` sets the destination directory (default `/home/user`); the file is written as `ssh-threats-<YYYY-MM-DD>.md`, with a sibling `.png` when the map renders.

### 7. Publication

A cron entry generates the previous day's report shortly after midnight UTC and commits it:

```cron
5 0 * * * /usr/bin/python3 /opt/ssh-dashboard/daily-report.py --out /opt/ssh-dashboard/repo/2026/09 >> /var/log/ssh-report.log 2>&1
```

followed by `git add`, `git commit` and `git push`. The output layout is `YYYY/MM/ssh-threats-YYYY-MM-DD.md`, which keeps directories small and makes the archive browsable by date.

---

## Data model

Every attempt is one point. Fields are numeric and therefore cheap to aggregate; tags are indexed strings and therefore what dashboards and reports group by.

| Kind | Key | Example |
| --- | --- | --- |
| Measurement | `geossh` | — |
| Field | `value` | `1` |
| Field | `latitude` | `48.8534` |
| Field | `longitude` | `2.3488` |
| Tag | `ip` | `77.239.124.210` |
| Tag | `username` | `root` |
| Tag | `port` | `22` |
| Tag | `geohash` | `u09tvw…` |
| Tag | `location` | `Île-de-France, Paris` |
| Tag | `country` / `city` / `regionName` | `France` / `Paris` / `Île-de-France` |
| Tag | `isp` / `as` | `Banatsync SRL` / `AS198364 Banatsync SRL` |

The collector spreads the *entire* remaining `ip-api.com` response into tags rather than selecting a few, so a point also carries `countryCode`, `zip`, `timezone`, `org`, `asname`, `mobile`, `proxy`, `hosting` and similar. That is convenient — every report field was available without a schema migration — but it is the model's main weakness; see below.

---

## Report anatomy

Each report is self-describing and opens with YAML front matter (`title`, `date`, `tags`, `description`), where the description already carries the day's headline numbers.

| Section | Contents |
| --- | --- |
| Attack map | Grafana geomap snapshot for the day, or an explicit note that rendering was unavailable |
| At a glance | Attempts, unique IPs, countries, per-hour average, top attacker with ISP and location, top country, most targeted account, peak hour, count of first-time attackers |
| Top attacking IPs | Up to 15 — attempts, share, ISP, location, first and last seen |
| Attempts by country | Up to 12 — attempts, share, proportional bar |
| Attempts by region / city | Up to 12 — as above |
| Targeted usernames | Up to 12 — attempts, share, bar |
| Top networks | Up to 6 ASNs |
| First-time attackers | IPs absent from the dataset before that day, with attempt counts |
| Hourly timeline | 24 UTC buckets as proportional bars |
| Recommended blocklist | Top 10 addresses in a plain `text` block plus an `iptables` example |

Empty days are handled explicitly rather than producing empty tables — a quiet day reads "no attempts recorded".

---

## Running it yourself

The included `docker-compose.yml` is a **sanitised starting point**, not the production file: credentials are placeholders and the container names differ from the ones `daily-report.py` expects. Treat the script's constants as the source of truth.

1. **Storage and dashboards.** Start InfluxDB and Grafana (`docker compose up -d`), then replace `CHANGE_USERNAME`/`CHANGE_PASSWORD` and point the collector at the same database. Recreate Grafana's geomap dashboard, or import your own — the report only depends on a panel id and dashboard slug matching `MAP_PANEL_ID` and `MAP_DASHBOARD_SLUG`.
2. **Rendering.** Rebuild Grafana with `renderer/config.json` mounted, or point `GRAFANA_URL` at an existing renderer.
3. **Forwarding.** Drop `rsyslog/30-ssh-geohash.conf` into `/etc/rsyslog.d/` and restart rsyslog.
4. **Collector.** Provide the `INFLUX_*` environment variables and run the collector on port `7070`. The `parser` and `api` modules it imports are not in this repository (see [Limitations](#limitations)) — supply your own implementations of the two functions it calls.
5. **Reports.** Set `GRAFANA_URL` and `GRAFANA_AUTH` (or let the script read `GRAFANA_ADMIN_PASSWORD` from `.env`), then schedule `daily-report.py` and commit its output.

The script defaults to `/home/user` for output and `admin:changeme` for Grafana auth, so neither the output path nor credentials need to live in the file.

---

## Limitations

Kept deliberately, because they explain why the project ended and what the rebuild changes:

- **The collector is incomplete as published.** `collector/index.js` imports `./parser` and `./api`, which are not in the repository. The entry point documents the design; it is not runnable on its own.
- **Tag cardinality.** Writing `ip`, `geohash`, `city` and `isp` as tags for every point means series count grows with the number of distinct attackers, cities and networks. This is the pattern InfluxDB warns about, and it is the first thing to fix at higher volume — details belong in fields, with only genuinely low-cardinality dimensions as tags.
- **A lookup failure loses the event.** If `ip-api.com` does not answer, the collector aborts that point entirely. There is also no cache, so a single noisy IP is re-resolved on every attempt, against a free-tier service with per-minute rate limits and no HTTPS.
- **Mixed InfluxDB generations.** The collector uses the legacy `influx` client (1.x write API with database and username/password) while `docker-compose.yml` stands up InfluxDB 2.7 with bucket setup. The reporting side speaks InfluxQL over the 1.x-style query endpoint.
- **`Disconnected from authenticating user` is a proxy**, not a confirmed attempt, so counts can be slightly generous. Separating it from outright failures would sharpen the totals.
- **One host, one vantage point.** Every observation is from a single network location; nothing here indicates internet-wide prevalence.
- **No tests, no CI.** The report generator was exercised through real daily runs, and formatting was fixed by hand — 18 of the commits here are "Fix formatting" corrections to generated Markdown.
- **Geolocation is approximate**, and the archive faithfully records whatever `ip-api.com` reported at the time, including clearly implausible pairs such as Iranian ASNs geolocated to Paris.

---

## Repository layout

```text
README.md                        this document
2026/09/ssh-threats-*.md         one report per UTC day (11 files)
collector/index.js               TCP collector entry point (see Limitations)
daily-report.py                  Markdown report generator
docker-compose.yml               sanitised InfluxDB + Grafana stack
renderer/config.json             grafana-image-renderer settings
rsyslog/30-ssh-geohash.conf      forwarding rule for sshd authentication failures
```

Start with [`2026/09/ssh-threats-2026-09-25.md`](2026/09/ssh-threats-2026-09-25.md) — the busiest and most complete day in the archive.

---

## Disclaimer

These reports are **observations made by one honeypot**, not attribution of attacks to individuals or organisations. IP geolocation, ISP and ASN data are approximate context; an IP address does not establish the identity or physical location of whoever operated it.

The generated blocklist is a list of addresses that were noisy on a given day, nothing more. Validate it against the environment before using it in firewall rules.

---

*Archived September 2026. The dataset remains as published; the code is kept as a reference implementation of the collection → storage → publication pipeline.*
