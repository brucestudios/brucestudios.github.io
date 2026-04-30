def factorial(n):
    """Return the factorial of n, an exact integer >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
