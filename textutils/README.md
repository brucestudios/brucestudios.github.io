# TextUtils

A comprehensive Python utility package for text processing and password generation.

## Features

- **Password Generation**: Create secure passwords with customizable character sets
- **Passphrase Generation**: Generate memorable passphrases from word lists
- **Text Analysis**: Count words, lines, and characters in text
- **Text Transformation**: Convert text to upper/lower/title case
- **Palindrome Detection**: Check if text is a palindrome (ignoring punctuation and case)
- **Random String Generation**: Generate random strings with configurable character sets
- **Command-Line Interface**: Easy-to-use CLI for all functionalities

## Installation

```bash
pip install textutils
```

Or from source:

```bash
pip install .
```

## Usage

### As a Library

```python
from textutils import core, utils

# Generate a password
password = core.generate_password(length=20)
print(f"Generated password: {password}")

# Generate a passphrase
passphrase = core.generate_passphrase(num_words=4, separator=" ")
print(f"Generated passphrase: {passphrase}")

# Analyze text
text = "Hello world! This is a test."
print(f"Words: {utils.count_words(text)}")
print(f"Lines: {utils.count_lines(text)}")
print(f"Characters: {utils.count_chars(text)}")

# Transform text
upper_text = utils.to_upper("hello world")
print(f"Uppercase: {upper_text}")

# Check palindrome
is_pal = utils.is_palindrome("A man, a plan, a canal: Panama")
print(f"Is palindrome: {is_pal}")

# Generate random string
random_str = utils.random_string(length=16, use_special=True)
print(f"Random string: {random_str}")
```

### Command-Line Interface

```bash
# Generate a password
textutils password -l 20

# Generate a passphrase
textutils passphrase -w 5 -s " "

# Analyze text
textutils analyze "Hello world this is a test"
# or from file
textutils analyze -f /path/to/file.txt

# Transform text
textutils transform "hello world" -t upper

# Check palindrome
textutils palindrome "A man, a plan, a canal: Panama"

# Generate random string
textutils random -l 16
```

## Development

### Running Tests

```bash
pytest
```

### Building Package

```bash
python -m build
```

### Publishing to Test PyPI

```bash
twine upload --repository testpypi dist/*
```

### Publishing to PyPI

```bash
twine upload dist/*
```

## License

MIT