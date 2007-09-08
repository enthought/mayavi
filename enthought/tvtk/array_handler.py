"""
This module contains all the array handling code for TVTK.

The most important functions provided by this module involve the
conversion of Numeric arrays/Python lists to different VTK data arrays
and vice-versa.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2007,  Enthought, Inc.
# License: BSD Style.

import types
import sys

import vtk
from vtk.util import vtkConstants

# Enthought library imports.
from enthought.util import numerix

# Conditional imports.
which_numerix = numerix.which[0]
if which_numerix == 'numeric':
    from enthought.tvtk.array_ext import empty_array, set_id_type_array
elif which_numerix == 'numpy':
    from enthought.tvtk.array_ext_sp import empty_array, set_id_type_array
else:
    from enthought.tvtk.array_ext_na import empty_array, set_id_type_array

# Useful constants for ID_TYPE_ARRAYS.
VTK_ID_TYPE_SIZE = vtk.vtkIdTypeArray().GetDataTypeSize()
if VTK_ID_TYPE_SIZE == 4:
    ID_TYPE_CODE = 'i'
elif VTK_ID_TYPE_SIZE == 8:
    ID_TYPE_CODE = 'l'

######################################################################
# The array cache.
######################################################################

# The array object cache (`_array_cache`) caches all the converted
# Numeric arrays that are not copied.  This prevents the user from
# deleting or resizing the Numeric array after it has been sent down
# to VTK.

_dummy = None
# This makes the cache work even when the module is reloaded.
for name in ['array_handler', 'enthought.tvtk.array_handler']:
    if sys.modules.has_key(name):
        mod = sys.modules[name]
        if hasattr(mod, '_array_cache'):
            _dummy = mod._array_cache
        del mod
        break

if _dummy:
    _array_cache = _dummy
else:
    _array_cache = {}
del _dummy


def _remove_cached_array(key):
    """Internal function that removes an array from the cache.  Do not
    call this unless you know what you are doing."""
    global _array_cache
    try:
        del _array_cache[key]
    except KeyError:
        pass


######################################################################
# Array conversion functions.
######################################################################
def get_vtk_array_type(numeric_array_type):
    """Returns a VTK typecode given a Numeric array."""
    # This is a Mapping from Numeric array types to VTK array types.
    _arr_vtk = {numerix.Character:vtkConstants.VTK_UNSIGNED_CHAR,
                numerix.UInt8:vtkConstants.VTK_UNSIGNED_CHAR,
                numerix.UInt16:vtkConstants.VTK_UNSIGNED_SHORT,
                numerix.UInt32:vtkConstants.VTK_UNSIGNED_LONG,
                numerix.Int8:vtkConstants.VTK_CHAR,
                numerix.Int16:vtkConstants.VTK_SHORT,
                numerix.Int32:vtkConstants.VTK_INT,
                numerix.Int:vtkConstants.VTK_LONG,
                numerix.Float32:vtkConstants.VTK_FLOAT,
                numerix.Float64:vtkConstants.VTK_DOUBLE,
                numerix.Complex32:vtkConstants.VTK_FLOAT,
                numerix.Complex64:vtkConstants.VTK_DOUBLE}
    if which_numerix == 'numarray':
        for k, v in _arr_vtk.items():
            _arr_vtk[numerix.type2charmap[k]] = v
    return _arr_vtk[numeric_array_type]


def get_vtk_to_numeric_typemap():
    """Returns the VTK array type to Numeric array type mapping."""
    _vtk_arr = {vtkConstants.VTK_BIT:numerix.Int8,
                vtkConstants.VTK_CHAR:numerix.Int8,
                vtkConstants.VTK_UNSIGNED_CHAR:numerix.UInt8,
                vtkConstants.VTK_SHORT:numerix.Int16,
                vtkConstants.VTK_UNSIGNED_SHORT:numerix.UInt16,
                vtkConstants.VTK_INT:numerix.Int32,
                vtkConstants.VTK_UNSIGNED_INT:numerix.UInt32,
                vtkConstants.VTK_LONG:numerix.Int,
                vtkConstants.VTK_UNSIGNED_LONG:numerix.UInt32,
                vtkConstants.VTK_ID_TYPE:ID_TYPE_CODE,
                vtkConstants.VTK_FLOAT:numerix.Float32,
                vtkConstants.VTK_DOUBLE:numerix.Float64}
    return _vtk_arr


def get_numeric_array_type(vtk_array_type):
    """Returns a Numeric array typecode given a VTK array type."""
    return get_vtk_to_numeric_typemap()[vtk_array_type]


def get_sizeof_vtk_array(vtk_array_type):
    """Returns the size of a VTK array type."""
    _size_dict = {vtkConstants.VTK_BIT : 1,
                  vtkConstants.VTK_CHAR : 1,
                  vtkConstants.VTK_UNSIGNED_CHAR : 1,
                  vtkConstants.VTK_SHORT : 2,
                  vtkConstants.VTK_UNSIGNED_SHORT : 2,
                  vtkConstants.VTK_INT : 4,
                  vtkConstants.VTK_UNSIGNED_INT : 4,
                  vtkConstants.VTK_LONG : 4,
                  vtkConstants.VTK_UNSIGNED_LONG : 4,
                  vtkConstants.VTK_ID_TYPE : VTK_ID_TYPE_SIZE,
                  vtkConstants.VTK_FLOAT : 4,
                  vtkConstants.VTK_DOUBLE : 8 }
    return _size_dict[vtk_array_type]


def create_vtk_array(vtk_arr_type):
    """Internal function used to create a VTK data array from another
    VTK array given the VTK array type.
    """
    tmp = vtk.vtkDataArray.CreateDataArray(vtk_arr_type)
    # CreateDataArray sets the refcount to 3 and this causes a severe
    # memory leak.
    tmp.SetReferenceCount(2)
    return tmp


def array2vtk(num_array, vtk_array=None):
    """Converts a real Numeric Array (or a Python list) to a VTK array
    object.

    This function only works for real arrays.  Complex arrays are NOT
    handled.  It also works for multi-component arrays.  However, only
    1, and 2 dimensional arrays are supported.  This function is very
    efficient, so large arrays should not be a problem.

    Even in cases when no copy of the Numeric array data is performed,
    a reference to the array is cached.  The passed array can
    therefore be deleted safely in all circumstances.

    Parameters
    ----------

    - num_array : Numeric array or Python list/tuple

      The input array must be 1 or 2D.  A copy of the numeric array
      data passed is made in the following circumstances:

       1. A Python list/tuple was passed.
       2. A non-contiguous Numeric array was passed.
       3. A `vtkBitArray` instance was passed as the second argument.
       4. The types of the `vtk_array` and the `num_array` are not
          equivalent to each other.  For example if one is an integer
          array and the other a float.


    - vtk_array : `vtkDataArray` (default: `None`)

      If an optional `vtkDataArray` instance, is passed as an argument
      then a new array is not created and returned.  The passed array
      is itself returned.

    Warning
    -------

    This code is unlikely to work with the vtkIdTypeArray if you are
    using 64 bit ID's.  This is because 64 bit ids are 8 bytes long
    and it is not clear what Numeric array type one has to use in this
    case!  This code will also not work with complex arrays.

    """

    z = numerix.asarray(num_array)

    shape = z.shape
    assert len(shape) < 3, \
           "Only arrays of dimensionality 2 or lower are allowed!"
    assert numerix.typecode(z) not in [numerix.Complex32, numerix.Complex64], \
           "Complex Numeric arrays cannot be converted to vtk arrays."\
           "Use real() or imag() to get a component of the array before"\
           " passing it to vtk."

    # First create an array of the right type by using the typecode.
    # Bit arrays need special casing.
    bit_array = False
    if vtk_array is None:
        vtk_typecode = get_vtk_array_type(numerix.typecode(z))
        result_array = create_vtk_array(vtk_typecode)
    elif vtk_array.GetDataType() == vtkConstants.VTK_BIT:
        vtk_typecode = vtkConstants.VTK_CHAR
        result_array = create_vtk_array(vtkConstants.VTK_CHAR)
        bit_array = True
    else:
        vtk_typecode = vtk_array.GetDataType()
        result_array = vtk_array

    # Find the shape and set number of components.
    if len(shape) == 1:
        result_array.SetNumberOfComponents(1)
    else:
        result_array.SetNumberOfComponents(shape[1])

    result_array.SetNumberOfTuples(shape[0])

    # Ravel the array appropriately.
    if get_numeric_array_type(vtk_typecode) != numerix.typecode(z):
        z_flat = numerix.ravel(z).astype(get_numeric_array_type(vtk_typecode))
    else:
        z_flat = numerix.ravel(z)

    # Point the VTK array to the Numeric data.  The last argument (1)
    # tells the array not to deallocate.
    if which_numerix in ('numeric', 'numpy'):
        result_array.SetVoidArray(z_flat, len(z_flat), 1)
    else:
        result_array.SetVoidArray(z_flat._data, len(z_flat), 1)

    if bit_array:
        # Handle bit arrays -- they have to be copied.  Note that bit
        # arrays are used ONLY when the user has passed one as an
        # argument to this function.
        vtk_array.SetNumberOfTuples(result_array.GetNumberOfTuples())
        vtk_array.SetNumberOfComponents(result_array.GetNumberOfComponents())
        for i in range(result_array.GetNumberOfComponents()):
            vtk_array.CopyComponent(i, result_array, i)
        result_array = vtk_array
    else:
        # Save a reference to the flatted array in the array cache.
        # This prevents the user from deleting or resizing the array
        # and getting into serious trouble.  This is only done for
        # non-bit array cases where the data is not copied.
        global _array_cache
        key = result_array.__this__
        _array_cache[key] = z_flat
        # Setup a callback so this cached array reference is removed
        # when the VTK array is destroyed.  Passing the key to the
        # `lambda` function is necessary because the callback will not
        # receive the object (it will receive `None`) and thus there
        # is no way to know which array reference one has to remove.
        result_array.AddObserver('DeleteEvent', lambda o, e, key=key: \
                                 _remove_cached_array(key))

    return result_array


def vtk2array(vtk_array):
    """Converts a VTK data array to a Numeric array.

    Given a subclass of vtkDataArray, this function returns an
    appropriate Numeric array containing the same data.  The function
    is very efficient since it uses the VTK imaging pipeline to
    convert the data.

    Parameters
    ----------

    - vtk_array : `vtkDataArray`

      The VTK data array to be converted.

    Warning
    -------

    This code is unlikely to work with the vtkIdTypeArray if you are
    using 64 bit ID's.  This is because 64 bit ids are 8 bytes long
    and it is not clear what Numeric array type one has to use in this
    case!

    """
    typ = vtk_array.GetDataType()
    assert typ in get_vtk_to_numeric_typemap().keys(), \
           "Unsupported array type %s"%typ

    shape = vtk_array.GetNumberOfTuples(), \
            vtk_array.GetNumberOfComponents()

    # First check if this array already has a numerix array cached, if
    # it does, reshape that and return it.
    key = vtk_array.__this__
    if key in _array_cache:
        arr = _array_cache[key]
        if shape[1] == 1:
            shape = (shape[0], )
        arr = numerix.reshape(arr, shape)
        return arr

    # Setup an imaging pipeline to export the array.
    img_data = vtk.vtkImageData()
    img_data.SetDimensions(shape[0], 1, 1)
    if typ == vtkConstants.VTK_BIT:
        iarr = vtk.vtkCharArray()
        iarr.DeepCopy(vtk_array)
        img_data.GetPointData().SetScalars(iarr)
    elif typ == vtkConstants.VTK_ID_TYPE:
        # Needed since VTK_ID_TYPE does not work with VTK 4.5.
        iarr = vtk.vtkLongArray()
        iarr.SetNumberOfTuples(vtk_array.GetNumberOfTuples())
        nc = vtk_array.GetNumberOfComponents()
        iarr.SetNumberOfComponents(nc)
        for i in range(nc):
            iarr.CopyComponent(i, vtk_array, i)
        img_data.GetPointData().SetScalars(iarr)
    else:
        img_data.GetPointData().SetScalars(vtk_array)

    img_data.SetNumberOfScalarComponents(shape[1])
    if typ == vtkConstants.VTK_ID_TYPE:
        # Hack necessary because vtkImageData can't handle VTK_ID_TYPE.
        img_data.SetScalarType(vtkConstants.VTK_LONG)
    elif typ == vtkConstants.VTK_BIT:
        img_data.SetScalarType(vtkConstants.VTK_CHAR)
    else:
        img_data.SetScalarType(typ)
    img_data.Update()

    exp = vtk.vtkImageExport()
    exp.SetInput(img_data)

    # Create an array of the right size and export the image into it.
    im_arr = empty_array((shape[0]*shape[1],), get_numeric_array_type(typ))
    if which_numerix in ('numeric', 'numpy'):
        exp.Export(im_arr)
    else:
        exp.Export(im_arr._data)

    # Now reshape it.
    if shape[1] == 1:
        shape = (shape[0], )
    im_arr = numerix.reshape(im_arr, shape)
    return im_arr


def array2vtkCellArray(num_array, vtk_array=None):
    """Given a nested Python list or a Numeric array, this method
    creates a vtkCellArray instance and returns it.

    A variety of input arguments are supported as described in the
    Parameter documentation.  If Numeric arrays are given, this method
    is highly efficient.  This function is most efficient if the
    passed Numeric arrays have a typecode of Numeric.Int ('l').
    Otherwise a typecast is necessary and this involves an extra copy.
    This method *always copies* the input data.

    An alternative and more efficient way to build the connectivity
    list is to create a vtkIdTypeArray having data of the form
    (npts,p0,p1,...p(npts-1), repeated for each cell) and then call
    <vtkCellArray_instance>.SetCells(n_cell, id_list).

    Parameters
    ----------

    - num_array : Numeric array or Python list/tuple

      Valid values are:

        1. A Python list of 1D lists.  Each 1D list can contain one
           cell connectivity list.  This is very slow and is to be
           used only when efficiency is of no consequence.

        2. A 2D Numeric array with the cell connectivity list.

        3. A Python list of 2D Numeric arrays.  Each numeric array can
           have a different shape.  This makes it easy to generate a
           cell array having cells of different kinds.

    - vtk_array : `vtkCellArray` (default: `None`)

      If an optional `vtkCellArray` instance, is passed as an argument
      then a new array is not created and returned.  The passed array
      is itself modified and returned.

    Example
    -------

       >>> a = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]
       >>> cells = array_handler.array2vtkCellArray(a)
       >>> a = Numeric.array([[0,1,2], [3,4,5], [6,7,8]], 'l')
       >>> cells = array_handler.array2vtkCellArray(a)
       >>> l_a = [a[:,:1], a[:2,:2], a]
       >>> cells = array_handler.array2vtkCellArray(l_a)

    """
    if vtk_array:
        cells = vtk_array
    else:
        cells = vtk.vtkCellArray()
    assert cells.GetClassName() == 'vtkCellArray', \
           'Second argument must be a `vtkCellArray` instance.'

    if len(num_array) == 0:
        return cells

    ########################################
    # Internal functions.
    def _slow_array2cells(z, cells):
        cells.Reset()
        vtk_ids = vtk.vtkIdList()
        for i in z:
            vtk_ids.Reset()
            for j in i:
                vtk_ids.InsertNextId(j)
            cells.InsertNextCell(vtk_ids)

    def _get_tmp_array(arr):
        try:
            tmp_arr = numerix.asarray(arr, ID_TYPE_CODE)
        except TypeError:
            tmp_arr = arr.astype(ID_TYPE_CODE)
        return tmp_arr

    def _set_cells(cells, n_cells, id_typ_arr):
        vtk_arr = vtk.vtkIdTypeArray()
        array2vtk(id_typ_arr, vtk_arr)
        cells.SetCells(n_cells, vtk_arr)
    ########################################

    msg = "Invalid argument.  Valid types are a Python list of lists,"\
          " a Python list of Numeric arrays, or a Numeric array."

    if type(num_array) in (types.ListType, types.TupleType):
        assert len(num_array[0]) > 0, "Input array must be 2D."
        tp = type(num_array[0])
        if tp == types.ListType: # Pure Python list.
            _slow_array2cells(num_array, cells)
            return cells
        elif tp == numerix.ArrayType:  # List of arrays.
            # Check shape of array and find total size.
            tot_size = 0
            n_cells = 0
            for arr in num_array:
                assert len(arr.shape) == 2, "Each array must be 2D"
                shp = arr.shape
                tot_size += shp[0]*(shp[1] + 1)
                n_cells += shp[0]
            # Create an empty array.
            id_typ_arr = empty_array((tot_size,), ID_TYPE_CODE)
            # Now populate it with the ids.
            count = 0
            for arr in num_array:
                tmp_arr = _get_tmp_array(arr)
                shp = arr.shape
                sz = shp[0]*(shp[1] + 1)
                set_id_type_array(tmp_arr, id_typ_arr[count:count+sz])
                count += sz
            # Now set them cells.
            _set_cells(cells, n_cells, id_typ_arr)
            return cells
        else:
            raise TypeError, msg
    elif type(num_array) == numerix.ArrayType:
        assert len(num_array.shape) == 2, "Input array must be 2D."
        tmp_arr = _get_tmp_array(num_array)
        shp = tmp_arr.shape
        id_typ_arr = empty_array((shp[0]*(shp[1] + 1),), ID_TYPE_CODE)
        set_id_type_array(tmp_arr, id_typ_arr)
        _set_cells(cells, shp[0], id_typ_arr)
        return cells
    else:
        raise TypeError, msg


def array2vtkPoints(num_array, vtk_points=None):
    """Converts a Numeric array/Python list to a vtkPoints object.

    Unless a Python list/tuple or a non-contiguous array is given, no
    copy of the data is made.  Thus the function is very efficient.

    Parameters
    ----------

    - num_array : Numeric array or Python list/tuple

      The input array must be 2D with `shape[1] == 3`.

    - vtk_points : `vtkPoints` (default: `None`)

      If an optional `vtkPoints` instance, is passed as an argument
      then a new array is not created and returned.  The passed array
      is itself modified and returned.

    """
    if vtk_points:
        points  = vtk_points
    else:
        points = vtk.vtkPoints()

    arr = numerix.asarray(num_array)
    assert len(arr.shape) == 2, "Points array must be 2 dimensional."
    assert arr.shape[1] == 3, "Incorrect shape: shape[1] must be 3."
    vtk_array = array2vtk(arr)
    points.SetData(vtk_array)
    return points


def array2vtkIdList(num_array, vtk_idlist=None):
    """Converts a Numeric array/Python list to a vtkIdList object.

    Parameters
    ----------

    - num_array : Numeric array or Python list/tuple

      The input array must be 2D with `shape[1] == 3`.

    - vtk_idlist : `vtkIdList` (default: `None`)

      If an optional `vtkIdList` instance, is passed as an argument
      then a new array is not created and returned.  The passed array
      is itself modified and returned.

    """
    if vtk_idlist:
        ids = vtk_idlist
    else:
        ids = vtk.vtkIdList()

    arr = numerix.asarray(num_array)
    assert len(arr.shape) == 1, "Array for vtkIdList must be 1D"
    ids.SetNumberOfIds(len(arr))
    for i, j in enumerate(arr):
        ids.SetId(i, j)
    return ids


######################################################################
# Array argument handling functions.
######################################################################

def is_array(arr):
    """Returns True if the passed `arr` is a Numeric array or a List."""
    if type(arr) in [numerix.ArrayType, types.ListType]:
        return True
    return False


def convert_array(arr, vtk_typ=None):
    """Convert the given array to the optional type specified by
    `vtk_typ`.

    Parameters
    ----------

    - arr : Numeric array/list.
    - vtk_typ : `string` or `None`
      represents the type the array is to be converted to.

    """
    if vtk_typ:
        conv = {'vtkCellArray': array2vtkCellArray,
                'vtkPoints': array2vtkPoints,
                'vtkIdList': array2vtkIdList}
        if vtk_typ in conv.keys():
            vtk_arr = getattr(vtk, vtk_typ)()
            return conv[vtk_typ](arr, vtk_arr)
        elif vtk_typ.find('Array') > -1:
            try:
                vtk_arr = getattr(vtk, vtk_typ)()
            except TypeError: # vtk_typ == 'vtkDataArray'
                return array2vtk(arr)
            else:
                return array2vtk(arr, vtk_arr)
        else:
            return arr
    else:
        return array2vtk(arr)


def is_array_sig(s):
    """Given a signature, return if the signature has an array."""
    if not isinstance(s, basestring):
        return False
    arr_types = ['Array', 'vtkPoints', 'vtkIdList']
    for i in arr_types:
        if s.find(i) > -1:
            return True
    return False


def is_array_or_vtkarray(arg):
    """Returns True if the argument is an array/Python list or if it
    is a vtk array."""

    if is_array(arg):
        return True
    else:
        if hasattr(arg, '_vtk_obj'):
            if is_array_sig(arg._vtk_obj.__class__.__name__):
                return True
    return False


def get_correct_sig(args, sigs):
    """Given a list of args and a collection of possible signatures,
    this function returns the most appropriate signature.  This
    function is only called by deref_array.  This implies that one of
    the signatures has an array type.

    """
    # First do the trivial cases.
    if sigs is None:
        return None
    if len(sigs) == 1:
        return sigs[0]
    else:
        # Non-trivial cases.
        la = len(args)
        candidate_sigs = [s for s in sigs if len(s) == la]
        count = len(candidate_sigs)
        if count == 0:
            # No sig has the right number of args.
            msg = "Insufficient number of arguments to method."\
                  "Valid arguments are:\n%s"%sigs
            raise TypeError, msg
        elif count == 1:
            # If only one of the sigs has the right number of args,
            # return it.
            return candidate_sigs[0]
        else:
            # More than one sig has the same number of args.
            # Check if args need conversion at all.
            array_idx = [i for i, a in enumerate(args) \
                         if is_array_or_vtkarray(a)]
            n_arr = len(array_idx)
            if n_arr == 0:
                # No conversion necessary so signature info is
                # useless.
                return None
            else:
                # Need to find the right sig.  This is done by finding
                # the first signature that matches all the arrays in
                # the argument.
                for sig in candidate_sigs:
                    array_in_sig = [is_array_sig(s) for s in sig]
                    if array_in_sig.count(True) != len(array_idx):
                        continue
                    bad = False
                    for i in array_idx:
                        if not array_in_sig[i]:
                            bad = True
                    if not bad:
                        return sig
                # Could not find any valid signature, so give up.
                return None


def deref_vtk(obj):
    """Dereferences the VTK object from the object if possible.  This
    is duplicated from `tvtk_base.py` because I'd like to keep this
    module independent of `tvtk_base.py`.
    """
    if hasattr(obj, '_vtk_obj'):
        return obj._vtk_obj
    else:
        return obj


def deref_array(args, sigs=None):
    """Given a bunch of arguments and optional signature information,
    this converts the arguments suitably.  If the argument is either a
    Python list or a Numeric array it is converted to a suitable type
    based on the signature information.  If it is not an array, but a
    TVTK object the VTK object is dereferenced.  Otherwise nothing is
    done.  If no signature information is provided the arrays are
    automatically converted (this can sometimes go wrong).  The
    signature information is provided in the form of a list of lists.

    """
    ret = []
    sig = get_correct_sig(args, sigs)
    if sig:
        for a, s in zip(args, sig):
            if is_array(a) and is_array_sig(s):
                ret.append(convert_array(a, s))
            else:
                ret.append(deref_vtk(a))
    else:
        for a in args:
            if is_array(a):
                ret.append(convert_array(a))
            else:
                ret.append(deref_vtk(a))
    return ret

