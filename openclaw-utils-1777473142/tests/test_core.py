import unittest
import sys
sys.path.insert(0, "src")
from openclaw_utils.core import factorial

class TestFactorial(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

if __name__ == "__main__":
    unittest.main()
