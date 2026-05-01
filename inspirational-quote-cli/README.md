# Inspirational Quote CLI

A command-line tool that prints random inspirational quotes.

## Features

- Print random inspirational quotes
- Specify number of quotes to display
- Optional color output
- Optional clipboard copy (requires `pyperclip`)

## Installation

You can install the package via pip:

```bash
pip install inspirational-quote-cli
```

Or install from source:

```bash
git clone https://github.com/brucestudios/inspirational-quote-cli.git
cd inspirational-quote-cli
pip install .
```

## Usage

```bash
quote              # Print a random inspirational quote
quote -c 3         # Print 3 random quotes
quote --copy       # Copy quote to clipboard (if available)
quote --color      # Display quote in color
quote -v           # Show version
```

## Examples

```bash
$ quote
Believe you can and you're halfway there. – Theodore Roosevelt

$ quote -c 2 --color
1. The only way to do great work is to love what you do. – Steve Jobs
2. Life is what happens when you're busy making other plans. – John Lennon
```

## Development

To install in development mode:

```bash
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.