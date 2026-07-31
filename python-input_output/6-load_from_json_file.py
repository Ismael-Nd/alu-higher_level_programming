#!/usr/bin/python3
"""Module that provides a function to create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create and return an object from the JSON content of a file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
