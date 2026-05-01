"""Fibonacci number calculation."""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed).
           Must be a non-negative integer.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iterative(n: int) -> int:
    """Return the nth Fibonacci number using an iterative approach.

    Args:
        n: The position in the Fibonacci sequence (0-indexed).
           Must be a non-negative integer.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b