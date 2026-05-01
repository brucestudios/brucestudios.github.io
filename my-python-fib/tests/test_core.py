import pytest
from fibutils.core import fib, fib_iterative


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ],
)
def test_fib(n, expected):
    assert fib(n) == expected
    assert fib_iterative(n) == expected


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(ValueError):
        fib_iterative(-1)


def test_fib_large():
    # Fib(100) = 354224848179261915075
    expected = 354224848179261915075
    assert fib(100) == expected
    assert fib_iterative(100) == expected