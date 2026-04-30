# Timezone CLI Tool

A simple command-line tool for converting time between different timezones.

## Features

- Convert current time to any timezone
- Convert a specific time between timezones
- List common timezones
- Easy to use and install

## Installation

```bash
pip install tz-cli
```

## Usage

### Convert current time to a timezone

```bash
tz now --to America/New_York
```

### Convert a specific time between timezones

```bash
tz convert "2026-04-29 10:00" --from Asia/Shanghai --to Europe/London
```

### List common timezones

```bash
tz list
```

## Requirements

- Python 3.6+
- pytz

## License

MIT