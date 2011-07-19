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

from tvtk.tvtk_classes.abstract_picker import AbstractPicker


class AbstractPropPicker(AbstractPicker):
    """
    AbstractPropPicker - abstract API for pickers that can pick an
    instance of Prop
    
    Superclass: AbstractPicker
    
    AbstractPropPicker is an abstract superclass for pickers that can
    pick an instance of Prop. Some pickers, like WorldPointPicker
    (not a subclass of this class), cannot identify the prop that is
    picked. Subclasses of AbstractPropPicker return a prop in the form
    of a AssemblyPath when a pick is invoked. Note that an
    AssemblyPath contain a list of AssemblyNodes, each of which in
    turn contains a reference to a Prop and a 4x4 transformation
    matrix. The path fully describes the entire pick path, so you can
    pick assemblies or portions of assemblies, or just grab the tail end
    of the AssemblyPath (which is the picked prop).
    
    Caveats:
    
    Because a Prop can be placed into different assemblies, or even in
    different leaf positions of the same assembly, the AssemblyPath is
    used to fully qualify exactly which use of the Prop was picked,
    including its position (since AssemblyPath includes a
    transformation matrix per node).
    
    The class returns information about picked actors, props, etc. Note
    that what is returned by these methods is the top level of the
    assembly path. This can cause a lot of confusion! For example, if you
    pick a Assembly, and the returned AssemblyPath has as a leaf a
    Actor, then if you invoke get_actor(), you will get NULL, even
    though an actor was indeed picked. (_get_assembly() will return
    something.) Note that the safest thing to do is to do a
    get_view_prop(), which will always return something if something was
    picked. A better way to manage picking is to work with
    AssemblyPath, since this completely defines the pick path from top
    to bottom in a assembly hierarchy, and avoids confusion when the same
    prop is used in different assemblies.
    
    The returned assembly paths refer to assembly nodes that in turn
    refer to Prop and Matrix. This association to Prop is not a
    reference counted association, meaning that dangling references are
    possible if you do a pick, get an assembly path, and then delete a
    Prop. (Reason: assembly paths create many self-referencing loops
    that destroy reference counting.)
    
    See Also:
    
    PropPicker Picker WorldPointPicker CellPicker
    PointPicker AssemblyPath AssemblyNode AssemblyPaths
    AbstractPicker Renderer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractPropPicker, obj, update, **traits)
    
    def _get_path(self):
        return wrap_vtk(self._vtk_obj.GetPath())
    def _set_path(self, arg):
        old_val = self._get_path()
        self._wrap_call(self._vtk_obj.SetPath,
                        deref_vtk(arg))
        self.trait_property_changed('path', old_val, arg)
    path = traits.Property(_get_path, _set_path, help=\
        """
        Return the AssemblyPath that has been picked. The assembly
        path lists all the Props that form an assembly. If no assembly
        is present, then the assembly path will have one node (which is
        the picked prop). The set method is used internally to set the
        path. (Note: the structure of an assembly path is a collection of
        AssemblyNode, each node pointing to a Prop and (possibly) a
        transformation matrix.)
        """
    )

    def _get_actor(self):
        return wrap_vtk(self._vtk_obj.GetActor())
    actor = traits.Property(_get_actor, help=\
        """
        Return the Actor that has been picked. If NULL, no actor was
        picked.
        """
    )

    def _get_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetActor2D())
    actor2d = traits.Property(_get_actor2d, help=\
        """
        Return the Actor2D that has been picked. If NULL, no actor_2d
        was picked.
        """
    )

    def _get_assembly(self):
        return wrap_vtk(self._vtk_obj.GetAssembly())
    assembly = traits.Property(_get_assembly, help=\
        """
        Return the Assembly that has been picked. If NULL, no assembly
        was picked. (Note: the returned assembly is the first node in the
        assembly path. If the path is one node long, then the assembly
        and the prop are the same, assuming that the first node is a
        Assembly.)
        """
    )

    def _get_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetProp3D())
    prop3d = traits.Property(_get_prop3d, help=\
        """
        Return the Prop that has been picked. If NULL, no Prop3D
        was picked.
        """
    )

    def _get_prop_assembly(self):
        return wrap_vtk(self._vtk_obj.GetPropAssembly())
    prop_assembly = traits.Property(_get_prop_assembly, help=\
        """
        Return the PropAssembly that has been picked. If NULL, no prop
        assembly was picked. (Note: the returned prop assembly is the
        first node in the assembly path. If the path is one node long,
        then the prop assembly and the prop are the same, assuming that
        the first node is a PropAssembly.)
        """
    )

    def _get_view_prop(self):
        return wrap_vtk(self._vtk_obj.GetViewProp())
    view_prop = traits.Property(_get_view_prop, help=\
        """
        Return the Prop that has been picked. If NULL, nothing was
        picked. If anything at all was picked, this method will return
        something.
        """
    )

    def _get_volume(self):
        return wrap_vtk(self._vtk_obj.GetVolume())
    volume = traits.Property(_get_volume, help=\
        """
        Return the Volume that has been picked. If NULL, no volume was
        picked.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractPropPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractPropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], []),
            title='Edit AbstractPropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractPropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

