---
title: "Daily SSH Honeypot Threat Report — 2026-09-20"
date: 2026-09-20T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "881 SSH brute-force attempts from 34 unique IPs across 15 countries hit the honeypot on 2026-09-20."
---

# Daily SSH Honeypot Threat Report — 2026-09-20

*Data window: `2026-09-20` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.comday in progress, stats partial*

## Attack map — 2026-09-20

<img width="2000" height="1240" alt="ssh-threats-2026-09-20" src="https://github.com/user-attachments/assets/299f427e-7739-4540-8fe3-e789e3eb30df" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **881 attempts** from **34 unique IPs** in **15 countries** (36.7/hour average)
- **Top attacker:** `45.148.10.141` — 75 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 335 (38%)
- **Most targeted account:** `root` — 606 (69%)
- **Peak hour:** 02:00–03:00 UTC — 123 attempts
- **First-time attackers:** 21 of 34 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.141` | 75 | 8.5% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:08 | 12:01 |
| 2 | `45.148.10.151` | 65 | 7.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:24 | 11:51 |
| 3 | `109.160.32.62` | 60 | 6.8% | TechTies Inc. | Cornelius, United States | 09:52 | 11:48 |
| 4 | `193.47.62.69` | 60 | 6.8% | BestDC Limited | Andorra la Vella, Andorra | 00:30 | 11:41 |
| 5 | `45.148.10.157` | 55 | 6.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:35 | 11:46 |
| 6 | `62.60.130.201` | 50 | 5.7% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:19 | 11:20 |
| 7 | `77.239.124.184` | 47 | 5.3% | Banatsync SRL | Paris, France | 05:18 | 06:42 |
| 8 | `109.160.32.75` | 45 | 5.1% | TechTies Inc. | Cornelius, United States | 05:53 | 07:15 |
| 9 | `45.148.10.152` | 45 | 5.1% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:03 | 11:36 |
| 10 | `62.60.130.242` | 45 | 5.1% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 02:26 | 12:17 |
| 11 | `62.60.130.253` | 38 | 4.3% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 02:36 | 11:56 |
| 12 | `4.240.96.30` | 28 | 3.2% | Microsoft Corporation | Pune, India | 02:40 | 04:13 |
| 13 | `80.94.92.179` | 28 | 3.2% | Unmanaged LTD | Amsterdam, The Netherlands | 00:26 | 01:39 |
| 14 | `2.57.122.238` | 26 | 3.0% | Unmanaged LTD | Amsterdam, The Netherlands | 03:35 | 04:35 |
| 15 | `45.181.45.238` | 20 | 2.3% | Generacion Wi-fi SA | Necochea, Argentina | 05:22 | 06:03 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 335 | 38.0% | ████████············ |
| Iran | 133 | 15.1% | ███················· |
| United States | 111 | 12.6% | ███················· |
| Andorra | 65 | 7.4% | █··················· |
| China | 50 | 5.7% | █··················· |
| France | 47 | 5.3% | █··················· |
| India | 45 | 5.1% | █··················· |
| Argentina | 20 | 2.3% | ···················· |
| Italy | 19 | 2.2% | ···················· |
| South Africa | 18 | 2.0% | ···················· |
| Bolivia | 17 | 1.9% | ···················· |
| Russia | 13 | 1.5% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 335 | 38.0% | ████████············ |
| Tehran | 133 | 15.1% | ███················· |
| Cornelius, North Carolina | 105 | 11.9% | ██·················· |
| Andorra la Vella | 65 | 7.4% | █··················· |
| Paris, Île-de-France | 47 | 5.3% | █··················· |
| Pune, Maharashtra | 28 | 3.2% | █··················· |
| Necochea, Buenos Aires | 20 | 2.3% | ···················· |
| Haidian, Beijing | 19 | 2.2% | ···················· |
| Tenno, Trentino-Alto Adige | 19 | 2.2% | ···················· |
| Johannesburg, Gauteng | 18 | 2.0% | ···················· |
| La Paz, La Paz Department | 17 | 1.9% | ···················· |
| Liuxiang, Shanxi | 17 | 1.9% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 606 | 68.8% | ██████████████······ |
| `admin` | 28 | 3.2% | █··················· |
| `test` | 16 | 1.8% | ···················· |
| `ubuntu` | 16 | 1.8% | ···················· |
| `deploy` | 8 | 0.9% | ···················· |
| `minecraft` | 8 | 0.9% | ···················· |
| `sol` | 6 | 0.7% | ···················· |
| `azureuser` | 4 | 0.5% | ···················· |
| `master` | 4 | 0.5% | ···················· |
| `montse` | 4 | 0.5% | ···················· |
| `node` | 4 | 0.5% | ···················· |
| `redash` | 4 | 0.5% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 245 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 133 |
| `AS197170 TechTies Inc.` | 105 |
| `AS47890 UNMANAGED LTD` | 93 |
| `AS216014 BestDC Limited` | 60 |
| `AS198364 BANATSYNC SRL` | 47 |

## First-time attackers

`109.160.32.62` (60), `77.239.124.184` (47), `109.160.32.75` (45), `4.240.96.30` (28), `45.181.45.238` (20), `78.134.49.171` (19), `102.210.149.105` (18), `117.34.85.168` (17), `190.181.25.210` (17), `125.20.16.22` (17), `2.57.122.150` (15), `124.174.32.95` (14), `80.247.110.206` (13), `94.154.43.254` (8), `180.167.207.234` (6), `106.12.148.154` (5), `118.145.240.6` (5), `210.123.88.216` (5), `119.119.6.53` (3), `34.140.22.32` (2), `77.90.185.107` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 63
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 81
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 123
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 77
`04:00` ▇▇▇▇▇▇▇▇ 33
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 83
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 70
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 56
`08:00` ▇▇▇▇▇▇▇▇▇▇▇ 46
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59
`10:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 97
`11:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 83
`12:00` ▇▇ 10

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.141
45.148.10.151
109.160.32.62
193.47.62.69
45.148.10.157
62.60.130.201
77.239.124.184
109.160.32.75
45.148.10.152
62.60.130.242
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
