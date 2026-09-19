---
title: "Daily SSH Honeypot Threat Report — 2026-09-19"
date: 2026-09-19T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "590 SSH brute-force attempts from 19 unique IPs across 7 countries hit the honeypot on 2026-09-19."
---

# Daily SSH Honeypot Threat Report — 2026-09-19

*Data window: `2026-09-19` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.comday in progress, stats partial*

## Attack map — 2026-09-19

<img width="2000" height="1240" alt="ssh-threats-2026-09-19" src="https://github.com/user-attachments/assets/52d07b2d-78ad-4ed6-8b5f-90a7a09a6431" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **590 attempts** from **19 unique IPs** in **7 countries** (24.6/hour average)
- **Top attacker:** `109.160.32.82` — 66 attempts (TechTies Inc., Cornelius, United States)
- **Top source country:** The Netherlands — 292 (49%)
- **Most targeted account:** `root` — 457 (77%)
- **Peak hour:** 00:00–01:00 UTC — 97 attempts
- **First-time attackers:** 7 of 19 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `109.160.32.82` | 66 | 11.2% | TechTies Inc. | Cornelius, United States | 00:05 | 02:11 |
| 2 | `45.148.10.151` | 60 | 10.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:02 | 09:57 |
| 3 | `80.94.92.55` | 53 | 9.0% | Unmanaged LTD | Amsterdam, The Netherlands | 04:01 | 06:27 |
| 4 | `45.148.10.152` | 50 | 8.5% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:35 | 09:52 |
| 5 | `62.60.130.201` | 45 | 7.6% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:24 | 08:07 |
| 6 | `62.60.130.242` | 45 | 7.6% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:13 | 08:47 |
| 7 | `109.160.32.155` | 44 | 7.5% | TechTies Inc. | Cornelius, United States | 05:38 | 07:00 |
| 8 | `45.148.10.157` | 40 | 6.8% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:07 | 08:27 |
| 9 | `193.47.62.69` | 35 | 5.9% | BestDC Limited | Andorra la Vella, Andorra | 00:46 | 09:47 |
| 10 | `2.57.122.168` | 34 | 5.8% | Unmanaged LTD | Amsterdam, The Netherlands | 09:07 | 11:12 |
| 11 | `45.148.10.141` | 30 | 5.1% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:07 | 09:37 |
| 12 | `62.60.130.253` | 30 | 5.1% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:53 | 08:17 |
| 13 | `80.94.92.179` | 25 | 4.2% | Unmanaged LTD | Amsterdam, The Netherlands | 00:10 | 01:49 |
| 14 | `195.178.110.217` | 15 | 2.5% | Techoff SRV Limited | Andorra la Vella, Andorra | 03:06 | 03:49 |
| 15 | `203.189.196.168` | 5 | 0.8% | Cloud Computing Corporation | Guangzhou, China | 10:54 | 10:57 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 292 | 49.5% | ██████████·········· |
| Iran | 120 | 20.3% | ████················ |
| United States | 115 | 19.5% | ████················ |
| Andorra | 50 | 8.5% | ██·················· |
| China | 5 | 0.8% | ···················· |
| Germany | 5 | 0.8% | ···················· |
| Belgium | 3 | 0.5% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 292 | 49.5% | ██████████·········· |
| Tehran | 120 | 20.3% | ████················ |
| Cornelius, North Carolina | 110 | 18.6% | ████················ |
| Andorra la Vella | 50 | 8.5% | ██·················· |
| Augsburg, Bavaria | 5 | 0.8% | ···················· |
| Guangzhou, Guangdong | 5 | 0.8% | ···················· |
| Minkler, California | 5 | 0.8% | ···················· |
| Brussels, Brussels Capital | 3 | 0.5% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 457 | 77.5% | ███████████████····· |
| `admin` | 26 | 4.4% | █··················· |
| `deploy` | 15 | 2.5% | █··················· |
| `developer` | 10 | 1.7% | ···················· |
| `administrator` | 6 | 1.0% | ···················· |
| `apache` | 6 | 1.0% | ···················· |
| `test` | 6 | 1.0% | ···················· |
| `appuser` | 4 | 0.7% | ···················· |
| `student` | 4 | 0.7% | ···················· |
| `work` | 4 | 0.7% | ···················· |
| `openclaw` | 3 | 0.5% | ···················· |
| `a` | 2 | 0.3% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 195 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 120 |
| `AS47890 UNMANAGED LTD` | 112 |
| `AS197170 TechTies Inc.` | 110 |
| `AS216014 BestDC Limited` | 35 |
| `AS213790 Limited Network LTD` | 5 |

## First-time attackers

`80.94.92.55` (53), `109.160.32.155` (44), `47.251.115.2` (5), `203.189.196.168` (5), `77.90.185.20` (5), `34.156.90.42` (2), `130.211.107.33` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 97
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 39
`02:00` ▇▇▇▇ 13
`03:00` ▇▇▇▇▇ 15
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 67
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 90
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 82
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 48
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 55
`10:00` ▇▇▇▇▇▇▇▇ 25
`11:00` ▇▇▇ 9

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
109.160.32.82
45.148.10.151
80.94.92.55
45.148.10.152
62.60.130.201
62.60.130.242
109.160.32.155
45.148.10.157
193.47.62.69
2.57.122.168
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
