#!/usr/bin/env python3
"""
renamer.py - A simple command-line utility for batch renaming files.

Features:
  - Replace text in filenames
  - Add prefix or suffix
  - Change case (upper, lower, title)
  - Sequential numbering

Usage:
  python renamer.py [options] <pattern> <replacement>
  python renamer.py [options] --prefix <text>
  python renamer.py [options] --suffix <text>
  python renamer.py [options] --case <upper|lower|title>
  python renamer.py [options] --number <start> [--step <step>] [--width <width>]

Options:
  -d, --directory <dir>   Directory to process (default: current directory)
  -r, --recursive         Process directories recursively
  -n, --dry-run           Show what would be done without renaming
  -v, --verbose           Verbose output
  -h, --help              Show this help message

Examples:
  # Replace "IMG_" with "photo_" in all .jpg files in current directory
  python renamer.py "IMG_" "photo_" *.jpg

  # Add prefix "backup_" to all files in directory
  python renamer.py --prefix "backup_" *

  # Change all filenames to lowercase
  python renamer.py --case lower *

  # Number files sequentially starting at 100 with step 5 and width 3
  python renamer.py --number 100 --step 5 --width 3 *

Note: The pattern and replacement are applied as string replace.
      For more complex patterns, consider using regular expressions (future enhancement).
"""
import os
import sys
import argparse
import fnmatch
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Batch rename files with various options.")
    parser.add_argument('pattern', nargs='?', help='Text to replace in filenames')
    parser.add_argument('replacement', nargs='?', help='Replacement text')
    parser.add_argument('-d', '--directory', default='.', help='Directory to process (default: current)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Process directories recursively')
    parser.add_argument('-n', '--dry-run', action='store_true', help='Show what would be done without renaming')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prefix', help='Add prefix to filenames')
    group.add_argument('--suffix', help='Add suffix to filenames')
    group.add_argument('--case', choices=['upper', 'lower', 'title'], help='Change case')
    group.add_argument('--number', type=int, help='Start number for sequential naming')
    parser.add_argument('--step', type=int, default=1, help='Step for sequential numbering (default: 1)')
    parser.add_argument('--width', type=int, help='Width for zero-padding in sequential numbering')

    args = parser.parse_args()

    # Validate arguments
    if not any([args.pattern, args.prefix, args.suffix, args.case, args.number]):
        parser.error("Please specify an action: pattern/replacement, --prefix, --suffix, --case, or --number")

    if args.pattern is not None and args.replacement is None:
        parser.error("When providing pattern, replacement is required")

    # Determine files to process
    if args.recursive:
        file_iter = Path(args.directory).rglob('*')
    else:
        file_iter = Path(args.directory).iterdir()

    files = [f for f in file_iter if f.is_file()]

    if not files:
        print("No files found to process.")
        return

    # Process each file
    for idx, filepath in enumerate(files):
        # For sequential numbering, we need to sort the files for consistent ordering
        if args.number is not None:
            # We'll sort by name for now; could be made configurable
            pass  # We'll handle sorting after collecting all files

    # If we are doing sequential numbering, we need to sort the files
    if args.number is not None:
        files.sort(key=lambda x: x.name)  # Sort by filename

    for idx, filepath in enumerate(files):
        dirname = filepath.parent
        basename = filepath.name
        name, ext = os.path.splitext(basename)
        new_name = name

        # Apply the requested operation
        if args.pattern is not None:
            new_name = name.replace(args.pattern, args.replacement)
        elif args.prefix:
            new_name = args.prefix + name
        elif args.suffix:
            new_name = name + args.suffix
        elif args.case:
            if args.case == 'upper':
                new_name = name.upper()
            elif args.case == 'lower':
                new_name = name.lower()
            elif args.case == 'title':
                new_name = name.title()
        elif args.number is not None:
            number = args.number + idx * args.step
            if args.width is not None:
                number_str = str(number).zfill(args.width)
            else:
                number_str = str(number)
            new_name = number_str

        new_name += ext
        new_path = dirname / new_name

        # Skip if the name hasn't changed
        if new_path == filepath:
            if args.verbose:
                print(f"Skipping '{filepath}' (no change)")
            continue

        # Check if target already exists
        if new_path.exists():
            print(f"Error: '{new_path}' already exists. Skipping '{filepath}'.")
            continue

        if args.dry_run:
            print(f"[DRY RUN] Renaming '{filepath}' -> '{new_path}'")
        else:
            try:
                filepath.rename(new_path)
                if args.verbose:
                    print(f"Renamed '{filepath}' -> '{new_path}'")
            except Exception as e:
                print(f"Error renaming '{filepath}': {e}")

    if args.dry_run:
        print("Dry run completed. No files were actually renamed.")
    else:
        print("Renaming completed.")


if __name__ == '__main__':
    main()