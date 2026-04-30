#!/usr/bin/env python3
"""
WeatherCLI - A simple command-line tool to get weather information.
"""

import sys
import urllib.request
import urllib.error
import argparse

def get_weather(location: str = "") -> str:
    """
    Fetch weather information for a given location using wttr.in.
    
    Args:
        location: The location to get weather for. If empty, uses IP-based location.
    
    Returns:
        Formatted weather string.
    """
    # Format 3 provides: "+City: Weather condition +Temperature"
    url = f"http://wttr.in/{location}?format=3"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode('utf-8').strip()
            return data
    except urllib.error.URLError as e:
        return f"Error fetching weather: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    parser = argparse.ArgumentParser(
        description="Get current weather information for a location.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  weathercli                    # Weather for your current location (based on IP)
  weathercli London             # Weather for London
  weathercli "New York"         # Weather for New York
  weathercli -h                 # Show this help message
        """
    )
    parser.add_argument(
        'location',
        nargs='?',
        default='',
        help='Location to get weather for (city, region, etc.). Defaults to your current location.'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='WeatherCLI 1.0.0'
    )
    
    args = parser.parse_args()
    
    weather_info = get_weather(args.location)
    print(weather_info)

if __name__ == "__main__":
    main()