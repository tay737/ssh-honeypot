---
title: "Daily SSH Honeypot Threat Report — 2026-09-23"
date: 2026-09-23T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "928 SSH brute-force attempts from 62 unique IPs across 27 countries hit the honeypot on 2026-09-23."
---

# Daily SSH Honeypot Threat Report — 2026-09-23

*Data window: `2026-09-23` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-23

<img width="2000" height="1240" alt="ssh-threats-2026-09-23" src="https://github.com/user-attachments/assets/582529fa-716f-4c7b-9634-a683a4ef39a3" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **928 attempts** from **62 unique IPs** in **27 countries** (38.7/hour average)
- **Top attacker:** `45.148.10.151` — 50 attempts (Techoff SRV Limited, Amsterdam, The Netherlands)
- **Top source country:** United States — 151 (16%)
- **Most targeted account:** `root` — 525 (57%)
- **Peak hour:** 23:00–24:00 UTC — 176 attempts
- **First-time attackers:** 47 of 62 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `45.148.10.151` | 50 | 5.4% | Techoff SRV Limited | Amsterdam, The Netherlands | 13:17 | 23:02 |
| 2 | `62.60.130.242` | 45 | 4.8% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 13:07 | 23:56 |
| 3 | `109.160.32.109` | 44 | 4.7% | TechTies Inc. | Cornelius, United States | 22:21 | 23:43 |
| 4 | `62.60.130.253` | 40 | 4.3% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 14:06 | 23:27 |
| 5 | `176.53.159.198` | 36 | 3.9% | Zorntech Web Solutions | Istanbul, Turkey | 10:17 | 23:53 |
| 6 | `176.53.159.197` | 33 | 3.6% | Zorntech Web Solutions | Istanbul, Turkey | 10:07 | 23:41 |
| 7 | `45.148.10.141` | 30 | 3.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 14:25 | 23:46 |
| 8 | `62.60.130.201` | 30 | 3.2% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 13:12 | 23:36 |
| 9 | `46.191.141.152` | 29 | 3.1% | JSC "Ufanet" | Ufa, Russia | 06:17 | 07:19 |
| 10 | `92.118.39.50` | 26 | 2.8% | Unmanaged LTD | Dallas, United States | 14:48 | 16:20 |
| 11 | `193.47.62.69` | 25 | 2.7% | BestDC Limited | Andorra la Vella, Andorra | 13:41 | 22:52 |
| 12 | `103.63.108.25` | 20 | 2.2% | Hai Phong Brand - CMC Telecommunication Infrastructure Corporation | Haiphong, Vietnam | 07:44 | 08:21 |
| 13 | `45.148.10.152` | 20 | 2.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 13:37 | 22:42 |
| 14 | `45.148.10.157` | 20 | 2.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 13:51 | 22:12 |
| 15 | `51.124.186.154` | 20 | 2.2% | Microsoft | Amsterdam, Netherlands | 08:57 | 09:33 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| United States | 151 | 16.3% | ███················· |
| The Netherlands | 148 | 15.9% | ███················· |
| Iran | 115 | 12.4% | ██·················· |
| China | 78 | 8.4% | ██·················· |
| Turkey | 69 | 7.4% | █··················· |
| Russia | 52 | 5.6% | █··················· |
| Vietnam | 37 | 4.0% | █··················· |
| Hong Kong | 36 | 3.9% | █··················· |
| India | 28 | 3.0% | █··················· |
| Andorra | 25 | 2.7% | █··················· |
| Netherlands | 20 | 2.2% | ···················· |
| Brazil | 19 | 2.0% | ···················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 168 | 18.1% | ████················ |
| Tehran | 115 | 12.4% | ██·················· |
| Istanbul | 69 | 7.4% | █··················· |
| Cornelius, North Carolina | 44 | 4.7% | █··················· |
| Hong Kong, Kowloon | 36 | 3.9% | █··················· |
| Ufa, Bashkortostan Republic | 29 | 3.1% | █··················· |
| Dallas, Texas | 26 | 2.8% | █··················· |
| Andorra la Vella | 25 | 2.7% | █··················· |
| Guangzhou, Guangdong | 25 | 2.7% | █··················· |
| Haiphong, Hai Phong | 20 | 2.2% | ···················· |
| Montenegro, Rio Grande do Sul | 19 | 2.0% | ···················· |
| Shanghai | 18 | 1.9% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 525 | 56.6% | ███████████········· |
| `admin` | 43 | 4.6% | █··················· |
| `ubuntu` | 16 | 1.7% | ···················· |
| `support` | 12 | 1.3% | ···················· |
| `user` | 9 | 1.0% | ···················· |
| `ftpuser` | 8 | 0.9% | ···················· |
| `telecomadmin` | 6 | 0.6% | ···················· |
| `alan` | 4 | 0.4% | ···················· |
| `baptiste` | 4 | 0.4% | ···················· |
| `dario` | 4 | 0.4% | ···················· |
| `dbadmin` | 4 | 0.4% | ···················· |
| `deploy` | 4 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 120 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 115 |
| `AS154383 ZORNTECH WEB SOLUTIONS` | 69 |
| `AS135377 UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED` | 44 |
| `AS197170 TechTies Inc.` | 44 |
| `AS47890 UNMANAGED LTD` | 43 |

## First-time attackers

`109.160.32.109` (44), `103.63.108.25` (20), `51.124.186.154` (20), `201.76.120.30` (19), `101.227.203.162` (18), `203.83.231.93` (17), `113.164.66.10` (17), `152.32.220.188` (16), `103.123.53.88` (16), `101.36.125.2` (16), `172.191.239.155` (16), `114.34.106.146` (16), `199.241.120.131` (15), `200.121.10.45` (15), `108.30.131.224` (15), `43.133.140.5` (15), `192.9.228.120` (14), `176.31.21.38` (14), `45.116.78.92` (14), `106.44.24.2` (13), `91.231.218.149` (12), `197.5.145.114` (12), `107.150.105.153` (12), `136.232.11.10` (12), `73.93.207.215` (12), `82.146.38.18` (11), `14.18.236.71` (8), `180.76.103.111` (8), `51.254.130.161` (7), `143.110.145.158` (6), `218.206.136.24` (6), `51.195.149.120` (6), `103.112.54.86` (6), `119.28.46.114` (6), `51.77.158.34` (5), `78.27.115.34` (5), `213.238.225.106` (5), `139.19.117.129` (4), `14.103.86.48` (4), `116.255.227.108` (2), `31.77.11.146` (2), `41.193.100.133` (2), `34.53.192.72` (2), `115.190.249.177` (2), `61.76.136.25` (2), `61.222.211.114` (2), `34.78.215.232` (1)

## Hourly timeline (UTC)

`06:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 90
`07:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 89
`08:00` ▇▇▇▇▇▇▇ 41
`09:00` ▇▇▇▇▇▇▇▇▇▇ 58
`10:00` ▇▇▇▇▇ 28
`11:00` ▇▇ 10
`12:00` ▇▇▇▇▇▇▇▇▇ 53
`13:00` ▇▇▇▇▇▇▇▇▇ 52
`14:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 69
`15:00` ▇▇▇▇▇▇▇▇▇▇▇▇ 72
`16:00` ▇▇▇▇▇▇▇▇▇▇ 57
`17:00` ▇ 5
`21:00` ▇▇▇ 16
`22:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 112
`23:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 176

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
45.148.10.151
62.60.130.242
109.160.32.109
62.60.130.253
176.53.159.198
176.53.159.197
45.148.10.141
62.60.130.201
46.191.141.152
92.118.39.50
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
