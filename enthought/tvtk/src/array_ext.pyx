"""
A Pyrex extension module.  Currently this extension module allows us
to:

  1. create an empty Numeric array very efficiently,

  2. Massage a 2D Numeric array into a form usable as a
     `vtkIdTypeArray`.  This is then used to set the cells of a
     `vtkCellArray` instance.

    

Eric Jones provided a first cut implementation of this using weave.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004, Enthought, Inc.
# License: BSD Style.

import Numeric

######################################################################
# External declarations.
######################################################################

# Expose various external interfaces needed subsequently.

cdef extern from "stdlib.h":
    ctypedef int size_t
    void *malloc(size_t size)

cdef extern from "Python.h":
    char* PyString_AsString(object a)
    void Py_XDECREF(object a)

cdef extern from "Numeric/arrayobject.h":
    ctypedef struct PyArray_Descr:
        int type_num, elsize
        char type

    ctypedef struct PyArrayObject:
        char *data
        int nd
        int *dimensions, *strides
        int flags        
       
    ctypedef class Numeric.ArrayType [object PyArrayObject]:
        cdef char *data
        cdef int nd
        cdef int *dimensions, *strides
        cdef object base
        cdef PyArray_Descr *descr
        cdef int flags

    PyArray_Descr* PyArray_DescrFromType(int)
    
    PyArrayObject* PyArray_FromDimsAndDataAndDescr(int, int *, PyArray_Descr *, char *)

    int PyArray_XDECREF(PyArrayObject *ap)

    cdef int OWN_DATA

    void import_array()


# This is very important -- if we don't call `import_array`,
# PyArray_DescFromType will segfault!
import_array()

######################################################################
# Internal C functions.
######################################################################
cdef c_empty_array(ArrayType dims, object typecode):
    # This is almost a direct translation of Eric's weave code.
    # zeros() is extremely slow at creating arrays.  c_empty_array
    # creates an unitialized Numeric array of numbers and is very
    # fast.
    
    if dims.nd <> 1:
        raise ValueError, "dimension array must be 1d"

    cdef char *real_type
    real_type = PyString_AsString(typecode)    
    
    # Create descriptor.
    cdef PyArray_Descr *descr
    descr = PyArray_DescrFromType(<int>real_type[0])
    if descr == NULL:
        raise ValueError, "Could not find descriptor from given typecode"

    # Calculate size of array.
    cdef int nd
    cdef int *d
    cdef int sd, i
    nd = dims.dimensions[0]
    d = <int*> dims.data
    sd = descr.elsize
    for i from 0 <= i < nd:
        if d[i] < 0:
            raise ValueError, "Negative dimensions are not allowed"
        # This may waste some space, but it seems to be
        # (unsuprisingly) unhealthy to allow strides that are longer
        # than sd.
        if d[i]:
            sd = sd*d[i]

    # Make sure we're alligned on ints.
    sd = sd + sizeof(int) - sd%sizeof(int); 
    
    # Allocate memory.
    cdef char* data
    data = <char *> malloc(sd)
    if data == NULL:
        raise MemoryError, "Can't allocate memory for array"

    # Create the array.
    cdef PyArrayObject *op
    op = PyArray_FromDimsAndDataAndDescr(nd, d, descr, data)
    
    # We own data.
    op.flags = op.flags | OWN_DATA

    cdef object o
    o = <object> op
    # This is needed for some reason.  Otherwise refcount is 3!
    Py_XDECREF(o)
    return o


cdef c_set_id_type_array(ArrayType id_array, ArrayType out_array):
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

def empty_array(dims, typecode='d'):
    """This function creates an unitialized Numeric array of numbers
    very quickly.  zeros() is extremely slow at creating arrays."""
    dims = Numeric.asarray(dims).astype(Numeric.Int)
    return c_empty_array(dims, typecode)


def set_id_type_array(id_array, out_array):
    """Given a 2D Int array (`id_array`), and a contiguous 1D Numeric
    array (`out_array`) having the correct size, this function sets
    the data from `id_array` into `out_array` so that it can be used
    in place of a `vtkIdTypeArray` in order to set the cells of a
    `vtkCellArray`.

    Note that if `shape = id_array.shape` then `size(out_array) ==
    shape[0]*(shape[1] + 1)` should be true.  If not you'll get an
    `AssertionError`.

    `id_array` need not be contiguous but `out_array` must be.
    """
    assert id_array.typecode() == 'l', \
           "id_array must have a typecode of 'l'."
    
    assert out_array.typecode() == 'l', \
           "out_array must have a typecode of 'l'."

    assert out_array.iscontiguous() == 1, \
           "out_array must be contiguous."
    
    shp = id_array.shape
    assert len(shp) == 2, "id_array must be a two dimensional array."

    sz = Numeric.size(out_array)
    e_sz = shp[0]*(shp[1]+1)
    assert sz == e_sz, \
           "out_array size is incorrect, expected: %s, given: %s"%(e_sz, sz)
       
    c_set_id_type_array(id_array, out_array)
