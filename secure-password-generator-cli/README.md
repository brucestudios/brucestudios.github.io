# Secure Password Generator CLI

A command-line tool and Python library for generating cryptographically secure passwords.

## Features

- Generate strong, random passwords
- Customizable length and character sets
- Option to exclude ambiguous characters
- Available as a CLI tool and importable Python library
- Zero dependencies (uses only Python standard library)

## Installation

```bash
pip install secure-password-generator-cli
```

Or install from source:

```bash
git clone https://github.com/brucestudios/secure-password-generator-cli.git
cd secure-password-generator-cli
pip install -e .
```

## Usage

### Command Line Interface

```bash
# Generate a password of default length (16 characters)
spg

# Generate a password of specific length
spg -l 32

# Generate a password without ambiguous characters (Il1O0o)
spg --no-ambiguous

# Generate a PIN (digits only)
spg --digits-only -l 6

# Generate a pronouncable password (alternating vowels/consonants)
spg --pronounceable -l 10

# Generate multiple passwords
spg -c 5
```

### As a Library

```python
from secure_password_generator import generate_password

# Generate a default password
password = generate_password()
print(password)  # e.g., "xK9#qL2$mP8@vN4*"

# Generate a password with specific options
password = generate_password(
    length=20,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True,
    ambiguous=False
)
print(password)
```

## Character Sets

- Uppercase letters: A-Z
- Lowercase letters: a-z
- Digits: 0-9
- Special characters: !@#$%^&*()-_=+[]{}|;:,.<>?/
- Ambiguous characters (excluded when `--no-ambiguous` is used): Il1O0o

## Development

### Running Tests

```bash
pip install pytest
pytest
```

### Building and Publishing

```bash
# Build the package
python -m build

# Upload to TestPyPI (first time)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request