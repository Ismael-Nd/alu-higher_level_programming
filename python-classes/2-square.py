#!/usr/bin/python3
"""Module that defines a Square class validating its size."""


class Square:
    """Represents a square whose size is validated at instantiation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
