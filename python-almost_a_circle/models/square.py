#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, a rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size: the length of a side of the square, an integer > 0.
            x: the horizontal offset, an integer >= 0, defaults to 0.
            y: the vertical offset, an integer >= 0, defaults to 0.
            id: the identifier, forwarded to Rectangle.__init__.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: the length of a side of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyworded arguments.

        Args:
            *args: values applied in order to id, size, x and y. If
                args is non-empty, kwargs is ignored.
            **kwargs: key/value pairs of attributes to update.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
