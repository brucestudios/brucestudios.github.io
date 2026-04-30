"""Tests for core module."""

import pytest
from textutils import core


def test_generate_password_length():
    """Test that generated password has correct length."""
    password = core.generate_password(length=10)
    assert len(password) == 10


def test_generate_password_character_sets():
    """Test that password contains required character sets."""
    # Test with all character sets
    password = core.generate_password(
        length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True
    )
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in core.string.punctuation for c in password)

    # Test with only lowercase
    password = core.generate_password(
        length=8, use_upper=False, use_lower=True, use_digits=False, use_special=False
    )
    assert all(c.islower() for c in password)
    assert not any(c.isupper() for c in password)
    assert not any(c.isdigit() for c in password)
    assert not any(c in core.string.punctuation for c in password)


def test_generate_password_min_length():
    """Test that password length validation works."""
    with pytest.raises(ValueError):
        core.generate_password(length=0)

    with pytest.raises(ValueError):
        core.generate_password(length=-1)


def test_generate_password_no_characters():
    """Test that error is raised when no character sets selected."""
    with pytest.raises(ValueError):
        core.generate_password(
            length=10, use_upper=False, use_lower=False, use_digits=False, use_special=False
        )


def test_generate_passphrase():
    """Test passphrase generation."""
    passphrase = core.generate_passphrase(num_words=3, separator="-")
    assert passphrase.count("-") == 2
    words = passphrase.split("-")
    assert len(words) == 3
    assert all(word.isalpha() for word in words)


def test_generate_passphrase_default_separator():
    """Test passphrase with default separator."""
    passphrase = core.generate_passphrase(num_words=2)
    assert "-" in passphrase
    words = passphrase.split("-")
    assert len(words) == 2


def test_generate_passphrase_empty_word_list():
    """Test passphrase with empty word list."""
    with pytest.raises(ValueError):
        core.generate_passphrase(num_words=2, word_list=[])


def test_generate_passphrase_invalid_num_words():
    """Test passphrase with invalid number of words."""
    with pytest.raises(ValueError):
        core.generate_passphrase(num_words=0)

    with pytest.raises(ValueError):
        core.generate_passphrase(num_words=-1)