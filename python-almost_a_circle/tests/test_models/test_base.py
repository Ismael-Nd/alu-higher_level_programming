#!/usr/bin/python3
"""Unit tests for models.base.Base."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Tests for the Base __init__ method."""

    def test_no_id(self):
        """A Base with no id auto-increments the id counter."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_public(self):
        """The id attribute is public."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_given_id(self):
        """A given id is used as-is, without touching the counter."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Passing id=None explicitly still auto-increments."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_counter_shared_across_subclasses(self):
        """Rectangle and Square share the same Base id counter."""
        b = Base()
        r = Rectangle(1, 1)
        s = Square(1)
        self.assertEqual(r.id, b.id + 1)
        self.assertEqual(s.id, r.id + 1)


class TestBase_to_json_string(unittest.TestCase):
    """Tests for the Base.to_json_string static method."""

    def test_none(self):
        """None returns the string "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list returns the string "[]"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """A list of dicts returns valid, round-trippable JSON."""
        dicts = [{"id": 1, "width": 10}, {"id": 2, "width": 4}]
        result = Base.to_json_string(dicts)
        self.assertEqual(json.loads(result), dicts)

    def test_return_type(self):
        """The return value is always a string."""
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)


class TestBase_from_json_string(unittest.TestCase):
    """Tests for the Base.from_json_string static method."""

    def test_none(self):
        """None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """A valid JSON string returns the matching list of dicts."""
        dicts = [{"id": 1, "width": 10}, {"id": 2, "width": 4}]
        json_string = json.dumps(dicts)
        self.assertEqual(Base.from_json_string(json_string), dicts)

    def test_round_trip(self):
        """to_json_string and from_json_string round-trip cleanly."""
        dicts = [{"id": 89, "size": 3}]
        json_string = Base.to_json_string(dicts)
        self.assertEqual(Base.from_json_string(json_string), dicts)


class TestBase_save_to_file(unittest.TestCase):
    """Tests for the Base.save_to_file class method."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_creates_file(self):
        """save_to_file creates a file named "<Class name>.json"."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_none_saves_empty_list(self):
        """Passing None saves an empty JSON list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_list_saves_empty_list(self):
        """Passing an empty list saves an empty JSON list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_none_saves_empty_list(self):
        """Square.save_to_file(None) saves an empty JSON list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_empty_list_saves_empty_list(self):
        """Square.save_to_file([]) saves an empty JSON list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_content_matches_dictionaries(self):
        """The saved JSON matches the instances' dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r1.to_dictionary(), r2.to_dictionary()])

    def test_overwrites_existing_file(self):
        """save_to_file overwrites a file that already exists."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2), Rectangle(3, 3)])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)

    def test_square_filename(self):
        """save_to_file for Square uses "Square.json"."""
        Square.save_to_file([Square(5)])
        self.assertTrue(os.path.exists("Square.json"))


class TestBase_create(unittest.TestCase):
    """Tests for the Base.create class method."""

    def test_create_rectangle(self):
        """create builds a distinct but attribute-equal Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_create_square(self):
        """create builds a distinct but attribute-equal Square."""
        s1 = Square(10, 2, 1)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_create_return_type(self):
        """create returns an instance of the calling class."""
        r = Rectangle.create(id=1, width=2, height=3, x=0, y=0)
        self.assertIsInstance(r, Rectangle)


class TestBase_load_from_file(unittest.TestCase):
    """Tests for the Base.load_from_file class method."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file_returns_empty_list(self):
        """Loading with no existing file returns an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_round_trip_rectangles(self):
        """Saved rectangles are reloaded with matching attributes."""
        originals = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(originals)
        loaded = Rectangle.load_from_file()
        self.assertEqual(
            [r.to_dictionary() for r in originals],
            [r.to_dictionary() for r in loaded])

    def test_round_trip_squares(self):
        """Saved squares are reloaded with matching attributes."""
        originals = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(originals)
        loaded = Square.load_from_file()
        self.assertEqual(
            [s.to_dictionary() for s in originals],
            [s.to_dictionary() for s in loaded])

    def test_loaded_instances_are_distinct_objects(self):
        """Loaded instances are new objects, not the originals."""
        originals = [Rectangle(10, 7, 2, 8)]
        Rectangle.save_to_file(originals)
        loaded = Rectangle.load_from_file()
        self.assertIsNot(originals[0], loaded[0])


if __name__ == "__main__":
    unittest.main()
