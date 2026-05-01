#!/usr/bin/env python3
"""
Weather CLI - A simple command-line tool to get weather information.

Usage:
    weathercli [location]

If no location is provided, it defaults to the user's current location (based on IP).
"""

import sys
import urllib.request
import urllib.error
import json

def get_weather(location=""):
    """
    Fetch weather data from wttr.in for the given location.
    Returns a string with the weather information.
    """
    # wttr.in format: we want a simple text output
    # We use the format option to get a concise output
    url = f"http://wttr.in/{location}?format=3" if location else "http://wttr.in?format=3"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8').strip()
    except urllib.error.URLError as e:
        return f"Error fetching weather data: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    # Get location from command line argument, if any
    location = sys.argv[1] if len(sys.argv) > 1 else ""
    weather_info = get_weather(location)
    print(weather_info)

if __name__ == "__main__":
    main()