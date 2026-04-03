# tests/test_app.py
import unittest
from app import calculate_sum  # अगर आप app.py में function define करोगे

class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculate_sum(10, 20), 30)
        self.assertEqual(calculate_sum(15, 25), 40)

if __name__ == "__main__":
    unittest.main()
