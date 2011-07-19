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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageProjection(ThreadedImageAlgorithm):
    """
    ImageProjection - project an image along the Z direction
    
    Superclass: ThreadedImageAlgorithm
    
    ImageProjection will combine all of the slices of an image to
    create a single slice.  The slices can be combined with the following
    operations: averaging, summation, minimum, maximum. If you require an
    arbitrary angle of projection, you can use ImageReslice to rotate
    the image before applying this filter.
    
    Thanks:
    
    Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageProjection, obj, update, **traits)
    
    multi_slice_output = tvtk_base.false_bool_trait(help=\
        """
        Turn on multi-slice output.  Each slice of the output will be a
        projection through the specified range of input slices, e.g. if
        the slice_range is [0,3] then slice 'i' of the output will be a
        projection through slices 'i' through '3+i' of the input. This
        flag is off by default.
        """
    )
    def _multi_slice_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMultiSliceOutput,
                        self.multi_slice_output_)

    operation = traits.Trait('average',
    tvtk_base.TraitRevPrefixMap({'average': 0, 'minimum': 2, 'maximum': 3, 'sum': 1}), help=\
        """
        Set the operation to use when combining slices.  The choices are
        "Average", "Sum", "Maximum", "Minimum".  The default is
        "Average".
        """
    )
    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    slice_direction = traits.Trait('z',
    tvtk_base.TraitRevPrefixMap({'y': 1, 'x': 0, 'z': 2}), help=\
        """
        Set the slice direction: zero for x, 1 for y, 2 for z. The
        default is the Z direction.
        """
    )
    def _slice_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceDirection,
                        self.slice_direction_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_input_scalar_type(self):
        """
        V.set_output_scalar_type_to_input_scalar_type()
        C++: void SetOutputScalarTypeToInputScalarType()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToInputScalarType()

    slice_range = traits.Array(shape=(2,), value=(-2147483648, 2147483647), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _slice_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceRange,
                        self.slice_range)

    _updateable_traits_ = \
    (('multi_slice_output', 'GetMultiSliceOutput'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('slice_direction',
    'GetSliceDirection'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('operation',
    'GetOperation'), ('slice_range', 'GetSliceRange'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'multi_slice_output', 'release_data_flag', 'operation',
    'slice_direction', 'number_of_threads', 'progress_text',
    'slice_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageProjection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['multi_slice_output'], ['operation',
            'slice_direction'], ['number_of_threads', 'slice_range']),
            title='Edit ImageProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

