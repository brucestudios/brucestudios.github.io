#!/usr/bin/env python3
"""
Weather CLI - Get current weather using wttr.in
"""

import sys
import subprocess
import argparse

def get_weather(location=None):
    """Get weather for a location using wttr.in"""
    if location:
        url = f"http://wttr.in/{location}?format=3"
    else:
        url = "http://wttr.in?format=3"
    
    try:
        # Use curl to fetch the weather
        proc = subprocess.Popen(
            ["curl", "-s", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            return stdout.decode('utf-8').strip()
        else:
            return f"Error: {stderr.decode('utf-8').strip()}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Get current weather")
    parser.add_argument(
        "location", 
        nargs="?", 
        help="Location to get weather for (city, zip code, etc.)"
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Show detailed weather information"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        # For verbose, we can use a different format
        if args.location:
            url = f"http://wttr.in/{args.location}?format=4"
        else:
            url = "http://wttr.in?format=4"
        
        try:
            proc = subprocess.Popen(
                ["curl", "-s", url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = proc.communicate()
            if proc.returncode == 0:
                print(stdout.decode('utf-8').strip())
            else:
                print(f"Error: {stderr.decode('utf-8').strip()}", file=sys.stderr)
                sys.exit(1)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)
    else:
        weather = get_weather(args.location)
        print(weather)

if __name__ == "__main__":
    main()
