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

from tvtk.tvtk_classes.collection import Collection


class AssemblyPath(Collection):
    """
    AssemblyPath - a list of nodes that form an assembly path
    
    Superclass: Collection
    
    AssemblyPath represents an ordered list of assembly nodes that
    represent a fully evaluated assembly path. This class is used
    primarily for picking. Note that the use of this class is to add one
    or more assembly nodes to form the path. (An assembly node consists
    of an instance of Prop and Matrix4x4, the matrix may be NULL.)
    As each node is added, the matrices are concatenated to create a
    final, evaluated matrix.
    
    See Also:
    
    AssemblyNode Assembly Actor Matrix4x4 Prop
    AbstractPicker
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssemblyPath, obj, update, **traits)
    
    def _get_first_node(self):
        return wrap_vtk(self._vtk_obj.GetFirstNode())
    first_node = traits.Property(_get_first_node, help=\
        """
        Get the first assembly node in the list. See the comments for
        get_next_node() regarding the contents of the returned node. (Note:
        This node corresponds to the Prop associated with the
        Renderer.
        """
    )

    def _get_last_node(self):
        return wrap_vtk(self._vtk_obj.GetLastNode())
    last_node = traits.Property(_get_last_node, help=\
        """
        Get the last assembly node in the list. See the comments for
        get_next_node() regarding the contents of the returned node.
        """
    )

    def _get_next_node(self):
        return wrap_vtk(self._vtk_obj.GetNextNode())
    next_node = traits.Property(_get_next_node, help=\
        """
        Get the next assembly node in the list. The node returned
        contains a pointer to a prop and a 4x4 matrix. The matrix is
        evaluated based on the preceding assembly hierarchy (i.e., the
        matrix is not necessarily as the same as the one that was added
        with add_node() because of the concatenation of matrices in the
        assembly hierarchy).
        """
    )

    def add_node(self, *args):
        """
        V.add_node(Prop, Matrix4x4)
        C++: void AddNode(Prop *p, Matrix4x4 *m)
        Convenience method adds a prop and matrix together, creating an
        assembly node transparently. The matrix pointer m may be NULL.
        Note: that matrix is the one, if any, associated with the prop.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddNode, *my_args)
        return ret

    def delete_last_node(self):
        """
        V.delete_last_node()
        C++: void DeleteLastNode()
        Delete the last assembly node in the list. This is like a stack
        pop.
        """
        ret = self._vtk_obj.DeleteLastNode()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(AssemblyPath)
        C++: void ShallowCopy(AssemblyPath *path)
        Perform a shallow copy (reference counted) on the incoming path.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AssemblyPath, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AssemblyPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AssemblyPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AssemblyPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

