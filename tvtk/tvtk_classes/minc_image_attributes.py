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

from tvtk.tvtk_classes.object import Object


class MINCImageAttributes(Object):
    """
    MINCImageAttributes - A container for a MINC image header.
    
    Superclass: Object
    
    This class provides methods to access all of the information
    contained in the MINC header.  If you read a MINC file into VTK and
    then write it out again, you can use
    writer->_set_image_attributes(reader->_get_image_attributes) to ensure that
    all of the medical information contained in the file is tranferred
    from the reader to the writer.  If you want to change any of the
    header information, you must use shallow_copy to make a copy of the
    reader's attributes and then modify only the copy.
    
    See Also:
    
    MINCImageReader MINCImageWriter
    
    Thanks:
    
    Thanks to David Gobbi for writing this class and Atamai Inc. for
    contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMINCImageAttributes, obj, update, **traits)
    
    validate_attributes = tvtk_base.true_bool_trait(help=\
        """
        Set this to Off if you do not want to automatically validate
        every attribute that is set.
        """
    )
    def _validate_attributes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidateAttributes,
                        self.validate_attributes_)

    number_of_image_min_max_dimensions = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the number of image_min_max dimensions.
        """
    )
    def _number_of_image_min_max_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfImageMinMaxDimensions,
                        self.number_of_image_min_max_dimensions)

    name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get the name of the image, not including the path or the
        extension.  This is only needed for printing the header and there
        is usually no need to set it.
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    data_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the image data type, as stored on disk.  This information is
        useful if the file was converted to floating-point when it was
        loaded.  When writing a file from float or double image data, you
        can use this method to prescribe the output type.
        """
    )
    def _data_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataType,
                        self.data_type)

    def get_attribute_value_as_double(self, *args):
        """
        V.get_attribute_value_as_double(string, string) -> float
        C++: virtual double GetAttributeValueAsDouble(
            const char *variable, const char *attribute)
        Set an attribute value as a double.  Set the variable to the
        empty string to access global attributes. If you specify a
        variable that does not exist, it will be created.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeValueAsDouble, *args)
        return ret

    def set_attribute_value_as_double(self, *args):
        """
        V.set_attribute_value_as_double(string, string, float)
        C++: virtual void SetAttributeValueAsDouble(const char *variable,
            const char *attribute, double value)
        Set an attribute value as a double.  Set the variable to the
        empty string to access global attributes. If you specify a
        variable that does not exist, it will be created.
        """
        ret = self._wrap_call(self._vtk_obj.SetAttributeValueAsDouble, *args)
        return ret

    def _get_image_min(self):
        return wrap_vtk(self._vtk_obj.GetImageMin())
    def _set_image_min(self, arg):
        old_val = self._get_image_min()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetImageMin,
                        my_arg[0])
        self.trait_property_changed('image_min', old_val, arg)
    image_min = traits.Property(_get_image_min, _set_image_min, help=\
        """
        Get the image min and max arrays. These are set by the reader,
        but they aren't used by the writer except to compute the full
        real data range of the original file.
        """
    )

    def _get_image_max(self):
        return wrap_vtk(self._vtk_obj.GetImageMax())
    def _set_image_max(self, arg):
        old_val = self._get_image_max()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetImageMax,
                        my_arg[0])
        self.trait_property_changed('image_max', old_val, arg)
    image_max = traits.Property(_get_image_max, _set_image_max, help=\
        """
        Get the image min and max arrays. These are set by the reader,
        but they aren't used by the writer except to compute the full
        real data range of the original file.
        """
    )

    def get_attribute_value_as_array(self, *args):
        """
        V.get_attribute_value_as_array(string, string) -> DataArray
        C++: virtual DataArray *GetAttributeValueAsArray(
            const char *variable, const char *attribute)
        Set attribute values for a variable as a DataArray. Set the
        variable to the empty string to access global attributes.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeValueAsArray, *args)
        return wrap_vtk(ret)

    def set_attribute_value_as_array(self, *args):
        """
        V.set_attribute_value_as_array(string, string, DataArray)
        C++: virtual void SetAttributeValueAsArray(const char *variable,
            const char *attribute, DataArray *array)
        Set attribute values for a variable as a DataArray. Set the
        variable to the empty string to access global attributes.
        """
        my_args = deref_array(args, [('string', 'string', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.SetAttributeValueAsArray, *my_args)
        return ret

    attribute_value_as_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set an attribute value as a string.  Set the variable to the
        empty string to access global attributes. If you specify a
        variable that does not exist, it will be created.
        """
    )
    def _attribute_value_as_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeValueAsString,
                        self.attribute_value_as_string)

    def get_attribute_value_as_int(self, *args):
        """
        V.get_attribute_value_as_int(string, string) -> int
        C++: virtual int GetAttributeValueAsInt(const char *variable,
            const char *attribute)
        Set an attribute value as an int. Set the variable to the empty
        string to access global attributes. If you specify a variable
        that does not exist, it will be created.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeValueAsInt, *args)
        return ret

    def set_attribute_value_as_int(self, *args):
        """
        V.set_attribute_value_as_int(string, string, int)
        C++: virtual void SetAttributeValueAsInt(const char *variable,
            const char *attribute, int value)
        Set an attribute value as an int. Set the variable to the empty
        string to access global attributes. If you specify a variable
        that does not exist, it will be created.
        """
        ret = self._wrap_call(self._vtk_obj.SetAttributeValueAsInt, *args)
        return ret

    def get_attribute_names(self, *args):
        """
        V.get_attribute_names(string) -> StringArray
        C++: virtual StringArray *GetAttributeNames(
            const char *variable)
        List the attribute names for a variable.  Set the variable to the
        empty string to get a list of the global attributes.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeNames, *args)
        return wrap_vtk(ret)

    def _get_dimension_lengths(self):
        return wrap_vtk(self._vtk_obj.GetDimensionLengths())
    dimension_lengths = traits.Property(_get_dimension_lengths, help=\
        """
        Get the lengths of all the dimensions.  The dimension lengths are
        informative, the MINCImageWriter does not look at these values
        but instead uses the dimension sizes of its input.
        """
    )

    def _get_dimension_names(self):
        return wrap_vtk(self._vtk_obj.GetDimensionNames())
    dimension_names = traits.Property(_get_dimension_names, help=\
        """
        Get the dimension names.  The dimension names are same order as
        written in the file, starting with the slowest-varying dimension.
         Use this method to get the array if you need to change "space"
        dimensions to "frequency" after performing a Fourier transform.
        """
    )

    def _get_variable_names(self):
        return wrap_vtk(self._vtk_obj.GetVariableNames())
    variable_names = traits.Property(_get_variable_names, help=\
        """
        Get the names of all the variables.
        """
    )

    def add_dimension(self, *args):
        """
        V.add_dimension(string)
        C++: virtual void AddDimension(const char *dimension)
        V.add_dimension(string, int)
        C++: virtual void AddDimension(const char *dimension,
            IdType length)
        Add the names of up to five dimensions. The ordering of these
        dimensions will determine the dimension order of the file.  If no
        dimension_names are set, the writer will set the dimension order
        of the file to be the same as the dimension order in memory.
        """
        ret = self._wrap_call(self._vtk_obj.AddDimension, *args)
        return ret

    def find_image_range(self, *args):
        """
        V.find_image_range([float, float])
        C++: virtual void FindImageRange(double range[2])
        Find the image range of the data from the information stored in
        the attributes.
        """
        ret = self._wrap_call(self._vtk_obj.FindImageRange, *args)
        return ret

    def find_valid_range(self, *args):
        """
        V.find_valid_range([float, float])
        C++: virtual void FindValidRange(double range[2])
        Find the valid range of the data from the information stored in
        the attributes.
        """
        ret = self._wrap_call(self._vtk_obj.FindValidRange, *args)
        return ret

    def has_attribute(self, *args):
        """
        V.has_attribute(string, string) -> int
        C++: virtual int HasAttribute(const char *variable,
            const char *attribute)
        Check to see if a particular attribute exists.
        """
        ret = self._wrap_call(self._vtk_obj.HasAttribute, *args)
        return ret

    def print_file_header(self):
        """
        V.print_file_header()
        C++: virtual void PrintFileHeader()
        A diagnostic function.  Print the header of the file in the same
        format as ncdump or mincheader.
        """
        ret = self._vtk_obj.PrintFileHeader()
        return ret
        

    def reset(self):
        """
        V.reset()
        C++: virtual void Reset()
        Reset all the attributes in preparation for loading new
        information.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(MINCImageAttributes)
        C++: virtual void ShallowCopy(MINCImageAttributes *source)
        Do a shallow copy.  This will copy all the attributes from the
        source.  It is much more efficient than a deep_copy would be,
        since it only copies pointers to the attribute values instead of
        copying the arrays themselves.  You must use this method to make
        a copy if you want to modify any MINC attributes from a
        MINCReader before you pass them to a MINCWriter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def validate_attribute(self, *args):
        """
        V.validate_attribute(string, string, DataArray) -> int
        C++: virtual int ValidateAttribute(const char *varname,
            const char *attname, DataArray *array)
        Validate a particular attribute.  This involves checking that the
        attribute is a MINC standard attribute, and checking whether it
        can be set (as opposed to being set automatically from the image
        information).  The return values is 0 if the attribute is set
        automatically and therefore should not be copied from here, 1 if
        this attribute is valid and should be set, and 2 if the attribute
        is non-standard.
        """
        my_args = deref_array(args, [('string', 'string', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.ValidateAttribute, *my_args)
        return ret

    _updateable_traits_ = \
    (('name', 'GetName'), ('data_type', 'GetDataType'),
    ('validate_attributes', 'GetValidateAttributes'),
    ('attribute_value_as_string', 'GetAttributeValueAsString'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'),
    ('number_of_image_min_max_dimensions',
    'GetNumberOfImageMinMaxDimensions'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'validate_attributes',
    'attribute_value_as_string', 'data_type', 'name',
    'number_of_image_min_max_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MINCImageAttributes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MINCImageAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['validate_attributes'], [],
            ['attribute_value_as_string', 'data_type', 'name',
            'number_of_image_min_max_dimensions']),
            title='Edit MINCImageAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MINCImageAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

