import unittest
from src.calculator import *

class TestCalculate(unittest.TestCase):
    def test_calculate_add(self):
        self.assertEqual(calculate(2, 3, "+"), 5)
    
    def test_calculate_subtract(self):
        self.assertEqual(subtract(5, 3, "-"), 2)

    def test_calculate_multiply(self):
        self.assertEqual(multiply(4, 3, "*"), 12)

    def test_calculate_divide(self):
        self.assertEqual(divide(10, 2, "/"), 5)
    
    def test_calculate_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0, "/")

    def test_calculate_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, 3, "%")
            