# Markdown Link Checker

A Python utility to check for broken links in Markdown files.

## Features

- Check local file links and HTTP/HTTPS links
- Recursive directory scanning
- Configurable timeout for HTTP requests
- Exclude patterns for files and URLs
- Detailed reporting of broken links
- Support for relative and absolute paths

## Installation

```bash
pip install markdown-link-checker
```

## Usage

### Command Line Interface

```bash
# Check a single file
markdown-link-checker README.md

# Check all markdown files in a directory
markdown-link-checker docs/

# Check with custom timeout (seconds)
markdown-link-checker --timeout 10 docs/

# Exclude certain files or directories
markdown-link-checker --exclude "*/node_modules/*" --exclude "*.tmp.md" docs/

# Exclude certain URL patterns (e.g., localhost)
markdown-link-checker --exclude-url "localhost" --exclude-url "127.0.0.1" docs/

# Show only broken links
markdown-link-checker --quiet docs/
```

### As a Library

```python
from markdown_link_checker import check_markdown_file

broken_links = check_markdown_file("README.md")
if broken_links:
    print("Broken links found:")
    for link, error in broken_links.items():
        print(f"  {link}: {error}")
else:
    print("No broken links found!")
```

## Configuration

Create a `.markdown-link-checker.yml` file in your project root to configure default options:

```yaml
timeout: 30
exclude:
  - "*/node_modules/*"
  - "*.tmp.md"
exclude_url:
  - "localhost"
  - "127.0.0.1"
quiet: false
```

## Requirements

- Python 3.7+
- Dependencies: `requests`, `pyyaml`

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.