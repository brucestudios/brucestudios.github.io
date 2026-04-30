"""Command-line interface for pwgen."""

import argparse
import sys
from typing import List, Optional

from .core import generate_password, generate_multiple_passwords


def _positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate secure passwords.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l",
        "--length",
        type=_positive_int,
        default=16,
        help="Length of each password",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=_positive_int,
        default=1,
        help="Number of passwords to generate",
    )
    parser.add_argument(
        "--no-upper",
        action="store_false",
        dest="use_upper",
        help="Do not include uppercase letters",
    )
    parser.add_argument(
        "--no-lower",
        action="store_false",
        dest="use_lower",
        help="Do not include lowercase letters",
    )
    parser.add_argument(
        "--no-digits",
        action="store_false",
        dest="use_digits",
        help="Do not include digits",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_false",
        dest="use_symbols",
        help="Do not include symbols",
    )
    parser.add_argument(
        "--exclude-ambiguous",
        action="store_true",
        help="Exclude ambiguous characters (il1Lo0O)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"pwgen {__import__('pwgen').__version__}",
    )

    args = parser.parse_args(argv)

    if args.number == 1:
        password = generate_password(
            args.length,
            use_upper=args.use_upper,
            use_lower=args.use_lower,
            use_digits=args.use_digits,
            use_symbols=args.use_symbols,
            exclude_ambiguous=args.exclude_ambiguous,
        )
        print(password)
    else:
        passwords = generate_multiple_passwords(
            args.number,
            args.length,
            use_upper=args.use_upper,
            use_lower=args.use_lower,
            use_digits=args.use_digits,
            use_symbols=args.use_symbols,
            exclude_ambiguous=args.exclude_ambiguous,
        )
        for pwd in passwords:
            print(pwd)

    return 0


if __name__ == "__main__":
    sys.exit(main())