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

from tvtk.tvtk_classes.lookup_table import LookupTable


class LogLookupTable(LookupTable):
    """
    LogLookupTable - map scalars into colors using log (base 10) scale
    
    Superclass: LookupTable
    
    This class is an empty shell.  Use LookupTable with
    set_scale_to_log10() instead.
    
    See Also:
    
    LookupTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLogLookupTable, obj, update, **traits)
    
    _updateable_traits_ = \
    (('scale', 'GetScale'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('saturation_range',
    'GetSaturationRange'), ('number_of_table_values',
    'GetNumberOfTableValues'), ('hue_range', 'GetHueRange'), ('nan_color',
    'GetNanColor'), ('ramp', 'GetRamp'), ('debug', 'GetDebug'),
    ('number_of_colors', 'GetNumberOfColors'), ('table_range',
    'GetTableRange'), ('range', 'GetRange'), ('vector_component',
    'GetVectorComponent'), ('value_range', 'GetValueRange'),
    ('reference_count', 'GetReferenceCount'), ('alpha', 'GetAlpha'),
    ('vector_mode', 'GetVectorMode'), ('alpha_range', 'GetAlphaRange'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'ramp', 'scale', 'vector_mode',
    'alpha', 'alpha_range', 'hue_range', 'nan_color', 'number_of_colors',
    'number_of_table_values', 'range', 'saturation_range', 'table_range',
    'value_range', 'vector_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LogLookupTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LogLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['ramp', 'scale', 'vector_mode'], ['alpha',
            'alpha_range', 'hue_range', 'nan_color', 'number_of_colors',
            'number_of_table_values', 'range', 'saturation_range', 'table_range',
            'value_range', 'vector_component']),
            title='Edit LogLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LogLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

