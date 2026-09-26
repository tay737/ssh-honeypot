---
title: "Daily SSH Honeypot Threat Report — 2026-09-25"
date: 2026-09-25T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1402 SSH brute-force attempts from 89 unique IPs across 25 countries hit the honeypot on 2026-09-25."
---

# Daily SSH Honeypot Threat Report — 2026-09-25

*Data window: `2026-09-25` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-25

*Map snapshot unavailable (<urlopen error [Errno 113] No route to host>). Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,402 attempts** from **89 unique IPs** in **25 countries** (58.4/hour average)
- **Top attacker:** `77.239.124.210` — 70 attempts (Banatsync SRL, Paris, France)
- **Top source country:** The Netherlands — 266 (19%)
- **Most targeted account:** `root` — 749 (53%)
- **Peak hour:** 11:00–12:00 UTC — 162 attempts
- **First-time attackers:** 68 of 89 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `77.239.124.210` | 70 | 5.0% | Banatsync SRL | Paris, France | 10:54 | 13:16 |
| 2 | `45.148.10.157` | 65 | 4.6% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:33 | 13:04 |
| 3 | `62.60.130.201` | 58 | 4.1% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:47 | 11:41 |
| 4 | `109.160.32.29` | 55 | 3.9% | TechTies Inc. | Cornelius, United States | 00:05 | 01:49 |
| 5 | `125.141.72.225` | 55 | 3.9% | Korea Telecom | Seoul, South Korea | 05:10 | 13:19 |
| 6 | `193.47.62.69` | 55 | 3.9% | BestDC Limited | Andorra la Vella, Andorra | 01:38 | 13:10 |
| 7 | `45.148.10.151` | 55 | 3.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:07 | 12:34 |
| 8 | `109.160.32.61` | 53 | 3.8% | TechTies Inc. | Cornelius, United States | 10:45 | 12:28 |
| 9 | `45.148.10.152` | 50 | 3.6% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:22 | 13:20 |
| 10 | `62.60.130.242` | 50 | 3.6% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:17 | 13:26 |
| 11 | `62.60.130.253` | 50 | 3.6% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:52 | 12:29 |
| 12 | `45.148.10.141` | 40 | 2.9% | Techoff SRV Limited | Amsterdam, The Netherlands | 03:43 | 12:44 |
| 13 | `92.118.39.49` | 40 | 2.9% | Unmanaged LTD | Dallas, United States | 04:28 | 06:10 |
| 14 | `43.134.84.150` | 32 | 2.3% | Shenzhen Tencent Computer Systems Company Limited | Singapore, Singapore | 04:58 | 09:32 |
| 15 | `80.94.92.234` | 30 | 2.1% | Unmanaged LTD | Amsterdam, The Netherlands | 06:47 | 08:39 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 266 | 19.0% | ████················ |
| United States | 209 | 14.9% | ███················· |
| Iran | 188 | 13.4% | ███················· |
| South Korea | 127 | 9.1% | ██·················· |
| France | 121 | 8.6% | ██·················· |
| Indonesia | 73 | 5.2% | █··················· |
| China | 61 | 4.4% | █··················· |
| Andorra | 55 | 3.9% | █··················· |
| Hong Kong | 46 | 3.3% | █··················· |
| United Kingdom | 45 | 3.2% | █··················· |
| India | 42 | 3.0% | █··················· |
| Singapore | 32 | 2.3% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 254 | 18.1% | ████················ |
| Tehran | 188 | 13.4% | ███················· |
| Cornelius, North Carolina | 108 | 7.7% | ██·················· |
| Paris, Île-de-France | 78 | 5.6% | █··················· |
| Seoul | 71 | 5.1% | █··················· |
| Andorra la Vella | 55 | 3.9% | █··················· |
| Rushden, England | 45 | 3.2% | █··················· |
| Dallas, Texas | 40 | 2.9% | █··················· |
| Jakarta | 40 | 2.9% | █··················· |
| Singapore, North West | 32 | 2.3% | ···················· |
| Hong Kong, Kowloon | 28 | 2.0% | ···················· |
| Roubaix, Hauts-de-France | 24 | 1.7% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 749 | 53.4% | ███████████········· |
| `admin` | 68 | 4.9% | █··················· |
| `ubuntu` | 28 | 2.0% | ···················· |
| `user` | 22 | 1.6% | ···················· |
| `support` | 16 | 1.1% | ···················· |
| `developer` | 14 | 1.0% | ···················· |
| `supervisor` | 12 | 0.9% | ···················· |
| `user1` | 11 | 0.8% | ···················· |
| `claude` | 10 | 0.7% | ···················· |
| `deploy` | 10 | 0.7% | ···················· |
| `test` | 10 | 0.7% | ···················· |
| `default` | 8 | 0.6% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 210 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 158 |
| `AS47890 UNMANAGED LTD` | 129 |
| `AS4766 Korea Telecom` | 110 |
| `AS197170 TechTies Inc.` | 108 |
| `AS198364 BANATSYNC SRL` | 70 |

## First-time attackers

`77.239.124.210` (70), `125.141.72.225` (55), `109.160.32.61` (53), `92.118.39.49` (40), `43.134.84.150` (32), `36.64.131.68` (22), `161.35.179.218` (22), `158.220.124.17` (19), `20.217.80.108` (19), `103.194.243.199` (18), `43.157.200.91` (18), `172.172.131.149` (18), `152.32.212.226` (16), `69.5.20.133` (16), `14.53.119.248` (16), `211.46.188.16` (16), `103.172.20.218` (16), `85.133.193.72` (16), `65.254.95.164` (16), `203.145.143.163` (16), `112.216.120.67` (16), `27.110.166.67` (15), `218.150.184.241` (15), `81.10.31.125` (15), `78.109.200.147` (14), `171.104.143.176` (14), `51.75.247.232` (12), `166.62.41.13` (11), `45.195.221.26` (11), `165.154.162.74` (10), `106.120.205.138` (8), `14.103.118.61` (8), `154.182.139.162` (6), `101.96.225.252` (6), `120.48.80.100` (6), `113.141.171.139` (6), `138.226.239.234` (5), `80.94.95.115` (4), `219.78.240.92` (3), `138.226.239.233` (3), `153.37.177.219` (2), `111.70.32.8` (2), `111.70.29.158` (2), `180.76.52.146` (2), `211.22.222.251` (2), `83.239.84.130` (2), `122.187.225.28` (2), `217.150.37.249` (2), `103.103.53.44` (2), `136.185.6.181` (2), `65.20.134.110` (2), `217.24.185.98` (2), `104.244.79.113` (2), `121.178.185.141` (2), `175.198.18.3` (2), `160.30.39.50` (2), `111.70.11.78` (2), `218.149.235.152` (2), `197.219.228.250` (2), `59.23.15.223` (2), `213.230.64.246` (2), `203.252.10.4` (1), `78.68.69.14` (1), `36.92.35.211` (1), `125.94.107.91` (1), `80.94.95.116` (1), `111.70.32.210` (1), `116.48.151.249` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇ 71
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 101
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 111
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 101
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 98
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 150
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 64
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 81
`08:00` ▇▇▇▇▇ 25
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 115
`10:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 111
`11:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 162
`12:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 150
`13:00` ▇▇▇▇▇▇▇▇▇▇▇ 62

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
77.239.124.210
45.148.10.157
62.60.130.201
109.160.32.29
125.141.72.225
193.47.62.69
45.148.10.151
109.160.32.61
45.148.10.152
62.60.130.242
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
