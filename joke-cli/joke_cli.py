#!/usr/bin/env python3
"""
A simple CLI tool to fetch and display a random joke.
"""

import sys
import requests

def fetch_joke():
    """Fetch a random joke from the Official Joke API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke_data = response.json()
        return f"{joke_data['setup']}\n{joke_data['punchline']}"
    except requests.RequestException as e:
        return f"Error fetching joke: {e}"

def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    
    joke = fetch_joke()
    print(joke)

if __name__ == "__main__":
    main()
