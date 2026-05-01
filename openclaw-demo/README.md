# Weather CLI

A simple command-line tool to get current weather for any location using [wttr.in](https://wttr.in).

## Features

- Fetches real-time weather data
- Displays temperature, feels like, humidity, wind speed, and weather description
- Supports any location that wttr.in understands (city name, coordinates, IP address, etc.)
- Lightweight and dependency-free (uses only Python standard library)

## Installation

You can install the package via pip:

```bash
pip install weather-cli
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/weather-cli.git
```

## Usage

```bash
weather-cli <location>
```

### Examples

```bash
weather-cli London
weather-cli "New York"
weather-cli paris
weather-cli 40.7128,-74.0060  # Coordinates
weather-cli @123.45.67.89     # IP address
```

## Output

The tool outputs a formatted weather report:

```
Weather: Partly cloudy
Temperature: 22°C (72°F)
Feels like: 23°C (73°F)
Humidity: 65%
Wind speed: 10 km/h (6 mph)
```

## Requirements

- Python 3.6+
- Internet connection (to fetch data from wttr.in)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data provided by [wttr.in](https://wttr.in)
- Built with ❤️ using Python