# InspiQuote

A simple Python command-line tool that generates random inspirational quotes.

## Features

- Fetch a random inspirational quote from a curated list.
- Easy-to-use command-line interface.
- Extensible: add your own quotes by editing the `quotes.json` file.
- Well-tested with pytest.
- Continuous Integration with GitHub Actions.

## Installation

```bash
pip install ispiriquote
```

## Usage

After installation, run:

```bash
insiquote
```

Example output:

> "The only way to do great work is to love what you do." – Steve Jobs

## Development

To set up the development environment:

```bash
git clone https://github.com/<your-username>/insiquote.git
cd inspiquote
pip install -e .[dev]
```

Run tests:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- Quote list inspired by various sources.