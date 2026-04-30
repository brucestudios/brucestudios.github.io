# Repo Stats CLI

A simple command-line tool to fetch and display statistics for a GitHub repository.

## Features

- Fetch stars, forks, watchers, open issues, and license info.
- Supports authentication via GitHub token for higher rate limits.
- Easy to install and use.

## Installation

```bash
pip install repo-stats-cli
```

## Usage

```bash
repo-stats owner/repo
```

Example:

```bash
repo-stats python/cpython
```

Output:

```
Repository: python/cpython
Stars: 45,000
Forks: 22,000
Watchers: 1,500
Open Issues: 1,200
License: PSF License
```

## Configuration

Set the environment variable `GITHUB_TOKEN` to a personal access token to avoid rate limiting.

## License

MIT