#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

KEYCHAIN_SERVICE = "parklifehack_github_traffic_token"


def repo_from_remote():
    try:
        remote = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None

    patterns = [
        r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, remote)
        if match:
            return match.group("owner"), match.group("repo")
    return None


def github_get(owner, repo, endpoint, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as res:
        return json.load(res)


def token_from_keychain():
    try:
        token = subprocess.check_output(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None
    return token or None


def print_daily(title, data, rows_key):
    print(f"\n## {title}")
    total = data.get("count", 0)
    uniques = data.get("uniques", 0)
    print(f"total: {total} / unique: {uniques}")
    rows = data.get(rows_key) or []
    if not rows:
        print("(no daily data)")
        return
    print("date        count  unique")
    for item in rows:
        day = str(item.get("timestamp", ""))[:10]
        print(f"{day:<10}  {item.get('count', 0):>5}  {item.get('uniques', 0):>6}")


def print_ranked(title, rows, name_key):
    print(f"\n## {title}")
    if not rows:
        print("(no data)")
        return
    print("count  unique  name")
    for item in rows:
        name = item.get(name_key) or item.get("path") or item.get("title") or ""
        print(f"{item.get('count', 0):>5}  {item.get('uniques', 0):>6}  {name}")


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or token_from_keychain()
    if not token:
        print("No GitHub traffic token found.", file=sys.stderr)
        print("Create a fine-grained token for this repo with Administration: read.", file=sys.stderr)
        print("Then store it in macOS Keychain:", file=sys.stderr)
        print("  read -s GITHUB_TRAFFIC_TOKEN", file=sys.stderr)
        print(f"  security add-generic-password -U -a \"$USER\" -s {KEYCHAIN_SERVICE} -w \"$GITHUB_TRAFFIC_TOKEN\"", file=sys.stderr)
        print("  unset GITHUB_TRAFFIC_TOKEN", file=sys.stderr)
        return 2

    repo = repo_from_remote()
    if not repo:
        print("Could not infer owner/repo from git remote origin.", file=sys.stderr)
        return 2

    owner, name = repo
    print(f"{owner}/{name}")
    try:
        print_daily("Views, last 14 days", github_get(owner, name, "traffic/views?per=day", token), "views")
        print_daily("Clones, last 14 days", github_get(owner, name, "traffic/clones?per=day", token), "clones")
        print_ranked("Popular paths, last 14 days", github_get(owner, name, "traffic/popular/paths", token), "path")
        print_ranked("Popular referrers, last 14 days", github_get(owner, name, "traffic/popular/referrers", token), "referrer")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"GitHub API error: HTTP {e.code}", file=sys.stderr)
        print(body, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
