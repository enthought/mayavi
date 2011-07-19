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

from tvtk.tvtk_classes.object import Object


class ScenePicker(Object):
    """
    ScenePicker - Picks an entire viewport at one shot. 
    
    Superclass: Object
    
    The Scene picker, unline conventional pickers picks an entire
    viewport at one shot and caches the result, which can be retrieved
    later.
       The utility of the class arises during Actor Selection. Let's say
    you have a couple of polygonal objects in your scene and you wish to
    have a status bar that indicates the object your mouse is over.
    Picking repeatedly every time your mouse moves would be very slow.
    The scene picker automatically picks your viewport every time the
    camera is changed and caches the information. Additionally, it
    observes the RenderWindowInteractor to avoid picking during
    interaction, so that you still maintain your interactivity. In
    effect, the picker does an additional pick-render of your scene every
    time you stop interacting with your scene. As an example, see
    rendering/_test_scene_picker.
    
    Caveats:
    
    - Unlike a HoverWidget, this class is not timer based. The hover
      widget picks a scene when the mouse is over an actor for a
      specified duration.
    - This class uses a HardwareSelector under the hood. Hence, it
      will work only for actors that have opaque geomerty and are
      rendered by a PolyDataMapper.
    
    See Also:
    
    HoverWidget HardwareSelector
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScenePicker, obj, update, **traits)
    
    enable_vertex_picking = tvtk_base.true_bool_trait(help=\
        """
        Vertex picking (using the method get_vertex_id()), required
        additional resources and can slow down still render time by
        5-10%. Enabled by default.
        """
    )
    def _enable_vertex_picking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableVertexPicking,
                        self.enable_vertex_picking_)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Set the renderer. Scene picks are restricted to the viewport.
        """
    )

    def get_cell_id(self, *args):
        """
        V.get_cell_id([int, int]) -> int
        C++: IdType GetCellId(int displayPos[2])
        Get cell id at the pick position. Returns -1 if no cell was
        picked. Makes sense only after Pick has been called.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellId, *args)
        return ret

    def get_vertex_id(self, *args):
        """
        V.get_vertex_id([int, int]) -> int
        C++: IdType GetVertexId(int displayPos[2])
        Get cell id at the pick position. Returns -1 if no cell was
        picked. Makes sense only after Pick has been called.
        """
        ret = self._wrap_call(self._vtk_obj.GetVertexId, *args)
        return ret

    def get_view_prop(self, *args):
        """
        V.get_view_prop([int, int]) -> Prop
        C++: Prop *GetViewProp(int displayPos[2])
        Get actor at the pick position. Returns NULL if none. Makes sense
        only after Pick has been called.
        """
        ret = self._wrap_call(self._vtk_obj.GetViewProp, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('enable_vertex_picking', 'GetEnableVertexPicking'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'enable_vertex_picking', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScenePicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScenePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enable_vertex_picking'], [], []),
            title='Edit ScenePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScenePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

