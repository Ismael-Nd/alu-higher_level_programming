# python-inheritance

This project covers Python inheritance: object introspection, class
checks (`is_same_class`, `is_kind_of_class`, `inherits_from`), and
building a small class hierarchy of geometric shapes
(`BaseGeometry` -> `Rectangle` -> `Square`).

## Tasks

| File | Description |
| --- | --- |
| 0-lookup.py | Returns the list of available attributes and methods of an object |
| 1-my_list.py | `MyList`, a list subclass that can print itself sorted |
| 2-is_same_class.py | Checks if an object is exactly an instance of a class |
| 3-is_kind_of_class.py | Checks if an object is an instance of a class or subclass |
| 4-inherits_from.py | Checks if an object's class is a strict subclass of another |
| 5-base_geometry.py | Empty `BaseGeometry` class |
| 6-base_geometry.py | Adds an `area()` method that raises an exception |
| 7-base_geometry.py | Adds an `integer_validator()` method |
| 8-rectangle.py | `Rectangle` class with private width/height, validated |
| 9-rectangle.py | Adds `area()` and `__str__()` to `Rectangle` |
| 10-square.py | `Square` class based on `Rectangle` |
| 11-square.py | Adds a `__str__()` override to `Square` |

## Tests

Doctest files live in `tests/` and run with:

```
python3 -m doctest ./tests/*
```
