# Motivational Quotes CLI

A simple command-line interface to get random motivational quotes.

## Features

- Get a random motivational quote
- Add your own quotes
- Lightweight and easy to use

## Installation

```bash
pip install motivational-quotes-cli
```

Or clone and run directly:

```bash
git clone https://github.com/yourusername/motivational-quotes-cli.git
cd motivational-quotes-cli
python -m quotes
```

## Usage

```bash
quotes
```

Example output:

> "The only way to do great work is to love what you do." – Steve Jobs

## Adding Quotes

Edit `quotes.json` to add more quotes in the format:

```json
[
  {
    "quote": "Your quote here",
    "author": "Author Name"
  }
]
```

## License

MIT
