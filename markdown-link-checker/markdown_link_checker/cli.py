"""Command line interface for markdown link checker."""

import argparse
import sys
import os
from typing import List, Dict
import yaml

from .core import check_markdown_file

def _load_config(config_path: str) -> Dict:
    """Load configuration from a YAML file."""
    if not os.path.exists(config_path):
        return {}
    with open(config_path, 'r') as f:
        return yaml.safe_load(f) or {}

def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Check for broken links in markdown files."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Markdown files or directories to check."
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=10,
        help="Timeout in seconds for HTTP requests (default: 10)."
    )
    parser.add_argument(
        "-e", "--exclude",
        action="append",
        default=[],
        help="Exclude files or directories matching this pattern (can be used multiple times)."
    )
    parser.add_argument(
        "--exclude-url",
        action="append",
        default=[],
        help="Exclude URLs containing this string (can be used multiple times)."
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only output broken links, suppress other messages."
    )
    parser.add_argument(
        "--config",
        default=".markdown-link-checker.yml",
        help="Path to configuration file (default: .markdown-link-checker.yml)."
    )

    args = parser.parse_args()

    # Load configuration
    config = _load_config(args.config)
    # Override with command line arguments
    timeout = args.timeout if args.timeout != 10 else config.get('timeout', 10)
    exclude_patterns = args.exclude if args.exclude else config.get('exclude', [])
    exclude_url_patterns = args.exclude_url if args.exclude_url else config.get('exclude_url', [])
    quiet = args.quiet if args.quiet else config.get('quiet', False)

    # Collect all markdown files to check
    markdown_files: List[str] = []
    for path in args.paths:
        if os.path.isfile(path):
            if path.endswith('.md'):
                markdown_files.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                # Skip excluded directories
                if any(pattern in root for pattern in exclude_patterns):
                    continue
                for file in files:
                    if file.endswith('.md'):
                        full_path = os.path.join(root, file)
                        # Skip excluded files
                        if any(pattern in full_path for pattern in exclude_patterns):
                            continue
                        markdown_files.append(full_path)
        else:
            print(f"Warning: {path} is not a file or directory", file=sys.stderr)

    if not markdown_files:
        print("No markdown files found to check.", file=sys.stderr)
        sys.exit(1)

    total_broken = 0
    for file_path in markdown_files:
        broken = check_markdown_file(file_path, timeout=timeout)
        if broken:
            if not quiet:
                print(f"\n{file_path}:")
            for link, error in broken.items():
                print(f"  {link} -> {error}")
            total_broken += len(broken)
        elif not quiet:
            print(f"{file_path}: OK")

    if total_broken > 0:
        print(f"\nTotal broken links: {total_broken}", file=sys.stderr)
        sys.exit(1)
    else:
        if not quiet:
            print("\nAll links are OK!")

if __name__ == "__main__":
    main()