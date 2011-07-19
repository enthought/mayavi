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

from tvtk.tvtk_classes.prop import Prop


class PropAssembly(Prop):
    """
    PropAssembly - create hierarchies of props
    
    Superclass: Prop
    
    PropAssembly is an object that groups props and other prop
    assemblies into a tree-like hierarchy. The props can then be treated
    as a group (e.g., turning visibility on and off).
    
    A PropAssembly object can be used in place of an Prop since it
    is a subclass of Prop. The difference is that PropAssembly
    maintains a list of other prop and prop assembly instances (its
    "parts") that form the assembly. Note that this process is recursive:
    you can create groups consisting of prop assemblies to arbitrary
    depth.
    
    PropAssembly's and Prop's that compose a prop assembly need not
    be added to a renderer's list of props, as long as the parent
    assembly is in the prop list. This is because they are automatically
    renderered during the hierarchical traversal process.
    
    Caveats:
    
    PropAssemblies can consist of hierarchies of assemblies, where one
    actor or assembly used in one hierarchy is also used in other
    hierarchies. However, make that there are no cycles (e.g.,
    parent->child->parent), this will cause program failure.
    
    See Also:
    
    Prop3D Actor Assembly Actor2D Volume
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPropAssembly, obj, update, **traits)
    
    def _get_parts(self):
        return wrap_vtk(self._vtk_obj.GetParts())
    parts = traits.Property(_get_parts, help=\
        """
        Return the list of parts.
        """
    )

    def add_part(self, *args):
        """
        V.add_part(Prop)
        C++: void AddPart(Prop *)
        Add a part to the list of parts.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPart, *my_args)
        return ret

    def remove_part(self, *args):
        """
        V.remove_part(Prop)
        C++: void RemovePart(Prop *)
        Remove a part from the list of parts,
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemovePart, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('reference_count', 'GetReferenceCount'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PropAssembly, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PropAssembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time',
            'render_time_multiplier']),
            title='Edit PropAssembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PropAssembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

