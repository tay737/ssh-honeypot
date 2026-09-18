---
title: "Daily SSH Honeypot Threat Report — 2026-09-16"
date: 2026-09-16T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "734 SSH brute-force attempts from 26 unique IPs across 13 countries hit the honeypot on 2026-09-16."
---

# Daily SSH Honeypot Threat Report — 2026-09-16

*Data window: `2026-09-16` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## At a glance...

- **734 attempts** from **26 unique IPs** in **13 countries** (30.6/hour average)
- **Top attacker:** `193.47.62.69` — 65 attempts (BestDC Limited, Andorra la Vella, Andorra)
- **Top source country:** The Netherlands — 368 (50%)
- **Most targeted account:** `root` — 562 (77%)
- **Peak hour:** 07:00–08:00 UTC — 64 attempts
- **First-time attackers:** 26 of 26 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `193.47.62.69` | 65 | 8.9% | BestDC Limited | Andorra la Vella, Andorra | 04:08 | 15:35 |
| 2 | `45.148.10.141` | 65 | 8.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:36 | 16:55 |
| 3 | `45.148.10.151` | 65 | 8.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 05:42 | 16:35 |
| 4 | `45.148.10.157` | 65 | 8.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:30 | 16:48 |
| 5 | `109.160.32.39` | 64 | 8.7% | TechTies Inc. | Cornelius, United States | 02:15 | 04:19 |
| 6 | `45.148.10.152` | 60 | 8.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:41 | 17:01 |
| 7 | `62.60.130.253` | 60 | 8.2% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 05:04 | 16:28 |
| 8 | `80.94.92.234` | 50 | 6.8% | Unmanaged LTD | Amsterdam, The Netherlands | 11:57 | 14:18 |
| 9 | `176.53.159.198` | 47 | 6.4% | Zorntech Web Solutions | Istanbul, Turkey | 08:09 | 16:03 |
| 10 | `62.60.130.242` | 40 | 5.4% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:19 | 13:55 |
| 11 | `176.53.159.197` | 38 | 5.2% | Zorntech Web Solutions | Istanbul, Turkey | 08:08 | 15:58 |
| 12 | `2.57.122.238` | 26 | 3.5% | Unmanaged LTD | Amsterdam, The Netherlands | 07:04 | 08:04 |
| 13 | `193.32.162.84` | 22 | 3.0% | Unmanaged LTD | Amsterdam, The Netherlands | 06:45 | 11:22 |
| 14 | `2.57.122.209` | 15 | 2.0% | Unmanaged LTD | Amsterdam, The Netherlands | 02:09 | 02:45 |
| 15 | `120.48.165.75` | 10 | 1.4% | Baidu | Beijing, China | 02:08 | 02:24 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 368 | 50.1% | ██████████·········· |
| Iran | 100 | 13.6% | ███················· |
| Turkey | 85 | 11.6% | ██·················· |
| Andorra | 75 | 10.2% | ██·················· |
| United States | 69 | 9.4% | ██·················· |
| China | 11 | 1.5% | ···················· |
| Russia | 6 | 0.8% | ···················· |
| Finland | 5 | 0.7% | ···················· |
| Hong Kong | 5 | 0.7% | ···················· |
| South Korea | 4 | 0.5% | ···················· |
| Belgium | 3 | 0.4% | ···················· |
| Switzerland | 2 | 0.3% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 368 | 50.1% | ██████████·········· |
| Tehran | 100 | 13.6% | ███················· |
| Istanbul | 85 | 11.6% | ██·················· |
| Andorra la Vella | 75 | 10.2% | ██·················· |
| Cornelius, North Carolina | 64 | 8.7% | ██·················· |
| Beijing | 11 | 1.5% | ···················· |
| St Petersburg, St.-Petersburg | 6 | 0.8% | ···················· |
| Dallas, Texas | 5 | 0.7% | ···················· |
| Helsinki, Uusimaa | 5 | 0.7% | ···················· |
| Wan Chai | 5 | 0.7% | ···················· |
| Seo-gu, Daegu | 4 | 0.5% | ···················· |
| Brussels, Brussels Capital | 3 | 0.4% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 562 | 76.6% | ███████████████····· |
| `admin` | 37 | 5.0% | █··················· |
| `user` | 14 | 1.9% | ···················· |
| `support` | 12 | 1.6% | ···················· |
| `test` | 11 | 1.5% | ···················· |
| `ubuntu` | 8 | 1.1% | ···················· |
| `debian` | 6 | 0.8% | ···················· |
| `developer` | 6 | 0.8% | ···················· |
| `git` | 6 | 0.8% | ···················· |
| `pi` | 6 | 0.8% | ···················· |
| `sol` | 6 | 0.8% | ···················· |
| `telecomadmin` | 6 | 0.8% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 265 |
| `AS47890 UNMANAGED LTD` | 118 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 100 |
| `AS154383 ZORNTECH WEB SOLUTIONS` | 85 |
| `AS216014 BestDC Limited` | 65 |
| `AS197170 TechTies Inc.` | 64 |

## First-time attackers

`45.148.10.141` (65), `45.148.10.157` (65), `193.47.62.69` (65), `45.148.10.151` (65), `109.160.32.39` (64), `62.60.130.253` (60), `45.148.10.152` (60), `80.94.92.234` (50), `176.53.159.198` (47), `62.60.130.242` (40), `176.53.159.197` (38), `2.57.122.238` (26), `193.32.162.84` (22), `2.57.122.209` (15), `120.48.165.75` (10), `195.178.110.217` (10), `188.227.111.138` (6), `185.225.203.84` (5), `39.109.109.136` (5), `92.118.39.50` (5), `218.157.163.203` (4), `209.99.187.10` (2), `34.77.16.133` (2), `46.217.229.3` (1), `34.62.141.115` (1), `125.34.226.59` (1)

## Hourly timeline (UTC)

`00:00` ▇ 1
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 49
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 40
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 54
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 53
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 55
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 64
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 64
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 60
`10:00` ▇▇▇▇▇▇▇ 14
`11:00` ▇▇▇▇▇▇▇▇▇▇▇ 24
`12:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 40
`13:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 57
`14:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 62
`15:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 36
`16:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 54
`17:00` ▇▇▇ 7

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall:

```text
193.47.62.69
45.148.10.141
45.148.10.151
45.148.10.157
109.160.32.39
45.148.10.152
62.60.130.253
80.94.92.234
176.53.159.198
62.60.130.242
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
