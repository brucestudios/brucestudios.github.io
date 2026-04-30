#!/usr/bin/env python3
"""
Password Generator - Generate secure passwords.

Usage:
    python main.py [--length LENGTH] [--count COUNT] [--no-symbols] [--no-numbers] [--no-uppercase] [--no-lowercase]

Options:
    --length LENGTH   Length of each password (default: 16)
    --count COUNT     Number of passwords to generate (default: 1)
    --no-symbols      Exclude symbols
    --no-numbers      Exclude numbers
    --no-uppercase    Exclude uppercase letters
    --no-lowercase    Exclude lowercase letters
"""

import argparse
import string
import random
import sys


def generate_password(length=16, use_symbols=True, use_numbers=True, use_uppercase=True, use_lowercase=True):
    """Generate a random password."""
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(random.choice(characters) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument('--length', type=int, default=16, help='Length of each password')
    parser.add_argument('--count', type=int, default=1, help='Number of passwords to generate')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('--no-numbers', action='store_true', help='Exclude numbers')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lowercase', action='store_true', help='Exclude lowercase letters')

    args = parser.parse_args()

    try:
        for _ in range(args.count):
            pwd = generate_password(
                length=args.length,
                use_symbols=not args.no_symbols,
                use_numbers=not args.no_numbers,
                use_uppercase=not args.no_uppercase,
                use_lowercase=not args.no_lowercase
            )
            print(pwd)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()