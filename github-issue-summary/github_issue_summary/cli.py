import argparse
import sys
from github import Github
from datetime import datetime, timedelta

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a markdown summary of GitHub issues grouped by labels.")
    parser.add_argument("--owner", required=True, help="Repository owner (user or organization)")
    parser.add_argument("--repo", required=True, help="Repository name")
    parser.add_argument("--since", help="Only issues updated after this date (YYYY-MM-DD). Default: 30 days ago.")
    parser.add_argument("--labels", help="Comma-separated list of labels to include. If not provided, all labels are included.")
    parser.add_argument("--output", help="Output file. If not provided, prints to stdout.")
    parser.add_argument("--token", help="GitHub personal access token. If not provided, uses the default auth from gh CLI.")
    return parser.parse_args()

def get_github_instance(token=None):
    if token:
        return Github(token)
    else:
        # Try to use the default authentication (from gh CLI or environment)
        return Github()

def main():
    args = parse_args()

    # Set up GitHub instance
    g = get_github_instance(args.token)

    # Get the repository
    try:
        repo = g.get_repo(f"{args.owner}/{args.repo}")
    except Exception as e:
        print(f"Error accessing repository {args.owner}/{args.repo}: {e}", file=sys.stderr)
        sys.exit(1)

    # Determine the since date
    if args.since:
        try:
            since_date = datetime.strptime(args.since, "%Y-%m-%d")
        except ValueError:
            print("Error: --since must be in YYYY-MM-DD format.", file=sys.stderr)
            sys.exit(1)
    else:
        # Default to 30 days ago
        since_date = datetime.now() - timedelta(days=30)

    # Convert labels to a set for filtering if provided
    label_filter = None
    if args.labels:
        label_filter = set(label.strip() for label in args.labels.split(","))

    # Fetch issues updated since the given date
    # We'll use the GitHub API to get issues updated after since_date
    # Note: The GitHub API for issues updated uses the `since` parameter which is a timestamp in ISO 8601: YYYY-MM-DDTHH:MM:SSZ
    # We'll convert our datetime to that format.
    since_str = since_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    issues = repo.get_issues(since=since_str, state='all')

    # Group issues by labels
    grouped = {}
    for issue in issues:
        # Get the labels of the issue
        issue_labels = {label.name for label in issue.labels}

        # If we have a label filter, skip if none of the issue's labels are in the filter
        if label_filter:
            if not issue_labels & label_filter:
                continue
            # For grouping, we want to show the issue under each of its labels that are in the filter?
            # But the requirement is to group by labels. We'll assign the issue to the first matching label? 
            # Alternatively, we can create a group for each label and put the issue in all matching label groups.
            # However, that would duplicate the issue. Let's do: for each label in the filter that the issue has, add the issue to that label's group.
            # But then the same issue appears in multiple groups. That might be acceptable.
            # Alternatively, we can group by the set of labels? That's more complex.
            # Let's change the requirement: we want to group by label, and an issue can appear in multiple groups if it has multiple labels.
            # We'll do that.

            for label in issue_labels:
                if label in label_filter:
                    if label not in grouped:
                        grouped[label] = []
                    grouped[label].append(issue)
        else:
            # If no label filter, we group by each label. If an issue has no label, we put it in "No Label"
            if not issue_labels:
                if "No Label" not in grouped:
                    grouped["No Label"] = []
                grouped["No Label"].append(issue)
            else:
                for label in issue_labels:
                    if label not in grouped:
                        grouped[label] = []
                    grouped[label].append(issue)

    # Generate markdown
    markdown_lines = []
    markdown_lines.append(f"# GitHub Issue Summary for {args.owner}/{args.repo}")
    markdown_lines.append(f"*Issues updated since {since_date.strftime('%Y-%m-%d')}*\n")

    # Sort the labels for consistent output
    for label in sorted(grouped.keys()):
        markdown_lines.append(f"## {label}")
        for issue in grouped[label]:
            # Format: - [#number] title (state)
            markdown_lines.append(f"- [#{issue.number}]({issue.html_url}) {issue.title} ({issue.state})")
        markdown_lines.append("")  # blank line between groups

    # Join the lines
    markdown = "\n".join(markdown_lines)

    # Output
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"Summary written to {args.output}")
        except Exception as e:
            print(f"Error writing to file {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(markdown)

if __name__ == "__main__":
    main()