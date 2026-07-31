#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, that adds two
numbers together after casting any float arguments to integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to integers first.

    Args:
        a: the first value, must be an int or a float.
        b: the second value, must be an int or a float, defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a is not an int or a float.
        TypeError: If b is not an int or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
