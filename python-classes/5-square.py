#!/usr/bin/python3
"""Module that defines a Square class able to print itself."""


class Square:
    """Represents a square that can be printed with the # character."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Return the length of a side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of a side of the square.

        Args:
            value: The new length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using the # character.

        An empty line is printed when the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
