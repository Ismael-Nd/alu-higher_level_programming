#!/usr/bin/python3
"""Module that defines a Square class with a printing position."""


class Square:
    """Represents a square printed at a given offset position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: The length of a side of the square.
            position: The offset used when printing the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the offset used when printing the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the offset used when printing the square.

        Args:
            value: A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using the # character.

        The square is offset by its position, and an empty line is
        printed when the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
