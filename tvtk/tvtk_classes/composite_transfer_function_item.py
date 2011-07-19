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

from tvtk.tvtk_classes.color_transfer_function_item import ColorTransferFunctionItem


class CompositeTransferFunctionItem(ColorTransferFunctionItem):
    """
    CompositeTransferFunctionItem - no description provided.
    
    Superclass: ColorTransferFunctionItem
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeTransferFunctionItem, obj, update, **traits)
    
    def _get_opacity_function(self):
        return wrap_vtk(self._vtk_obj.GetOpacityFunction())
    def _set_opacity_function(self, arg):
        old_val = self._get_opacity_function()
        self._wrap_call(self._vtk_obj.SetOpacityFunction,
                        deref_vtk(arg))
        self.trait_property_changed('opacity_function', old_val, arg)
    opacity_function = traits.Property(_get_opacity_function, _set_opacity_function, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('mask_above_curve', 'GetMaskAboveCurve'), ('width', 'GetWidth'),
    ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'label', 'mask_above_curve',
    'opacity', 'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeTransferFunctionItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeTransferFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'mask_above_curve', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit CompositeTransferFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeTransferFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

