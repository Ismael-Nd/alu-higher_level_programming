#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max of an ascending list is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list is found correctly."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max of a descending list is the first element."""
        self.assertEqual(max_integer([9, 5, 3, 1]), 9)

    def test_negative_numbers(self):
        """Max works correctly with negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10]), -1)

    def test_mixed_numbers(self):
        """Max works correctly with a mix of positive and negative."""
        self.assertEqual(max_integer([-5, 4, 0, -10, 9]), 9)

    def test_single_element(self):
        """Max of a single element list is that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Max of an empty list is None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Max with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_duplicate_max(self):
        """Max works correctly when the max value repeats."""
        self.assertEqual(max_integer([4, 4, 2, 4]), 4)

    def test_floats(self):
        """Max works correctly with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
