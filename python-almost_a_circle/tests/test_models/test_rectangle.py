#!/usr/bin/python3
"""Unit tests for models.rectangle.Rectangle."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Tests for the Rectangle __init__ method."""

    def test_is_base_instance(self):
        """A Rectangle is also an instance of Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_no_id(self):
        """A Rectangle with no id gets an auto-incremented id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_given_id(self):
        """A given id is used as-is."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(3, 4)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_attributes_assigned(self):
        """width, height, x and y are assigned from the arguments."""
        r = Rectangle(3, 4, 1, 2)
        self.assertEqual(
            (r.width, r.height, r.x, r.y), (3, 4, 1, 2))

    def test_too_few_args(self):
        """Missing required arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Too many arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangle_validation(unittest.TestCase):
    """Tests for width/height/x/y validation on set and init."""

    def test_width_not_int_str(self):
        """A string width raises TypeError with the right message."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_not_int_float(self):
        """A float width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10.5, 2)

    def test_height_not_int(self):
        """A non-integer height raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_zero(self):
        """A width of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """A negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        """A height of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """A negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_not_int(self):
        """A non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 0)

    def test_x_negative(self):
        """A negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)

    def test_y_not_int(self):
        """A non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {})

    def test_y_negative(self):
        """A negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_is_valid(self):
        """x equal to 0 is valid."""
        self.assertEqual(Rectangle(10, 2, 0, 0).x, 0)

    def test_setter_width_negative(self):
        """Setting width to a negative value raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_setter_x_wrong_type(self):
        """Setting x to a non-integer raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_bool_rejected_as_width(self):
        """A bool is not accepted as a valid width (not an int type)."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)


class TestRectangle_area(unittest.TestCase):
    """Tests for the Rectangle.area method."""

    def test_area_basic(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_after_update(self):
        """area reflects attribute changes made after instantiation."""
        r = Rectangle(2, 10)
        r.width = 5
        self.assertEqual(r.area(), 50)

    def test_area_with_id(self):
        """area ignores id, x and y."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangle_display(unittest.TestCase):
    """Tests for the Rectangle.display method."""

    def test_display_basic(self):
        """display prints a width x height block of '#'."""
        f = io.StringIO()
        with redirect_stdout(f):
            Rectangle(4, 2).display()
        self.assertEqual(f.getvalue(), "####\n####\n")

    def test_display_with_x_y(self):
        """display offsets the block by x spaces and y blank lines."""
        f = io.StringIO()
        with redirect_stdout(f):
            Rectangle(2, 3, 2, 2).display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_x_only(self):
        """display with y=0 has no leading blank lines."""
        f = io.StringIO()
        with redirect_stdout(f):
            Rectangle(3, 2, 1, 0).display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")


class TestRectangle_str(unittest.TestCase):
    """Tests for the Rectangle.__str__ method."""

    def test_str_basic(self):
        """__str__ returns the documented format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_x_y(self):
        """__str__ reflects default x/y values of 0."""
        r = Rectangle(5, 5, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/5")

    def test_print_uses_str(self):
        """print() on a Rectangle uses its __str__ output."""
        f = io.StringIO()
        with redirect_stdout(f):
            print(Rectangle(5, 5, 1, 0, 1))
        self.assertEqual(f.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")


class TestRectangle_update_args(unittest.TestCase):
    """Tests for Rectangle.update with no-keyword arguments."""

    def setUp(self):
        """Create a fresh Rectangle before each test."""
        self.r = Rectangle(10, 10, 10, 10)

    def test_update_id_only(self):
        """A single argument updates only the id."""
        self.r.update(89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_id_width(self):
        """Two arguments update id and width."""
        self.r.update(89, 2)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_id_width_height(self):
        """Three arguments update id, width and height."""
        self.r.update(89, 2, 3)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_all_args(self):
        """Five arguments update id, width, height, x and y."""
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """Calling update with no arguments changes nothing."""
        before = str(self.r)
        self.r.update()
        self.assertEqual(str(self.r), before)


class TestRectangle_update_kwargs(unittest.TestCase):
    """Tests for Rectangle.update with keyworded arguments."""

    def setUp(self):
        """Create a fresh Rectangle with a fixed id before each test."""
        self.r = Rectangle(10, 10, 10, 10, id=1)

    def test_update_single_kwarg(self):
        """A single kwarg updates only that attribute."""
        self.r.update(height=1)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_multiple_kwargs(self):
        """Multiple kwargs update all of the named attributes."""
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_skipped_if_args_present(self):
        """kwargs are ignored whenever args is non-empty."""
        self.r.update(1, 2, height=99)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 2/10")

    def test_update_unknown_kwarg_ignored_attribute(self):
        """An unrecognized kwarg just sets a new attribute via setattr."""
        self.r.update(foo=1)
        self.assertEqual(self.r.foo, 1)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests for the Rectangle.to_dictionary method."""

    def test_keys_and_values(self):
        """to_dictionary returns the 5 expected key/value pairs."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(
            r.to_dictionary(),
            {"id": r.id, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_return_type(self):
        """to_dictionary returns a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_update_from_dictionary(self):
        """update(**to_dictionary()) reproduces the same attributes."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_changing_dictionary_does_not_affect_instance(self):
        """Mutating the returned dict doesn't affect the instance."""
        r = Rectangle(10, 2)
        d = r.to_dictionary()
        d["width"] = 999
        self.assertEqual(r.width, 10)


if __name__ == "__main__":
    unittest.main()
