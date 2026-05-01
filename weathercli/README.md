# WeatherCLI

A simple command-line tool to get current weather information for any location.

## Features

- Get weather for your current location (based on IP)
- Get weather for any city, region, or location
- Simple and fast, powered by [wttr.in](https://wttr.in)
- No API key required

## Installation

You can install WeatherCLI via pip:

```bash
pip install weathercli
```

Or install directly from source:

```bash
git clone https://github.com/brucestudios/weathercli.git
cd weathercli
pip install .
```

## Usage

```bash
# Get weather for your current location
weathercli

# Get weather for a specific city
weathercli London
weathercli "New York"
weathercli Tokyo,JP
```

## Example Output

```
London: +15°C ☀️
```

## Requirements

- Python 3.6+
- Internet connection (to fetch weather data)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Weather data provided by [wttr.in](https://wttr.in)
- Built with Python and setuptools