import unittest

import max_functions


class FindMaxTest(unittest.TestCase):
    def test_get_max(self):
        result = max_functions.get_max(1, 34)
        self.assertEqual(result, 34)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, max_functions.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = max_functions.get_max_with_one_argument(123)
        self.assertEqual(result, 123)

    def test_get_max_with_many_arguments(self):
        result = max_functions.get_max_with_many_arguments(1, 2, 3, 4)
        self.assertEqual(4, result)

    def test_get_max_with_one_or_more_arguments(self):
        first = 12454
        array = [1123, 1421, 12]
        result = max_functions.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(12454, result)

    def test_get_max_bounded(self):
        kwargs = {
            'low': 0,
            'high': 127
        }
        result = max_functions.get_max_bounded(-54, 45, 140, **kwargs)
        self.assertEqual(45, result)