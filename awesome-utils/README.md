# Awesome Utils

A collection of useful utility functions for everyday programming tasks.

## Features

- String manipulation utilities
- File and directory helpers
- Data validation helpers
- Simple CLI for quick tasks

## Installation

```bash
pip install awesome-utils
```

## Usage

### Python API

```python
from awesome_utils import strings, files

# String utilities
result = strings.capitalize_words("hello world")
print(result)  # Hello World

# File utilities
files.ensure_dir("output/logs")
```

### CLI

```bash
awesome-utils strings capitalize --text "hello world"
```

## Development

### Setup

```bash
git clone https://github.com/<your-username>/awesome-utils.git
cd awesome-utils
pip install -e .[dev]
```

### Running Tests

```bash
pytest
```

### Building

```bash
python -m build
```

## License

MIT
