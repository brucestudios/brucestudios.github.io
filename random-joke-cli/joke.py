#!/usr/bin/env python3
"""
Random Joke CLI - A simple command-line tool to fetch and display random jokes.
"""

import json
import random
import sys
from urllib import request, error

# Local fallback jokes in case the API is unavailable
LOCAL_JOKES = [
    {
        "setup": "Why don't scientists trust atoms anymore?",
        "punchline": "Because they make up everything!"
    },
    {
        "setup": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "setup": "I'm reading a book about anti-gravity.",
        "punchline": "It's impossible to put down!"
    },
    {
        "setup": "Did you hear about the mathematician who's afraid of negative numbers?",
        "punchline": "He'll stop at nothing to avoid them!"
    },
    {
        "setup": "Why did the bicycle fall over?",
        "punchline": "Because it was two-tired!"
    }
]

def fetch_joke_from_api():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        with request.urlopen(url, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return {
                    "setup": data.get("setup", ""),
                    "punchline": data.get("punchline", "")
                }
    except (error.URLError, error.HTTPError, json.JSONDecodeError, KeyError) as e:
        print(f"Warning: Could not fetch joke from API: {e}", file=sys.stderr)
    return None

def get_random_joke():
    """Get a random joke, trying the API first then falling back to local jokes."""
    joke = fetch_joke_from_api()
    if joke is None:
        joke = random.choice(LOCAL_JOKES)
    return joke

def main():
    """Main entry point for the CLI."""
    joke = get_random_joke()
    print(f"\n{joke['setup']}")
    print(f"{joke['punchline']}\n")

if __name__ == "__main__":
    main()