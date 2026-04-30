"""Password generation utilities."""

import random
import string
from typing import Optional


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """Generate a random password.

    Args:
        length: Length of the password. Must be at least 1.
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_digits: Include digits.
        use_special: Include special characters.

    Returns:
        A randomly generated password.

    Raises:
        ValueError: If length < 1 or no character sets are selected.
    """
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


def generate_passphrase(
    num_words: int = 4,
    word_list: Optional[list] = None,
    separator: str = '-',
) -> str:
    """Generate a passphrase by joining random words.

    Args:
        num_words: Number of words in the passphrase.
        word_list: List of words to choose from. If None, uses a built-in list.
        separator: String to join the words.

    Returns:
        A passphrase string.
    """
    if word_list is None:
        word_list = [
            "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
            "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach",
            "quince", "raspberry", "strawberry", "tangerine", "watermelon",
            "zucchini", "apricot", "blueberry", "coconut", "dragonfruit",
        ]
    if not word_list:
        raise ValueError("Word list must not be empty")
    if num_words < 1:
        raise ValueError("Number of words must be at least 1")

    selected = [random.choice(word_list) for _ in range(num_words)]
    return separator.join(selected)