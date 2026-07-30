# Python - More Classes and Objects

This project builds a `Rectangle` class in Python step by step, introducing
core object-oriented concepts along the way: private attributes, properties
with validation, instance/static/class methods, class attributes, and the
special methods `__str__`, `__repr__`, and `__del__`.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code follows `pycodestyle` (version 2.7.*)
- No modules imported
- All files are executable and start with `#!/usr/bin/python3`

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | Empty `Rectangle` class. |
| `1-rectangle.py` | Private `width` and `height` with validated property setters. |
| `2-rectangle.py` | Adds `area()` and `perimeter()`. |
| `3-rectangle.py` | Adds `__str__` to print the rectangle with `#`. |
| `4-rectangle.py` | Adds `__repr__` so `eval(repr(r))` recreates an instance. |
| `5-rectangle.py` | Adds `__del__` printing `Bye rectangle...` on deletion. |
| `6-rectangle.py` | Adds `number_of_instances` class attribute. |
| `7-rectangle.py` | Adds `print_symbol` class attribute for the drawing character. |
| `8-rectangle.py` | Adds `bigger_or_equal` static method comparing areas. |
| `9-rectangle.py` | Adds `square` class method returning a square `Rectangle`. |

## Usage

```
$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```
