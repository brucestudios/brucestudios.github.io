# Secretsmith

A Python package for generating secure passwords, passphrases, and API keys.

## Installation

```bash
pip install secretsmith
```

## Usage

```python
from secretsmith import generate_password, generate_passphrase, generate_api_key

# Generate a password
password = generate_password(length=20)
print(password)  # e.g., "v8X!zQ2#pL9@mN5$wE"

# Generate a passphrase
passphrase = generate_passphrase(word_count=4, separator="-")
print(passphrase)  # e.g., "apple-banana-cherry-date"

# Generate an API key
api_key = generate_api_key()
print(api_key)  # e.g., "aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"
```

## API

### `generate_password`

Generate a secure random password.

**Parameters:**

- `length` (int): The length of the password to generate. Default: 16.
- `use_uppercase` (bool): Include uppercase letters (A-Z). Default: True.
- `use_lowercase` (bool): Include lowercase letters (a-z). Default: True.
- `use_digits` (bool): Include digits (0-9). Default: True.
- `use_punctuation` (bool): Include punctuation characters. Default: True.

**Returns:** A randomly generated password string.

### `generate_passphrase`

Generate a secure passphrase from a word list.

**Parameters:**

- `word_count` (int): Number of words in the passphrase. Default: 4.
- `word_list` (List[str], optional): List of words to choose from. If None, uses a built-in list.
- `separator` (str): String to join the words with. Default: "-".

**Returns:** A randomly generated passphrase string.

### `generate_api_key`

Generate a secure random API key (URL-safe base64).

**Parameters:**

- `length` (int): The length of the API key in bytes (will be base64 encoded). Default: 32.

**Returns:** A URL-safe base64 encoded string.

## Testing

Run the tests with:

```bash
python -m unittest discover tests
```

## License

MIT