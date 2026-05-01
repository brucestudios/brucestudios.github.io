"""
Test suite for handy-python utilities
"""

import os
import tempfile
import json
import csv
from pathlib import Path
import pytest
from utils import *


def test_ensure_dir():
    """Test directory creation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir) / "test_subdir"
        result = ensure_dir(test_dir)
        assert result == test_dir
        assert test_dir.exists()
        assert test_dir.is_dir()


def test_backup_file():
    """Test file backup functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.txt"
        test_file.write_text("Hello, World!")
        
        backup_path = backup_file(test_file)
        assert backup_path.exists()
        assert backup_path.name.startswith("test_")
        assert backup_path.suffix == ".txt"
        assert backup_path.read_text() == "Hello, World!"
        
        # Test with custom backup directory
        backup_dir = Path(tmpdir) / "backups"
        backup_path2 = backup_file(test_file, backup_dir)
        assert backup_path2.parent == backup_dir
        assert backup_path2.exists()


def test_get_file_hash():
    """Test file hash calculation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.txt"
        test_content = "Hello, World!"
        test_file.write_text(test_content)
        
        # Test SHA256
        hash_sha256 = get_file_hash(test_file, "sha256")
        expected_sha256 = hashlib.sha256(test_content.encode()).hexdigest()
        assert hash_sha256 == expected_sha256
        
        # Test MD5
        hash_md5 = get_file_hash(test_file, "md5")
        expected_md5 = hashlib.md5(test_content.encode()).hexdigest()
        assert hash_md5 == expected_md5


def test_read_write_json():
    """Test JSON read/write functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.json"
        test_data = {"name": "John", "age": 30, "city": "New York"}
        
        # Write JSON
        write_json(test_data, test_file)
        assert test_file.exists()
        
        # Read JSON
        loaded_data = read_json(test_file)
        assert loaded_data == test_data


def test_read_write_csv():
    """Test CSV read/write functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.csv"
        test_data = [
            {"name": "John", "age": "30", "city": "New York"},
            {"name": "Jane", "age": "25", "city": "Los Angeles"}
        ]
        
        # Write CSV
        write_csv(test_data, test_file)
        assert test_file.exists()
        
        # Read CSV
        loaded_data = read_csv(test_file)
        assert len(loaded_data) == 2
        assert loaded_data[0]["name"] == "John"
        assert loaded_data[1]["city"] == "Los Angeles"


def test_flatten_unflatten_dict():
    """Test dictionary flattening/unflattening"""
    # Test flattening
    nested = {"a": {"b": {"c": 1, "d": 2}}, "e": 3}
    flat = flatten_dict(nested)
    expected = {"a.b.c": 1, "a.b.d": 2, "e": 3}
    assert flat == expected
    
    # Test unflattening
    flat = {"a.b.c": 1, "a.b.d": 2, "e": 3}
    nested = unflatten_dict(flat)
    expected = {"a": {"b": {"c": 1, "d": 2}}, "e": 3}
    assert nested == expected


def test_safe_get():
    """Test safe dictionary access"""
    data = {"user": {"profile": {"name": "John", "age": 30}}}
    
    # Test existing path
    assert safe_get(data, "user.profile.name") == "John"
    assert safe_get(data, "user.profile.age") == 30
    
    # Test non-existing path with default
    assert safe_get(data, "user.profile.address", "Unknown") == "Unknown"
    assert safe_get(data, "user.nonexistent", None) is None
    
    # Test with custom separator
    data_custom = {"user-profile": {"name": "John"}}
    assert safe_get(data_custom, "user-profile-name", sep="-") == "John"


def test_merge_dicts():
    """Test dictionary merging"""
    dict1 = {"a": 1, "b": {"x": 10}}
    dict2 = {"b": {"y": 20}, "c": 3}
    
    # Test shallow merge
    shallow = merge_dicts(dict1, dict2)
    assert shallow == {"a": 1, "b": {"y": 20}, "c": 3}  # b is overwritten
    
    # Test deep merge
    deep = merge_dicts(dict1, dict2, deep=True)
    assert deep == {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}


def test_chunk_list():
    """Test list chunking"""
    # Test normal chunking
    items = list(range(10))
    chunks = chunk_list(items, 3)
    assert chunks == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    # Test exact division
    items = list(range(9))
    chunks = chunk_list(items, 3)
    assert chunks == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    # Test chunk size larger than list
    items = [1, 2, 3]
    chunks = chunk_list(items, 5)
    assert chunks == [[1, 2, 3]]
    
    # Test invalid chunk size
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], 0)
    
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], -1)


if __name__ == "__main__":
    pytest.main([__file__])