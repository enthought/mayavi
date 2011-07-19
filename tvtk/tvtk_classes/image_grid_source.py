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


class ImageGridSource(ImageAlgorithm):
    """
    ImageGridSource - Create an image of a grid.
    
    Superclass: ImageAlgorithm
    
    ImageGridSource produces an image of a grid.  The default output
    type is double.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageGridSource, obj, update, **traits)
    
    def get_data_scalar_type(self):
        """
        V.get_data_scalar_type() -> int
        C++: int GetDataScalarType()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        ret = self._vtk_obj.GetDataScalarType()
        return ret
        

    def set_data_scalar_type(self, *args):
        """
        V.set_data_scalar_type(int)
        C++: void SetDataScalarType(int a)
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataScalarType, *args)
        return ret

    def set_data_scalar_type_to_int(self):
        """
        V.set_data_scalar_type_to_int()
        C++: void SetDataScalarTypeToInt()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToInt()

    def set_data_scalar_type_to_short(self):
        """
        V.set_data_scalar_type_to_short()
        C++: void SetDataScalarTypeToShort()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToShort()

    def set_data_scalar_type_to_unsigned_char(self):
        """
        V.set_data_scalar_type_to_unsigned_char()
        C++: void SetDataScalarTypeToUnsignedChar()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedChar()

    def set_data_scalar_type_to_unsigned_short(self):
        """
        V.set_data_scalar_type_to_unsigned_short()
        C++: void SetDataScalarTypeToUnsignedShort()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedShort()

    data_extent = traits.Array(shape=(6,), value=(0, 255, 0, 255, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataExtent,
                        self.data_extent)

    fill_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the grey level of the fill. Default 0.0.
        """
    )
    def _fill_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillValue,
                        self.fill_value)

    grid_spacing = traits.Array(shape=(3,), value=(10, 10, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSpacing,
                        self.grid_spacing)

    line_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the grey level of the lines. Default 1.0.
        """
    )
    def _line_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineValue,
                        self.line_value)

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

    grid_origin = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridOrigin,
                        self.grid_origin)

    _updateable_traits_ = \
    (('line_value', 'GetLineValue'), ('grid_origin', 'GetGridOrigin'),
    ('data_extent', 'GetDataExtent'), ('fill_value', 'GetFillValue'),
    ('progress_text', 'GetProgressText'), ('grid_spacing',
    'GetGridSpacing'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('data_spacing', 'GetDataSpacing'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('data_origin',
    'GetDataOrigin'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'data_extent', 'data_origin', 'data_spacing',
    'fill_value', 'grid_origin', 'grid_spacing', 'line_value',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageGridSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['data_extent', 'data_origin', 'data_spacing',
            'fill_value', 'grid_origin', 'grid_spacing', 'line_value']),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

