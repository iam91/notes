# Data Structure
[pandas doc on data structure](http://pandas.pydata.org/pandas-docs/stable/dsintro.html)
## Series
### basic
- A 1d labeled array capable of holding any data type.
- Axis labels are collectively referred to as the **index**
```python
s = pandas.Series(data, index=index)
```
- `data`
 - a Python dict
 - an ndarray
 - a scalar values
 - another Series
 ## DataFrame
 ### basic
- A 2d labeled data structure with columns of potentially different types.
- Think of it like a `spreadsheet` `SQL table` `dict of Series objects`
```python
df = pandas.DataFrame(data, index=index, columns=columns)
```
- `data`
 - Dict of 1D ndarrays, lists, dicts, or Series
 - 2-D numpy.ndarray, list
 - Structured or record ndarray
 - A Series
 - Another DataFrame
 ### Column selection, addition, deletion
You can treat a DataFrame semantically like a dict of like-indexed Series objects. Getting, setting, and deleting columns works with the same syntax as the analogous dict operations