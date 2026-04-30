# textcase-cli

A command-line tool to convert text to different cases.

## Features

- Convert to uppercase (`--upper`)
- Convert to lowercase (`--lower`)
- Convert to title case (`--title`)
- Convert to sentence case (`--sentence`)
- Convert to alternating case (e.g., hElLo) (`--alternating`)
- Reverse the string (`--reverse`)
- Capitalize each word (`--capitalize`)
- Reads from stdin if no text argument provided
- Simple and intuitive

## Installation

```bash
pip install textcase-cli
```

Or clone and install locally:

```bash
git clone https://github.com/brucestudios/textcase-cli.git
cd textcase-cli
pip install .
```

## Usage

```bash
# Convert to uppercase
echo "hello world" | textcase --upper
# HELLO WORLD

# Title case
textcase --title "hello world"
# Hello World

# Sentence case
textcase --sentence "HELLO WORLD. this is a test."
# Hello world. This is a test.

# Alternating case
textcase --alternating "hello"
# hElLo

# Reverse
textcase --reverse "hello"
# olleh

# Capitalize each word
textcase --capitalize "hello world"
# Hello World

# Combine multiple operations (applied in order)
textcase --upper --reverse "hello"
# OLLEH
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests (if any)
python -m pytest
```

## License

MIT