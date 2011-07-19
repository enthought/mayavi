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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class SpherePuzzle(PolyDataAlgorithm):
    """
    SpherePuzzle - create a polygonal sphere centered at the origin
    
    Superclass: PolyDataAlgorithm
    
    SpherePuzzle creates
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpherePuzzle, obj, update, **traits)
    
    def move_horizontal(self, *args):
        """
        V.move_horizontal(int, int, int)
        C++: void MoveHorizontal(int section, int percentage,
            int rightFlag)
        Move the top/bottom half one segment either direction.
        """
        ret = self._wrap_call(self._vtk_obj.MoveHorizontal, *args)
        return ret

    def move_point(self, *args):
        """
        V.move_point(int)
        C++: void MovePoint(int percentage)
        Move actually implements the pending move. When percentage is
        100, the pending move becomes inactive, and set_point will have to
        be called again to setup another move.
        """
        ret = self._wrap_call(self._vtk_obj.MovePoint, *args)
        return ret

    def move_vertical(self, *args):
        """
        V.move_vertical(int, int, int)
        C++: void MoveVertical(int section, int percentage, int rightFlag)
        Rotate vertical half of sphere along one of the longitude lines.
        """
        ret = self._wrap_call(self._vtk_obj.MoveVertical, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the state of this puzzle back to its original state.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_point(self, *args):
        """
        V.set_point(float, float, float) -> int
        C++: int SetPoint(double x, double y, double z)
        set_point will be called as the mouse moves over the screen. The
        output will change to indicate the pending move. set_point returns
        zero if move is not activated by point. Otherwise it encodes the
        move into a unique integer so that the caller can determine if
        the move state has changed. This will answer the question, "Should I
        render."
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpherePuzzle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SpherePuzzle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SpherePuzzle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpherePuzzle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

