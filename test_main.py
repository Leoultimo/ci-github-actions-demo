import unittest
from main import main
from io import StringIO
import sys

class TestMain(unittest.TestCase):
    def test_main_with_string(self):
        """Test main function with a string argument"""
        captured_output = StringIO()
        sys.stdout = captured_output
        main("GitHub")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, GitHub CI with GitHub Actions!\n")

    def test_main_with_different_string(self):
        """Test main function with different string"""
        captured_output = StringIO()
        sys.stdout = captured_output
        main("Leo")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, Leo CI with GitHub Actions!\n")

    def test_main_with_empty_string(self):
        """Test main function with empty string"""
        captured_output = StringIO()
        sys.stdout = captured_output
        main("")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello,  CI with GitHub Actions!\n")


if __name__ == '__main__':
    unittest.main()