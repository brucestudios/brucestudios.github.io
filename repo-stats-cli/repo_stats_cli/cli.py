import argparse
import os
import sys
import requests

def fetch_repo_stats(owner, repo, token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Unable to fetch repository data (status {response.status_code})")
        sys.exit(1)
    data = response.json()
    stats = {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "watchers": data.get("watchers_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "license": data.get("license", {}).get("name", "No license") if data.get("license") else "No license",
    }
    return stats

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repository statistics.")
    parser.add_argument("repo", help="Repository in the form 'owner/repo'")
    parser.add_argument(
        "-t", "--token", help="GitHub personal access token (overrides GITHUB_TOKEN env var)"
    )
    args = parser.parse_args()

    if "/" not in args.repo:
        print("Error: Repository must be in the format 'owner/repo'")
        sys.exit(1)

    owner, repo = args.repo.split("/", 1)

    token = args.token or os.getenv("GITHUB_TOKEN")

    stats = fetch_repo_stats(owner, repo, token)

    print(f"Repository: {owner}/{repo}")
    print(f"Stars: {stats['stars']:,}")
    print(f"Forks: {stats['forks']:,}")
    print(f"Watchers: {stats['watchers']:,}")
    print(f"Open Issues: {stats['open_issues']:,}")
    print(f"License: {stats['license']}")

if __name__ == "__main__":
    main()