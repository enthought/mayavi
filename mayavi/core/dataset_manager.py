"""
Code to help with managing a TVTK data set in Pythonic ways.
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from traits.api import (HasTraits, Instance, Array, Str,
                        Property, Dict)
from tvtk.api import tvtk
from tvtk.array_handler import array2vtk
import tvtk.common as tvtk_common

######################################################################
# Utility functions.
######################################################################
def get_array_type(arr):
    """Returns if the array is a scalar ('scalars'), vector
    ('vectors') or tensor ('tensors').  It looks at the number of
    components to decide.  If it has a wierd number of components it
    returns the empty string.
    """
    n = arr.number_of_components
    ret = {1: 'scalars', 3: 'vectors', 4: 'scalars', 9:'tensors'}
    return ret.get(n) or ''


def get_attribute_list(data):
    """ Gets scalar, vector and tensor information from the given data
    (either cell or point data).
    """
    attr = {'scalars':[], 'vectors':[], 'tensors':[]}
    if data is not None:
        n = data.number_of_arrays
        for i in range(n):
            name = data.get_array_name(i)
            t = get_array_type(data.get_array(i))
            if len(t) > 0 and name is not None:
                attr[t].extend([name])

    def _mk_first(lst, value):
        """Makes the specified `value` the first item in `lst`."""
        lst.remove(value)
        lst.insert(0, value)

    attr1 = attr.copy()
    for a in attr:
        v = getattr(data, a)
        if v is not None:
            name = v.name
            if name is not None:
                try:
                    _mk_first(attr[a], v.name)
                except ValueError:
                    # Sometimes we have a multi-component scalar.
                    attr1[a].insert(0, name)
    return attr1


def get_all_attributes(obj):
    """Gets the scalar, vector and tensor attributes that are
    available in the given VTK data object.
    """
    point_attr = get_attribute_list(obj.point_data)
    cell_attr = get_attribute_list(obj.cell_data)
    return point_attr, cell_attr


################################################################################
# `DatasetManager` class.
################################################################################
class DatasetManager(HasTraits):

    # The TVTK dataset we manage.
    dataset = Instance(tvtk.DataSet)

    # Our output, this is the dataset modified by us with different
    # active arrays.
    output = Property(Instance(tvtk.DataSet))

    # The point scalars for the dataset.  You may manipulate the arrays
    # in-place.  However adding new keys in this dict will not set the
    # data in the `dataset` for that you must explicitly call
    # `add_array`.
    point_scalars = Dict(Str, Array)
    # Point vectors.
    point_vectors = Dict(Str, Array)
    # Point tensors.
    point_tensors = Dict(Str, Array)

    # The cell scalars for the dataset.
    cell_scalars = Dict(Str, Array)
    cell_vectors = Dict(Str, Array)
    cell_tensors = Dict(Str, Array)

    # This filter allows us to change the attributes of the data
    # object and will ensure that the pipeline is properly taken care
    # of.  Directly setting the array in the VTK object will not do
    # this.
    _assign_attribute = Instance(tvtk.AssignAttribute, args=(),
                                 allow_none=False)


    ######################################################################
    # Public interface.
    ######################################################################
    def add_array(self, array, name, category='point'):
        """
        Add an array to the dataset to specified category ('point' or
        'cell').
        """
        assert len(array.shape) <= 2, "Only 2D arrays can be added."
        data = getattr(self.dataset, '%s_data'%category)
        if len(array.shape) == 2:
            assert array.shape[1] in [1, 3, 4, 9], \
                    "Only Nxm arrays where (m in [1,3,4,9]) are supported"
            va = tvtk.to_tvtk(array2vtk(array))
            va.name = name
            data.add_array(va)
            mapping = {1:'scalars', 3: 'vectors', 4: 'scalars',
                       9: 'tensors'}
            dict = getattr(self, '%s_%s'%(category,
                                          mapping[array.shape[1]]))
            dict[name] = array
        else:
            va = tvtk.to_tvtk(array2vtk(array))
            va.name = name
            data.add_array(va)
            dict = getattr(self, '%s_scalars'%(category))
            dict[name] = array

    def remove_array(self, name, category='point'):
        """Remove an array by its name and optional category (point and
        cell).  Returns the removed array.
        """
        type = self._find_array(name, category)
        data = getattr(self.dataset, '%s_data'%category)
        data.remove_array(name)
        d = getattr(self, '%s_%s'%(category, type))
        return d.pop(name)

    def rename_array(self, name1, name2, category='point'):
        """Rename a particular array from `name1` to `name2`.
        """
        type = self._find_array(name1, category)
        data = getattr(self.dataset, '%s_data'%category)
        arr = data.get_array(name1)
        arr.name = name2
        d = getattr(self, '%s_%s'%(category, type))
        d[name2] = d.pop(name1)

    def activate(self, name, category='point'):
        """Make the specified array the active one.
        """
        type = self._find_array(name, category)
        self._activate_data_array(type, category, name)

    def update(self):
        """Update the dataset when the arrays are changed.
        """
        self.dataset.modified()
        self._assign_attribute.update()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _dataset_changed(self, value):
        self._setup_data()
        tvtk_common.configure_input_data(self._assign_attribute, value)

    def _get_output(self):
        return self._assign_attribute.output

    def _setup_data(self):
        """Updates the arrays from what is available in the input data.
        """
        input = self.dataset
        pnt_attr, cell_attr = get_all_attributes(input)

        self._setup_data_arrays(cell_attr, 'cell')
        self._setup_data_arrays(pnt_attr, 'point')

    def _setup_data_arrays(self, attributes, d_type):
        """Given the dict of the attributes from the
        `get_all_attributes` function and the data type (point/cell)
        data this will setup the object and the data.
        """
        attrs = ['scalars', 'vectors', 'tensors']
        aa = self._assign_attribute
        input = self.dataset
        data = getattr(input, '%s_data'%d_type)
        for attr in attrs:
            values = attributes[attr]
            # Get the arrays from VTK, create numpy arrays and setup our
            # traits.
            arrays = {}
            for name in values:
                va = data.get_array(name)
                npa = va.to_array()
                # Now test if changes to the numpy array are reflected
                # in the VTK array, if they are we are set, else we
                # have to set the VTK array back to the numpy array.
                if len(npa.shape) > 1:
                    old = npa[0,0]
                    npa[0][0] = old - 1
                    if abs(va[0][0] - npa[0,0]) > 1e-8:
                        va.from_array(npa)
                    npa[0][0] = old
                else:
                    old = npa[0]
                    npa[0] = old - 1
                    if abs(va[0] - npa[0]) > 1e-8:
                        va.from_array(npa)
                    npa[0] = old
                arrays[name] = npa

            setattr(self, '%s_%s'%(d_type, attr), arrays)

    def _activate_data_array(self, data_type, category, name):
        """Activate (or deactivate) a particular array.

        Given the nature of the data (scalars, vectors etc.) and the
        type of data (cell or points) it activates the array given by
        its name.

        Parameters:
        -----------

        data_type: one of 'scalars', 'vectors', 'tensors'
        category: one of 'cell', 'point'.
        name: string of array name to activate.
        """
        input = self.dataset
        data = None
        data = getattr(input, category + '_data')
        method = getattr(data, 'set_active_%s'%data_type)
        if len(name) == 0:
            # If the value is empty then we deactivate that attribute.
            method(None)
        else:
            aa = self._assign_attribute
            method(name)
            aa.assign(name, data_type.upper(), category.upper() +'_DATA')
            aa.update()

    def _find_array(self, name, category='point'):
        """Return information on which kind of attribute contains the
        specified named array in a particular category."""
        types = ['scalars', 'vectors', 'tensors']
        for type in types:
            attr = '%s_%s'%(category, type)
            d = getattr(self, attr)
            if name in d.keys():
                return type
        raise KeyError('No %s array named %s available in dataset'
                        %(category, name))

