from pyutils.string_utils import slugify, is_valid_email, truncate, camel_to_snake, snake_to_camel, pluralize

def test_slugify():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  Multiple   Spaces  ") == "multiple-spaces"
    assert slugify("---") == ""
    assert slugify("Café", separator="_") == "café"

def test_is_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("invalid.email") == False
    assert is_valid_email("another.test@domain.co.uk") == True

def test_truncate():
    assert truncate("Hello, World!", 5) == "He..."
    assert truncate("Hi", 10) == "Hi"
    assert truncate("Hello, World!", 5, suffix="") == "Hello"

def test_camel_to_snake():
    assert camel_to_snake("camelCase") == "camel_case"
    assert camel_to_snake("CamelCase") == "camel_case"
    assert camel_to_snake("getHTTPResponse") == "get_http_response"

def test_snake_to_camel():
    assert snake_to_camel("snake_case") == "snakeCase"
    assert snake_to_camel("Snake_case") == "SnakeCase"
    assert snake_to_camel("get_http_response") == "getHttpResponse"

def test_pluralize():
    assert pluralize("cat", 1) == "cat"
    assert pluralize("cat", 2) == "cats"
    assert pluralize("cat") == "cats"  # default to plural
    assert pluralize("baby", 1) == "baby"
    assert pluralize("baby", 2) == "babies"
    assert pluralize("bus", 2) == "buses"