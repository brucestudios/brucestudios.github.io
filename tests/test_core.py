import pytest
from pwdgen.core import generate_password

def test_generate_password_default():
    pwd = generate_password()
    assert len(pwd) == 16
    # Should contain at least one of each type if all are used
    assert any(c.isupper() for c in pwd)
    assert any(c.islower() for c in pwd)
    assert any(c.isdigit() for c in pwd)
    assert any(not c.isalnum() for c in pwd)

def test_generate_password_length():
    pwd = generate_password(length=10)
    assert len(pwd) == 10

def test_generate_password_no_symbols():
    pwd = generate_password(length=10, use_symbols=False)
    assert all(c.isalnum() for c in pwd)

def test_generate_password_no_digits():
    pwd = generate_password(length=10, use_digits=False)
    assert not any(c.isdigit() for c in pwd)

def test_generate_password_no_lower():
    pwd = generate_password(length=10, use_lower=False)
    assert not any(c.islower() for c in pwd)

def test_generate_password_no_upper():
    pwd = generate_password(length=10, use_upper=False)
    assert not any(c.isupper() for c in pwd)

def test_generate_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=3)

def test_generate_password_no_charset():
    with pytest.raises(ValueError):
        generate_password(length=10, use_upper=False, use_lower=False, use_digits=False, use_symbols=False)