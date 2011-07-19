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

from tvtk.tvtk_classes.poly_data_painter import PolyDataPainter


class StandardPolyDataPainter(PolyDataPainter):
    """
    StandardPolyDataPainter - A standard implementation of
    PolyDataPainter.
    
    Superclass: PolyDataPainter
    
    StandardPolyDataPainter is a catch-all painter.  It should work
    with pretty much any PolyData, and attributes, and
    PolyDataPainterDeviceAdapter.  On the flip side, the
    StandardPolyDataPainter will be slower than the more special
    purpose painters.
    
    See Also:
    
    DefaultPainter
    
    Thanks:
    
    Support for generic vertex attributes in VTK was contributed in
    collaboration with Stephane Ploix at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStandardPolyDataPainter, obj, update, **traits)
    
    def add_multi_texture_coords_array(self, *args):
        """
        V.add_multi_texture_coords_array(DataArray)
        C++: void AddMultiTextureCoordsArray(DataArray *array)"""
        my_args = deref_array(args, [['vtkDataArray']])
        ret = self._wrap_call(self._vtk_obj.AddMultiTextureCoordsArray, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StandardPolyDataPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StandardPolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit StandardPolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StandardPolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

