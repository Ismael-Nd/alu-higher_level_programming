#!/usr/bin/python3
"""Module that prints a full name."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first name> <last name>'.

    Args:
        first_name: the first name, must be a string.
        last_name: the last name, must be a string, defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
