#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle, inheriting id management from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width: the width of the rectangle, an integer > 0.
            height: the height of the rectangle, an integer > 0.
            x: the horizontal offset, an integer >= 0, defaults to 0.
            y: the vertical offset, an integer >= 0, defaults to 0.
            id: the identifier, forwarded to Base.__init__.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the '#' character, honoring x/y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyworded arguments.

        Args:
            *args: values applied in order to id, width, height, x
                and y. If args is non-empty, kwargs is ignored.
            **kwargs: key/value pairs of attributes to update.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
