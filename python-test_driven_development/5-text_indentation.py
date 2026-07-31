#!/usr/bin/python3
"""Module that prints text with extra indentation after punctuation."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text: the string to print, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
