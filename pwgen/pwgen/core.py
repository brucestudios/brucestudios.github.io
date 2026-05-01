"""Password generation core."""

import secrets
import string
from typing import List, Optional


def generate_password(
    length: int = 16,
    *,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> str:
    """Generate a secure random password.

    Args:
        length: Length of the password. Must be >= 1.
        use_upper: Include uppercase letters (A-Z).
        use_lower: Include lowercase letters (a-z).
        use_digits: Include digits (0-9).
        use_symbols: Include punctuation symbols.
        exclude_ambiguous: Exclude ambiguous characters like il1Lo0O.

    Returns:
        A randomly generated password string.

    Raises:
        ValueError: If length < 1 or no character sets selected.
    """
    if length < 1:
        raise ValueError("length must be at least 1")

    # Build character set
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if exclude_ambiguous:
        ambiguous = "il1Lo0O"
        chars = "".join(c for c in chars if c not in ambiguous)

    if not chars:
        raise ValueError("No characters selected for password generation")

    # Use secrets.choice for cryptographically secure random selection
    return "".join(secrets.choice(chars) for _ in range(length))


def generate_multiple_passwords(
    count: int,
    length: int = 16,
    *,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> List[str]:
    """Generate multiple secure passwords.

    Args:
        count: Number of passwords to generate.
        length: Length of each password.
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include punctuation symbols.
        exclude_ambiguous: Exclude ambiguous characters.

    Returns:
        List of generated password strings.
    """
    return [
        generate_password(
            length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_ambiguous=exclude_ambiguous,
        )
        for _ in range(count)
    ]


__all__ = ["generate_password", "generate_multiple_passwords"]