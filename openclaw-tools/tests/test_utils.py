import unittest
from openclawtools.utils import hello_world, add_numbers, is_even

class TestUtils(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World! Welcome to OpenClaw Tools.")
        self.assertEqual(hello_world("Alice"), "Hello, Alice! Welcome to OpenClaw Tools.")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()