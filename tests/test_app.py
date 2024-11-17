# tests/test_appy.py

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World from Mohamad Bailoun!"), "Hello, World from Mohamad Bailoun!"
        )


if __name__ == "__main__":
    unittest.main
