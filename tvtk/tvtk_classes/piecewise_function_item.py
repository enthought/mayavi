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

from tvtk.tvtk_classes.scalars_to_colors_item import ScalarsToColorsItem


class PiecewiseFunctionItem(ScalarsToColorsItem):
    """
    PiecewiseFunctionItem - no description provided.
    
    Superclass: ScalarsToColorsItem
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPiecewiseFunctionItem, obj, update, **traits)
    
    def _get_piecewise_function(self):
        return wrap_vtk(self._vtk_obj.GetPiecewiseFunction())
    def _set_piecewise_function(self, arg):
        old_val = self._get_piecewise_function()
        self._wrap_call(self._vtk_obj.SetPiecewiseFunction,
                        deref_vtk(arg))
        self.trait_property_changed('piecewise_function', old_val, arg)
    piecewise_function = traits.Property(_get_piecewise_function, _set_piecewise_function, help=\
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
            return super(PiecewiseFunctionItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PiecewiseFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'mask_above_curve', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit PiecewiseFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PiecewiseFunctionItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

