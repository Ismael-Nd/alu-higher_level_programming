#!/usr/bin/python3
"""Defines a function that checks an object's exact class."""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a class.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
