import csv
import json
from typing import Any, Dict, List

def read_csv(filepath: str, delimiter: str = ',') -> List[Dict[str, Any]]:
    """Read a CSV file and return a list of dictionaries."""
    with open(filepath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return [row for row in reader]

def write_json(data: Any, filepath: str, indent: int = 2) -> None:
    """Write data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)