# passgen

A simple secure password generator written in Python.

## Features

- Generate cryptographically strong random passwords
- Ensure passwords contain at least one lowercase, uppercase, digit, and special character
- Customizable password length and quantity
- No dependencies, uses only Python standard library

## Usage

```bash
# Generate a single password of default length (16 characters)
python3 passgen.py

# Generate a password of specific length
python3 passgen.py -l 20

# Generate multiple passwords
python3 passgen.py -n 5 -l 12
```

## Installation

Just copy `passgen.py` to your desired location and make it executable:

```bash
chmod +x passgen.py
```

## License

MIT License - see the [LICENSE](LICENSE) file for details.