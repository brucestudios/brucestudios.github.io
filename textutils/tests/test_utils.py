"""Tests for utils module."""

import pytest
from textutils import utils


def test_count_words():
    """Test word counting."""
    assert utils.count_words("Hello world") == 2
    assert utils.count_words("  Hello   world  ") == 2
    assert utils.count_words("") == 0
    assert utils.count_words("single") == 1
    assert utils.count_words("one two three four") == 4


def test_count_lines():
    """Test line counting."""
    assert utils.count_lines("Hello\nworld") == 2
    assert utils.count_lines("Hello\nworld\n") == 2
    assert utils.count_lines("") == 1  # splitlines on empty string returns ['']
    assert utils.count_lines("no newline") == 1
    assert utils.count_lines("line1\nline2\nline3") == 3


def test_count_chars():
    """Test character counting."""
    assert utils.count_chars("Hello") == 5
    assert utils.count_chars("Hello world") == 11
    assert utils.count_chars("") == 0
    assert utils.count_chars(" ") == 1
    assert utils.count_chars("\n") == 1


def test_to_upper():
    """Test uppercase conversion."""
    assert utils.to_upper("hello") == "HELLO"
    assert utils.to_upper("Hello World") == "HELLO WORLD"
    assert utils.to_upper("123abc") == "123ABC"
    assert utils.to_upper("") == ""


def test_to_lower():
    """Test lowercase conversion."""
    assert utils.to_lower("HELLO") == "hello"
    assert utils.to_lower("Hello World") == "hello world"
    assert utils.to_lower("123ABC") == "123abc"
    assert utils.to_lower("") == ""


def test_to_title():
    """Test title case conversion."""
    assert utils.to_title("hello world") == "Hello World"
    assert utils.to_title("HELLO WORLD") == "Hello World"
    assert utils.to_title("123abc") == "123Abc"
    assert utils.to_title("") == ""


def test_is_palindrome():
    """Test palindrome detection."""
    assert utils.is_palindrome("racecar") == True
    assert utils.is_palindrome("Racecar") == True
    assert utils.is_palindrome("A man, a plan, a canal: Panama") == True
    assert utils.is_palindrome("hello") == False
    assert utils.is_palindrome("") == True  # Empty string is palindrome
    assert utils.is_palindrome("a") == True
    assert utils.is_palindrome("12321") == True
    assert utils.is_palindrome("12345") == False


def test_random_string():
    """Test random string generation."""
    # Test default parameters
    random_str = utils.random_string(length=10)
    assert len(random_str) == 10

    # Test with only lowercase
    random_str = utils.random_string(length=8, use_upper=False, use_digits=False, use_special=False)
    assert all(c.islower() for c in random_str)

    # Test with only uppercase
    random_str = utils.random_string(length=8, use_lower=False, use_digits=False, use_special=False)
    assert all(c.isupper() for c in random_str)

    # Test with only digits
    random_str = utils.random_string(length=8, use_lower=False, use_upper=False, use_special=False)
    assert all(c.isdigit() for c in random_str)

    # Test that length parameter works
    for length in [0, 1, 5, 20]:
        random_str = utils.random_string(length=length)
        assert len(random_str) == length

    # Test that no character sets raises error
    with pytest.raises(ValueError):
        utils.random_string(length=10, use_lower=False, use_upper=False, use_digits=False, use_special=False)