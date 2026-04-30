#!/usr/bin/env python3
"""
Awesome Password Generator
A simple and secure password generator written in Python.

Usage:
    python awesome_password_generator.py [length] [--no-symbols] [--no-numbers] [--uppercase]

Example:
    python awesome_password_generator.py 16
    python awesome_password_generator.py 20 --no-symbols
"""

import argparse
import random
import string
import sys

def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True):
    """Generate a random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Ensure at least one character from each required set
    required_chars = []
    required_chars.append(random.choice(lowercase))  # always include lowercase
    
    if use_uppercase:
        required_chars.append(random.choice(uppercase))
    if use_numbers:
        required_chars.append(random.choice(numbers))
    if use_symbols:
        required_chars.append(random.choice(symbols))
    
    # Fill the rest of the password length with random choices from all allowed characters
    all_chars = lowercase + uppercase + numbers + symbols
    if not all_chars:
        raise ValueError("At least one character set must be enabled.")
    
    remaining_length = length - len(required_chars)
    if remaining_length < 0:
        # If length is too short for the required sets, truncate required_chars
        required_chars = required_chars[:length]
        remaining_length = 0
    
    password_chars = required_chars + [random.choice(all_chars) for _ in range(remaining_length)]
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument('length', nargs='?', type=int, default=12,
                        help='Length of the password (default: 12)')
    parser.add_argument('--no-symbols', action='store_true',
                        help='Exclude symbols from the password')
    parser.add_argument('--no-numbers', action='store_true',
                        help='Exclude numbers from the password')
    parser.add_argument('--uppercase', action='store_true',
                        help='Include uppercase letters (default: off)')
    
    args = parser.parse_args()
    
    try:
        password = generate_password(
            length=args.length,
            use_symbols=not args.no_symbols,
            use_numbers=not args.no_numbers,
            use_uppercase=args.uppercase
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
