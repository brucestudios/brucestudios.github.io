#!/usr/bin/env python3
"""
World Clock Utility
Displays current time in multiple timezones.
"""

import datetime
import pytz

def main():
    # Define the timezones we want to display
    timezones = [
        'UTC',
        'Asia/Shanghai',
        'America/New_York',
        'Europe/London',
        'Asia/Tokyo',
        'Australia/Sydney'
    ]

    print("Current time around the world:")
    print("-" * 30)
    for tz in timezones:
        timezone = pytz.timezone(tz)
        now = datetime.datetime.now(timezone)
        print(f"{tz}: {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

if __name__ == "__main__":
    main()