#!/usr/bin/python3
"""Defines a function that checks an object's class hierarchy."""


def is_kind_of_class(obj, a_class):
    """Check whether an object is an instance of a class or its subclass.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or of a subclass
            of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
