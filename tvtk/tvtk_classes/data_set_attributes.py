# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.field_data import FieldData


class DataSetAttributes(FieldData):
    """
    DataSetAttributes - represent and manipulate attribute data in a
    dataset
    
    Superclass: FieldData
    
    DataSetAttributes is a class that is used to represent and
    manipulate attribute data (e.g., scalars, vectors, normals, texture
    coordinates, tensors, global ids, pedigree ids, and field data).
    
    This adds to FieldData the ability to pick one of the arrays from
    the field as the currently active array for each attribute type. In
    other words, you pick one array to be called "THE" Scalars, and then
    filters down the pipeline will treat that array specially. For
    example ContourFilter will contour "THE" Scalar array unless a
    different array is asked for.
    
    Additionally DataSetAttributes provides methods that filters call
    to pass data through, copy data into, and interpolate from Fields.
    pass_data passes entire arrays from the source to the destination.
    Copy passes through some subset of the tuples from the source to the
    destination. Interpolate interpolates from the chosen tuple(s) in the
    source data, using the provided weights, to produce new tuples in the
    destination. Each attribute type has pass, copy and interpolate
    "copy" flags that can be set in the destination to choose which
    attribute arrays will be transfered from the source to the
    destination.
    
    Finally this class provides a mechanism to determine which attributes
    a group of sources have in common, and to copy tuples from a source
    into the destination, for only those attributes that are held by all.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetAttributes, obj, update, **traits)
    
    copy_vectors = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of vector data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyVectors,
                        self.copy_vectors)

    copy_pedigree_ids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of pedigree id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyPedigreeIds,
                        self.copy_pedigree_ids)

    copy_tensors = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of tensor data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_tensors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyTensors,
                        self.copy_tensors)

    copy_t_coords = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of texture coordinates data. ctype is one
        of the attribute_copy_operations, and controls copy, interpolate
        and passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyTCoords,
                        self.copy_t_coords)

    def _get_vectors(self):
        return wrap_vtk(self._vtk_obj.GetVectors())
    def _set_vectors(self, arg):
        old_val = self._get_vectors()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetVectors,
                        my_arg[0])
        self.trait_property_changed('vectors', old_val, arg)
    vectors = traits.Property(_get_vectors, _set_vectors, help=\
        """
        Set/Get the vector data.
        """
    )

    copy_scalars = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of scalar data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyScalars,
                        self.copy_scalars)

    def _get_global_ids(self):
        return wrap_vtk(self._vtk_obj.GetGlobalIds())
    def _set_global_ids(self, arg):
        old_val = self._get_global_ids()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetGlobalIds,
                        my_arg[0])
        self.trait_property_changed('global_ids', old_val, arg)
    global_ids = traits.Property(_get_global_ids, _set_global_ids, help=\
        """
        Set/Get the global id data.
        """
    )

    def _get_scalars(self):
        return wrap_vtk(self._vtk_obj.GetScalars())
    def _set_scalars(self, arg):
        old_val = self._get_scalars()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetScalars,
                        my_arg[0])
        self.trait_property_changed('scalars', old_val, arg)
    scalars = traits.Property(_get_scalars, _set_scalars, help=\
        """
        Set/Get the scalar data.
        """
    )

    copy_normals = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of normals data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyNormals,
                        self.copy_normals)

    copy_global_ids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the copying of global id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
    )
    def _copy_global_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyGlobalIds,
                        self.copy_global_ids)

    def _get_normals(self):
        return wrap_vtk(self._vtk_obj.GetNormals())
    def _set_normals(self, arg):
        old_val = self._get_normals()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetNormals,
                        my_arg[0])
        self.trait_property_changed('normals', old_val, arg)
    normals = traits.Property(_get_normals, _set_normals, help=\
        """
        Set/get the normal data.
        """
    )

    def _get_t_coords(self):
        return wrap_vtk(self._vtk_obj.GetTCoords())
    def _set_t_coords(self, arg):
        old_val = self._get_t_coords()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetTCoords,
                        my_arg[0])
        self.trait_property_changed('t_coords', old_val, arg)
    t_coords = traits.Property(_get_t_coords, _set_t_coords, help=\
        """
        Set/Get the texture coordinate data.
        """
    )

    def _get_tensors(self):
        return wrap_vtk(self._vtk_obj.GetTensors())
    def _set_tensors(self, arg):
        old_val = self._get_tensors()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetTensors,
                        my_arg[0])
        self.trait_property_changed('tensors', old_val, arg)
    tensors = traits.Property(_get_tensors, _set_tensors, help=\
        """
        Set/Get the tensor data.
        """
    )

    def _get_pedigree_ids(self):
        return wrap_vtk(self._vtk_obj.GetPedigreeIds())
    def _set_pedigree_ids(self, arg):
        old_val = self._get_pedigree_ids()
        my_arg = deref_array([arg], [['vtkAbstractArray']])
        self._wrap_call(self._vtk_obj.SetPedigreeIds,
                        my_arg[0])
        self.trait_property_changed('pedigree_ids', old_val, arg)
    pedigree_ids = traits.Property(_get_pedigree_ids, _set_pedigree_ids, help=\
        """
        Set/Get the pedigree id data.
        """
    )

    def get_abstract_attribute(self, *args):
        """
        V.get_abstract_attribute(int) -> AbstractArray
        C++: AbstractArray *GetAbstractAttribute(int attributeType)
        Return an attribute given the attribute type (see
        DataSetAttributes::AttributeTypes). This is the same as
        get_attribute(), except that the returned array is a
        AbstractArray instead of DataArray. Some attributes (such
        as PEDIGREEIDS) may not be DataArray subclass.
        """
        ret = self._wrap_call(self._vtk_obj.GetAbstractAttribute, *args)
        return wrap_vtk(ret)

    def get_attribute(self, *args):
        """
        V.get_attribute(int) -> DataArray
        C++: DataArray *GetAttribute(int attributeType)
        Return an attribute given the attribute type (see
        DataSetAttributes::AttributeTypes). Some attributes (such as
        PEDIGREEIDS) may not be DataArray subclass, so in that case
        use get_abstract_attribute().
        """
        ret = self._wrap_call(self._vtk_obj.GetAttribute, *args)
        return wrap_vtk(ret)

    def get_attribute_type_as_string(self, *args):
        """
        V.get_attribute_type_as_string(int) -> string
        C++: static const char *GetAttributeTypeAsString(
            int attributeType)
        Given an integer attribute type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Scalars").
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeTypeAsString, *args)
        return ret

    def get_long_attribute_type_as_string(self, *args):
        """
        V.get_long_attribute_type_as_string(int) -> string
        C++: static const char *GetLongAttributeTypeAsString(
            int attributeType)
        Given an integer attribute type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Scalars").
        """
        ret = self._wrap_call(self._vtk_obj.GetLongAttributeTypeAsString, *args)
        return ret

    def copy_allocate(self, *args):
        """
        V.copy_allocate(DataSetAttributes, int, int)
        C++: void CopyAllocate(DataSetAttributes *pd, IdType sze=0,
            IdType ext=1000)
        V.copy_allocate(DataSetAttributes, int, int, int)
        C++: void CopyAllocate(DataSetAttributes *pd, IdType sze,
            IdType ext, int shallowCopyArrays)
        Allocates point data for point-by-point (or cell-by-cell) copy
        operation. If sze=0, then use the input data_set_attributes to
        create (i.e., find initial size of) new objects; otherwise use
        the sze variable. Note that pd HAS to be the DataSetAttributes
        object which will later be used with copy_data. If this is not the
        case, consider using the alternative forms of copy_allocate and
        copy_data. ext is no longer used. If shallow_copy_arrays is true,
        input arrays are copied to the output instead of new ones being
        allocated.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAllocate, *my_args)
        return ret

    def copy_data(self, *args):
        """
        V.copy_data(DataSetAttributes, int, int)
        C++: void CopyData(DataSetAttributes *fromPd, IdType fromId,
             IdType toId)
        Copy the attribute data from one id to another. Make sure
        copy_allocate() has been invoked before using this method. When
        copying a field, the following copying rules are followed: 1)
        Check if a field is an attribute, if yes and if there is a
        COPYTUPLE copy flag for that attribute (on or off), obey the 
        flag for that attribute, ignore (2) and (3), 2) if there is a
        copy field for that field (on or off), obey the flag, ignore (3)
        3) obey copy_all_on/_off
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyData, *my_args)
        return ret

    def copy_global_ids_off(self):
        """
        V.copy_global_ids_off()
        C++: void CopyGlobalIdsOff()
        Turn on/off the copying of global id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyGlobalIdsOff()
        return ret
        

    def copy_global_ids_on(self):
        """
        V.copy_global_ids_on()
        C++: void CopyGlobalIdsOn()
        Turn on/off the copying of global id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyGlobalIdsOn()
        return ret
        

    def copy_normals_off(self):
        """
        V.copy_normals_off()
        C++: void CopyNormalsOff()
        Turn on/off the copying of normals data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyNormalsOff()
        return ret
        

    def copy_normals_on(self):
        """
        V.copy_normals_on()
        C++: void CopyNormalsOn()
        Turn on/off the copying of normals data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyNormalsOn()
        return ret
        

    def copy_pedigree_ids_off(self):
        """
        V.copy_pedigree_ids_off()
        C++: void CopyPedigreeIdsOff()
        Turn on/off the copying of pedigree id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyPedigreeIdsOff()
        return ret
        

    def copy_pedigree_ids_on(self):
        """
        V.copy_pedigree_ids_on()
        C++: void CopyPedigreeIdsOn()
        Turn on/off the copying of pedigree id data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass for an attribute is set (on or
           off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyPedigreeIdsOn()
        return ret
        

    def copy_scalars_off(self):
        """
        V.copy_scalars_off()
        C++: void CopyScalarsOff()
        Turn on/off the copying of scalar data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyScalarsOff()
        return ret
        

    def copy_scalars_on(self):
        """
        V.copy_scalars_on()
        C++: void CopyScalarsOn()
        Turn on/off the copying of scalar data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyScalarsOn()
        return ret
        

    def copy_t_coords_off(self):
        """
        V.copy_t_coords_off()
        C++: void CopyTCoordsOff()
        Turn on/off the copying of texture coordinates data. ctype is one
        of the attribute_copy_operations, and controls copy, interpolate
        and passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyTCoordsOff()
        return ret
        

    def copy_t_coords_on(self):
        """
        V.copy_t_coords_on()
        C++: void CopyTCoordsOn()
        Turn on/off the copying of texture coordinates data. ctype is one
        of the attribute_copy_operations, and controls copy, interpolate
        and passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyTCoordsOn()
        return ret
        

    def copy_tensors_off(self):
        """
        V.copy_tensors_off()
        C++: void CopyTensorsOff()
        Turn on/off the copying of tensor data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyTensorsOff()
        return ret
        

    def copy_tensors_on(self):
        """
        V.copy_tensors_on()
        C++: void CopyTensorsOn()
        Turn on/off the copying of tensor data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyTensorsOn()
        return ret
        

    def copy_tuple(self, *args):
        """
        V.copy_tuple(AbstractArray, AbstractArray, int, int)
        C++: void CopyTuple(AbstractArray *fromData,
            AbstractArray *toData, IdType fromId, IdType toId)
        Copy a tuple of data from one data array to another. This method
        assumes that the from_data and to_data objects are of the same
        type, and have the same number of components. This is true if you
        invoke copy_allocate() or interpolate_allocate().
        """
        my_args = deref_array(args, [('vtkAbstractArray', 'vtkAbstractArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.CopyTuple, *my_args)
        return ret

    def copy_vectors_off(self):
        """
        V.copy_vectors_off()
        C++: void CopyVectorsOff()
        Turn on/off the copying of vector data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyVectorsOff()
        return ret
        

    def copy_vectors_on(self):
        """
        V.copy_vectors_on()
        C++: void CopyVectorsOn()
        Turn on/off the copying of vector data. ctype is one of the
        attribute_copy_operations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        During copying, interpolation and passdata, the following rules
        are followed for each array:
        1. If the copy/interpolate/pass flag for an attribute is set (on
           or off), it is applied. This overrides rules 2 and 3.
        2. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 3.
        3. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyVectorsOn()
        return ret
        

    def interpolate_allocate(self, *args):
        """
        V.interpolate_allocate(DataSetAttributes, int, int)
        C++: void InterpolateAllocate(DataSetAttributes *pd,
            IdType sze=0, IdType ext=1000)
        V.interpolate_allocate(DataSetAttributes, int, int, int)
        C++: void InterpolateAllocate(DataSetAttributes *pd,
            IdType sze, IdType ext, int shallowCopyArrays)
        Initialize point interpolation method. Note that pd HAS to be the
        DataSetAttributes object which will later be used with
        interpolate_point or interpolate_edge. ext is no longer used. If
        shallow_copy_arrays is true, input arrays are copied to the output
        instead of new ones being allocated.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateAllocate, *my_args)
        return ret

    def interpolate_edge(self, *args):
        """
        V.interpolate_edge(DataSetAttributes, int, int, int, float)
        C++: void InterpolateEdge(DataSetAttributes *fromPd,
            IdType toId, IdType p1, IdType p2, double t)
        Interpolate data from the two points p1,p2 (forming an edge) and
        an interpolation factor, t, along the edge. The weight ranges
        from (0,1), with t=0 located at p1. Make sure that the method
        interpolate_allocate() has been invoked before using this method.
        If the INTERPOLATION copy flag is set to 0 for an array,
        interpolation is prevented. If the flag is set to 1, weighted
        interpolation occurs. If the flag is set to 2, nearest neighbor
        interpolation is used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateEdge, *my_args)
        return ret

    def interpolate_time(self, *args):
        """
        V.interpolate_time(DataSetAttributes, DataSetAttributes, int,
             float)
        C++: void InterpolateTime(DataSetAttributes *from1,
            DataSetAttributes *from2, IdType id, double t)
        Interpolate data from the same id (point or cell) at different
        points in time (parameter t). Two input data set attributes
        objects are input. The parameter t lies between (0<=t<=1).
        IMPORTANT: it is assumed that the number of attributes and number
        of components is the same for both from1 and from2, and the type
        of data for from1 and from2 are the same. Make sure that the
        method interpolate_allocate() has been invoked before using this
        method. If the INTERPOLATION copy flag is set to 0 for an array,
        interpolation is prevented. If the flag is set to 1, weighted
        interpolation occurs. If the flag is set to 2, nearest neighbor
        interpolation is used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateTime, *my_args)
        return ret

    def is_array_an_attribute(self, *args):
        """
        V.is_array_an_attribute(int) -> int
        C++: int IsArrayAnAttribute(int idx)
        Determine whether a data array of index idx is considered a data
        set attribute (i.e., scalar, vector, tensor, etc). Return
        less-than zero if it is, otherwise an index 0<=idx<NUM_ATTRIBUTES
        to indicate which attribute.
        """
        ret = self._wrap_call(self._vtk_obj.IsArrayAnAttribute, *args)
        return ret

    def set_active_attribute(self, *args):
        """
        V.set_active_attribute(string, int) -> int
        C++: int SetActiveAttribute(const char *name, int attributeType)
        V.set_active_attribute(int, int) -> int
        C++: int SetActiveAttribute(int index, int attributeType)
        Make the array with the given name the active attribute.
        Attribute types are:
         DataSetAttributes::SCALARS = 0
         DataSetAttributes::VECTORS = 1
         DataSetAttributes::NORMALS = 2
         DataSetAttributes::TCOORDS = 3
         DataSetAttributes::TENSORS = 4
         DataSetAttributes::GLOBALIDS = 5
         DataSetAttributes::PEDIGREEIDS = 6
         DataSetAttributes::EDGEFLAG = 7 Returns the index of the
        array if succesful, -1 if the array is not in the list of arrays.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveAttribute, *args)
        return ret

    def set_active_global_ids(self, *args):
        """
        V.set_active_global_ids(string) -> int
        C++: int SetActiveGlobalIds(const char *name)
        Set/Get the global id data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveGlobalIds, *args)
        return ret

    def set_active_normals(self, *args):
        """
        V.set_active_normals(string) -> int
        C++: int SetActiveNormals(const char *name)
        Set/get the normal data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveNormals, *args)
        return ret

    def set_active_pedigree_ids(self, *args):
        """
        V.set_active_pedigree_ids(string) -> int
        C++: int SetActivePedigreeIds(const char *name)
        Set/Get the pedigree id data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActivePedigreeIds, *args)
        return ret

    def set_active_scalars(self, *args):
        """
        V.set_active_scalars(string) -> int
        C++: int SetActiveScalars(const char *name)
        Set/Get the scalar data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveScalars, *args)
        return ret

    def set_active_t_coords(self, *args):
        """
        V.set_active_t_coords(string) -> int
        C++: int SetActiveTCoords(const char *name)
        Set/Get the texture coordinate data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveTCoords, *args)
        return ret

    def set_active_tensors(self, *args):
        """
        V.set_active_tensors(string) -> int
        C++: int SetActiveTensors(const char *name)
        Set/Get the tensor data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveTensors, *args)
        return ret

    def set_active_vectors(self, *args):
        """
        V.set_active_vectors(string) -> int
        C++: int SetActiveVectors(const char *name)
        Set/Get the vector data.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveVectors, *args)
        return ret

    def set_copy_attribute(self, *args):
        """
        V.set_copy_attribute(int, int, int)
        C++: void SetCopyAttribute(int index, int value,
            int ctype=ALLCOPY)
        Specify whether to copy the data attribute referred to by index.
        ctype selects from the attribute_copy_operations. If ctype is set
        to ALLCOPY, then COPYTUPLE, INTERPOLATE, and PASSDATA are set to
        value. If value is 0, copying is disallowed. otherwise it is
        allowed.
        """
        ret = self._wrap_call(self._vtk_obj.SetCopyAttribute, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Attributes have a chance to bring themselves up to date; right
        now this is ignored.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('copy_tensors', 'GetCopyTensors'), ('copy_vectors',
    'GetCopyVectors'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('copy_normals',
    'GetCopyNormals'), ('copy_global_ids', 'GetCopyGlobalIds'),
    ('copy_t_coords', 'GetCopyTCoords'), ('copy_scalars',
    'GetCopyScalars'), ('copy_pedigree_ids', 'GetCopyPedigreeIds'),
    ('reference_count', 'GetReferenceCount'), ('number_of_tuples',
    'GetNumberOfTuples'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'copy_global_ids',
    'copy_normals', 'copy_pedigree_ids', 'copy_scalars', 'copy_t_coords',
    'copy_tensors', 'copy_vectors', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetAttributes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['copy_global_ids', 'copy_normals',
            'copy_pedigree_ids', 'copy_scalars', 'copy_t_coords', 'copy_tensors',
            'copy_vectors', 'number_of_tuples']),
            title='Edit DataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

