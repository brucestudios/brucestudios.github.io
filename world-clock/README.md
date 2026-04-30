# World Clock

A simple Python utility that displays the current time in multiple timezones.

## Features

- Shows current time in UTC, Shanghai, New York, London, Tokyo, and Sydney
- Easy to extend with additional timezones
- Uses the `pytz` library for accurate timezone handling

## Usage

```bash
python world_clock.py
```

Sample output:
```
Current time around the world:
------------------------------
UTC: 2026-04-30 16:30:00 UTC+0000
Asia/Shanghai: 2026-04-31 00:30:00 CST+0800
America/New_York: 2026-04-30 12:30:00 EDT-0400
Europe/London: 2026-04-30 17:30:00 BST+0100
Asia/Tokyo: 2026-04-31 01:30:00 JST+0900
Australia/Sydney: 2026-04-31 02:30:00 AEST+1000
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/brucestudios/world-clock.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python world_clock.py
   ```

## License

This project is open source and available under the MIT License.