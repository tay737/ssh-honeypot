---
title: "Daily SSH Honeypot Threat Report — 2026-09-20"
date: 2026-09-20T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1527 SSH brute-force attempts from 70 unique IPs across 24 countries hit the honeypot on 2026-09-20."
---

# Daily SSH Honeypot Threat Report — 2026-09-20

*Data window: `2026-09-20` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-20

<img width="2000" height="1240" alt="ssh-threats-2026-09-20" src="https://github.com/user-attachments/assets/5bb06522-8636-49f6-885c-cbfad76c76cc" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,527 attempts** from **70 unique IPs** in **24 countries** (63.6/hour average)
- **Top attacker:** `45.148.10.141` — 105 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 496 (32%)
- **Most targeted account:** `root` — 947 (62%)
- **Peak hour:** 16:00–17:00 UTC — 129 attempts
- **First-time attackers:** 55 of 70 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.141` | 105 | 6.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:08 | 21:15 |
| 2 | `193.47.62.69` | 85 | 5.6% | BestDC Limited | Andorra la Vella, Andorra | 00:30 | 21:25 |
| 3 | `45.148.10.151` | 85 | 5.6% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:24 | 21:45 |
| 4 | `45.148.10.152` | 70 | 4.6% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:03 | 21:35 |
| 5 | `109.160.32.62` | 60 | 3.9% | TechTies Inc. | Cornelius, United States | 09:52 | 11:48 |
| 6 | `45.148.10.157` | 60 | 3.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 00:35 | 16:59 |
| 7 | `62.60.130.201` | 60 | 3.9% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 00:19 | 21:30 |
| 8 | `62.60.130.242` | 60 | 3.9% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 02:26 | 21:51 |
| 9 | `109.160.32.64` | 56 | 3.7% | TechTies Inc. | Cornelius, United States | 14:09 | 15:54 |
| 10 | `62.60.130.253` | 53 | 3.5% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 02:36 | 21:10 |
| 11 | `77.239.124.184` | 47 | 3.1% | Banatsync SRL | Paris, France | 05:18 | 06:42 |
| 12 | `109.160.32.75` | 45 | 2.9% | TechTies Inc. | Cornelius, United States | 05:53 | 07:15 |
| 13 | `2.57.122.150` | 45 | 2.9% | Unmanaged LTD | Amsterdam, The Netherlands | 01:59 | 16:17 |
| 14 | `2.57.122.209` | 36 | 2.4% | Unmanaged LTD | Amsterdam, The Netherlands | 12:49 | 23:26 |
| 15 | `4.240.96.30` | 28 | 1.8% | Microsoft Corporation | Pune, India | 02:40 | 04:13 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 496 | 32.5% | ██████·············· |
| United States | 217 | 14.2% | ███················· |
| Iran | 173 | 11.3% | ██·················· |
| Andorra | 90 | 5.9% | █··················· |
| China | 75 | 4.9% | █··················· |
| Russia | 65 | 4.3% | █··················· |
| France | 54 | 3.5% | █··················· |
| Vietnam | 50 | 3.3% | █··················· |
| India | 45 | 2.9% | █··················· |
| South Korea | 37 | 2.4% | ···················· |
| Hong Kong | 33 | 2.2% | ···················· |
| Indonesia | 21 | 1.4% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 492 | 32.2% | ██████·············· |
| Cornelius, North Carolina | 177 | 11.6% | ██·················· |
| Tehran | 173 | 11.3% | ██·················· |
| Andorra la Vella | 90 | 5.9% | █··················· |
| Paris, Île-de-France | 47 | 3.1% | █··················· |
| Moscow | 34 | 2.2% | ···················· |
| Hanoi | 28 | 1.8% | ···················· |
| Pune, Maharashtra | 28 | 1.8% | ···················· |
| Las Vegas, Nevada | 21 | 1.4% | ···················· |
| Lusaka, Lusaka Province | 20 | 1.3% | ···················· |
| Necochea, Buenos Aires | 20 | 1.3% | ···················· |
| Rushden, England | 20 | 1.3% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 947 | 62.0% | ████████████········ |
| `admin` | 91 | 6.0% | █··················· |
| `test` | 28 | 1.8% | ···················· |
| `ubuntu` | 28 | 1.8% | ···················· |
| `deploy` | 10 | 0.7% | ···················· |
| `ads` | 8 | 0.5% | ···················· |
| `minecraft` | 8 | 0.5% | ···················· |
| `svnadmin` | 8 | 0.5% | ···················· |
| `salomon` | 7 | 0.5% | ···················· |
| `support` | 7 | 0.5% | ···················· |
| `user` | 7 | 0.5% | ···················· |
| `admin1` | 6 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 325 |
| `AS47890 UNMANAGED LTD` | 184 |
| `AS197170 TechTies Inc.` | 177 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 173 |
| `AS216014 BestDC Limited` | 85 |
| `AS198364 BANATSYNC SRL` | 47 |

## First-time attackers

`109.160.32.62` (60), `109.160.32.64` (56), `77.239.124.184` (47), `109.160.32.75` (45), `2.57.122.150` (45), `4.240.96.30` (28), `102.23.122.235` (20), `45.181.45.238` (20), `78.134.49.171` (19), `45.119.212.99` (19), `102.210.149.105` (18), `220.246.183.78` (18), `123.25.115.112` (18), `46.191.141.152` (18), `117.34.85.168` (17), `81.211.72.167` (17), `125.20.16.22` (17), `80.253.31.232` (17), `190.181.25.210` (17), `221.162.218.85` (16), `109.160.32.208` (16), `38.224.49.7` (16), `209.141.47.217` (16), `115.178.75.243` (16), `165.154.70.139` (15), `163.7.13.17` (15), `124.174.32.95` (14), `201.149.53.243` (14), `80.247.110.206` (13), `197.153.57.103` (13), `136.36.189.65` (13), `123.25.115.189` (10), `222.71.205.34` (8), `94.154.43.254` (8), `2.57.121.25` (8), `2.57.121.112` (7), `36.151.150.93` (7), `37.187.35.26` (7), `141.95.54.130` (7), `43.129.33.101` (6), `125.122.37.247` (6), `180.167.207.234` (6), `140.150.226.84` (6), `118.145.240.6` (5), `106.12.148.154` (5), `144.172.105.41` (5), `210.123.88.216` (5), `193.46.255.86` (5), `107.189.27.179` (4), `203.150.107.87` (4), `121.229.25.10` (4), `103.159.51.70` (3), `119.119.6.53` (3), `34.140.22.32` (2), `77.90.185.107` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 63
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 81
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 123
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 77
`04:00` ▇▇▇▇▇▇▇▇ 33
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 83
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 70
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇ 56
`08:00` ▇▇▇▇▇▇▇▇▇▇▇ 46
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59
`10:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 97
`11:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 83
`12:00` ▇▇▇▇▇▇▇▇▇▇▇ 46
`13:00` ▇▇▇▇▇▇ 24
`14:00` ▇▇▇▇▇▇▇▇▇▇ 41
`15:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 116
`16:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 129
`17:00` ▇▇▇▇▇ 23
`20:00` ▇▇▇ 15
`21:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 124
`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 78
`23:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 60

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.141
193.47.62.69
45.148.10.151
45.148.10.152
109.160.32.62
45.148.10.157
62.60.130.201
62.60.130.242
109.160.32.64
62.60.130.253
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
