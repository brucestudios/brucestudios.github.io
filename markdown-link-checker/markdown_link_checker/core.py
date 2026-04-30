"""Core functionality for markdown link checking."""

import os
import re
import requests
from typing import Dict, Tuple, Optional
from urllib.parse import urljoin, urlparse

# Regular expression to find markdown links: [text](url) and also <url>
# This regex captures the URL in markdown links and also standalone URLs in angle brackets.
# It does not capture images (![](url)) but we can ignore those for now.
MARKDOWN_LINK_PATTERN = re.compile(
    r'''(?<!\!)\[(?:[^\]]*|\[[^\]]*\])*\]\(([^)]+)\)|<([^>]+)>'''
)

def _is_local_path(url: str) -> bool:
    """Check if the URL is a local file path."""
    parsed = urlparse(url)
    return not parsed.scheme or parsed.scheme in ('', 'file')

def _normalize_path(path: str, base_dir: str) -> str:
    """Convert a possibly relative path to an absolute path."""
    if os.path.isabs(path):
        return path
    return os.path.normpath(os.path.join(base_dir, path))

def check_markdown_file(file_path: str, timeout: int = 10) -> Dict[str, str]:
    """
    Check all links in a single markdown file.

    Args:
        file_path: Path to the markdown file.
        timeout: Timeout in seconds for HTTP requests.

    Returns:
        A dictionary mapping broken links to error messages.
        Empty dictionary means no broken links.
    """
    if not os.path.isfile(file_path):
        return {file_path: "File not found"}

    base_dir = os.path.dirname(os.path.abspath(file_path))
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {file_path: f"Unable to read file: {e}"}

    return check_markdown_string(content, base_dir, timeout)


def check_markdown_string(markdown: str, base_dir: str, timeout: int = 10) -> Dict[str, str]:
    """
    Check all links in a markdown string.

    Args:
        markdown: The markdown content as a string.
        base_dir: The base directory to resolve relative links.
        timeout: Timeout in seconds for HTTP requests.

    Returns:
        A dictionary mapping broken links to error messages.
        Empty dictionary means no broken links.
    """
    broken_links: Dict[str, str] = {}

    # Find all matches in the markdown
    for match in MARKDOWN_LINK_PATTERN.finditer(markdown):
        # The regex has two groups: one for markdown-style [text](url) and one for <url>
        url = match.group(1) or match.group(2)
        if url is None:
            continue

        # Skip empty URLs
        if not url.strip():
            continue

        # Handle local paths
        if _is_local_path(url):
            # Normalize the path
            if url.startswith('file://'):
                # Remove the file:// prefix
                url = url[7:]
            path = _normalize_path(url, base_dir)
            if not os.path.exists(path):
                broken_links[url] = f"Local file not found: {path}"
        else:
            # Handle web URLs
            try:
                # Try HEAD first, fallback to GET if HEAD not allowed or fails
                try:
                    response = requests.head(url, timeout=timeout, allow_redirects=True)
                    if response.status_code >= 400:
                        # If HEAD fails with 4xx or 5xx, try GET
                        response = requests.get(url, timeout=timeout, allow_redirects=True)
                except requests.exceptions.RequestException:
                    # If HEAD fails, try GET
                    response = requests.get(url, timeout=timeout, allow_redirects=True)

                if response.status_code >= 400:
                    broken_links[url] = f"HTTP {response.status_code}: {response.reason}"
            except requests.exceptions.RequestException as e:
                broken_links[url] = f"Request failed: {e}"

    return broken_links