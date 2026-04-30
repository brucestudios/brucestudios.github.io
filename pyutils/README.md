# PyUtils

A collection of lightweight Python utilities for common tasks.

## Features

- File utilities: safe file operations, batch renaming, etc.
- String utilities: formatting, validation, conversion, etc.
- More utilities to be added...

## Installation

```bash
pip install pyutils
```

## Usage

### File Utilities

```python
from pyutils.file_utils import safe_write, batch_rename

# Safely write content to a file (creates directories if needed)
safe_write("path/to/file.txt", "Hello, World!")

# Batch rename files in a directory
batch_rename("path/to/directory", pattern="*.txt", prefix="new_")
```

### String Utilities

```python
from pyutils.string_utils import slugify, is_valid_email

# Convert a string to a URL-friendly slug
slug = slugify("Hello, World!")  # returns "hello-world"

# Validate an email address
if is_valid_email("test@example.com"):
    print("Valid email")
```

## Running Tests

```bash
pytest
```

## License

MIT