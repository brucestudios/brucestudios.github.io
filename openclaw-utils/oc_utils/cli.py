#!/usr/bin/env python3
"""
OpenClaw Toolkit CLI
"""

import argparse
import sys
from pathlib import Path

def memory_summary():
    """Summarize memory files."""
    memory_dir = Path.home() / ".openclaw" / "workspace" / "memory"
    if not memory_dir.exists():
        print("No memory directory found.")
        return
    files = list(memory_dir.glob("*.md"))
    if not files:
        print("No memory files found.")
        return
    total_lines = 0
    for f in files:
        try:
            lines = len(f.read_text().splitlines())
            total_lines += lines
        except Exception:
            pass
    print(f"Found {len(files)} memory files with approximately {total_lines} lines.")

def main():
    parser = argparse.ArgumentParser(description="OpenClaw Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # memory-summary
    parser_mem = subparsers.add_parser("memory-summary", help="Summarize memory files")
    parser_mem.set_defaults(func=memory_summary)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()