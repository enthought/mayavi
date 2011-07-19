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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class TensorProbeRepresentation(WidgetRepresentation):
    """
    TensorProbeRepresentation - Abstract class that serves as a
    representation for TensorProbeWidget
    
    Superclass: WidgetRepresentation
    
    The class serves as an abstract geometrical representation for the
    TensorProbeWidget. It is left to the concrete implementation to
    render the tensors as it desires. For instance,
    EllipsoidTensorProbeRepresentation renders the tensors as
    ellipsoids.
    
    See Also:
    
    TensorProbeWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTensorProbeRepresentation, obj, update, **traits)
    
    probe_position = traits.Array(shape=(3,), value=(1.0000000000000001e+299, 1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _probe_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbePosition,
                        self.probe_position)

    probe_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the position of the Tensor probe.
        """
    )
    def _probe_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbeCellId,
                        self.probe_cell_id)

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Set the probe position to a reasonable location on the
        trajectory.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def move(self, *args):
        """
        V.move([float, float]) -> int
        C++: virtual int Move(double motionVector[2])
        INTERNAL - Do not use This method is invoked by the widget during
        user interaction. Move probe based on the position and the motion
        vector.
        """
        ret = self._wrap_call(self._vtk_obj.Move, *args)
        return ret

    def select_probe(self, *args):
        """
        V.select_probe([int, int]) -> int
        C++: virtual int SelectProbe(int pos[2])
        This method is invoked by the widget during user interaction. Can
        we pick the tensor glyph at the current cursor pos
        """
        ret = self._wrap_call(self._vtk_obj.SelectProbe, *args)
        return ret

    def set_trajectory(self, *args):
        """
        V.set_trajectory(PolyData)
        C++: virtual void SetTrajectory(PolyData *)
        Set the trajectory that we are trying to probe tensors on
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTrajectory, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('probe_position', 'GetProbePosition'),
    ('probe_cell_id', 'GetProbeCellId'), ('use_bounds', 'GetUseBounds'),
    ('reference_count', 'GetReferenceCount'), ('visibility',
    'GetVisibility'), ('need_to_render', 'GetNeedToRender'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('pickable', 'GetPickable'),
    ('dragable', 'GetDragable'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'place_factor',
    'probe_cell_id', 'probe_position', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TensorProbeRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'place_factor', 'probe_cell_id', 'probe_position',
            'render_time_multiplier']),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

