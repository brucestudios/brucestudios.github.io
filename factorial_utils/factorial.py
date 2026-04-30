def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Return the factorial of a non-negative integer n using recursion.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative-integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
    try:
        print(f"Factorial of {n} is {factorial(n)}")
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()