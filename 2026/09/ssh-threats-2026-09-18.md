---
title: "Daily SSH Honeypot Threat Report — 2026-09-18"
date: 2026-09-18T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "894 SSH brute-force attempts from 23 unique IPs across 9 countries hit the honeypot on 2026-09-18."
---

# Daily SSH Honeypot Threat Report — 2026-09-18

*Data window: `2026-09-18` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.comday in progress, stats partial*

## At a glance...

- **894 attempts** from **23 unique IPs** in **9 countries** (37.2/hour average)
- **Top attacker:** `45.148.10.151` — 95 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 396 (44%)
- **Most targeted account:** `root` — 693 (78%)
- **Peak hour:** 14:00–15:00 UTC — 98 attempts
- **First-time attackers:** 14 of 23 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.151` | 95 | 10.6% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:07 | 15:55 |
| 2 | `45.148.10.141` | 83 | 9.3% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:22 | 16:01 |
| 3 | `109.160.32.24` | 82 | 9.2% | TechTies Inc. | Cornelius, United States | 08:32 | 11:11 |
| 4 | `45.148.10.152` | 78 | 8.7% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:32 | 15:50 |
| 5 | `62.60.130.242` | 75 | 8.4% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:12 | 14:54 |
| 6 | `193.47.62.69` | 65 | 7.3% | BestDC Limited | Andorra la Vella, Andorra | 02:45 | 15:19 |
| 7 | `45.148.10.157` | 65 | 7.3% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:17 | 15:40 |
| 8 | `109.160.32.87` | 59 | 6.6% | TechTies Inc. | Cornelius, United States | 13:25 | 15:18 |
| 9 | `92.118.39.77` | 51 | 5.7% | Unmanaged LTD | Dallas, United States | 12:01 | 14:18 |
| 10 | `77.239.124.174` | 46 | 5.1% | Banatsync SRL | Paris, France | 08:08 | 09:33 |
| 11 | `62.60.130.201` | 45 | 5.0% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:56 | 15:09 |
| 12 | `62.60.130.253` | 45 | 5.0% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:52 | 15:04 |
| 13 | `80.94.92.179` | 45 | 5.0% | Unmanaged LTD | Amsterdam, The Netherlands | 02:15 | 06:28 |
| 14 | `2.57.122.168` | 22 | 2.5% | Unmanaged LTD | Amsterdam, The Netherlands | 07:57 | 14:16 |
| 15 | `2.57.122.209` | 8 | 0.9% | Unmanaged LTD | Amsterdam, The Netherlands | 18:18 | 18:41 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 396 | 44.3% | █████████··········· |
| United States | 200 | 22.4% | ████················ |
| Iran | 165 | 18.5% | ████················ |
| Andorra | 69 | 7.7% | ██·················· |
| France | 46 | 5.1% | █··················· |
| China | 6 | 0.7% | ···················· |
| Albania | 5 | 0.6% | ···················· |
| Russia | 4 | 0.4% | ···················· |
| Belgium | 3 | 0.3% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 396 | 44.3% | █████████··········· |
| Tehran | 165 | 18.5% | ████················ |
| Cornelius, North Carolina | 145 | 16.2% | ███················· |
| Andorra la Vella | 69 | 7.7% | ██·················· |
| Dallas, Texas | 51 | 5.7% | █··················· |
| Paris, Île-de-France | 46 | 5.1% | █··················· |
| Jinan, Shandong | 6 | 0.7% | ···················· |
| Durrës, Durrës County | 5 | 0.6% | ···················· |
| Katy, Texas | 4 | 0.4% | ···················· |
| Saratov, Saratov Oblast | 4 | 0.4% | ···················· |
| Brussels, Brussels Capital | 3 | 0.3% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 693 | 77.5% | ████████████████···· |
| `admin` | 24 | 2.7% | █··················· |
| `ubuntu` | 13 | 1.5% | ···················· |
| `deploy` | 12 | 1.3% | ···················· |
| `developer` | 10 | 1.1% | ···················· |
| `pi` | 10 | 1.1% | ···················· |
| `ts3` | 6 | 0.7% | ···················· |
| `appuser` | 4 | 0.4% | ···················· |
| `claude` | 4 | 0.4% | ···················· |
| `demo` | 4 | 0.4% | ···················· |
| `deployer` | 4 | 0.4% | ···················· |
| `docker` | 4 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 325 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 165 |
| `AS197170 TechTies Inc.` | 145 |
| `AS47890 UNMANAGED LTD` | 126 |
| `AS216014 BestDC Limited` | 65 |
| `AS198364 BANATSYNC SRL` | 46 |

## First-time attackers

`109.160.32.24` (82), `109.160.32.87` (59), `92.118.39.77` (51), `77.239.124.174` (46), `80.94.92.179` (45), `62.60.130.201` (45), `2.57.122.168` (22), `39.87.248.213` (6), `193.163.187.123` (5), `64.92.3.141` (4), `109.160.32.89` (4), `109.195.19.44` (4), `207.175.156.27` (2), `35.189.200.192` (1)

## Hourly timeline (UTC)

`00:00` ▇ 4
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 45
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 54
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 40
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 65
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 68
`07:00` ▇▇ 6
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 51
`10:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 61
`11:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50
`12:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 76
`13:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 88
`14:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 98
`15:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59
`16:00` ▇ 3
`18:00` ▇▇ 8

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall:

```text
45.148.10.151
45.148.10.141
109.160.32.24
45.148.10.152
62.60.130.242
193.47.62.69
45.148.10.157
109.160.32.87
92.118.39.77
77.239.124.174
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
