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

You can treat a DataFrame semantically like a dict of like-indexed Series objects. Getting, setting, and deleting columns works with the same syntax as the analogous dict operations:
```python
df['one']
```
```
    one
a   1.0
b   2.0
c   3.0
d   NaN
```
```python
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
```
```
   one  two  three   flag
a  1.0  1.0    1.0  False
b  2.0  2.0    4.0  False
c  3.0  3.0    9.0   True
d  NaN  4.0    NaN  False
```
### inserting
```python
df['one']
```
```
    one
a   1.0
b   2.0
c   3.0
d   NaN
```
When inserting a scalar value, it will naturally be propagated to fill the column:
```python
df['foo'] = 'bar'
```
```
   one   flag  foo
a  1.0  False  bar
b  2.0  False  bar
c  3.0   True  bar
d  NaN  False  bar
```
When inserting a Series that does not have the same index as the DataFrame, it will be conformed to the DataFrame’s index:
```python
df['one_trunc'] = df['one'][:2]
```
```
   one   flag  foo  one_trunc
a  1.0  False  bar        1.0
b  2.0  False  bar        2.0
c  3.0   True  bar        NaN
d  NaN  False  bar        NaN
```
### indexing / selection
|Operation|Syntax|Result|
|---|---|---|
|Select column|df[col]|Series|
|Select row by label|df.loc[label]|Series|
|Select row by integer location|df.iloc[loc]|Series|
|Slice rows|df[5:10]|DataFrame|
|Select rows by boolean vector|df[bool_vec]|DataFrame|