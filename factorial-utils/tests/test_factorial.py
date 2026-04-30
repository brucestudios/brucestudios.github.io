import pytest
from factorial_utils.core import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_small():
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_factorial_large():
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

if __name__ == "__main__":
    pytest.main()