---
title: "Daily SSH Honeypot Threat Report — 2026-09-18"
date: 2026-09-18T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1292 SSH brute-force attempts from 26 unique IPs across 9 countries hit the honeypot on 2026-09-18."
---

# Daily SSH Honeypot Threat Report — 2026-09-18

*Data window: `2026-09-18` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-18

<img width="2000" height="1240" alt="ssh-threats-2026-09-18 (2)" src="https://github.com/user-attachments/assets/61c900d6-ccba-454a-aff8-57f34aea74e0" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,292 attempts** from **26 unique IPs** in **9 countries** (53.8/hour average)
- **Top attacker:** `45.148.10.151` — 135 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 569 (44%)
- **Most targeted account:** `root` — 964 (75%)
- **Peak hour:** 14:00–15:00 UTC — 98 attempts
- **First-time attackers:** 17 of 26 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.151` | 135 | 10.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:07 | 23:45 |
| 2 | `45.148.10.141` | 118 | 9.1% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:22 | 23:28 |
| 3 | `45.148.10.152` | 108 | 8.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:32 | 23:34 |
| 4 | `193.47.62.69` | 95 | 7.4% | BestDC Limited | Andorra la Vella, Andorra | 02:45 | 23:39 |
| 5 | `45.148.10.157` | 95 | 7.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:17 | 23:03 |
| 6 | `62.60.130.242` | 95 | 7.4% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:12 | 23:50 |
| 7 | `109.160.32.24` | 82 | 6.3% | TechTies Inc. | Cornelius, United States | 08:32 | 11:11 |
| 8 | `62.60.130.201` | 75 | 5.8% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:56 | 23:18 |
| 9 | `62.60.130.253` | 65 | 5.0% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:52 | 23:13 |
| 10 | `109.160.32.156` | 60 | 4.6% | TechTies Inc. | Cornelius, United States | 19:25 | 21:18 |
| 11 | `109.160.32.87` | 59 | 4.6% | TechTies Inc. | Cornelius, United States | 13:25 | 15:18 |
| 12 | `92.118.39.77` | 51 | 3.9% | Unmanaged LTD | Dallas, United States | 12:01 | 14:18 |
| 13 | `80.94.92.179` | 50 | 3.9% | Unmanaged LTD | Amsterdam, The Netherlands | 02:15 | 23:59 |
| 14 | `77.239.124.173` | 46 | 3.6% | Banatsync SRL | Paris, France | 21:46 | 23:10 |
| 15 | `77.239.124.174` | 46 | 3.6% | Banatsync SRL | Paris, France | 08:08 | 09:33 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 569 | 44.0% | █████████··········· |
| United States | 279 | 21.6% | ████················ |
| Iran | 235 | 18.2% | ████················ |
| Andorra | 99 | 7.7% | ██·················· |
| France | 92 | 7.1% | █··················· |
| China | 6 | 0.5% | ···················· |
| Albania | 5 | 0.4% | ···················· |
| Russia | 4 | 0.3% | ···················· |
| Belgium | 3 | 0.2% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 569 | 44.0% | █████████··········· |
| Tehran | 235 | 18.2% | ████················ |
| Cornelius, North Carolina | 224 | 17.3% | ███················· |
| Andorra la Vella | 99 | 7.7% | ██·················· |
| Paris, Île-de-France | 92 | 7.1% | █··················· |
| Dallas, Texas | 51 | 3.9% | █··················· |
| Jinan, Shandong | 6 | 0.5% | ···················· |
| Durrës, Durrës County | 5 | 0.4% | ···················· |
| Katy, Texas | 4 | 0.3% | ···················· |
| Saratov, Saratov Oblast | 4 | 0.3% | ···················· |
| Brussels, Brussels Capital | 3 | 0.2% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 964 | 74.6% | ███████████████····· |
| `admin` | 36 | 2.8% | █··················· |
| `ubuntu` | 19 | 1.5% | ···················· |
| `deploy` | 18 | 1.4% | ···················· |
| `debian` | 12 | 0.9% | ···················· |
| `test` | 11 | 0.9% | ···················· |
| `developer` | 10 | 0.8% | ···················· |
| `pi` | 10 | 0.8% | ···················· |
| `backup` | 8 | 0.6% | ···················· |
| `demo` | 8 | 0.6% | ···················· |
| `ts3` | 6 | 0.5% | ···················· |
| `ai` | 4 | 0.3% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 460 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 235 |
| `AS197170 TechTies Inc.` | 224 |
| `AS47890 UNMANAGED LTD` | 164 |
| `AS216014 BestDC Limited` | 95 |
| `AS198364 BANATSYNC SRL` | 92 |

## First-time attackers

`109.160.32.24` (82), `62.60.130.201` (75), `109.160.32.156` (60), `109.160.32.87` (59), `92.118.39.77` (51), `80.94.92.179` (50), `77.239.124.173` (46), `77.239.124.174` (46), `2.57.122.168` (22), `109.160.32.82` (19), `39.87.248.213` (6), `193.163.187.123` (5), `109.195.19.44` (4), `109.160.32.89` (4), `64.92.3.141` (4), `207.175.156.27` (2), `35.189.200.192` (1)

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
`18:00` ▇▇▇▇ 12
`19:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 90
`20:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 83
`21:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 71
`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 71
`23:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 79

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.151
45.148.10.141
45.148.10.152
193.47.62.69
45.148.10.157
62.60.130.242
109.160.32.24
62.60.130.201
62.60.130.253
109.160.32.156
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
