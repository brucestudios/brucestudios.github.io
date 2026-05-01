#!/usr/bin/env python3
import requests
import sys

def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list):
            quote = data[0].get('q')
            author = data[0].get('a')
            return f'"{quote}" — {author}'
        else:
            return "No quote found."
    except Exception as e:
        return f"Error fetching quote: {e}"

def main():
    quote = fetch_quote()
    print(quote)

if __name__ == "__main__":
    main()