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


class AssemblyNode(Object):
    """
    AssemblyNode - represent a node in an assembly
    
    Superclass: Object
    
    AssemblyNode represents a node in an assembly. It is used by
    AssemblyPath to create hierarchical assemblies of props. The props
    can be either 2d or 3d.
    
    An assembly node refers to a Prop, and possibly a Matrix4x4.
    Nodes are used by AssemblyPath to build fully evaluated path
    (matrices are concatenated through the path) that is used by picking
    and other operations involving assemblies.
    
    Caveats:
    
    The assembly node is guaranteed to contain a reference to an instance
    of Matrix4x4 if the prop referred to by the node is of type
    Prop3D (or subclass). The matrix is evaluated through the assembly
    path, so the assembly node's matrix is a function of its location in
    the AssemblyPath.
    
    AssemblyNode does not reference count its association with
    Prop. Therefore, do not create an assembly node, associate a prop
    with it, delete the prop, and then try to dereference the prop. The
    program will break! (Reason: AssemblyPath (which uses
    AssemblyNode) create self-referencing loops that destroy reference
    counting.)
    
    See Also:
    
    AssemblyPath Prop Picker Matrix4x4
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssemblyNode, obj, update, **traits)
    
    def _get_view_prop(self):
        return wrap_vtk(self._vtk_obj.GetViewProp())
    def _set_view_prop(self, arg):
        old_val = self._get_view_prop()
        self._wrap_call(self._vtk_obj.SetViewProp,
                        deref_vtk(arg))
        self.trait_property_changed('view_prop', old_val, arg)
    view_prop = traits.Property(_get_view_prop, _set_view_prop, help=\
        """
        Set/Get the prop that this assembly node refers to.
        """
    )

    def _get_matrix(self):
        return wrap_vtk(self._vtk_obj.GetMatrix())
    def _set_matrix(self, arg):
        old_val = self._get_matrix()
        self._wrap_call(self._vtk_obj.SetMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('matrix', old_val, arg)
    matrix = traits.Property(_get_matrix, _set_matrix, help=\
        """
        Specify a transformation matrix associated with the prop. Note:
        if the prop is not a type of Prop3D, then the transformation
        matrix is ignored (and expected to be NULL). Also, internal to
        this object the matrix is copied because the matrix is used for
        computation by AssemblyPath.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AssemblyNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AssemblyNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AssemblyNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AssemblyNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

