import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertIn("Tawheed", greet("Tawheed"))

    def test_farewell(self):
        self.assertIn("Tawheed", farewell("Tawheed"))

if __name__ == "__main__":
    unittest.main()