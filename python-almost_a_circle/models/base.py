#!/usr/bin/python3
"""Defines the Base class, the base of all other classes in this project."""
import json


class Base:
    """Manage the id attribute for all classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id: the identifier to assign. If None, a private class
                counter is incremented and used as the id instead.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries: a list of dictionaries.

        Returns:
            str: "[]" if list_dictionaries is None or empty, otherwise
                the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs: a list of instances that inherit from Base.

        The output file is named "<Class name>.json" and is
        overwritten if it already exists.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string: a string representing a list of dictionaries.

        Returns:
            list: an empty list if json_string is None or empty,
                otherwise the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with all attributes already set.

        Args:
            dictionary: key/value pairs of attributes to assign to
                the new instance via its update method.

        Returns:
            An instance of cls built from a dummy instance whose
            attributes have been overwritten with dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from "<Class name>.json".

        Returns:
            list: an empty list if the file doesn't exist, otherwise
                a list of cls instances built from the file content.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
        except IOError:
            return []
        return [cls.create(**d) for d in list_dicts]
