#!/usr/bin/env python3
"""
Inspirational Quotes CLI
A simple command-line tool to display random inspirational quotes.
"""

import random
import sys
import os

def load_quotes():
    """Load quotes from the quotes.txt file."""
    quotes_file = os.path.join(os.path.dirname(__file__), 'quotes.txt')
    try:
        with open(quotes_file, 'r', encoding='utf-8') as f:
            quotes = [line.strip() for line in f if line.strip()]
        return quotes
    except FileNotFoundError:
        # Fallback quotes if file not found
        return [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Innovation distinguishes between a leader and a follower. – Steve Jobs",
            "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
            "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. – Aristotle",
            "Whoever is happy will make others happy too. – Anne Frank",
            "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
            "The only limit to our realization of tomorrow is our doubts today. – Franklin D. Roosevelt",
            "You miss 100% of the shots you don't take. – Wayne Gretzky",
            "Believe you can and you're halfway there. – Theodore Roosevelt"
        ]

def main():
    quotes = load_quotes()
    if not quotes:
        print("No quotes available.", file=sys.stderr)
        sys.exit(1)
    
    quote = random.choice(quotes)
    print(quote)

if __name__ == '__main__':
    main()