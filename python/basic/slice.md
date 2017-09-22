# Slice
- The `slice` object is used to slice a given sequence or any object supporting sequence protocol (implements `__getitem()__` and `__len__()` method)
- Slice object represents the indices specified by `range(start, stop, step)`

Syntax of slice:
```python
slice(stop)
slice(start, stop, step)
```