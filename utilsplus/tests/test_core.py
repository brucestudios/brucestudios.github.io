import unittest
from utilsplus.core import to_snake_case, to_camel_case, read_lines

class TestUtilsPlus(unittest.TestCase):
    
    def test_to_snake_case(self):
        self.assertEqual(to_snake_case("Hello World"), "hello_world")
        self.assertEqual(to_snake_case("helloWorld"), "hello_world")
        self.assertEqual(to_snake_case("Hello-World"), "hello_world")
        self.assertEqual(to_snake_case("hello world"), "hello_world")
    
    def test_to_camel_case(self):
        self.assertEqual(to_camel_case("hello world"), "helloWorld")
        self.assertEqual(to_camel_case("Hello World"), "helloWorld")
        self.assertEqual(to_camel_case("hello-world"), "helloWorld")
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")
    
    def test_read_lines(self):
        # Create a temporary file for testing
        with open("test.txt", "w") as f:
            f.write("line1\\nline2\\nline3")
        lines = read_lines("test.txt")
        self.assertEqual(lines, ["line1", "line2", "line3"])
        # Clean up
        import os
        os.remove("test.txt")

if __name__ == '__main__':
    unittest.main()