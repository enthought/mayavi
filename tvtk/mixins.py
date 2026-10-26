"""Hand-written behaviour for a few generated TVTK classes.

The generator (``special_gen.MIXINS``) puts each mixin here first among the
bases of the class it is named for, so its methods override any the class
inherits, and every subclass gets them too (``FloatArray`` the
``DataArrayMixin`` ones, for instance).
"""
# Author: Prabhu Ramachandran
# Copyright (c) Enthought, Inc.
# License: BSD Style.

from tvtk import array_handler
from tvtk import tvtk_base
from tvtk import vtk_module as vtk
from tvtk.tvtk_base import deref_vtk


def _wrap_vtk(obj):
    # deferred: tvtk_helper is generated, and imports the classes that
    # import this module
    from tvtk.tvtk_classes.tvtk_helper import wrap_vtk
    return wrap_vtk(obj)


def _check_key(key, n):
    """Return `key` as a non-negative index into a sequence of length `n`."""
    if not isinstance(key, int):
        raise TypeError("Only integers are valid keys.")
    if key < 0:
        key = n + key
    if key < 0 or key >= n:
        raise IndexError("Index %s out of range." % key)
    return key


def _short_repr(seq, n, first, last):
    """The whole of `seq` if it is short, otherwise its ends."""
    if n <= 10:
        return repr([x for x in seq])
    return '[%s, ..., %s], length = %s' % (first(), last(), n)


class Matrix4x4Mixin:
    """Pickles the matrix elements; converts to and from arrays."""

    def __getstate__(self):
        d = tvtk_base.TVTKBase.__getstate__(self)
        obj = self._vtk_obj
        d['elements'] = [obj.GetElement(i, j)
                         for i in range(4) for j in range(4)]
        return d

    def __setstate__(self, dict):
        e = dict.pop('elements')
        tvtk_base.TVTKBase.__setstate__(self, dict)
        self._in_set = 1
        obj = self._vtk_obj
        for i in range(4):
            for j in range(4):
                obj.SetElement(i, j, e[4*i+j])
        self._in_set = 0
        self.update_traits()

    def from_array(self, arr):
        '''Set the value of the matrix using the passed
        Numeric array or Python list.
        '''
        obj = self._vtk_obj
        for i in range(4):
            for j in range(4):
                obj.SetElement(i, j, arr[i, j])

    def to_array(self):
        '''Return the object as a numpy array.'''
        obj = self._vtk_obj
        e = [obj.GetElement(i, j) for i in range(4) for j in range(4)]
        arr = array_handler.numpy.array(e, dtype=float)
        return array_handler.reshape_view(arr, (4, 4))


class PropertyMixin:
    """Leaves ``color`` out of the pickle: it is made from the other colors.

    Used by ``Property`` and ``Light``.
    """

    def __getstate__(self):
        d = tvtk_base.TVTKBase.__getstate__(self)
        if 'color' in d:
            del d['color']
        return d

    def __setstate__(self, dict):
        tvtk_base.TVTKBase.__setstate__(self, dict)
        self.update_traits()


class CollectionMixin:
    """Makes a collection behave like a Python list of TVTK objects."""

    def __len__(self):
        return self._vtk_obj.GetNumberOfItems()

    def __iter__(self):
        self._vtk_obj.InitTraversal()
        return self

    def next(self):
        try:
            val = self._vtk_obj.GetNextItem()
        except AttributeError:
            val = self._vtk_obj.GetNextProp()
        if val is None:
            raise StopIteration
        return _wrap_vtk(val)

    __next__ = next

    def __getitem__(self, key):
        obj = self._vtk_obj
        if not isinstance(key, int):
            raise TypeError("Only integers are valid keys.")
        if key < 0:
            key = obj.GetNumberOfItems() + key
        ret = obj.GetItemAsObject(key)
        if ret is None:
            raise IndexError("Index %s out of range." % key)
        return _wrap_vtk(ret)

    def __setitem__(self, key, val):
        obj = self._vtk_obj
        key = _check_key(key, obj.GetNumberOfItems())
        obj.ReplaceItem(key, deref_vtk(val))

    def __delitem__(self, key):
        obj = self._vtk_obj
        key = _check_key(key, obj.GetNumberOfItems())
        obj.RemoveItem(key)

    def __repr__(self):
        return repr([repr(x) for x in self])

    def append(self, val):
        self._vtk_obj.AddItem(deref_vtk(val))

    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.AddItem(deref_vtk(i))


class DataArrayMixin:
    """Makes a data array behave like a Python list of tuples."""

    def __len__(self):
        return self._vtk_obj.GetNumberOfTuples()

    def __iter__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfTuples()
        nc = obj.GetNumberOfComponents()
        if nc in [1, 2, 3, 4, 9]:
            meth = getattr(obj, 'GetTuple%d' % nc)
            for i in range(n):
                yield meth(i)
        else:
            for i in range(n):
                yield tuple([obj.GetComponent(i, x) for x in range(nc)])

    def _check_key(self, key, n):
        return _check_key(key, n)

    def __getitem__(self, key):
        obj = self._vtk_obj
        key = self._check_key(key, obj.GetNumberOfTuples())
        nc = obj.GetNumberOfComponents()
        if nc in [1, 2, 3, 4, 9]:
            return getattr(obj, 'GetTuple%d' % nc)(key)
        else:
            return tuple([obj.GetComponent(key, x) for x in range(nc)])

    def __setitem__(self, key, val):
        obj = self._vtk_obj
        key = self._check_key(key, obj.GetNumberOfTuples())
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            obj.SetValue(key, val)
        elif nc in [2, 3, 4, 9]:
            getattr(obj, 'SetTuple%d' % nc)(key, *val)
        else:
            assert len(val) == nc, 'length of %s != %s.' % (val, nc)
            for x in range(nc):
                obj.SetComponent(key, x, val[x])

    def __repr__(self):
        n = self._vtk_obj.GetNumberOfTuples()
        return _short_repr(self, n, lambda: self[0], lambda: self[-1])

    def append(self, val):
        obj = self._vtk_obj
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            obj.InsertNextTuple1(val)
        elif nc in [2, 3, 4, 9]:
            meth = getattr(obj, 'InsertNextTuple%d' % nc)
            meth(*val)
        else:
            n = obj.GetNumberOfTuples()
            for x in range(nc):
                obj.InsertComponent(n, x, val[x])
        self.update_traits()

    def extend(self, arr):
        obj = self._vtk_obj
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            for i in arr:
                obj.InsertNextTuple1(i)
        elif nc in [2, 3, 4, 9]:
            meth = getattr(obj, 'InsertNextTuple%d' % nc)
            for i in arr:
                meth(*i)
        else:
            n = obj.GetNumberOfTuples()
            for i in range(len(arr)):
                for x in range(nc):
                    obj.InsertComponent(n+i, x, arr[i][x])
        self.update_traits()

    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtk(arr, self._vtk_obj)
        self.update_traits()

    def to_array(self):
        '''Return the object as a Numeric array.'''
        return array_handler.vtk2array(self._vtk_obj)


class PointsMixin:
    """Makes a points object behave like a Python list of points."""

    def __len__(self):
        return self._vtk_obj.GetNumberOfPoints()

    def __iter__(self):
        obj = self._vtk_obj
        for i in range(obj.GetNumberOfPoints()):
            yield obj.GetPoint(i)

    def _check_key(self, key, n):
        return _check_key(key, n)

    def __getitem__(self, key):
        obj = self._vtk_obj
        return obj.GetPoint(self._check_key(key, obj.GetNumberOfPoints()))

    def __setitem__(self, key, val):
        obj = self._vtk_obj
        obj.SetPoint(self._check_key(key, obj.GetNumberOfPoints()), val)

    def __repr__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfPoints()
        return _short_repr(self, n, lambda: obj.GetPoint(0),
                           lambda: obj.GetPoint(n-1))

    def append(self, val):
        self._vtk_obj.InsertNextPoint(val)
        self.update_traits()

    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.InsertNextPoint(i)
        self.update_traits()

    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkPoints(arr, self._vtk_obj)
        self.update_traits()

    def to_array(self):
        '''Return the object as a Numeric array.'''
        return array_handler.vtk2array(self._vtk_obj.GetData())


class IdListMixin:
    """Makes an id list behave like a Python list of ids."""

    def __len__(self):
        return self._vtk_obj.GetNumberOfIds()

    def __iter__(self):
        obj = self._vtk_obj
        for i in range(obj.GetNumberOfIds()):
            yield obj.GetId(i)

    def _check_key(self, key, n):
        return _check_key(key, n)

    def __getitem__(self, key):
        obj = self._vtk_obj
        return obj.GetId(self._check_key(key, obj.GetNumberOfIds()))

    def __setitem__(self, key, val):
        obj = self._vtk_obj
        obj.SetId(self._check_key(key, obj.GetNumberOfIds()), val)

    def __repr__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfIds()
        return _short_repr(self, n, lambda: obj.GetId(0),
                           lambda: obj.GetId(n-1))

    def append(self, val):
        self._vtk_obj.InsertNextId(val)
        self.update_traits()

    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.InsertNextId(i)
        self.update_traits()

    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkIdList(arr, self._vtk_obj)
        self.update_traits()


class CellArrayMixin:
    """Converts a cell array to and from the legacy flat id array."""

    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkCellArray(arr, self._vtk_obj)
        self.update_traits()

    def to_array(self):
        '''Return the object as a Numeric array.'''
        # GetData() was removed in VTK 9.7; the legacy-format API is the
        # forward fix, present since 9.0 (see tvtk/WORKAROUNDS.md)
        id_arr = vtk.vtkIdTypeArray()
        self._vtk_obj.ExportLegacyFormat(id_arr)
        return array_handler.vtk2array(id_arr)
