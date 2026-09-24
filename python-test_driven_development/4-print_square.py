#!/usr/bin/python3
"""Module that prints a square made of the '#' character."""


def print_square(size):
    """Print a square with the '#' character.

    Args:
        size: the length of a side of the square, must be an integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
