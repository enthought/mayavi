#cython: language_level=3

"""
A Cython extension module for numpy.  Currently this extension module
allows us to massage a 2D scipy array into a form usable as a
`vtkIdTypeArray`.  This is then used to set the cells of a
`vtkCellArray` instance.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

import numpy
cimport numpy

######################################################################
# External declarations.
######################################################################

# Expose various external interfaces needed subsequently.
cdef extern from "numpy/arrayobject.h":
    ctypedef int intp

    struct PyArray_Descr:
        int type_num, elsize
        char type

    ctypedef extern class numpy.ndarray [object PyArrayObject]:
        cdef char *data
        cdef int nd
        cdef intp *dimensions
        cdef intp *strides
        cdef object base
        cdef PyArray_Descr *descr
        cdef int flags

numpy.import_array()

######################################################################
# Internal C functions.
######################################################################

cdef c_set_id_type_array(ndarray id_array, ndarray out_array):
    # This function sets the data of the passed 2D `id_array` into the
    # passed out_array such that out_array can be used as a
    # `vtkIdTypeArray`.
    #
    # `id_array` need not be contiguous.
    #
    # No type or size checking is done here.  All that is done in the
    # Python function upstream that calls this.

    cdef int cell_length, dim0
    cdef int *id_data
    cdef int *out_data
    cdef int stride0, stride1

    cell_length = id_array.dimensions[1];
    dim0 = id_array.dimensions[0]
    id_data = <int*> id_array.data
    out_data = <int*> out_array.data
    stride0 = id_array.strides[0]//sizeof(int)
    stride1 = id_array.strides[1]//sizeof(int)

    cdef int i, j, in_idx, out_idx
    for i from 0 <= i < dim0:
        in_idx = i*stride0
        out_idx = i*cell_length + i
        out_data[out_idx] = cell_length
        for j from 0 <= j < cell_length:
            out_data[out_idx + j + 1] = id_data[in_idx + j*stride1]

cdef c_set_id_type_array_long(ndarray id_array, ndarray out_array):
    # This function sets the data of the passed 2D `id_array` into the
    # passed out_array such that out_array can be used as a
    # `vtkIdTypeArray`.
    #
    # `id_array` need not be contiguous.
    #
    # No type or size checking is done here.  All that is done in the
    # Python function upstream that calls this.
    cdef Py_ssize_t cell_length, dim0
    cdef Py_ssize_t *id_data
    cdef Py_ssize_t *out_data
    cdef Py_ssize_t stride0, stride1

    cell_length = id_array.dimensions[1];
    dim0 = id_array.dimensions[0]
    id_data = <Py_ssize_t*> id_array.data
    out_data = <Py_ssize_t*> out_array.data
    stride0 = id_array.strides[0]//sizeof(Py_ssize_t)
    stride1 = id_array.strides[1]//sizeof(Py_ssize_t)

    cdef int i, j, in_idx, out_idx
    for i from 0 <= i < dim0:
        in_idx = i*stride0
        out_idx = i*cell_length + i
        out_data[out_idx] = cell_length
        for j from 0 <= j < cell_length:
            out_data[out_idx + j + 1] = id_data[in_idx + j*stride1]

######################################################################
# Exported (externally visible) functions.
######################################################################

def set_id_type_array(id_array, out_array):
    """Given a 2D Int array (`id_array`), and a contiguous 1D numarray
    array (`out_array`) having the correct size, this function sets
    the data from `id_array` into `out_array` so that it can be used
    in place of a `vtkIdTypeArray` in order to set the cells of a
    `vtkCellArray`.

    Note that if `shape = id_array.shape` then `size(out_array) ==
    shape[0]*(shape[1] + 1)` should be true.  If not you'll get an
    `AssertionError`.

    `id_array` need not be contiguous but `out_array` must be.
    """
    import vtk
    VTK_ID_TYPE_SIZE = vtk.vtkIdTypeArray().GetDataTypeSize()
    assert numpy.issubdtype(id_array.dtype, numpy.signedinteger) and \
       id_array.dtype.itemsize == VTK_ID_TYPE_SIZE

    assert out_array.flags.contiguous == 1, \
           "out_array must be contiguous."

    shp = id_array.shape
    assert len(shp) == 2, "id_array must be a two dimensional array."

    sz = numpy.size(out_array)
    e_sz = shp[0]*(shp[1]+1)
    assert sz == e_sz, \
           "out_array size is incorrect, expected: %s, given: %s"%(e_sz, sz)

    if VTK_ID_TYPE_SIZE == 4:
        c_set_id_type_array(id_array, out_array)
    elif VTK_ID_TYPE_SIZE == 8:
        c_set_id_type_array_long(id_array, out_array)
    else:
        raise ValueError('Unsupported VTK_ID_TYPE_SIZE=%d'\
                         %VTK_ID_TYPE_SIZE)
