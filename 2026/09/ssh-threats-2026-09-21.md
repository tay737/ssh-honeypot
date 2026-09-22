---
title: "Daily SSH Honeypot Threat Report — 2026-09-21"
date: 2026-09-21T06:00:00Z
tags: [honeypot, ssh, security, threat-intel, brute-force]
description: "1436 SSH brute-force attempts from 71 unique IPs across 25 countries hit the honeypot on 2026-09-21."
---

# Daily SSH Honeypot Threat Report — 2026-09-21

*Data window: `2026-09-21` 00:00–24:00 UTC · source: ssh-log-to-influx collector · geolocation: ip-api.com*

## Attack map — 2026-09-21

<img width="2000" height="1240" alt="ssh-threats-2026-09-21" src="https://github.com/user-attachments/assets/ad545440-7856-4c4b-8760-8fbdb62da787" />

*Live interactive version: Grafana → Security → “SSH Login Attempts — Geohash”.*

## At a glance

- **1,436 attempts** from **71 unique IPs** in **25 countries** (59.8/hour average)
- **Top attacker:** `77.239.124.215` — 76 attempts (Banatsync SRL, Paris, France)
- **Top source country:** The Netherlands — 336 (23%)
- **Most targeted account:** `root` — 894 (62%)
- **Peak hour:** 01:00–02:00 UTC — 232 attempts
- **First-time attackers:** 49 of 71 IPs had never been seen before this day

## Top attacking IPs

| # | IP | Attempts | Share | ISP | Location | First | Last |
|---|---|---|---|---|---|---|---|
| 1 | `77.239.124.215` | 76 | 5.3% | Banatsync SRL | Paris, France | 02:02 | 04:36 |
| 2 | `45.148.10.151` | 75 | 5.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:04 | 12:54 |
| 3 | `109.160.32.219` | 66 | 4.6% | TechTies Inc. | Cornelius, United States | 07:28 | 09:37 |
| 4 | `45.148.10.157` | 65 | 4.5% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:22 | 12:06 |
| 5 | `45.148.10.141` | 60 | 4.2% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:45 | 12:51 |
| 6 | `109.160.32.101` | 55 | 3.8% | TechTies Inc. | Cornelius, United States | 00:05 | 01:49 |
| 7 | `62.60.130.242` | 55 | 3.8% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:10 | 12:35 |
| 8 | `62.60.130.253` | 55 | 3.8% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 02:11 | 12:57 |
| 9 | `193.47.62.69` | 50 | 3.5% | BestDC Limited | Andorra la Vella, Andorra | 01:33 | 12:41 |
| 10 | `45.148.10.152` | 48 | 3.3% | Techoff SRV Limited | Amsterdam, The Netherlands | 01:19 | 12:44 |
| 11 | `2.57.122.209` | 42 | 2.9% | Unmanaged LTD | Amsterdam, The Netherlands | 04:01 | 06:20 |
| 12 | `92.118.39.14` | 30 | 2.1% | Unmanaged LTD | Dallas, United States | 00:16 | 09:30 |
| 13 | `180.93.1.64` | 27 | 1.9% | SPT | Quận Bốn, Vietnam | 11:55 | 23:55 |
| 14 | `2.57.122.238` | 26 | 1.8% | Unmanaged LTD | Amsterdam, The Netherlands | 06:40 | 07:40 |
| 15 | `62.60.130.201` | 25 | 1.7% | Cipher Operations DOO Beograd - Novi Beograd | Tehran, Iran | 01:07 | 03:41 |

## Attempts by country

| Country | Attempts | Share |  |
|---|---|---|---|
| The Netherlands | 336 | 23.4% | █████··············· |
| United States | 214 | 14.9% | ███················· |
| Iran | 135 | 9.4% | ██·················· |
| France | 104 | 7.2% | █··················· |
| Vietnam | 82 | 5.7% | █··················· |
| Andorra | 70 | 4.9% | █··················· |
| China | 68 | 4.7% | █··················· |
| South Korea | 50 | 3.5% | █··················· |
| Russia | 49 | 3.4% | █··················· |
| Indonesia | 45 | 3.1% | █··················· |
| Brazil | 38 | 2.6% | █··················· |
| India | 36 | 2.5% | █··················· |

## Attempts by region / city

| City, Region | Attempts | Share |  |
|---|---|---|---|
| Amsterdam, North Holland | 331 | 23.1% | █████··············· |
| Tehran | 135 | 9.4% | ██·················· |
| Cornelius, North Carolina | 121 | 8.4% | ██·················· |
| Paris, Île-de-France | 84 | 5.8% | █··················· |
| Andorra la Vella | 70 | 4.9% | █··················· |
| Jakarta | 31 | 2.2% | ···················· |
| Dallas, Texas | 30 | 2.1% | ···················· |
| Quận Bốn, Ho Chi Minh City (HCMC) | 27 | 1.9% | ···················· |
| Krasnoyarsk, Krasnoyarsk Krai | 23 | 1.6% | ···················· |
| Belo Horizonte, Minas Gerais | 22 | 1.5% | ···················· |
| Beijing | 20 | 1.4% | ···················· |
| Strasbourg, Grand Est | 20 | 1.4% | ···················· |

## Targeted usernames

| Username | Attempts | Share |  |
|---|---|---|---|
| `root` | 894 | 62.3% | ████████████········ |
| `ubuntu` | 38 | 2.6% | █··················· |
| `admin` | 35 | 2.4% | ···················· |
| `deploy` | 16 | 1.1% | ···················· |
| `user` | 13 | 0.9% | ···················· |
| `administrator` | 8 | 0.6% | ···················· |
| `git` | 8 | 0.6% | ···················· |
| `logviewer` | 6 | 0.4% | ···················· |
| `sol` | 6 | 0.4% | ···················· |
| `song` | 6 | 0.4% | ···················· |
| `soporte` | 6 | 0.4% | ···················· |
| `test` | 6 | 0.4% | ···················· |

## Top networks

| Network | Attempts |
|---|---|
| `AS48090 TECHOFF SRV LIMITED` | 268 |
| `AS215930 CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD` | 135 |
| `AS197170 TechTies Inc.` | 121 |
| `AS47890 UNMANAGED LTD` | 103 |
| `AS198364 BANATSYNC SRL` | 84 |
| `AS216014 BestDC Limited` | 50 |

## First-time attackers

`77.239.124.215` (76), `109.160.32.219` (66), `109.160.32.101` (55), `92.118.39.14` (30), `180.93.1.64` (27), `95.188.91.101` (23), `179.106.99.179` (22), `135.235.138.43` (19), `103.200.22.154` (19), `201.186.40.161` (19), `202.51.214.99` (19), `51.195.141.167` (18), `222.107.156.227` (18), `117.6.44.221` (18), `203.192.232.180` (17), `112.217.188.122` (16), `190.89.34.9` (16), `45.172.152.74` (16), `119.209.12.20` (16), `180.153.91.15` (16), `103.241.43.193` (16), `34.142.110.144` (16), `89.126.208.27` (16), `103.143.238.100` (15), `165.154.147.69` (15), `93.99.104.96` (14), `165.154.235.9` (14), `202.152.201.166` (14), `37.77.150.241` (14), `34.63.42.56` (14), `54.38.190.246` (13), `189.203.163.10` (13), `45.17.39.120` (12), `88.205.172.170` (12), `80.102.218.187` (12), `147.90.234.22` (12), `97.74.236.4` (11), `14.103.110.123` (10), `195.178.110.228` (9), `115.190.213.72` (8), `183.251.230.98` (8), `77.239.124.121` (8), `150.138.115.76` (8), `183.78.181.124` (5), `202.103.157.115` (4), `60.12.44.234` (3), `45.43.37.254` (3), `14.103.103.211` (2), `35.205.254.213` (2)

## Hourly timeline (UTC)

`00:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇ 100
`01:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 232
`02:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 215
`03:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 201
`04:00` ▇▇▇▇▇▇▇▇▇▇ 77
`05:00` ▇▇ 19
`06:00` ▇▇▇▇▇▇▇▇▇ 66
`07:00` ▇▇▇▇▇▇▇▇▇▇▇ 82
`08:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 109
`09:00` ▇▇▇▇▇▇▇▇▇▇▇▇▇ 101
`10:00` ▇▇▇▇▇▇▇▇▇ 70
`11:00` ▇▇▇▇▇▇▇▇ 62
`12:00` ▇▇▇▇▇▇▇▇▇▇▇ 83
`13:00` ▇ 7
`14:00` ▇ 6
`22:00` ▇ 2
`23:00` ▇ 4

## Recommended blocklist

Top offenders of the day, one per line (drop-in for firewall):

```text
77.239.124.215
45.148.10.151
109.160.32.219
45.148.10.157
45.148.10.141
109.160.32.101
62.60.130.242
62.60.130.253
193.47.62.69
45.148.10.152
```

```bash
# example: block the list with iptables
# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s "$ip" -j DROP; done
```

---

*About this report – The honeypot records every failed SSH login (pwd brute-force + invalid credentials) against exposed host, tags each source IP with geolocation + network ownership data >stores in InfluxDB. Charts + raw queries: Grafana → Security → “SSH Login Attempts — Geohash”. Generated automatically by `daily-report.py`.*
