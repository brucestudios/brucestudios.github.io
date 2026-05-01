# pwdmanager

A simple command-line password manager written in Python.

## Features

- Securely stores passwords using AES encryption (via Fernet from cryptography library)
- Master password protected vault
- Add, list, retrieve, and delete credentials
- Simple and intuitive CLI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pwdmanager.git
   ```
2. Install the required package:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with `python -m pwdmanager.main` or make it executable and run `./pwdmanager/main.py`.

### Commands

- `add <service> [--username USERNAME]`: Add a new credential for a service.
- `list`: List all stored services.
- `get <service>`: Retrieve the credential for a service.
- `delete <service>`: Delete the credential for a service.

### Example

```bash
# Add a new credential
python -m pwdmanager.main add github.com --username myuser

# List services
python -m pwdmanager.main list

# Get a credential
python -m pwdmanager.main get github.com

# Delete a credential
python -m pwdmanager.main delete github.com
```

## Security

- The vault file (`~/.pwdmanager/vault.enc`) is encrypted using AES-128 in CBC mode (via Fernet).
- The encryption key is derived from a master password using PBKDF2HMAC with SHA256, a random salt, and 100,000 iterations.
- The vault file and the key derivation salt are stored separately in the same file (salt + encrypted data).
- Never store your master password in plain text or lose it; without it, the vault cannot be recovered.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with the [cryptography](https://cryptography.io/) library.