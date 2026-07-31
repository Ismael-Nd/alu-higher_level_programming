#!/usr/bin/python3
"""Defines a square shape."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description as [Square] width/height."""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
