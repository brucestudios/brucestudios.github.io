#!/usr/bin/env python3
"""
A simple command-line password generator.
"""

import argparse
import string
import random
import sys

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a random password."""
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password (default: 12)')
    parser.add_argument('--no-upper', action='store_false', dest='use_upper', help='Do not include uppercase letters')
    parser.add_argument('--no-lower', action='store_false', dest='use_lower', help='Do not include lowercase letters')
    parser.add_argument('--no-digits', action='store_false', dest='use_digits', help='Do not include digits')
    parser.add_argument('--no-symbols', action='store_false', dest='use_symbols', help='Do not include symbols')
    parser.add_argument('-q', '--quiet', action='store_true', help='Only output the password')

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=args.use_upper,
            use_lower=args.use_lower,
            use_digits=args.use_digits,
            use_symbols=args.use_symbols
        )
    except ValueError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

    if args.quiet:
        print(password)
    else:
        print(f"Generated password: {password}")

if __name__ == '__main__':
    main()