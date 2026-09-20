---
title: "Daily SSH Honeypot Threat Report — 2026-09-19"
date: 2026-09-19T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1084 SSH brute-force attempts from 36 unique IPs across 15 countries hit the honeypot on 2026-09-19."
---

# Daily SSH Honeypot Threat Report — 2026-09-19

*Data window: `2026-09-19` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-19

<img width="2000" height="1240" alt="ssh-threats-2026-09-19 (1)" src="https://github.com/user-attachments/assets/4faf495a-1653-42cd-b659-09b97915afdd" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,084 attempts** from **36 unique IPs** in **15 countries** (45.2/hour average)
- **Top attacker:** `45.148.10.141` — 85 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 470 (43%)
- **Most targeted account:** `root` — 757 (70%)
- **Peak hour:** 20:00–21:00 UTC — 137 attempts
- **First-time attackers:** 23 of 36 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.141` | 85 | 7.8% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:07 | 23:58 |
| 2 | `45.148.10.152` | 85 | 7.8% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:35 | 23:08 |
| 3 | `45.148.10.151` | 80 | 7.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:02 | 23:52 |
| 4 | `45.148.10.157` | 75 | 6.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:07 | 22:41 |
| 5 | `109.160.32.82` | 66 | 6.1% | TechTies Inc. | Cornelius, United States | 00:05 | 02:11 |
| 6 | `193.47.62.69` | 60 | 5.5% | BestDC Limited | Andorra la Vella, Andorra | 00:46 | 23:41 |
| 7 | `62.60.130.201` | 55 | 5.1% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:24 | 13:38 |
| 8 | `62.60.130.242` | 55 | 5.1% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:13 | 23:19 |
| 9 | `80.94.92.55` | 53 | 4.9% | Unmanaged LTD | Amsterdam, The Netherlands | 04:01 | 06:27 |
| 10 | `109.160.32.110` | 51 | 4.7% | TechTies Inc. | Cornelius, United States | 20:30 | 22:03 |
| 11 | `62.60.130.253` | 50 | 4.6% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:53 | 22:30 |
| 12 | `109.160.32.155` | 44 | 4.1% | TechTies Inc. | Cornelius, United States | 05:38 | 07:00 |
| 13 | `2.57.122.168` | 39 | 3.6% | Unmanaged LTD | Amsterdam, The Netherlands | 09:07 | 11:31 |
| 14 | `109.160.32.212` | 31 | 2.9% | TechTies Inc. | Cornelius, United States | 21:19 | 22:13 |
| 15 | `80.94.92.234` | 28 | 2.6% | Unmanaged LTD | Amsterdam, The Netherlands | 20:31 | 21:58 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 470 | 43.4% | █████████··········· |
| United States | 202 | 18.6% | ████················ |
| Iran | 160 | 14.8% | ███················· |
| Andorra | 75 | 6.9% | █··················· |
| China | 48 | 4.4% | █··················· |
| Argentina | 20 | 1.8% | ···················· |
| Bolivia | 18 | 1.7% | ···················· |
| India | 18 | 1.7% | ···················· |
| Pakistan | 16 | 1.5% | ···················· |
| Singapore | 16 | 1.5% | ···················· |
| Venezuela | 15 | 1.4% | ···················· |
| Hong Kong | 14 | 1.3% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 470 | 43.4% | █████████··········· |
| Cornelius, North Carolina | 192 | 17.7% | ████················ |
| Tehran | 160 | 14.8% | ███················· |
| Andorra la Vella | 75 | 6.9% | █··················· |
| Nanjing, Jiangsu | 25 | 2.3% | ···················· |
| Córdoba, Cordoba | 20 | 1.8% | ···················· |
| Cochabamba | 18 | 1.7% | ···················· |
| Pune, Maharashtra | 18 | 1.7% | ···················· |
| Multan, Punjab | 16 | 1.5% | ···················· |
| Singapore, South West | 16 | 1.5% | ···················· |
| Caracas, Distrito Federal | 15 | 1.4% | ···················· |
| Hong Kong, Kowloon | 14 | 1.3% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 757 | 69.8% | ██████████████······ |
| `admin` | 48 | 4.4% | █··················· |
| `deploy` | 15 | 1.4% | ···················· |
| `developer` | 10 | 0.9% | ···················· |
| `test` | 10 | 0.9% | ···················· |
| `ubuntu` | 10 | 0.9% | ···················· |
| `apache` | 7 | 0.6% | ···················· |
| `administrator` | 6 | 0.6% | ···················· |
| `student` | 6 | 0.6% | ···················· |
| `user` | 5 | 0.5% | ···················· |
| `abbott` | 4 | 0.4% | ···················· |
| `appuser` | 4 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 340 |
| `AS197170 TechTies Inc.` | 192 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 160 |
| `AS47890 UNMANAGED LTD` | 150 |
| `AS216014 BestDC Limited` | 60 |
| `AS4837 CHINA UNICOM China169 Backbone` | 24 |

## First-time attackers

`80.94.92.55` (53), `109.160.32.110` (51), `109.160.32.155` (44), `109.160.32.212` (31), `190.96.127.50` (20), `98.70.50.166` (18), `190.129.122.185` (18), `118.139.164.171` (16), `103.166.103.173` (16), `201.249.192.30` (15), `122.96.50.241` (14), `43.132.150.89` (14), `58.221.60.25` (11), `122.97.209.194` (10), `60.204.139.188` (6), `203.189.196.168` (5), `92.118.39.71` (5), `77.90.185.20` (5), `47.251.115.2` (5), `92.184.107.72` (4), `125.119.19.122` (2), `34.156.90.42` (2), `130.211.107.33` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 97
`01:00` ▇▇▇▇▇▇▇▇▇ 39
`02:00` ▇▇▇ 13
`03:00` ▇▇▇ 15
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 67
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 90
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 82
`07:00` ▇▇▇▇▇▇▇▇▇▇▇ 48
`08:00` ▇▇▇▇▇▇▇▇▇▇▇ 50
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 55
`10:00` ▇▇▇▇▇ 25
`11:00` ▇▇▇ 14
`12:00` ▇ 2
`13:00` ▇▇▇▇▇▇▇▇▇▇▇ 50
`14:00` ▇▇ 10
`17:00` ▇ 3
`18:00` ▇▇▇▇▇▇▇▇▇▇ 47
`19:00` ▇▇▇▇▇▇▇ 31
`20:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 137
`21:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 72
`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 82
`23:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 55

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.141
45.148.10.152
45.148.10.151
45.148.10.157
109.160.32.82
193.47.62.69
62.60.130.201
62.60.130.242
80.94.92.55
109.160.32.110
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
