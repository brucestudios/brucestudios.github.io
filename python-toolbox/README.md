# Python Toolbox

A small collection of Python utilities for common tasks.

## Features

- **File utilities**: safe file operations (copy, move, delete with confirmation).
- **Text utilities**: slugify, truncate, capitalize, etc.
- **Data utilities**: simple CSV and JSON helpers.

## Installation

```bash
pip install python-toolbox
```

## Usage

### File utilities

```python
from python_toolbox.file_utils import copy_file, move_file, safe_delete

copy_file('src.txt', 'dst.txt')
move_file('old.txt', 'new/old.txt')
safe_delete('temp.txt')
```

### Text utilities

```python
from python_toolbox.text_utils import slugify, truncate

slug = slugify('Hello World!')
short = truncate('This is a very long sentence that needs shortening.', 20)
```

### Data utilities

```python
from python_toolbox.data_utils import read_csv, write_json

data = read_csv('data.csv')
write_json(data, 'data.json')
```

## License

MIT
