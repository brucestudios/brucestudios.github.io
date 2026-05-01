import pytest
from python_utils import strings

def test_capitalize_words():
    assert strings.capitalize_words("hello world") == "Hello World"
    assert strings.capitalize_words("PYTHON") == "Python"
    assert strings.capitalize_words("") == ""
    assert strings.capitalize_words("single") == "Single"

def test_snake_to_camel():
    assert strings.snake_to_camel("hello_world") == "helloWorld"
    assert strings.snake_to_camel("hello") == "hello"
    assert strings.snake_to_camel("") == ""
    assert strings.snake_to_camel("hello_world_test") == "helloWorldTest"

def test_camel_to_snake():
    assert strings.camel_to_snake("helloWorld") == "hello_world"
    assert strings.camel_to_snake("hello") == "hello"
    assert strings.camel_to_snake("") == ""
    assert strings.camel_to_snake("helloWorldTest") == "hello_world_test"

def test_truncate():
    assert strings.truncate("Hello world", 8) == "Hello..."
    assert strings.truncate("Hi", 10) == "Hi"
    assert strings.truncate("Hello world", 5, "") == "Hello"
    assert strings.truncate("", 5) == ""

def test_is_palindrome():
    assert strings.is_palindrome("A man, a plan, a canal: Panama") == True
    assert strings.is_palindrome("racecar") == True
    assert strings.is_palindrome("hello") == False
    assert strings.is_palindrome("") == True