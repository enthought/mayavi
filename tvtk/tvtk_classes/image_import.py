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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageImport(ImageAlgorithm):
    """
    ImageImport - Import data from a C array.
    
    Superclass: ImageAlgorithm
    
    ImageImport provides methods needed to import image data from a
    source independent of VTK, such as a simple C array or a third-party
    pipeline. Note that the VTK convention is for the image voxel index
    (0,0,0) to be the lower-left corner of the image, while most 2d image
    formats use the upper-left corner.  You can use ImageFlip to
    correct the orientation after the image has been loaded into VTK.
    Note that is also possible to import the raw data from a Python
    string instead of from a C array. The array applies on scalar point
    data only, not on cell data.
    
    See Also:
    
    ImageExport
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageImport, obj, update, **traits)
    
    def get_data_scalar_type(self):
        """
        V.get_data_scalar_type() -> int
        C++: int GetDataScalarType()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        ret = self._vtk_obj.GetDataScalarType()
        return ret
        

    def set_data_scalar_type(self, *args):
        """
        V.set_data_scalar_type(int)
        C++: void SetDataScalarType(int a)
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataScalarType, *args)
        return ret

    def set_data_scalar_type_to_double(self):
        """
        V.set_data_scalar_type_to_double()
        C++: void SetDataScalarTypeToDouble()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToDouble()

    def set_data_scalar_type_to_float(self):
        """
        V.set_data_scalar_type_to_float()
        C++: void SetDataScalarTypeToFloat()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToFloat()

    def set_data_scalar_type_to_int(self):
        """
        V.set_data_scalar_type_to_int()
        C++: void SetDataScalarTypeToInt()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToInt()

    def set_data_scalar_type_to_short(self):
        """
        V.set_data_scalar_type_to_short()
        C++: void SetDataScalarTypeToShort()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToShort()

    def set_data_scalar_type_to_unsigned_char(self):
        """
        V.set_data_scalar_type_to_unsigned_char()
        C++: void SetDataScalarTypeToUnsignedChar()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedChar()

    def set_data_scalar_type_to_unsigned_short(self):
        """
        V.set_data_scalar_type_to_unsigned_short()
        C++: void SetDataScalarTypeToUnsignedShort()
        Set/Get the data type of pixels in the imported data.  This is
        used as the scalar type of the Output.  Default: Short.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedShort()

    scalar_array_name = traits.String(r"scalars", enter_set=True, auto_set=False, help=\
        """
        Set/get the scalar array name for this data set. Initial value is
        "scalars".
        """
    )
    def _scalar_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArrayName,
                        self.scalar_array_name)

    data_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataExtent,
                        self.data_extent)

    whole_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    number_of_scalar_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of scalar components, for RGB images this must
        be 3. Default: 1.
        """
    )
    def _number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfScalarComponents,
                        self.number_of_scalar_components)

    def _get_import_void_pointer(self):
        return self._vtk_obj.GetImportVoidPointer()
    def _set_import_void_pointer(self, arg):
        old_val = self._get_import_void_pointer()
        self._wrap_call(self._vtk_obj.SetImportVoidPointer,
                        arg)
        self.trait_property_changed('import_void_pointer', old_val, arg)
    import_void_pointer = traits.Property(_get_import_void_pointer, _set_import_void_pointer, help=\
        """
        Set the pointer from which the image data is imported.  VTK will
        not make its own copy of the data, it will access the data
        directly from the supplied array.  VTK will not attempt to delete
        the data nor modify the data.
        """
    )

    def _get_callback_user_data(self):
        return self._vtk_obj.GetCallbackUserData()
    def _set_callback_user_data(self, arg):
        old_val = self._get_callback_user_data()
        self._wrap_call(self._vtk_obj.SetCallbackUserData,
                        arg)
        self.trait_property_changed('callback_user_data', old_val, arg)
    callback_user_data = traits.Property(_get_callback_user_data, _set_callback_user_data, help=\
        """
        Set/Get the user data which will be passed as the first argument
        to all of the third-party pipeline callbacks.
        """
    )

    data_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    data_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    def copy_import_void_pointer(self, *args):
        """
        V.copy_import_void_pointer(, int)
        C++: void CopyImportVoidPointer(void *ptr, int size)
        Import data and make an internal copy of it.  If you do not want
        VTK to copy the data, then use set_import_void_pointer instead (do
        not use both).  Give the size of the data array in bytes.
        """
        ret = self._wrap_call(self._vtk_obj.CopyImportVoidPointer, *args)
        return ret

    def invoke_execute_data_callbacks(self):
        """
        V.invoke_execute_data_callbacks()
        C++: void InvokeExecuteDataCallbacks()
        Invoke the appropriate callbacks
        """
        ret = self._vtk_obj.InvokeExecuteDataCallbacks()
        return ret
        

    def invoke_execute_information_callbacks(self):
        """
        V.invoke_execute_information_callbacks()
        C++: void InvokeExecuteInformationCallbacks()
        Invoke the appropriate callbacks
        """
        ret = self._vtk_obj.InvokeExecuteInformationCallbacks()
        return ret
        

    def invoke_pipeline_modified_callbacks(self):
        """
        V.invoke_pipeline_modified_callbacks() -> int
        C++: int InvokePipelineModifiedCallbacks()
        Invoke the appropriate callbacks
        """
        ret = self._vtk_obj.InvokePipelineModifiedCallbacks()
        return ret
        

    def invoke_update_information_callbacks(self):
        """
        V.invoke_update_information_callbacks()
        C++: void InvokeUpdateInformationCallbacks()
        Invoke the appropriate callbacks
        """
        ret = self._vtk_obj.InvokeUpdateInformationCallbacks()
        return ret
        

    def legacy_check_whole_extent(self):
        """
        V.legacy_check_whole_extent()
        C++: void LegacyCheckWholeExtent()
        Invoke the appropriate callbacks
        """
        ret = self._vtk_obj.LegacyCheckWholeExtent()
        return ret
        

    def set_data_extent_to_whole_extent(self):
        """
        V.set_data_extent_to_whole_extent()
        C++: void SetDataExtentToWholeExtent()
        Get/Set the extent of the data buffer.  The dimensions of your
        data must be equal to (extent[1]-extent[0]+1) *
        (extent[3]-extent[2]+1) * (extent[_5]-_data_extent[_4]+_1).  For
        example, for a 2d image use (0,width-1, 0,height-1, 0,0).
        """
        ret = self._vtk_obj.SetDataExtentToWholeExtent()
        return ret
        

    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('data_extent', 'GetDataExtent'),
    ('progress_text', 'GetProgressText'), ('scalar_array_name',
    'GetScalarArrayName'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('data_spacing', 'GetDataSpacing'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('data_origin',
    'GetDataOrigin'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'data_extent', 'data_origin', 'data_spacing',
    'number_of_scalar_components', 'progress_text', 'scalar_array_name',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageImport, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageImport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['data_extent', 'data_origin', 'data_spacing',
            'number_of_scalar_components', 'scalar_array_name', 'whole_extent']),
            title='Edit ImageImport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageImport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

