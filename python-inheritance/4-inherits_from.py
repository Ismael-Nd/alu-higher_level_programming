#!/usr/bin/python3
"""Defines a function that checks strict class inheritance."""


def inherits_from(obj, a_class):
    """Check whether an object's class is a strict subclass of a class.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
            (not a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
