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

from tvtk.tvtk_classes.prop3d import Prop3D


class Assembly(Prop3D):
    """
    Assembly - create hierarchies of Prop3Ds (transformable props)
    
    Superclass: Prop3D
    
    Assembly is an object that groups Prop3Ds, its subclasses, and
    other assemblies into a tree-like hierarchy. The Prop3Ds and
    assemblies can then be transformed together by transforming just the
    root assembly of the hierarchy.
    
    A Assembly object can be used in place of an Prop3D since it is
    a subclass of Prop3D. The difference is that Assembly maintains
    a list of Prop3D instances (its "parts") that form the assembly.
    Then, any operation that transforms (i.e., scales, rotates,
    translates) the parent assembly will transform all its parts.  Note
    that this process is recursive: you can create groups consisting of
    assemblies and/or Prop3Ds to arbitrary depth.
    
    To add an assembly to the renderer's list of props, you only need to
    add the root of the assembly. During rendering, the parts of the
    assembly are rendered during a hierarchical traversal process.
    
    Caveats:
    
    Collections of assemblies are slower to render than an equivalent
    list of actors. This is because to support arbitrary nesting of
    assemblies, the state of the assemblies (i.e., transformation
    matrices) must be propagated through the assembly hierarchy.
    
    Assemblies can consist of hierarchies of assemblies, where one actor
    or assembly used in one hierarchy is also used in other hierarchies.
    However, make that there are no cycles (e.g., parent->child->parent),
    this will cause program failure.
    
    If you wish to create assemblies without any transformation (using
    the assembly strictly as a grouping mechanism), then you may wish to
    consider using PropAssembly.
    
    See Also:
    
    Actor Transform Mapper PolyDataMapper PropAssembly
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssembly, obj, update, **traits)
    
    def _get_parts(self):
        return wrap_vtk(self._vtk_obj.GetParts())
    parts = traits.Property(_get_parts, help=\
        """
        Return the parts (direct descendants) of this assembly.
        """
    )

    def add_part(self, *args):
        """
        V.add_part(Prop3D)
        C++: void AddPart(Prop3D *)
        Add a part to the list of parts.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPart, *my_args)
        return ret

    def remove_part(self, *args):
        """
        V.remove_part(Prop3D)
        C++: void RemovePart(Prop3D *)
        Remove a part from the list of parts,
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemovePart, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'), ('orientation',
    'GetOrientation'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Assembly, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Assembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale']),
            title='Edit Assembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Assembly properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

