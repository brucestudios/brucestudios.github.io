#!/usr/bin/env python3
"""
file_organizer - Organize files in a directory by their extensions.

Usage:
    python -m file_organizer <directory> [--dry-run] [--ignore-hidden]

Example:
    python -m file_organizer ~/Downloads
"""

import argparse
import os
import shutil
import sys
from pathlib import Path


def organize_directory(target_dir: Path, dry_run: bool = False, ignore_hidden: bool = True) -> None:
    """
    Organize files in target_dir into subdirectories based on file extension.

    Args:
        target_dir: The directory to organize.
        dry_run: If True, only show what would be done.
        ignore_hidden: If True, skip files and directories starting with '.'.
    """
    if not target_dir.is_dir():
        print(f"Error: {target_dir} is not a directory.", file=sys.stderr)
        sys.exit(1)

    # Iterate over items in the directory
    for item in target_dir.iterdir():
        # Skip hidden files/directories if requested
        if ignore_hidden and item.name.startswith('.'):
            continue

        # We only want to organize files, not directories
        if item.is_file():
            # Get file extension (lowercase, without the dot) or use 'no_extension'
            ext = item.suffix.lower()
            if ext:
                ext = ext[1:]  # remove leading dot
            else:
                ext = 'no_extension'

            # Destination directory
            dest_dir = target_dir / ext
            # Ensure destination directory exists
            if not dry_run:
                dest_dir.mkdir(exist_ok=True)

            # Destination file path
            dest_file = dest_dir / item.name

            # Handle naming conflicts
            counter = 1
            while dest_file.exists():
                stem = item.stem
                suffix = item.suffix
                dest_file = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

            # Perform move or just print
            if dry_run:
                print(f"[DRY-RUN] Would move: {item} -> {dest_file}")
            else:
                try:
                    shutil.move(str(item), str(dest_file))
                    print(f"Moved: {item} -> {dest_file}")
                except Exception as e:
                    print(f"Error moving {item}: {e}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by their extensions."
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="The directory to organize.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually moving files.",
    )
    parser.add_argument(
        "--ignore-hidden",
        action="store_true",
        default=True,
        help="Ignore hidden files and directories (default: True).",
    )
    parser.add_argument(
        "--include-hidden",
        dest="ignore_hidden",
        action="store_false",
        help="Include hidden files and directories.",
    )

    args = parser.parse_args()

    organize_directory(
        target_dir=args.directory.resolve(),
        dry_run=args.dry_run,
        ignore_hidden=args.ignore_hidden,
    )


if __name__ == "__main__":
    main()