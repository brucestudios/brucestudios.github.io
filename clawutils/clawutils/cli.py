import argparse
import sys
from . import __version__

def hello(args):
    print(f"Hello, {args.name}! Welcome to clawutils v{__version__}")

def version(args):
    print(f"clawutils version {__version__}")

def main():
    parser = argparse.ArgumentParser(
        prog="clawutils",
        description="A collection of useful CLI utilities for OpenClaw workflow"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"clawutils {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # hello command
    parser_hello = subparsers.add_parser("hello", help="Print a greeting")
    parser_hello.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World)"
    )
    parser_hello.set_defaults(func=hello)

    # version command (explicit, though we already have -v/--version)
    parser_version = subparsers.add_parser("version", help="Print the version")
    parser_version.set_defaults(func=version)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    sys.exit(main())