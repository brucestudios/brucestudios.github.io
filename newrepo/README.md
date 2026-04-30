# File Organizer

A simple Python script to organize files in a directory by their extensions.

## Features

- Organizes files into subdirectories based on file extension (e.g., `.txt` files go into a `txt` folder).
- Handles files without extensions (placed in a `no_extension` folder).
- Option to ignore hidden files and directories (default behavior).
- Dry-run mode to preview changes without making any modifications.
- Safe handling of naming conflicts by appending a counter to duplicate filenames.

## Installation

You can install the package using pip:

```bash
pip install file-organizer
```

Or install from source:

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
pip install .
```

## Usage

Run the script from the command line:

```bash
python -m file_organizer <directory> [options]
```

### Arguments

- `directory`: The directory to organize (required).

### Options

- `--dry-run`: Show what would be done without actually moving files.
- `--ignore-hidden`: Ignore hidden files and directories (default).
- `--include-hidden`: Include hidden files and directories.

### Examples

Organize the `Downloads` directory:

```bash
python -m file_organizer ~/Downloads
```

Preview changes without moving files:

```bash
python -m file_organizer ~/Downloads --dry-run
```

Include hidden files:

```bash
python -m file_organizer ~/Downloads --include-hidden
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.