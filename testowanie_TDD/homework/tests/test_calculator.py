import unittest

from testowanie_TDD.homework import calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_add_method_with_two_values(self):
        result = self.calculator.add(4, 2)
        self.assertEqual(6, result)

    def test_add_method_with_multiple_values(self):
        result = self.calculator.add(4, 2, 3, 1)
        self.assertEqual(10, result)

    def test_multiply_method(self):
        result = self.calculator.multiply(5, 3)
        self.assertEqual(15, result)

    def test_sub_method(self):
        result = self.calculator.subtract(6, 4)
        self.assertEqual(2, result)

    def test_div_method(self):
        result = self.calculator.divide(5, 1)
        self.assertEqual(5, result)

    def test_div_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.divide, "five", "four")

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 5, 0)
