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

from tvtk.tvtk_classes.color_transfer_function import ColorTransferFunction


class DiscretizableColorTransferFunction(ColorTransferFunction):
    """
    DiscretizableColorTransferFunction - a combination of
    ColorTransferFunction and
    
    Superclass: ColorTransferFunction
    
    This is a cross between a ColorTransferFunction and a
    LookupTable selectively combiniting the functionality of both.
    NOTE: One must call Build() after making any changes to the points in
    the color_transfer_function to ensure that the discrete and
    non-discrete version match up.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiscretizableColorTransferFunction, obj, update, **traits)
    
    discretize = tvtk_base.false_bool_trait(help=\
        """
        Set if the values are to mapped after discretization. The number
        of discrete values is set by using set_number_of_values(). Not set
        by default, i.e. color value is determined by interpolating at
        the scalar value.
        """
    )
    def _discretize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiscretize,
                        self.discretize_)

    number_of_values = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        Set the number of values i.e. colors to be generated in the
        discrete lookup table. This has no effect if Discretize is off.
        The default is 256.
        """
    )
    def _number_of_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfValues,
                        self.number_of_values)

    use_log_scale = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set if log scale must be used while mapping scalars to
        colors. The default is 0.
        """
    )
    def _use_log_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLogScale,
                        self.use_log_scale)

    _updateable_traits_ = \
    (('discretize', 'GetDiscretize'), ('color_space', 'GetColorSpace'),
    ('scale', 'GetScale'), ('hsv_wrap', 'GetHSVWrap'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_values', 'GetNumberOfValues'), ('allow_duplicate_scalars',
    'GetAllowDuplicateScalars'), ('nan_color', 'GetNanColor'), ('debug',
    'GetDebug'), ('range', 'GetRange'), ('vector_component',
    'GetVectorComponent'), ('reference_count', 'GetReferenceCount'),
    ('alpha', 'GetAlpha'), ('vector_mode', 'GetVectorMode'), ('clamping',
    'GetClamping'), ('use_log_scale', 'GetUseLogScale'))
    
    _full_traitnames_list_ = \
    (['allow_duplicate_scalars', 'clamping', 'debug', 'discretize',
    'global_warning_display', 'hsv_wrap', 'color_space', 'scale',
    'vector_mode', 'alpha', 'nan_color', 'number_of_values', 'range',
    'use_log_scale', 'vector_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiscretizableColorTransferFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_duplicate_scalars', 'clamping', 'discretize',
            'hsv_wrap'], ['color_space', 'scale', 'vector_mode'], ['alpha',
            'nan_color', 'number_of_values', 'range', 'use_log_scale',
            'vector_component']),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

