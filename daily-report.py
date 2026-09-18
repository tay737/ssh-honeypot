#!/usr/bin/env python3
"""Daily SSH honeypot threat report generator.

Queries the InfluxDB `geossh` measurement (populated by ssh-log-to-influx
collector + historical backfill) for each day (UTC) > writes an
easily-readable .md report.

Usage:
    python3 daily-report.py                      
    python3 daily-report.py --date 2026-09-17    
    python3 daily-report.py --from 2026-09-15 --to 2026-09-18   # one file per day
    python3 daily-report.py --date 2026-09-18 --stdout
    python3 daily-report.py --date 2026-09-18 --no-front-matter

Output:  <output-directory>/ssh-threats-<YYYY-MM-DD>.md 
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

CONTAINER = "ssh-influxdb"
DB = "ssh_logs"

TOP_IPS = 15
TOP_COUNTRIES = 12
TOP_CITIES = 12
TOP_USERS = 12
TOP_ASNS = 6
BLOCKLIST_SIZE = 10


# ---------------------------------------------------------------- influx ---
def influx_query(q):
    cmd = [
        "docker", "exec", CONTAINER, "curl", "-s", "-G",
        "--data-urlencode", f"db={DB}",
        "--data-urlencode", f"q={q}",
        "http://localhost:8086/query",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if proc.returncode != 0:
        raise RuntimeError(f"influx query failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    if data.get("results", [{}])[0].get("error"):
        raise RuntimeError(f"influx error: {data['results'][0]['error']}")
    return data["results"][0].get("series", [])


def rows(series_list):
    """Flatten series using the column names."""
    for s in series_list:
        cols = s["columns"]
        for vals in s.get("values", []):
            yield s.get("tags", {}), dict(zip(cols, vals))


def day_bounds(date_str):
    start = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return start, start + timedelta(days=1)


def rfc(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def hhmm(iso_ts):
    """'2026-09-18T15:46:47.638Z' -> '15:46'"""
    try:
        dt = datetime.fromisoformat(str(iso_ts).replace("Z", "+00:00"))
        return dt.strftime("%H:%M")
    except ValueError:
        return "–"


# ------------------------------------------------------------- gatherers ---
def collect(day_start, day_end, in_day_q, before_start_q):
    """Run all queries for the day; return dict of assembled data."""
    d = {}

    # totals
    d["total"] = next((r["count"] for _, r in rows(influx_query(
        f'SELECT count("value") FROM "geossh" WHERE {in_day_q}'))), 0)

    # per-IP with first/last seen
    counts = {}
    for tags, r in rows(influx_query(
            f'SELECT count("value") FROM "geossh" WHERE {in_day_q} GROUP BY "ip"')):
        counts[tags.get("ip", "unknown")] = int(r.get("count") or 0)
    first_seen, last_seen = {}, {}
    for tags, r in rows(influx_query(
            f'SELECT first("value") FROM "geossh" WHERE {in_day_q} GROUP BY "ip"')):
        first_seen[tags.get("ip", "unknown")] = hhmm(r.get("time"))
    for tags, r in rows(influx_query(
            f'SELECT last("value") FROM "geossh" WHERE {in_day_q} GROUP BY "ip"')):
        last_seen[tags.get("ip", "unknown")] = hhmm(r.get("time"))
    d["ips"] = counts
    d["first_seen"] = first_seen
    d["last_seen"] = last_seen

    meta = {}
    for tag in ("country", "city", "isp", "as"):
        for tags, r in rows(influx_query(
                f'SELECT count("value") FROM "geossh" WHERE {in_day_q} GROUP BY "{tag}"')):
            key = tags.get(tag)
            if key and r.get("count"):
                meta.setdefault(key, {})
                
    per_ip_meta = {}
    for tags, r in rows(influx_query(
            f'SELECT count("value") FROM "geossh" WHERE {in_day_q} '
            f'GROUP BY "ip", "country", "city", "isp", "as"')):
        ip = tags.get("ip", "unknown")
        cur = per_ip_meta.get(ip)
        cnt = int(r.get("count") or 0)
        if cur is None or cnt > cur[0]:
            per_ip_meta[ip] = (cnt, tags)
    d["ip_meta"] = {ip: t for ip, (c, t) in per_ip_meta.items()}


    def tally(tag):
        out = {}
        for tags, r in rows(influx_query(
                f'SELECT count("value") FROM "geossh" WHERE {in_day_q} GROUP BY "{tag}"')):
            key = tags.get(tag) or "unknown"
            out[key] = out.get(key, 0) + int(r.get("count") or 0)
        return out

    d["countries"] = tally("country")
    d["usernames"] = tally("username")
    d["isps"] = tally("isp")
    d["asns"] = tally("as")

    cities = {}
    for tags, r in rows(influx_query(
            f'SELECT count("value") FROM "geossh" WHERE {in_day_q} GROUP BY "city", "regionName"')):
        city = tags.get("city") or "unknown"
        region = tags.get("regionName") or ""
        label = f"{city}, {region}" if region and region != city else city
        cities[label] = cities.get(label, 0) + int(r.get("count") or 0)
    d["cities"] = cities

    
    hours = [0] * 24
    for _, r in rows(influx_query(
            f'SELECT count("value") FROM "geossh" WHERE {in_day_q} '
            f'GROUP BY time(1h) fill(0)')):
        t = str(r.get("time", ""))
        try:
            h = datetime.fromisoformat(t.replace("Z", "+00:00")).hour
            hours[h] = int(r.get("count") or 0)
        except ValueError:
            pass
    d["hours"] = hours

    
    before = set()
    for tags, _ in rows(influx_query(
            f'SELECT count("value") FROM "geossh" WHERE {before_start_q} GROUP BY "ip"')):
        before.add(tags.get("ip", "unknown"))
    d["new_ips"] = set(counts) - before

    return d


# format
def pct(n, total):
    return (n / total * 100) if total else 0.0


def bar(p, width=20):
    filled = round(p / 100 * width)
    return "█" * filled + "·" * (width - filled)


def table(headers, rows_):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows_]
    return "\n".join(out)


def top(d, n):
    return sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:n]


def build_report(day, data, now_utc, front_matter=True):
    start, end = day_bounds(day)
    in_progress = start <= now_utc < end
    total = data["total"]
    n_ips = len(data["ips"])

    L = []
    ap = L.append

    if front_matter:
        ap("---")
        ap(f'title: "Daily SSH Honeypot Threat Report — {day}"')
        ap(f'date: {day}T06:00:00Z')
        ap("tags: [honeypot, ssh, security, threat-intel, brute-force]")
        ap(f'description: "{total} SSH brute-force attempts from {n_ips} unique IPs '
           f'across {len(data["countries"])} countries hit the honeypot on {day}."')
        ap("---")
        ap("")

    ap(f"# Daily SSH Honeypot Threat Report — {day}")
    ap("")
    ap(f"*Data window: `{day}` 00:00–24:00 UTC · source: ssh-log-to-influx collector · "
       f"geolocation: ip-api.com" +
       ("day in progress, stats partial" if in_progress else "") + "*")
    ap("")


    peak_h = max(range(24), key=lambda h: data["hours"][h]) if total else 0
    peak_v = data["hours"][peak_h]
    top_ip = top(data["ips"], 1)
    top_user = top(data["usernames"], 1)
    top_cc = top(data["countries"], 1)
    ap("## At a glance...")
    ap("")
    if total:
        ip, ipn = top_ip[0] if top_ip else ("—", 0)
        im = data["ip_meta"].get(ip, {})
        ap(f"- **{total:,} attempts** from **{n_ips} unique IPs** "
           f"in **{len(data['countries'])} countries** "
           f"({total / 24:.1f}/hour average)")
        ap(f"- **Top attacker:** `{ip}` — {ipn} attempts "
           f"({im.get('isp', 'unknown ISP')}, {im.get('city', '?')}, {im.get('country', '?')})")
        if top_cc:
            ap(f"- **Top source country:** {top_cc[0][0]} — {top_cc[0][1]} "
               f"({pct(top_cc[0][1], total):.0f}%)")
        if top_user:
            ap(f"- **Most targeted account:** `{top_user[0][0]}` — {top_user[0][1]} "
               f"({pct(top_user[0][1], total):.0f}%)")
        ap(f"- **Peak hour:** {peak_h:02d}:00–{peak_h + 1:02d}:00 UTC — {peak_v} attempts")
        ap(f"- **First-time attackers:** {len(data['new_ips'])} of {n_ips} IPs "
           f"had never been seen before this day")
    else:
        ap("- Quiet day — **no attempts recorded**.")
    ap("")


    ap(f"## Top attacking IPs")
    ap("")
    if data["ips"]:
        rows_ = []
        for i, (ip, n) in enumerate(top(data["ips"], TOP_IPS), 1):
            m = data["ip_meta"].get(ip, {})
            rows_.append([i, f"`{ip}`", n, f"{pct(n, total):.1f}%",
                          m.get("isp", "—"), f"{m.get('city', '—')}, {m.get('country', '—')}",
                          data["first_seen"].get(ip, "—"), data["last_seen"].get(ip, "—")])
        ap(table(["#", "IP", "Attempts", "Share", "ISP", "Location", "First", "Last"], rows_))
    else:
        ap("_No attacking IPs._")
    ap("")


    ap("## Attempts by country")
    ap("")
    if data["countries"]:
        rows_ = [[cc, n, f"{pct(n, total):.1f}%", bar(pct(n, total))]
                 for cc, n in top(data["countries"], TOP_COUNTRIES)]
        ap(table(["Country", "Attempts", "Share", ""], rows_))
    else:
        ap("_None._")
    ap("")


    ap("## Attempts by region / city")
    ap("")
    if data["cities"]:
        rows_ = [[c, n, f"{pct(n, total):.1f}%", bar(pct(n, total))]
                 for c, n in top(data["cities"], TOP_CITIES)]
        ap(table(["City, Region", "Attempts", "Share", ""], rows_))
    else:
        ap("_None._")
    ap("")


    ap("## Targeted usernames")
    ap("")
    if data["usernames"]:
        rows_ = [[f"`{u}`", n, f"{pct(n, total):.1f}%", bar(pct(n, total))]
                 for u, n in top(data["usernames"], TOP_USERS)]
        ap(table(["Username", "Attempts", "Share", ""], rows_))
    else:
        ap("_None._")
    ap("")

    if data["asns"]:
        ap("## Top networks")
        ap("")
        rows_ = [[f"`{a}`", n] for a, n in top(data["asns"], TOP_ASNS)]
        ap(table(["Network", "Attempts"], rows_))
        ap("")

    ap("## First-time attackers")
    ap("")
    if data["new_ips"]:
        items = sorted(((ip, data["ips"][ip]) for ip in data["new_ips"]),
                       key=lambda kv: kv[1], reverse=True)
        ap(", ".join(f"`{ip}` ({n})" for ip, n in items))
    else:
        ap("_All attackers today were previously seen — no new actors._")
    ap("")

    ap("## Hourly timeline (UTC)")
    ap("")
    if total:
        mx = max(data["hours"]) or 1
        lines = []
        for h in range(24):
            v = data["hours"][h]
            if v:
                lines.append(f"`{h:02d}:00` {'▇' * max(1, round(v / mx * 30))} {v}")
        ap("\n".join(lines))
    else:
        ap("_No activity._")
    ap("")

    
    if total:
        ap("## Recommended blocklist")
        ap("")
        ap("Top offenders of the day, one per line (drop-in for firewall:")
        ap("")
        ap("```text")
        for ip, _ in top(data["ips"], BLOCKLIST_SIZE):
            ap(ip)
        ap("```")
        ap("")
        ap("```bash")
        ap("# example: block the list with iptables")
        ap("# for ip in $(cat blocklist.txt); do sudo iptables -A INPUT -s \"$ip\" -j DROP; done")
        ap("```")
        ap("")

    # Footer
    ap("---")
    ap("")
    ap("*About this report – The honeypot records every failed SSH login "
       "(pwd brute-force + invalid credentials) against exposed host, "
       "tags each source IP with geolocation + network ownership data >stores "
       "in InfluxDB. Charts + raw queries: Grafana → Security → "
       "“SSH Login Attempts — Geohash”. Generated automatically by "
       "`daily-report.py`.*")
    ap("")

    return "\n".join(L)


# ------------------------------------------------------------------ main ---
def generate_for_day(day, out_dir, stdout=False, front_matter=True):
    start, end = day_bounds(day)
    in_day_q = f"time >= '{rfc(start)}' AND time < '{rfc(end)}'"
    before_start_q = f"time < '{rfc(start)}'"
    data = collect(start, end, in_day_q, before_start_q)
    md = build_report(day, data, datetime.now(timezone.utc), front_matter)
    if stdout:
        print(md)
    path = f"{out_dir}/ssh-threats-{day}.md"
    with open(path, "w") as f:
        f.write(md)
    return path, data


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--date", help="single day YYYY-MM-DD (default: yesterday UTC)")
    p.add_argument("--from", dest="from_", help="range start YYYY-MM-DD (inclusive)")
    p.add_argument("--to", dest="to_", help="range end YYYY-MM-DD (inclusive)")
    p.add_argument("--out", default="reports", help="output directory (default: ./reports)")
    p.add_argument("--stdout", action="store_true", help="also print the report")
    p.add_argument("--no-front-matter", action="store_true",
                   help="omit YAML front matter (plain Markdown)")
    args = p.parse_args()

    now = datetime.now(timezone.utc)
    if args.from_ and args.to_:
        d0 = datetime.strptime(args.from_, "%Y-%m-%d").date()
        d1 = datetime.strptime(args.to_, "%Y-%m-%d").date()
        if d1 < d0:
            sys.exit("--to is before --from")
        days = [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    elif args.date:
        days = [args.date]
    else:
        days = [(now - timedelta(days=1)).date().isoformat()]

    import os
    os.makedirs(args.out, exist_ok=True)
    for day in days:
        path, data = generate_for_day(day, args.out, args.stdout,
                                      not args.no_front_matter)
        print(f"[{day}] total={data['total']:,} ips={len(data['ips'])} "
              f"countries={len(data['countries'])} -> {path}")


if __name__ == "__main__":
    main()
