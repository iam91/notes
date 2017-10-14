# Basics
## Concepts
- Dimensions are called axes
- Number of axes is rank
- Numpy's array class is `ndarray`
 - `ndarray` is a table if elements, all of the same type
## Attributes
- `ndarray.ndim` = length of `ndarray.shape`
- `ndarray.size` = product of elements of `ndarray.shape`
- `ndarray.dtype`: describing the type of the elements in the array
## Elements Realignment
- `numpy.reshape(a, newshape, order='C')`
- `numpy.vstack(tup)`
 - stack arrays in sequence vertically (row wise).
 - `tup`: sequence of ndarrays -- Tuple containing arrays to be stacked. The arrays must have the same shape along all but the first axis.
- `numpy.hstack(tup)`
 - stack arrays in sequence horizontally (column wise).
 - `tup`: sequence of ndarrays -- All arrays must have the same shape along all but the second axis.