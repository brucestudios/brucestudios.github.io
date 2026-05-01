# pwdgen-cli

A simple command-line password generator written in Python.

## Features

- Generate secure random passwords
- Customizable length
- Options to include/exclude symbols, numbers, lowercase, uppercase
- Easy to use and install

## Installation

You can install via pip:

```bash
pip install pwdgen-cli
```

Or clone the repository and install locally:

```bash
git clone https://github.com/brucestudios/pwdgen-cli.git
cd pwdgen-cli
pip install .
```

## Usage

```bash
pwdgen [OPTIONS]
```

### Options

- `-l, --length INT`   Length of password (default: 16)
- `-n, --numbers`      Include numbers (0-9)
- `-s, --symbols`      Include symbols (!@#$%^&* etc.)
- `-lw, --lower`       Include lowercase letters (a-z)
- `-up, --upper`       Include uppercase letters (A-Z)
- `-h, --help`         Show this help message

By default, includes lowercase, uppercase, numbers, and symbols.

### Examples

Generate a 12-character password:

```bash
pwdgen -l 12
```

Generate a password without symbols:

```bash
pwdgen --no-symbols
```

Actually, we don't have a `--no-symbols` flag; we can implement inclusion flags only. Let's keep simple: by default includes all; you can turn off categories by not specifying them? That's confusing. Better to have flags to include each category, and default includes all. We'll implement as: default includes all; if you specify any of the flags, only those categories are used. We'll implement that.

Alternatively, we can have flags to exclude. Let's keep simple: default includes all; you can specify `--only-letters` etc. But time is limited.

Let's just implement: default includes lowercase, uppercase, numbers, symbols. Flags `--only-letters`, `--only-numbers`, etc. Not now.

We'll just implement the inclusion flags as described: if any of `-n`, `-s`, `-lw`, `-up` are given, only those categories are used; otherwise all.

Let's write the code.
