# Python Utils

A collection of useful Python utility functions for common programming tasks.

## Features

- String manipulation utilities
- File and directory helpers
- Data validation functions
- Date/time utilities
- JSON helpers
- And more!

## Installation

```bash
pip install python-utils
```

## Usage

```python
from python_utils import strings, files, validation

# String utilities
result = strings.capitalize_words("hello world")
print(result)  # Hello World

# File utilities
files.ensure_dir("path/to/directory")

# Validation
if validation.is_email("user@example.com"):
    print("Valid email")
```

## Development

To install development dependencies:

```bash
pip install -e .[dev]
```

To run tests:

```bash
pytest
```

## License

MIT