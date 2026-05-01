# Weather CLI

A simple command-line tool to get weather information using [wttr.in](https://wttr.in).

## Features

- Get weather for any location by providing it as an argument.
- If no location is provided, it uses your IP to determine your current location.
- Lightweight and dependency-free (uses only Python standard library).

## Installation

You can install it via pip:

```bash
pip install git+https://github.com/<your-username>/weathercli.git
```

Or clone the repository and install locally:

```bash
git clone https://github.com/<your-username>/weathercli.git
cd weathercli
pip install .
```

## Usage

```bash
weathercli [location]
```

Examples:

```bash
# Get weather for your current location (based on IP)
weathercli

# Get weather for New York
weathercli New%20York

# Get weather for London
weathercli London
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.