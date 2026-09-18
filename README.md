# SSH Honeypot – Daily Threat Reports

Daily threat reports generated from an internet-facing SSH honeypot.

This repository contains automatically generated, date-based reports documenting SSH brute-force activity observed by the honeypot. The underlying data is collected by a log collector, enriched with geolocation and network information, stored in InfluxDB, visualised through Grafana, and periodically converted into Markdown reports.

The reports are organised by **year → month → day** so that the repository can act as a long-term historical record of observed SSH threats.

---

## Overview

The project follows this pipeline:

```text
                    Internet
                       │
                       ▼
                ┌──────────────┐
                │ SSH Honeypot │
                └──────┬───────┘
                       │
                 Failed SSH
                login attempt
                       │
                       ▼
             ┌──────────────────┐
             │ Log collector    │
             │                  │
             │ ssh-log-to-influx│
             └────────┬─────────┘
                      │
                Enriches logs
                      │
                      ▼
               ┌─────────────┐
               │   InfluxDB  │
               │  + geossh   │
               └──────┬──────┘
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
       ┌─────────────┐  ┌───────────────┐
       │   Grafana   │  │ daily-report  │
       │             │  │    .py        │
       └─────────────┘  └───────┬───────┘
                                │
                         Daily .md file
                                │
                                ▼
                         ┌─────────────┐
                         │   GitHub    │
                         │ repository  │
                         └─────────────┘
```

Separates **data collection**, **storage/visualisation**, and **publication**.

---

## Structure

Reports are organised chronologically, for example:

```text
2026/
└── 09/
  ├── ssh-threats-2026-09-15.md
  ├── ssh-threats-2026-09-16.md
  ├── ssh-threats-2026-09-17.md
  └── ssh-threats-2026-09-18.md
```
## Report script + example config files from my server (if you want to try this yourself)
```text
daily-report.py
collector/
  ├── index.js
renderer/
  ├── config,json
rsyslog/
  ├── docker-compose.yml
```
---

# How It Works

## 1. SSH Honeypot

The honeypot exposes an SSH service to the internet and records failed authentication attempts.

This is to collect data on:

* Source IP addresses
* Attempt timestamps
* Attempted usernames
* Failed authentication attempts
* Geolocation
* ISP / network information
* Autonomous system information (botnets)
* City/regional information

Provides the raw event data > processed by the collector.

---

## 2. Data Collection

A collector script processes the SSH/honeypot logs > sends the resulting events to InfluxDB.

The collector is responsible for turning raw SSH events > structured time-series data.

The resulting data is stored in the InfluxDB measurement:

```text
geossh
```

The database used by the reporting script is:

```text
ssh_logs
```

The reporting script connects to the InfluxDB instance running inside the Docker container:

```text
ssh-influxdb
```

and queries the InfluxDB HTTP API on:

```text
http://localhost:8086/query
```

These values are defined near the beginning of `daily-report.py`.

---

## 3. Data Enrichment

Source IP addresses are enriched with additional information, including:

* Country
* City
* Region
* ISP
* Botnet

Geoolocation source: **ip-api.com**

This enrichment makes it possible to analyse not only individual attacking IP addresses but also broader geographic and network patterns.

---

# InfluxDB

InfluxDB: central time-series data store.

Each SSH event is stored with a timestamp and associated metadata.

The reporting process queries the `geossh` measurement to reconstruct activity for an individual UTC calendar day.

The report generator performs multiple queries against InfluxDB to calculate:

* Total attempts
* Unique attacking IPs
* First and last observation times
* Countries
* Cities
* ISPs
* ASNs
* Targeted usernames
* Hourly activity
* Previously unseen IP addresses

These are assembled into a single daily dataset before the Markdown report is generated.

---

# Grafana

Grafana provides the interactive monitoring and visualisation layer.

The underlying InfluxDB data can be explored through Grafana dashboards while the generated Markdown reports provide a permanent, version-controlled historical record.

The report currently references the Grafana view:

```text
Security → SSH Login Attempts — Geohash
```

The generated report describes Grafana as the interface for viewing charts and raw queries.

This gives the project two complementary views:

| Component        | Purpose                                     |
| ---------------- | ------------------------------------------- |
| InfluxDB         | Store time-series threat data               |
| Grafana          | Interactive investigation and visualisation |
| Markdown reports | Human-readable daily summaries              |
| GitHub           | Long-term public/version-controlled archive |

---

# Daily Report Generation

The `daily-report.py` script queries InfluxDB and generates a Markdown report for each UTC calendar day.

By default, running:

```bash
python3 daily-report.py
```

generates the report for **yesterday in UTC**.

A specific date can be requested:

```bash
python3 daily-report.py --date 2026-09-17
```

A date range can also be generated:

```bash
python3 daily-report.py \
    --from 2026-09-15 \
    --to 2026-09-18
```

The script generates one report per day in the requested range.

---

## UTC Calendar Days

Reports deliberately use **UTC calendar days** rather than the server's local timezone.

For a requested date such as:

```text
2026-09-17
```

the query window is:

```text
2026-09-17 00:00:00 UTC
        │
        │ 24 hours
        ▼
2026-09-18 00:00:00 UTC
```

The script constructs these boundaries explicitly using timezone-aware UTC datetimes.

The resulting InfluxDB query uses:

```text
time >= START
AND
time < END
```

which ensures that events belong to exactly one calendar day.

---

# Detecting new attackers

The report also attempts to identify IP addresses that were not observed before the start of the reporting day.

Two queries are effectively compared:

```text
Today's IP addresses
        │
        ├── minus ──► IPs seen before today
        │
        ▼
First-time attackers
```

The script queries all IPs observed before the beginning of the selected day and subtracts them from the IPs observed during that day.

This allows reports to distinguish between:

* Previously observed attackers
* IPs appearing for the first time in the dataset

---

# What's included in a daily report?


## At a Glance

* Total SSH attempts
* Number of unique IP addresses
* Number of countries
* Average attempts per hour
* Top attacking IP
* Top source country
* Most targeted username
* Peak hour
* Number of first-time attackers

## Top Attacking IPs

* Attempt count
* Percentage of total activity
* ISP
* Location
* First observed time
* Last observed time


## Attempts by Country

* Country
* Number of attempts
* Percentage of total
* Relative visual bar

## Attempts by Region / City

Displays the top **12 locations**.

## Targeted Usernames

Attempted usernames are aggregated to show which accounts attackers are attempting to authenticate against.

Displays the top **12 usernames**.

## Top Networks

Botnet / network information is also included.

The default report displays the top **6 networks**.

## First-Time Attackers

The report lists IP addresses that had not previously appeared in the dataset before the reporting day.

## Hourly Timeline

Activity is grouped into 24 UTC hours.

This provides a simple way of identifying periods of increased activity during the day.

## Blocklist

When activity is present, the report also generates a list containing the top 10 offenders.

This is intended as a convenient starting point for defensive investigation or firewall automation, rather than as an assertion that every listed address is permanently malicious.

---

# Automation

The report generation script is intended to run automatically, using `cron`.

Simplified workflow:

```text
Cron
 │
 │ once per day
 ▼
daily-report.py
 │
 ▼
Query InfluxDB
 │
 ▼
Calculate daily statistics
 │
 ▼
Generate Markdown
 │
 ▼
Place report in year/month directory
 │
 ▼
Git commit
 │
 ▼
Git push
 │
 ▼
GitHub
```

A typical automated schedule might run shortly after midnight UTC, generating the report for the previous UTC day.

For example:

```cron
5 0 * * * /path/to/daily-report.py
```

The exact cron configuration is deployment-specific.

# Running manually

The report generator supports several modes.

### Generate yesterday's report

```bash
python3 daily-report.py
```

### Generate a specific day

```bash
python3 daily-report.py --date 2026-09-17
```

### Generate multiple days

```bash
python3 daily-report.py \
    --from 2026-09-15 \
    --to 2026-09-18
```

### Print the report to stdout

```bash
python3 daily-report.py \
    --date 2026-09-18 \
    --stdout
```

### Disable YAML front matter

```bash
python3 daily-report.py \
    --date 2026-09-18 \
    --no-front-matter
```

These command-line options are implemented directly by the report generator.

---

# Report Metadata

Reports can include YAML front matter containing information such as:

```yaml
---
title: "Daily SSH Honeypot Threat Report — 2026-09-18"
date: 2026-09-18T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "Daily SSH brute-force activity observed by the honeypot."
---
```

This makes the generated Markdown suitable for static-site generators and other Markdown-aware tooling.

---


# Disclaimer

The information in these reports represents **observations made by the honeypot**, not attribution of attacks to individuals or organisations.

IP geolocation and ISP/ASN information should be treated as approximate contextual information. An IP address does not, by itself, establish the identity or physical location of the person operating it.

The generated blocklist is also an observation-based list of active source addresses and should be evaluated against the requirements of the environment before being used in production firewall rules.

---

# Project Components

| Component           | Role                                         |
| ------------------- | -------------------------------------------- |
| SSH Honeypot        | Captures SSH authentication activity         |
| `ssh-log-to-influx` | Processes and sends events to InfluxDB       |
| InfluxDB            | Stores time-series event data                |
| Grafana             | Provides dashboards and interactive analysis |
| `daily-report.py`   | Generates daily .md reports                  |
| Cron                | Runs reporting process automatically         |
| Git                 | Tracks generated reports                     |
| GitHub              | Hosts historical threat archive              |

---

# Purpose

The purpose of this repository is to maintain a transparent, chronological record of SSH brute-force activity observed by the honeypot.

* Attack volume
* Source IPs
* Geographic distribution
* Targeted usernames
* Networks / ASNs
* New attacking infrastructure
* Time-of-day activity

Over time, the collection of daily reports can therefore serve as a historical dataset for security monitoring, threat-intelligence research, and analysis of internet-wide SSH scanning and brute-force behaviour.
