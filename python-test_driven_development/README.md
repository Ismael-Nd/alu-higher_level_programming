# python-test_driven_development

This project introduces Test Driven Development (TDD) in Python: writing
doctests and unittests before/alongside implementation, validating input
types, and raising precise exceptions with clear messages.

## Tasks

| File | Description |
| --- | --- |
| 0-add_integer.py | Adds two integers (floats are cast to int first) |
| 2-matrix_divided.py | Divides all elements of a matrix by a divisor |
| 3-say_my_name.py | Prints `My name is <first name> <last name>` |
| 4-print_square.py | Prints a square of `#` characters |
| 5-text_indentation.py | Prints text with extra newlines after `.`, `?`, `:` |
| 6-max_integer.py | Returns the max integer in a list |
| tests/6-max_integer_test.py | Unittest suite for `max_integer` |

## Testing

Doctests:

```
python3 -m doctest ./tests/*.txt
```

Unittests:

```
python3 -m unittest tests.6-max_integer_test
```
