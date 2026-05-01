# GitHub Issue Summary

A CLI tool to generate a markdown summary of GitHub issues grouped by labels.

## Features

- Fetch issues from any public or private repository (requires authentication)
- Group issues by labels (e.g., bug, feature, enhancement)
- Output formatted markdown suitable for changelogs or release notes
- Customizable date ranges and label filters
- Easy to use as a command-line tool or as a Python library

## Installation

```bash
pip install github-issue-summary
```

## Usage

```bash
# Generate summary for the last month
github-issue-summary --owner brucestudios --repo github-issue-summary --since 2026-03-01

# Specify labels to include
github-issue-summary --owner brucestudios --repo github-issue-summary --labels bug,feature

# Output to file
github-issue-summary --owner brucestudios --repo github-issue-summary --output changelog.md
```

## Development

To contribute:

1. Fork the repository
2. Create a feature branch
3. Install dependencies: `pip install -e ".[dev]"`
4. Run tests: `pytest`
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) for details.
