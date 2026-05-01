import os
import tempfile
from pyutils.file_utils import safe_write, batch_rename, copy_file, move_file, delete_file

def test_safe_write():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "subdir", "test.txt")
        safe_write(file_path, "Hello, World!")
        assert os.path.exists(file_path)
        with open(file_path, 'r') as f:
            assert f.read() == "Hello, World!"

def test_batch_rename():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a few test files
        for i in range(3):
            with open(os.path.join(tmpdir, f"file{i}.txt"), 'w') as f:
                f.write(f"content {i}")
        # Rename files with prefix "new_"
        renamed = batch_rename(tmpdir, pattern="*.txt", prefix="new_")
        assert len(renamed) == 3
        for i, path in enumerate(renamed):
            assert os.path.basename(path) == f"new_file{i}.txt"

def test_copy_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "src.txt")
        dst = os.path.join(tmpdir, "dst.txt")
        with open(src, 'w') as f:
            f.write("Hello")
        copy_file(src, dst)
        assert os.path.exists(dst)
        with open(dst, 'r') as f:
            assert f.read() == "Hello"

def test_move_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "src.txt")
        dst = os.path.join(tmpdir, "dst.txt")
        with open(src, 'w') as f:
            f.write("Hello")
        move_file(src, dst)
        assert not os.path.exists(src)
        assert os.path.exists(dst)
        with open(dst, 'r') as f:
            assert f.read() == "Hello"

def test_delete_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test.txt")
        with open(file_path, 'w') as f:
            f.write("Hello")
        delete_file(file_path)
        assert not os.path.exists(file_path)