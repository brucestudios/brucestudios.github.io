# UtilsPlus

A collection of useful Python utilities for common tasks.

## Features

- String manipulation utilities (snake_case, camelCase conversion)
- File reading helpers
- Simple and easy to use

## Installation

```bash
pip install utilsplus
```

## Usage

```python
from utilsplus.core import to_snake_case, to_camel_case, read_lines

# Convert string to snake_case
print(to_snake_case("Hello World"))  # hello_world

# Convert string to camelCase
print(to_camel_case("hello world"))  # helloWorld

# Read lines from a file
lines = read_lines("example.txt")
for line in lines:
    print(line)
```

## Development

### Requirements

- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/<your-username>/utilsplus.git
cd utilsplus
pip install -e .
```

### Running Tests

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
