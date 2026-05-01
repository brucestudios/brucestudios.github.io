import secrets
import string
from typing import List

def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_punctuation: bool = True,
) -> str:
    """Generate a secure random password.

    Args:
        length: The length of the password to generate.
        use_uppercase: Include uppercase letters (A-Z).
        use_lowercase: Include lowercase letters (a-z).
        use_digits: Include digits (0-9).
        use_punctuation: Include punctuation characters.

    Returns:
        A randomly generated password string.

    Raises:
        ValueError: If the resulting character set is empty.
    """
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(secrets.choice(characters) for _ in range(length))


def generate_passphrase(
    word_count: int = 4,
    word_list: List[str] = None,
    separator: str = "-",
) -> str:
    """Generate a secure passphrase from a word list.

    Args:
        word_count: Number of words in the passphrase.
        word_list: List of words to choose from. If None, uses a built-in list.
        separator: String to join the words with.

    Returns:
        A randomly generated passphrase string.
    """
    if word_list is None:
        # A small built-in word list for demonstration; in production, use a larger list.
        word_list = [
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon",
            "mango", "nectarine", "orange", "peach", "quince",
            "raspberry", "strawberry", "tomato", "ugli", "vanilla",
            "watermelon", "xigua", "yellow", "zucchini"
        ]

    if not word_list:
        raise ValueError("Word list must not be empty")

    words = [secrets.choice(word_list) for _ in range(word_count)]
    return separator.join(words)


def generate_api_key(
    length: int = 32,
) -> str:
    """Generate a secure random API key (URL-safe base64).

    Args:
        length: The length of the API key in bytes (will be base64 encoded).

    Returns:
        A URL-safe base64 encoded string.
    """
    token = secrets.token_bytes(length)
    # Use URL-safe base64 encoding without padding
    import base64
    return base64.urlsafe_b64encode(token).rstrip(b'=').decode('ascii')