#!/usr/bin/python3
"""Defines a base class for geometric shapes."""


class BaseGeometry:
    """Represents the base of all geometric shapes."""

    def area(self):
        """Raise an exception since area computation is not implemented."""
        raise Exception("area() is not implemented")
