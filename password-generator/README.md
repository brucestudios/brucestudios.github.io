# Password Generator

A simple command-line password generator written in Python.

## Features

- Generate secure random passwords
- Customize length and character sets
- Generate multiple passwords at once
- Exclude symbols, numbers, uppercase, or lowercase as needed

## Usage

```bash
python main.py [options]
```

### Options

- `--length LENGTH`   Length of each password (default: 16)
- `--count COUNT`     Number of passwords to generate (default: 1)
- `--no-symbols`      Exclude symbols
- `--no-numbers`      Exclude numbers
- `--no-uppercase`    Exclude uppercase letters
- `--no-lowercase`    Exclude lowercase letters

### Examples

Generate a single 16-character password:
```bash
python main.py
```

Generate 5 passwords of length 20:
```bash
python main.py --length 20 --count 5
```

Generate a password without symbols:
```bash
python main.py --no-symbols
```

## Installation

Requires Python 3.6+.

No installation needed; just run the script directly.

Alternatively, you can make it executable and place it in your PATH.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.