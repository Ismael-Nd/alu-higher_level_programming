#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square defined by the length of its side."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The length of a side of the square.
        """
        self.__size = size
