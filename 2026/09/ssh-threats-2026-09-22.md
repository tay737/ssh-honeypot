---
title: "Daily SSH Honeypot Threat Report — 2026-09-22"
date: 2026-09-22T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1391 SSH brute-force attempts from 75 unique IPs across 28 countries hit the honeypot on 2026-09-22."
---

# Daily SSH Honeypot Threat Report — 2026-09-22

*Data window: `2026-09-22` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-22

*Map snapshot unavailable (<urlopen error [Errno 113] No route to host>). Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,391 attempts** from **75 unique IPs** in **28 countries** (58.0/hour average)
- **Top attacker:** `45.148.10.151` — 70 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** The Netherlands — 265 (19%)
- **Most targeted account:** `root` — 800 (58%)
- **Peak hour:** 14:00–15:00 UTC — 208 attempts
- **First-time attackers:** 57 of 75 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.151` | 70 | 5.0% | Techoff SRV Limited | Amsterdam, The Netherlands | 05:04 | 15:20 |
| 2 | `62.60.130.253` | 65 | 4.7% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:15 | 15:10 |
| 3 | `193.47.62.69` | 60 | 4.3% | BestDC Limited | Andorra la Vella, Andorra | 04:05 | 15:00 |
| 4 | `62.60.130.242` | 60 | 4.3% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 04:25 | 15:15 |
| 5 | `109.160.32.115` | 58 | 4.2% | TechTies Inc. | Cornelius, United States | 05:43 | 07:37 |
| 6 | `45.148.10.141` | 55 | 4.0% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:10 | 13:46 |
| 7 | `2.57.122.168` | 45 | 3.2% | Unmanaged LTD | Amsterdam, The Netherlands | 04:25 | 06:30 |
| 8 | `45.148.10.152` | 45 | 3.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 04:40 | 15:05 |
| 9 | `62.60.130.201` | 45 | 3.2% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 06:36 | 15:24 |
| 10 | `92.118.39.14` | 40 | 2.9% | Unmanaged LTD | Dallas, United States | 12:09 | 14:19 |
| 11 | `180.93.1.64` | 24 | 1.7% | SPT | Quận Bốn, Vietnam | 00:18 | 12:18 |
| 12 | `212.64.201.210` | 22 | 1.6% | Sunucun Bilgi Iletisim Teknolojileri ve Ticaret Ltd. Sti. | Istanbul, Turkey | 13:18 | 14:05 |
| 13 | `103.60.175.200` | 20 | 1.4% | Mazeda Networks Limited | Dhaka, Bangladesh | 08:36 | 09:14 |
| 14 | `163.227.161.160` | 20 | 1.4% | Upnet Technology Solutions Company Limited | Vạn Phúc, Vietnam | 08:54 | 09:33 |
| 15 | `187.51.208.158` | 20 | 1.4% | Vivo | São José do Rio Preto, Brazil | 13:22 | 14:01 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 265 | 19.1% | ████················ |
| Iran | 184 | 13.2% | ███················· |
| United States | 174 | 12.5% | ███················· |
| India | 68 | 4.9% | █··················· |
| Hong Kong | 64 | 4.6% | █··················· |
| Andorra | 60 | 4.3% | █··················· |
| Russia | 60 | 4.3% | █··················· |
| South Korea | 60 | 4.3% | █··················· |
| Indonesia | 47 | 3.4% | █··················· |
| Vietnam | 44 | 3.2% | █··················· |
| France | 39 | 2.8% | █··················· |
| Brazil | 38 | 2.7% | █··················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 265 | 19.1% | ████················ |
| Tehran | 184 | 13.2% | ███················· |
| Andorra la Vella | 60 | 4.3% | █··················· |
| Cornelius, North Carolina | 58 | 4.2% | █··················· |
| Dallas, Texas | 40 | 2.9% | █··················· |
| Hong Kong, Kowloon | 36 | 2.6% | █··················· |
| Frankfurt am Main, Hesse | 31 | 2.2% | ···················· |
| Moscow | 28 | 2.0% | ···················· |
| Roubaix, Hauts-de-France | 28 | 2.0% | ···················· |
| Seongnam-si, Gyeonggi-do | 26 | 1.9% | ···················· |
| Vaxjo, Kronoberg County | 25 | 1.8% | ···················· |
| Quận Bốn, Ho Chi Minh City (HCMC) | 24 | 1.7% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 800 | 57.5% | ████████████········ |
| `admin` | 67 | 4.8% | █··················· |
| `user` | 25 | 1.8% | ···················· |
| `ubuntu` | 24 | 1.7% | ···················· |
| `administrator` | 19 | 1.4% | ···················· |
| `david` | 10 | 0.7% | ···················· |
| `support` | 10 | 0.7% | ···················· |
| `devuser` | 8 | 0.6% | ···················· |
| `test` | 8 | 0.6% | ···················· |
| `user1` | 8 | 0.6% | ···················· |
| `adnan` | 7 | 0.5% | ···················· |
| `ansible` | 6 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 180 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 170 |
| `AS47890 UNMANAGED LTD` | 135 |
| `AS197170 TechTies Inc.` | 82 |
| `AS216014 BestDC Limited` | 60 |
| `AS4766 Korea Telecom` | 60 |

## First-time attackers

`109.160.32.115` (58), `212.64.201.210` (22), `36.92.41.115` (20), `163.227.161.160` (20), `58.69.56.44` (20), `190.253.97.166` (20), `187.51.208.158` (20), `103.60.175.200` (20), `217.216.79.92` (19), `156.245.246.50` (19), `172.214.209.153` (19), `13.72.83.77` (19), `4.224.40.94` (19), `182.73.176.186` (19), `222.110.147.58` (18), `163.7.6.41` (18), `177.130.250.31` (18), `156.225.20.213` (17), `102.220.161.85` (16), `125.31.2.160` (16), `14.63.217.28` (16), `51.75.27.218` (16), `175.198.62.180` (16), `102.91.123.220` (16), `104.199.176.250` (15), `58.152.42.212` (15), `64.202.191.109` (15), `212.3.155.8` (14), `49.64.169.153` (14), `109.194.108.203` (14), `31.76.34.47` (14), `212.33.198.115` (14), `171.25.158.50` (14), `195.58.38.201` (13), `81.192.46.29` (13), `103.143.231.24` (13), `159.65.224.88` (12), `51.254.103.32` (12), `93.152.221.37` (12), `171.25.158.68` (11), `172.252.13.101` (11), `87.106.29.151` (11), `211.254.212.59` (10), `27.150.188.148` (10), `103.151.141.99` (9), `114.67.127.241` (8), `182.74.206.194` (8), `93.152.221.210` (6), `118.107.139.224` (6), `102.220.160.38` (6), `45.153.34.117` (6), `46.6.127.33` (4), `34.79.60.218` (2), `49.248.250.122` (2), `117.48.147.99` (2), `185.100.212.141` (1), `104.155.100.207` (1)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇ 36
`01:00` ▇▇ 12
`02:00` ▇▇▇ 20
`03:00` ▇ 10
`04:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 165
`05:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 138
`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 134
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 102
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 81
`09:00` ▇▇▇▇▇▇▇▇▇▇▇ 74
`10:00` ▇▇▇▇▇▇▇▇▇ 63
`11:00` ▇▇▇▇▇▇▇▇ 57
`12:00` ▇▇▇▇▇▇▇▇▇▇▇ 76
`13:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 154
`14:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 208
`15:00` ▇▇▇▇▇▇▇▇▇ 61

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.151
62.60.130.253
193.47.62.69
62.60.130.242
109.160.32.115
45.148.10.141
2.57.122.168
45.148.10.152
62.60.130.201
92.118.39.14
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
