# python-almost_a_circle

This project builds a small class hierarchy (`Base` -> `Rectangle` ->
`Square`) with private attributes and validated getters/setters,
`area`/`display`/`__str__`, flexible `update(*args, **kwargs)`,
dictionary/JSON (de)serialization, and file persistence. Everything
is covered by a `unittest` suite under `tests/`.

## Structure

| File | Description |
| --- | --- |
| models/base.py | `Base`: id management, JSON (de)serialization, file I/O |
| models/rectangle.py | `Rectangle(Base)`: validated width/height/x/y, area, display |
| models/square.py | `Square(Rectangle)`: a rectangle with equal width and height |
| tests/test_models/test_base.py | Unit tests for `Base` |
| tests/test_models/test_rectangle.py | Unit tests for `Rectangle` |
| tests/test_models/test_square.py | Unit tests for `Square` |

## Testing

```
python3 -m unittest discover tests
```

pycodestyle:

```
python3 -m pycodestyle models tests
```
