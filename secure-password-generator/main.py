#!/usr/bin/env python3
"""
Secure Password Generator
Generate strong, random passwords with customizable options.
"""

import argparse
import secrets
import string
import sys


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a secure random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Define character sets
    upper = string.ascii_uppercase if use_upper else ''
    lower = string.ascii_lowercase if use_lower else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Ensure at least one character from each selected set
    password_chars = []
    if use_upper:
        password_chars.append(secrets.choice(upper))
    if use_lower:
        password_chars.append(secrets.choice(lower))
    if use_digits:
        password_chars.append(secrets.choice(digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    # Fill the rest of the password length with random choices from all selected sets
    all_chars = upper + lower + digits + symbols
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)


def main():
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Length of the password (default: 16)"
    )
    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Exclude uppercase letters"
    )
    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Exclude lowercase letters"
    )
    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Exclude digits"
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclude symbols"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)"
    )
    args = parser.parse_args()

    # Validate arguments
    if args.length < 4:
        parser.error("Password length must be at least 4 characters")
    if args.number < 1:
        parser.error("Number of passwords must be at least 1")

    try:
        for _ in range(args.number):
            password = generate_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols
            )
            print(password)
    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()