"""
Helper functions for OpenClaw
"""
import re
from datetime import datetime

def format_timestamp(fmt="%Y-%m-%d %H:%M:%S"):
    """Return current timestamp formatted as string."""
    return datetime.now().strftime(fmt)

def sanitize_filename(filename):
    """Sanitize a string to be used as a filename."""
    # Remove invalid characters for Windows, macOS, and Linux
    filename = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    # Limit length to 255 characters (common filesystem limit)
    return filename[:255]

def parse_markdown_table(markdown_text):
    """Parse a markdown table into a list of dictionaries."""
    lines = [line.strip() for line in markdown_text.split('\n') if line.strip()]
    if not lines:
        return []
    # Find the header line (first line that contains '|')
    header_line = None
    for i, line in enumerate(lines):
        if '|' in line:
            header_line = i
            break
    if header_line is None:
        return []
    # Extract headers
    headers = [h.strip() for h in lines[header_line].split('|')[1:-1]]
    # Find the separator line (the line after header that contains only '|', '-', ':')
    separator_line = header_line + 1
    if separator_line >= len(lines) or not re.match(r'^[\s|:-\]+$', lines[separator_line]):
        # No proper separator, assume no data
        return []
    # Extract data lines
    data = []
    for line in lines[separator_line+1:]:
        if '|' not in line:
            continue
        values = [v.strip() for v in line.split('|')[1:-1]]
        if len(values) == len(headers):
            data.append(dict(zip(headers, values)))
    return data