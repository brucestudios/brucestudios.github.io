#!/usr/bin/env python3
"""
Weather Checker Utility

A simple command-line tool to get current weather information for any location
using the wttr.in service.
"""

import sys
import argparse
import json
import urllib.request
import urllib.error


def get_weather(location="", format="json"):
    """
    Fetch weather data from wttr.in.

    Args:
        location (str): Location to check (city, zip code, etc.). Empty for current location.
        format (str): Output format, either 'json' or 'text'.

    Returns:
        dict or str: Weather data in the requested format, or None on error.
    """
    if location:
        url = f"https://wttr.in/{location}?format={format}"
    else:
        url = f"https://wttr.in?format={format}"

    try:
        with urllib.request.urlopen(url) as response:
            if format == "json":
                return json.loads(response.read().decode())
            else:
                return response.read().decode()
    except urllib.error.URLError as e:
        print(f"Error fetching weather data: {e.reason}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing weather data: {e}", file=sys.stderr)
        return None


def display_weather_text(data):
    """Display weather data in a human-readable text format."""
    if not data:
        print("No weather data available.")
        return

    # Extract current condition
    current = data.get('current_condition', [{}])[0]
    # Extract location info
    nearest_area = data.get('nearest_area', [{}])[0]
    area_name = nearest_area.get('areaName', [{}])[0].get('value', 'Unknown')
    region = nearest_area.get('region', [{}])[0].get('value', '')
    country = nearest_area.get('country', [{}])[0].get('value', '')

    print(f"Weather for {area_name}, {region}, {country}")
    print("=" * 50)
    print(f"Temperature: {current.get('temp_C', 'N/A')}°C ({current.get('temp_F', 'N/A')}°F)")
    print(f"Feels like: {current.get('FeelsLikeC', 'N/A')}°C ({current.get('FeelsLikeF', 'N/A')}°F)")
    print(f"Humidity: {current.get('humidity', 'N/A')}%")
    print(f"Wind: {current.get('windspeedKmph', 'N/A')} km/h {current.get('winddir16Point', 'N/A')}")
    print(f"Condition: {current.get('weatherDesc', [{}])[0].get('value', 'N/A')}")
    print(f"Pressure: {current.get('pressure', 'N/A')} mb")
    print(f"Visibility: {current.get('visibility', 'N/A')} km")
    print(f"Cloud cover: {current.get('cloudcover', 'N/A')}%")


def main():
    parser = argparse.ArgumentParser(
        description="Get current weather information for any location."
    )
    parser.add_argument(
        "location",
        nargs="?",
        help="Location to check (city, zip code, etc.). If omitted, uses current location."
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output raw JSON data instead of formatted text."
    )

    args = parser.parse_args()

    if args.json:
        data = get_weather(args.location or "", "json")
        if data:
            print(json.dumps(data, indent=2))
    else:
        data = get_weather(args.location or "", "json")
        display_weather_text(data)


if __name__ == "__main__":
    main()