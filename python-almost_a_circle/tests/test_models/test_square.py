#!/usr/bin/python3
"""Unit tests for models.square.Square."""
import io
import unittest
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Tests for the Square __init__ method."""

    def test_is_rectangle_instance(self):
        """A Square is also an instance of Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_width_equals_height(self):
        """width and height are both set to size."""
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))

    def test_no_new_attributes(self):
        """Square does not define any new instance attributes."""
        s = Square(5, 1, 2, 99)
        self.assertEqual(
            set(s.__dict__.keys()),
            {"id", "_Rectangle__width", "_Rectangle__height",
             "_Rectangle__x", "_Rectangle__y"})

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_given_x_y(self):
        """x and y are assigned from the arguments."""
        s = Square(2, 2)
        self.assertEqual((s.x, s.y), (2, 0))

    def test_given_id(self):
        """A given id is used as-is."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.id, 12)

    def test_no_id_autoincrements(self):
        """A Square with no id gets an auto-incremented id."""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s2.id, s1.id + 1)

    def test_size_validation_reuses_rectangle(self):
        """Invalid size raises the same errors as Rectangle width."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_size_zero(self):
        """A size of 0 raises ValueError with width's message."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_not_int(self):
        """A non-integer x raises TypeError, inherited from Rectangle."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_not_int(self):
        """A non-integer y raises TypeError, inherited from Rectangle."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_x_negative(self):
        """A negative x raises ValueError, inherited from Rectangle."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_negative(self):
        """A negative y raises ValueError, inherited from Rectangle."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquare_size(unittest.TestCase):
    """Tests for the Square size property."""

    def test_getter_returns_width(self):
        """The size getter returns the current width."""
        self.assertEqual(Square(5).size, 5)

    def test_setter_updates_width_and_height(self):
        """The size setter updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_setter_invalid_type(self):
        """An invalid size type raises TypeError with width's message."""
        s = Square(5)
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_invalid_value(self):
        """An invalid size value raises ValueError with width's message."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquare_str(unittest.TestCase):
    """Tests for the Square.__str__ method."""

    def test_str_basic(self):
        """__str__ returns [Square] (<id>) <x>/<y> - <size>."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offsets(self):
        """__str__ reflects the x and y offsets."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")


class TestSquare_display(unittest.TestCase):
    """Tests for Square.display, inherited unchanged from Rectangle."""

    def test_display_basic(self):
        """display prints a size x size block of '#'."""
        f = io.StringIO()
        with redirect_stdout(f):
            Square(2, 2).display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        """display adds y leading blank lines."""
        f = io.StringIO()
        with redirect_stdout(f):
            Square(3, 1, 3).display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")


class TestSquare_area(unittest.TestCase):
    """Tests for Square.area, inherited unchanged from Rectangle."""

    def test_area(self):
        """area returns size squared."""
        self.assertEqual(Square(5).area(), 25)


class TestSquare_update_args(unittest.TestCase):
    """Tests for Square.update with no-keyword arguments."""

    def setUp(self):
        """Create a fresh Square before each test."""
        self.s = Square(5)

    def test_update_id_only(self):
        """A single argument updates only the id."""
        self.s.update(10)
        self.assertEqual(str(self.s), "[Square] (10) 0/0 - 5")

    def test_update_id_size(self):
        """Two arguments update id and size."""
        self.s.update(1, 2)
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 2")

    def test_update_id_size_x(self):
        """Three arguments update id, size and x."""
        self.s.update(1, 2, 3)
        self.assertEqual(str(self.s), "[Square] (1) 3/0 - 2")

    def test_update_all_args(self):
        """Four arguments update id, size, x and y."""
        self.s.update(1, 2, 3, 4)
        self.assertEqual(str(self.s), "[Square] (1) 3/4 - 2")


class TestSquare_update_kwargs(unittest.TestCase):
    """Tests for Square.update with keyworded arguments."""

    def setUp(self):
        """Create a fresh Square with a fixed id before each test."""
        self.s = Square(5, id=1)

    def test_single_kwarg(self):
        """A single kwarg updates only that attribute."""
        self.s.update(x=12)
        self.assertEqual(str(self.s), "[Square] (1) 12/0 - 5")

    def test_multiple_kwargs(self):
        """Multiple kwargs update all named attributes."""
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s), "[Square] (89) 0/1 - 7")

    def test_kwargs_skipped_if_args_present(self):
        """kwargs are ignored whenever args is non-empty."""
        self.s.update(1, 2, size=99)
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 2")


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests for the Square.to_dictionary method."""

    def test_keys_and_values(self):
        """to_dictionary returns exactly id, size, x and y."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(
            s.to_dictionary(), {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_no_width_height_keys(self):
        """to_dictionary does not expose width or height keys."""
        d = Square(10, 2, 1).to_dictionary()
        self.assertNotIn("width", d)
        self.assertNotIn("height", d)

    def test_update_from_dictionary(self):
        """update(**to_dictionary()) reproduces the same attributes."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
