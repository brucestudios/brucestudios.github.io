import argparse
import random
import string
import sys


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
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
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    # Ensure at least one character from each selected set
    password = []
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest with random choices from the combined set
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument(
        "-l", "--length", type=int, default=16, help="Length of the password (default: 16)"
    )
    parser.add_argument(
        "-n", "--no-special", action="store_true", help="Exclude special characters"
    )
    parser.add_argument(
        "-d", "--no-digits", action="store_true", help="Exclude digits"
    )
    parser.add_argument(
        "-c", "--lower-only", action="store_true", help="Generate lowercase letters only"
    )
    parser.add_argument(
        "-u", "--upper-only", action="store_true", help="Generate uppercase letters only"
    )
    args = parser.parse_args()

    # Handle mutually exclusive options
    if args.lower_only and args.upper_only:
        parser.error("Options --lower-only and --upper-only are mutually exclusive")

    use_lower = not args.no_special  # Actually, we want to control lowercase separately
    # Let's redefine the flags for clarity:
    # We have: --no-special, --no-digits, --lower-only, --upper-only
    # We'll interpret:
    #   use_lower = True unless --upper-only is set (then False) or if we want to exclude lowercase? Actually, we don't have a flag to exclude lowercase.
    # Let's change approach: we'll have explicit inclusion flags, but for simplicity, we'll use:
    #   use_lower = not args.upper_only  (if upper_only, then no lower) but we also have lower_only.
    # This is getting messy. Let's redesign the flags.

    # Instead, let's use:
    #   --no-special: exclude special
    #   --no-digits: exclude digits
    #   --no-lower: exclude lowercase (we don't have this, but we can add if needed)
    #   --no-upper: exclude uppercase (we don't have this)
    # But the user asked for --lower-only and --upper-only.

    # We'll do:
    #   If --lower-only: then only lowercase (so upper=False, digits=False, special=False)
    #   If --upper-only: then only uppercase (so lower=False, digits=False, special=False)
    #   Otherwise, we use the flags to exclude special and digits, and we always include both lower and upper unless overridden by the only flags.

    if args.lower_only:
        use_lower = True
        use_upper = False
        use_digits = False
        use_special = False
    elif args.upper_only:
        use_lower = False
        use_upper = True
        use_digits = False
        use_special = False
    else:
        use_lower = True
        use_upper = True
        use_digits = not args.no_digits
        use_special = not args.no_special

    try:
        password = generate_password(
            length=args.length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_special=use_special,
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()