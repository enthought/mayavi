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

from tvtk.tvtk_classes.cell3d import Cell3D


class ConvexPointSet(Cell3D):
    """
    ConvexPointSet - a 3d cell defined by a set of convex points
    
    Superclass: Cell3D
    
    ConvexPointSet is a concrete implementation that represents a 3d
    cell defined by a convex set of points. An example of such a cell is
    an octant (from an octree). ConvexPointSet uses the ordered
    triangulations approach (vtk_ordered_triangulator) to create
    triangulations guaranteed to be compatible across shared faces. This
    allows a general approach to processing complex, convex cell types.
    
    See Also:
    
    Hexahedron Pyramid Tetra Voxel Wedge
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConvexPointSet, obj, update, **traits)
    
    def has_fixed_topology(self):
        """
        V.has_fixed_topology() -> int
        C++: virtual int HasFixedTopology()
        See Cell3D API for description of this method.
        """
        ret = self._vtk_obj.HasFixedTopology()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('merge_tolerance', 'GetMergeTolerance'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConvexPointSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConvexPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['merge_tolerance']),
            title='Edit ConvexPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConvexPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

