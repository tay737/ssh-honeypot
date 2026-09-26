---
title: "Daily SSH Honeypot Threat Report — 2026-09-24"
date: 2026-09-24T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1180 SSH brute-force attempts from 62 unique IPs across 23 countries hit the honeypot on 2026-09-24."
---

# Daily SSH Honeypot Threat Report — 2026-09-24

*Data window: `2026-09-24` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-24

![Geographic distribution of SSH brute-force attempts on 2026-09-24](ssh-threats-2026-09-24.png)

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,180 attempts** from **62 unique IPs** in **23 countries** (49.2/hour average)
- **Top attacker:** `45.148.10.183` — 81 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 391 (33%)
- **Most targeted account:** `root` — 706 (60%)
- **Peak hour:** 07:00–08:00 UTC — 213 attempts
- **First-time attackers:** 41 of 62 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.183` | 81 | 6.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:50 | 08:48 |
| 2 | `45.148.10.151` | 70 | 5.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:05 | 10:41 |
| 3 | `2.57.122.76` | 65 | 5.5% | Unmanaged LTD | Amsterdam, The Netherlands | 08:05 | 10:35 |
| 4 | `45.148.10.152` | 60 | 5.1% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:30 | 11:07 |
| 5 | `45.148.10.141` | 55 | 4.7% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:54 | 11:02 |
| 6 | `62.60.130.253` | 55 | 4.7% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:04 | 09:39 |
| 7 | `62.60.130.242` | 50 | 4.2% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:15 | 10:46 |
| 8 | `62.60.130.201` | 45 | 3.8% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:20 | 10:51 |
| 9 | `45.148.10.157` | 35 | 3.0% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:10 | 08:38 |
| 10 | `193.47.62.69` | 30 | 2.5% | BestDC Limited | Andorra la Vella, Andorra | 00:01 | 07:07 |
| 11 | `92.118.39.14` | 27 | 2.3% | Unmanaged LTD | Dallas, United States | 00:22 | 23:29 |
| 12 | `41.193.100.133` | 25 | 2.1% | Vox Telecommunications PTY Ltd | Century City, South Africa | 00:02 | 01:04 |
| 13 | `46.191.141.152` | 24 | 2.0% | JSC "Ufanet" | Ufa, Russia | 05:32 | 06:20 |
| 14 | `159.89.198.186` | 22 | 1.9% | DigitalOcean, LLC | Singapore, Singapore | 02:29 | 03:22 |
| 15 | `81.28.167.30` | 22 | 1.9% | AIST Networks | Tolyatti, Russia | 00:59 | 01:49 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 391 | 33.1% | ███████············· |
| Iran | 150 | 12.7% | ███················· |
| United States | 115 | 9.7% | ██·················· |
| Singapore | 77 | 6.5% | █··················· |
| Russia | 58 | 4.9% | █··················· |
| Germany | 54 | 4.6% | █··················· |
| Vietnam | 51 | 4.3% | █··················· |
| China | 44 | 3.7% | █··················· |
| Andorra | 30 | 2.5% | █··················· |
| South Africa | 25 | 2.1% | ···················· |
| India | 23 | 1.9% | ···················· |
| Kazakhstan | 19 | 1.6% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 376 | 31.9% | ██████·············· |
| Tehran | 150 | 12.7% | ███················· |
| Frankfurt am Main, Hesse | 43 | 3.6% | █··················· |
| Singapore, Central Singapore | 39 | 3.3% | █··················· |
| Andorra la Vella | 30 | 2.5% | █··················· |
| Dallas, Texas | 27 | 2.3% | ···················· |
| New York | 27 | 2.3% | ···················· |
| Century City, Western Cape | 25 | 2.1% | ···················· |
| Ufa, Bashkortostan Republic | 24 | 2.0% | ···················· |
| Singapore, South West | 22 | 1.9% | ···················· |
| Tolyatti, Samara Oblast | 22 | 1.9% | ···················· |
| Almaty | 19 | 1.6% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 706 | 59.8% | ████████████········ |
| `admin` | 47 | 4.0% | █··················· |
| `ubuntu` | 22 | 1.9% | ···················· |
| `test` | 18 | 1.5% | ···················· |
| `debian` | 10 | 0.8% | ···················· |
| `user` | 10 | 0.8% | ···················· |
| `ftpuser` | 8 | 0.7% | ···················· |
| `ann` | 6 | 0.5% | ···················· |
| `dev` | 6 | 0.5% | ···················· |
| `frappe` | 6 | 0.5% | ···················· |
| `minecraft` | 6 | 0.5% | ···················· |
| `mysql` | 6 | 0.5% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 301 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 150 |
| `AS47890 UNMANAGED LTD` | 102 |
| `AS14061 DigitalOcean, LLC` | 70 |
| `AS216014 BestDC Limited` | 30 |
| `AS11845 Vox Telecom Ltd` | 25 |

## First-time attackers

`45.148.10.183` (81), `2.57.122.76` (65), `81.28.167.30` (22), `159.89.198.186` (22), `52.237.80.79` (20), `82.200.235.132` (19), `103.20.122.54` (19), `171.76.108.65` (18), `45.119.81.245` (18), `146.190.74.52` (17), `201.184.50.251` (17), `103.167.89.222` (17), `171.244.143.209` (16), `72.167.227.34` (16), `101.47.15.26` (16), `187.110.238.50` (16), `77.91.66.181` (16), `139.59.133.58` (15), `147.90.234.15` (15), `203.150.107.244` (15), `81.192.46.49` (14), `213.206.207.162` (13), `150.241.113.163` (12), `23.29.118.81` (12), `45.9.75.8` (12), `35.210.61.208` (12), `109.160.32.29` (10), `42.51.32.228` (10), `118.145.115.134` (10), `203.83.234.180` (8), `106.13.209.152` (5), `20.244.28.141` (5), `14.155.236.160` (4), `103.143.239.201` (4), `45.120.216.232` (4), `207.175.33.128` (2), `80.91.223.114` (2), `74.130.53.87` (2), `119.96.158.87` (2), `31.57.62.245` (2), `34.38.77.240` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 152
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 120
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 123
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 82
`04:00` ▇ 7
`05:00` ▇▇▇▇▇▇▇▇▇▇ 71
`06:00` ▇▇▇▇▇▇ 44
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 213
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 122
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 121
`10:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 88
`11:00` ▇▇ 11
`23:00` ▇▇▇▇ 26

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.183
45.148.10.151
2.57.122.76
45.148.10.152
45.148.10.141
62.60.130.253
62.60.130.242
62.60.130.201
45.148.10.157
193.47.62.69
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
