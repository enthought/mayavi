"""
A Pyrex extension module for new scipy_core.  Currently this extension
module allows us to massage a 2D scipy array into a form usable as a
`vtkIdTypeArray`.  This is then used to set the cells of a
`vtkCellArray` instance.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

import numpy
Int = 'l'

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

    void import_array()

import_array()

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
    stride0 = id_array.strides[0]/sizeof(int)
    stride1 = id_array.strides[1]/sizeof(int)

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

def empty_array(dims, dtype=numpy.float64):
    """A simple wrapper function along the lines of what is done for
    older Numeric versions that returns an uninitialized numarray
    array."""
    return numpy.empty(dims, dtype)


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
    assert id_array.dtype.char == Int, \
           "id_array must have a dtype.char of Int."
    
    assert out_array.dtype.char == Int, \
           "out_array must have a dtype.char of Int."

    assert out_array.flags.contiguous == 1, \
           "out_array must be contiguous."
    
    shp = id_array.shape
    assert len(shp) == 2, "id_array must be a two dimensional array."

    sz = numpy.size(out_array)
    e_sz = shp[0]*(shp[1]+1)
    assert sz == e_sz, \
           "out_array size is incorrect, expected: %s, given: %s"%(e_sz, sz)
       
    c_set_id_type_array(id_array, out_array)
