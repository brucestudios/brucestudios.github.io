#!/usr/bin/env python3
"""
Simple command-line password manager.
"""

import argparse
import os
import sys
import json
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import secrets

VAULT_FILE = os.path.expanduser("~/.pwdmanager/vault.enc")
KEY_FILE = os.path.expanduser("~/.pwdmanager/key.key")
SALT_SIZE = 16
ITERATIONS = 100000

def ensure_dir():
    os.makedirs(os.path.dirname(VAULT_FILE), exist_ok=True)

def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def load_vault() -> dict:
    ensure_dir()
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "rb") as f:
        data = f.read()
    # First 16 bytes are salt, next is encrypted data
    if len(data) < SALT_SIZE:
        return {}
    salt = data[:SALT_SIZE]
    encrypted = data[SALT_SIZE:]
    # Ask for master password
    master_password = getpass("Master password: ")
    try:
        key = derive_key(master_password, salt)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)
        vault = json.loads(decrypted.decode())
        return vault
    except Exception as e:
        print(f"Error unlocking vault: {e}")
        sys.exit(1)

def save_vault(vault: dict):
    ensure_dir()
    # Generate salt
    salt = secrets.token_bytes(SALT_SIZE)
    # Ask for master password
    master_password = getpass("Master password: ")
    # Derive key
    key = derive_key(master_password, salt)
    fernet = Fernet(key)
    # Serialize vault
    plaintext = json.dumps(vault).encode()
    encrypted = fernet.encrypt(plaintext)
    # Write salt + encrypted
    with open(VAULT_FILE, "wb") as f:
        f.write(salt + encrypted)

def cmd_add(args):
    vault = load_vault()
    service = args.service
    username = args.username or input("Username: ")
    password = getpass("Password: ")
    if service in vault:
        overwrite = input(f"Service '{service}' already exists. Overwrite? (y/N) ").lower() == 'y'
        if not overwrite:
            print("Aborted.")
            return
    vault[service] = {"username": username, "password": password}
    save_vault(vault)
    print(f"Saved credential for {service}.")

def cmd_list(args):
    vault = load_vault()
    if not vault:
        print("No entries found.")
        return
    print("Services:")
    for service in sorted(vault.keys()):
        print(f"  {service}")

def cmd_get(args):
    vault = load_vault()
    service = args.service
    if service not in vault:
        print(f"No entry for service '{service}'.")
        return
    entry = vault[service]
    print(f"Service: {service}")
    print(f"Username: {entry['username']}")
    print(f"Password: {entry['password']}")

def cmd_delete(args):
    vault = load_vault()
    service = args.service
    if service not in vault:
        print(f"No entry for service '{service}'.")
        return
    confirm = input(f"Delete entry for '{service}'? (y/N) ").lower() == 'y'
    if confirm:
        del vault[service]
        save_vault(vault)
        print(f"Deleted entry for {service}.")
    else:
        print("Aborted.")

def main():
    parser = argparse.ArgumentParser(description="Simple password manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    parser_add = subparsers.add_parser("add", help="Add a new credential")
    parser_add.add_argument("service", help="Service name (e.g., github.com)")
    parser_add.add_argument("--username", help="Username (if not provided, will prompt)")
    parser_add.set_defaults(func=cmd_add)

    # list
    parser_list = subparsers.add_parser("list", help="List stored services")
    parser_list.set_defaults(func=cmd_list)

    # get
    parser_get = subparsers.add_parser("get", help="Get credential for a service")
    parser_get.add_argument("service", help="Service name")
    parser_get.set_defaults(func=cmd_get)

    # delete
    parser_del = subparsers.add_parser("delete", help="Delete credential for a service")
    parser_del.add_argument("service", help="Service name")
    parser_del.set_defaults(func=cmd_delete)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()