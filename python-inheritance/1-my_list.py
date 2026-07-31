#!/usr/bin/python3
"""Defines a list subclass that can print itself sorted."""


class MyList(list):
    """Represents a list that can display its contents in sorted order."""

    def print_sorted(self):
        """Print the list contents in ascending sorted order."""
        print(sorted(self))
