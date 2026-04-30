# Weather CLI

A simple command-line tool to get current weather and forecasts using the [wttr.in](https://wttr.in) service.

## Installation

```bash
pip install weather-cli
```

## Usage

### Current weather

```bash
weather
```
or specify a location:
```bash
weather London
```

### Forecast

```bash
weather forecast
```
or for a specific location and number of days:
```bash
weather forecast Paris --days 2
```

## Options

- `--days`, `-d`: Number of days for forecast (1-3, default: 3)

## Examples

```bash
# Current weather for New York
weather New York

# 2-day forecast for Tokyo
weather forecast Tokyo --days 2
```

## License

MIT