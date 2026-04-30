# Factorial Utils

A simple Python utility for computing factorials of non-negative integers.

## Features

- Iterative factorial computation
- Recursive factorial computation
- Command-line interface
- Comprehensive error handling
- Well-tested and documented

## Installation

```bash
pip install factorial-utils-python
```

Or clone the repository:

```bash
git clone https://github.com/brucestudios/factorial-utils-python.git
cd factorial-utils-python
```

## Usage

### As a Module

```python
from factorial_utils.factorial import factorial, factorial_recursive

# Iterative approach
result = factorial(5)  # Returns 120

# Recursive approach
result = factorial_recursive(5)  # Returns 120
```

### Command Line Interface

```bash
python factorial.py 5
# Output: Factorial of 5 is 120
```

## Running Tests

```bash
python -m unittest discover tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.