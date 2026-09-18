---
title: "Daily SSH Honeypot Threat Report — 2026-09-15"
date: 2026-09-15T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "198 SSH brute-force attempts from 2 unique IPs across 2 countries hit the honeypot on 2026-09-15."
---

# Daily SSH Honeypot Threat Report — 2026-09-15

*Data window: `2026-09-15` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## At a glance...

- **198 attempts** from **2 unique IPs** in **2 countries** (8.2/hour average)
- **Top attacker:** `45.15.225.137` — 190 attempts (Primanet SRL, Chisinau, Moldova)
- **Top source country:** Moldova — 190 (96%)
- **Most targeted account:** `root` — 24 (12%)
- ⏱️ **Peak hour:** 22:00–23:00 UTC — 198 attempts
- 🆕 **First-time attackers:** 2 of 2 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.15.225.137` | 190 | 96.0% | Primanet SRL | Chisinau, Moldova | 22:38 | 22:48 |
| 2 | `35.187.231.181` | 8 | 4.0% | Google LLC | Singapore, Singapore | 22:43 | 22:44 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| Moldova | 190 | 96.0% | ███████████████████· |
| Singapore | 8 | 4.0% | █··················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Chisinau, Chișinău Municipality | 190 | 96.0% | ███████████████████· |
| Singapore, Central Singapore | 8 | 4.0% | █··················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 24 | 12.1% | ██·················· |
| `admin` | 23 | 11.6% | ██·················· |
| `ubuntu` | 23 | 11.6% | ██·················· |
| `ftpuser` | 19 | 9.6% | ██·················· |
| `oracle` | 17 | 8.6% | ██·················· |
| `test` | 17 | 8.6% | ██·················· |
| `test1` | 17 | 8.6% | ██·················· |
| `test2` | 17 | 8.6% | ██·················· |
| `user` | 17 | 8.6% | ██·················· |
| `usuario` | 17 | 8.6% | ██·················· |
| `pi` | 5 | 2.5% | █··················· |
| `baikal` | 2 | 1.0% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS207164 PRIMANET SRL` | 190 |
| `AS396982 Google LLC` | 8 |

## First-time attackers

`45.15.225.137` (190), `35.187.231.181` (8)

## Hourly timeline (UTC)

`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 198

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall:

```text
45.15.225.137
35.187.231.181
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
