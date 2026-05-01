# pwgen

A modern, secure password generator with CLI and library interfaces.

## Features

- Cryptographically secure password generation using `secrets`
- Highly customizable: length, character sets, ambiguous character exclusion
- Simple CLI and easy-to-use Python library
- Well-typed and well-tested
- Zero dependencies

## Installation

```bash
pip install pwgen
```

## Usage

### Command Line

```bash
# Generate a single 16-character password
pwgen

# Generate 5 passwords of length 20
pwgen -n 5 -l 20

# Exclude ambiguous characters (il1Lo0O)
pwgen --exclude-ambiguous

# Customize character sets
pwgen --no-symbols --no-digits  # letters only
```

### Library

```python
from pwgen import generate_password, generate_multiple_passwords

# Single password
password = generate_password(length=16)
print(password)

# Multiple passwords
passwords = generate_multiple_passwords(count=5, length=20)
for p in passwords:
    print(p)
```

## Customization

All generation functions accept the following optional boolean flags:

- `use_upper` (default: True) – Include uppercase letters (A-Z)
- `use_lower` (default: True) – Include lowercase letters (a-z)
- `use_digits` (default: True) – Include digits (0-9)
- `use_symbols` (default: True) – Include punctuation symbols
- `exclude_ambiguous` (default: False) – Exclude ambiguous characters (il1Lo0O)

## Examples

Generate a secure 12-character password with letters and numbers only:

```bash
pwgen -l 12 --no-symbols
```

Generate 10 passwords of length 32, excluding ambiguous characters:

```bash
pwgen -n 10 -l 32 --exclude-ambiguous
```

## License

MIT

## Author

OpenClaw Assistant