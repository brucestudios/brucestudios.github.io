import secrets
import string
from typing import Optional


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
    ambiguous: bool = False,
) -> str:
    """
    Generate a cryptographically secure password.

    Args:
        length: The length of the password to generate. Must be >= 1.
        use_uppercase: Include uppercase letters (A-Z).
        use_lowercase: Include lowercase letters (a-z).
        use_digits: Include digits (0-9).
        use_special: Include special characters.
        ambiguous: If False, exclude ambiguous characters (Il1O0o).

    Returns:
        A randomly generated password string.

    Raises:
        ValueError: If length is less than 1 or if no character sets are selected.
    """
    if length < 1:
        raise ValueError("Length must be at least 1")

    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Remove ambiguous characters if requested
    if not ambiguous:
        ambiguous_chars = "Il1O0o"
        uppercase = uppercase.translate(str.maketrans("", "", ambiguous_chars))
        lowercase = lowercase.translate(str.maketrans("", "", ambiguous_chars))
        digits = digits.translate(str.maketrans("", "", ambiguous_chars))
        # Note: special characters do not contain ambiguous ones by our definition

    # Build the character set
    chars = ""
    if use_uppercase:
        chars += uppercase
    if use_lowercase:
        chars += lowercase
    if use_digits:
        chars += digits
    if use_special:
        chars += special

    if not chars:
        raise ValueError("At least one character set must be selected")

    # Generate the password
    return ''.join(secrets.choice(chars) for _ in range(length))


def main():
    """Entry point for the command-line interface."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure passwords."
    )
    parser.add_argument(
        "-l", "--length", type=int, default=16, help="Length of the password (default: 16)"
    )
    parser.add_argument(
        "--no-uppercase", action="store_false", dest="use_uppercase", help="Exclude uppercase letters"
    )
    parser.add_argument(
        "--no-lowercase", action="store_false", dest="use_lowercase", help="Exclude lowercase letters"
    )
    parser.add_argument(
        "--no-digits", action="store_false", dest="use_digits", help="Exclude digits"
    )
    parser.add_argument(
        "--no-special", action="store_false", dest="use_special", help="Exclude special characters"
    )
    parser.add_argument(
        "--ambiguous", action="store_true", help="Include ambiguous characters (Il1O0o)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)"
    )
    parser.add_argument(
        "--digits-only", action="store_true", help="Generate a PIN (digits only)"
    )
    parser.add_argument(
        "--pronounceable", action="store_true", help="Generate a pronounceable password (alternating vowels/consonants)"
    )

    args = parser.parse_args()

    # Handle special flags that override other options
    if args.digits_only:
        args.use_uppercase = False
        args.use_lowercase = False
        args.use_digits = True
        args.use_special = False
        args.ambiguous = False  # digits are not ambiguous in our set
        # We'll ignore length for now, but note: the user can still set length

    if args.pronounceable:
        # We'll implement a simple pronounceable generator: alternating vowels and consonants
        # For simplicity, we'll just use a predefined set and generate accordingly.
        # But note: this is a separate algorithm. We'll override the standard generation.
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        # Alternate: start with either vowel or consonant? Let's do consonant then vowel by default.
        # We'll generate by picking randomly from the set for each position, but alternating sets.
        # However, the user might want a specific length. We'll generate accordingly.
        passwords = []
        for _ in range(args.count):
            password = []
            for i in range(args.length):
                if i % 2 == 0:
                    # even index: consonant
                    password.append(secrets.choice(consonants))
                else:
                    # odd index: vowel
                    password.append(secrets.choice(vowels))
            passwords.append(''.join(password))
        for p in passwords:
            print(p)
        return

    # Standard generation
    try:
        for _ in range(args.count):
            password = generate_password(
                length=args.length,
                use_uppercase=args.use_uppercase,
                use_lowercase=args.use_lowercase,
                use_digits=args.use_digits,
                use_special=args.use_special,
                ambiguous=args.ambiguous,
            )
            print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()