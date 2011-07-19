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


class ChooserPainter(PolyDataPainter):
    """
    ChooserPainter - Painter that selects painters to render
    
    Superclass: PolyDataPainter
    
    This painter does not actually do any painting.  Instead, it picks
    other painters based on the current state of itself and its poly
    data.  It then delegates the work to these other painters.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChooserPainter, obj, update, **traits)
    
    use_lines_painter_for_wireframes = tvtk_base.false_bool_trait(help=\
        """
        When set, the lines painter is used for drawing wireframes (off
        by default, except on Mac, where it's on by default).
        """
    )
    def _use_lines_painter_for_wireframes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLinesPainterForWireframes,
                        self.use_lines_painter_for_wireframes_)

    def set_line_painter(self, *args):
        """
        V.set_line_painter(PolyDataPainter)
        C++: void SetLinePainter(PolyDataPainter *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLinePainter, *my_args)
        return ret

    def set_poly_painter(self, *args):
        """
        V.set_poly_painter(PolyDataPainter)
        C++: void SetPolyPainter(PolyDataPainter *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPolyPainter, *my_args)
        return ret

    def set_strip_painter(self, *args):
        """
        V.set_strip_painter(PolyDataPainter)
        C++: void SetStripPainter(PolyDataPainter *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStripPainter, *my_args)
        return ret

    def set_vert_painter(self, *args):
        """
        V.set_vert_painter(PolyDataPainter)
        C++: void SetVertPainter(PolyDataPainter *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVertPainter, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'), ('use_lines_painter_for_wireframes',
    'GetUseLinesPainterForWireframes'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display',
    'use_lines_painter_for_wireframes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChooserPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ChooserPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_lines_painter_for_wireframes'], [], []),
            title='Edit ChooserPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChooserPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

