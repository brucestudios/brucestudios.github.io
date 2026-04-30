#!/usr/bin/env python3
"""
git-summary: A command-line tool to summarize GitHub repositories.
"""

import sys
import argparse
import requests
from urllib.parse import urlparse

def parse_repo_url(url):
    """Extract owner and repo name from a GitHub URL."""
    parsed = urlparse(url)
    if parsed.netloc != 'github.com':
        raise ValueError("URL must be from github.com")
    path = parsed.path.strip('/')
    if not path:
        raise ValueError("No repository path in URL")
    parts = path.split('/')
    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")
    owner, repo = parts[0], parts[1]
    # Remove .git suffix if present
    if repo.endswith('.git'):
        repo = repo[:-4]
    return owner, repo

def get_repo_info(owner, repo, token=None):
    """Fetch repository information from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "git-summary"
    }
    if token:
        headers["Authorization"] = f"token {token}"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        raise ValueError(f"Repository {owner}/{repo} not found")
    elif response.status_code == 403:
        # Check if rate limit exceeded
        if 'X-RateLimit-Remaining' in response.headers and response.headers['X-RateLimit-Remaining'] == '0':
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            raise RuntimeError(f"GitHub API rate limit exceeded. Reset time: {reset_time}")
        else:
            raise RuntimeError("Access forbidden. Check your token permissions.")
    elif response.status_code != 200:
        raise RuntimeError(f"GitHub API error: {response.status_code} - {response.text}")
    return response.json()

def format_summary(repo_info):
    """Format repository information into a readable summary."""
    summary = []
    summary.append(f"Repository: {repo_info['full_name']}")
    summary.append(f"Description: {repo_info['description'] or 'No description'}")
    summary.append(f"Language: {repo_info['language'] or 'Not specified'}")
    summary.append(f"Stars: {repo_info['stargazers_count']:,}")
    summary.append(f"Forks: {repo_info['forks_count']:,}")
    summary.append(f"Watchers: {repo_info['subscribers_count']:,}")
    summary.append(f"Open Issues: {repo_info['open_issues_count']:,}")
    summary.append(f"License: {repo_info['license']['name'] if repo_info['license'] else 'None'}")
    summary.append(f"Created: {repo_info['created_at'][:10]}")
    summary.append(f"Updated: {repo_info['updated_at'][:10]}")
    summary.append(f"URL: {repo_info['html_url']}")
    return "\n".join(summary)

def main():
    parser = argparse.ArgumentParser(description="Summarize a GitHub repository.")
    parser.add_argument("repo_url", help="GitHub repository URL (e.g., https://github.com/owner/repo)")
    parser.add_argument("-t", "--token", help="GitHub personal access token (optional, for higher rate limits)")
    args = parser.parse_args()

    try:
        owner, repo = parse_repo_url(args.repo_url)
        repo_info = get_repo_info(owner, repo, args.token)
        print(format_summary(repo_info))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()