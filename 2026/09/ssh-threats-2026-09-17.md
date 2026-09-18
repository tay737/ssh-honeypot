---
title: "Daily SSH Honeypot Threat Report — 2026-09-17"
date: 2026-09-17T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "12 SSH brute-force attempts from 2 unique IPs across 2 countries hit the honeypot on 2026-09-17."
---

# Daily SSH Honeypot Threat Report — 2026-09-17

*Data window: `2026-09-17` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## At a glance...

- **12 attempts** from **2 unique IPs** in **2 countries** (0.5/hour average)
- **Top attacker:** `178.175.167.40` — 6 attempts (Studio An-tv SRL, Anenii Noi, Moldova)
- **Top source country:** Andorra — 6 (50%)
- **Most targeted account:** `root` — 12 (100%)
- ⏱️ **Peak hour:** 22:00–23:00 UTC — 6 attempts
- 🆕 **First-time attackers:** 2 of 2 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `178.175.167.40` | 6 | 50.0% | Studio An-tv SRL | Anenii Noi, Moldova | 22:26 | 22:26 |
| 2 | `195.178.110.232` | 6 | 50.0% | Techoff SRV Limited | Andorra la Vella, Andorra | 23:41 | 23:59 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| Andorra | 6 | 50.0% | ██████████·········· |
| Moldova | 6 | 50.0% | ██████████·········· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Andorra la Vella | 6 | 50.0% | ██████████·········· |
| Anenii Noi | 6 | 50.0% | ██████████·········· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 12 | 100.0% | ████████████████████ |

## Top networks

| Network | Attempts |
|---|---|
| `AS211504 STUDIO AN-TV SRL` | 6 |
| `AS48090 TECHOFF SRV LIMITED` | 6 |

## First-time attackers

`195.178.110.232` (6), `178.175.167.40` (6)

## Hourly timeline (UTC)

`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 6
`23:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 6

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall:

```text
178.175.167.40
195.178.110.232
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
