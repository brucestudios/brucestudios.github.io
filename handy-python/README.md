# Handy Python Utilities

A collection of useful utility functions for everyday Python tasks. This package provides helpers for common operations like file handling, data processing, dictionary manipulation, and more.

## Features

- **File Operations**: Ensure directories, backup files, calculate file hashes
- **Data Handling**: Read/write JSON and CSV files with ease
- **Dictionary Utilities**: Flatten/unflatten nested dictionaries, safe deep access, merging
- **List Processing**: Chunk lists into smaller pieces
- **Type Safety**: Full type hints for better IDE support
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

You can use this package by copying the `utils.py` file into your project, or install it as a package:

```bash
# If published to PyPI (future)
pip install handy-python

# Or just copy utils.py to your project
cp handy-python/utils.py your_project/
```

## Usage

### File Operations

```python
from utils import ensure_dir, backup_file, get_file_hash

# Ensure a directory exists
ensure_dir("data/logs")

# Backup a file
backup_path = backup_file("config.json")

# Get file hash
file_hash = get_file_hash("data.csv", "sha256")
```

### JSON Handling

```python
from utils import read_json, write_json

# Read JSON file
data = read_json("config.json")

# Write JSON file
write_json(data, "output.json", indent=4)
```

### CSV Handling

```python
from utils import read_csv, write_csv

# Read CSV (with header)
rows = read_csv("data.csv")

# Write CSV
write_csv(rows, "output.csv")
```

### Dictionary Utilities

```python
from utils import flatten_dict, unflatten_dict, safe_get, merge_dicts

# Flatten nested dictionary
nested = {"a": {"b": {"c": 1}}}
flat = flatten_dict(nested)  # {"a.b.c": 1}

# Unflatten dictionary
flat = {"a.b.c": 1}
nested = unflatten_dict(flat)  # {"a": {"b": {"c": 1}}}

# Safe nested access
data = {"user": {"profile": {"name": "John"}}}
name = safe_get(data, "user.profile.name", "Unknown")  # "John"

# Merge dictionaries
dict1 = {"a": 1, "b": {"x": 10}}
dict2 = {"b": {"y": 20}, "c": 3}
merged = merge_dicts(dict1, dict2, deep=True)
# {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}
```

### List Processing

```python
from utils import chunk_list

# Split list into chunks
items = list(range(10))
chunks = chunk_list(items, 3)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

## Functions Reference

### File Operations
- `ensure_dir(path)`: Create directory if it doesn't exist
- `backup_file(file_path, backup_dir=None)`: Create timestamped backup
- `get_file_hash(file_path, algorithm='sha256')`: Calculate file hash

### JSON Handling
- `read_json(file_path)`: Read and parse JSON file
- `write_json(data, file_path, indent=2)`: Write data to JSON file

### CSV Handling
- `read_csv(file_path, has_header=True)`: Read CSV to list of dicts
- `write_csv(data, file_path)`: Write list of dicts to CSV

### Dictionary Utilities
- `flatten_dict(nested_dict, separator='.')`: Flatten nested dict
- `unflatten_dict(flat_dict, separator='.')`: Unflatten dict
- `safe_get(nested_dict, key_path, default=None, separator='.')`: Safe nested access
- `merge_dicts(*dicts, deep=False)`: Merge dictionaries

### List Processing
- `chunk_list(lst, chunk_size)`: Split list into chunks

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

Run tests with pytest:

```bash
pip install pytest
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Your Name - [brucestudios](https://github.com/brucestudios)

Project Link: [https://github.com/brucestudios/handy-python](https://github.com/brucestudios/handy-python)