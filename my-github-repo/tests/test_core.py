import pytest
from ispiriquote.core import get_random_quote, load_quotes

def test_load_quotes():
    quotes = load_quotes()
    assert isinstance(quotes, list)
    assert len(quotes) > 0
    for q in quotes:
        assert 'text' in q
        assert 'author' in q

def test_get_random_quote():
    quote = get_random_quote()
    # Check that the quote is a string and contains the expected format
    assert isinstance(quote, str)
    assert quote.startswith('"') and quote.endswith('”’)  # Note: we used a straight double quote in the text, but the author uses a straight dash?
    # Actually, we are using a straight double quote for the text and a straight dash for the author.
    # Let's just check that it contains a quote and a dash.
    assert '” –' in quote or '" –' in quote  # We used straight double quote in the text and a straight dash.