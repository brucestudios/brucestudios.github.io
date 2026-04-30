#!/usr/bin/env python3
"""
Inspirational Quote CLI
A command-line tool that prints random inspirational quotes.
"""

import argparse
import sys
import random
from . import __version__

# Collection of inspirational quotes
QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. – Aristotle",
    "Whoever is happy will make others happy too. – Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "In the end, it's not the years in your life that count. It's the life in your years. – Abraham Lincoln",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The best way to predict the future is to create it. – Peter Drucker",
    "Strive not to be a success, but rather to be of value. – Albert Einstein",
    "Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference. – Robert Frost",
    "I attribute my success to this: I never gave or took any excuse. – Florence Nightingale",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Why fit in when you were born to stand out? – Dr. Seuss",
    "The question isn't who is going to let me; it's who is going to stop me. – Ayn Rand",
]


def get_random_quote():
    """Return a random inspirational quote."""
    return random.choice(QUOTES)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Print random inspirational quotes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  quote              Print a random inspirational quote
  quote -c 3         Print 3 random quotes
  quote --copy       Copy quote to clipboard (if available)
  quote --color      Display quote in color
        """
    )
    
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of quotes to display (default: 1)'
    )
    
    parser.add_argument(
        '--copy',
        action='store_true',
        help='Copy quote to clipboard (requires pyperclip)'
    )
    
    parser.add_argument(
        '--color',
        action='store_true',
        help='Display quote in color'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'inspirational-quote-cli {__version__}'
    )
    
    args = parser.parse_args()
    
    # Validate count
    if args.count < 1:
        print("Error: count must be at least 1", file=sys.stderr)
        sys.exit(1)
    
    # Get quotes
    quotes = [get_random_quote() for _ in range(args.count)]
    
    # Display quotes
    for i, quote in enumerate(quotes, 1):
        if args.color:
            # Simple ANSI color codes
            colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
            color = colors[i % len(colors)]
            reset = '\033[0m'
            if args.count > 1:
                print(f"{color}{i}. {quote}{reset}")
            else:
                print(f"{color}{quote}{reset}")
        else:
            if args.count > 1:
                print(f"{i}. {quote}")
            else:
                print(quote)
    
    # Handle clipboard copy
    if args.copy and args.count == 1:
        try:
            import pyperclip
            pyperclip.copy(quotes[0])
            print("\nQuote copied to clipboard!", file=sys.stderr)
        except ImportError:
            print("\nWarning: pyperclip not installed. Install with: pip install pyperclip", file=sys.stderr)
        except Exception as e:
            print(f"\nWarning: Could not copy to clipboard: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()