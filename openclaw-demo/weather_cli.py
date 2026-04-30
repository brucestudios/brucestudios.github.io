#!/usr/bin/env python3
"""
Weather CLI - A simple command-line tool to get current weather.

Usage:
    weather-cli <location>
    weather-cli (-h | --help)

Options:
    -h --help     Show this screen.
"""
import sys
import json
import urllib.request
import urllib.error

def get_weather(location):
    """Fetch weather data from wttr.in for the given location."""
    url = f"https://wttr.in/{location}?format=j1"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data
    except urllib.error.URLError as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        sys.exit(1)

def format_weather(data):
    """Format the weather data into a human-readable string."""
    current = data['current_condition'][0]
    weather_desc = current['weatherDesc'][0]['value']
    temp_c = current['temp_C']
    temp_f = current['temp_F']
    feels_like_c = current['FeelsLikeC']
    feels_like_f = current['FeelsLikeF']
    humidity = current['humidity']
    wind_speed_kmh = current['windspeedKmph']
    wind_speed_mph = current['windspeedMiles']

    output = (
        f"Weather: {weather_desc}\n"
        f"Temperature: {temp_c}°C ({temp_f}°F)\n"
        f"Feels like: {feels_like_c}°C ({feels_like_f}°F)\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind_speed_kmh} km/h ({wind_speed_mph} mph)"
    )
    return output

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)

    location = sys.argv[1]
    data = get_weather(location)
    print(format_weather(data))

if __name__ == '__main__':
    main()