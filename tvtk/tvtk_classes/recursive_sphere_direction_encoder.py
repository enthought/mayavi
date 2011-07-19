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

from tvtk.tvtk_classes.direction_encoder import DirectionEncoder


class RecursiveSphereDirectionEncoder(DirectionEncoder):
    """
    RecursiveSphereDirectionEncoder - A direction encoder based on the
    recursive subdivision of an octahedron
    
    Superclass: DirectionEncoder
    
    RecursiveSphereDirectionEncoder is a direction encoder which uses
    the vertices of a recursive subdivision of an octahedron (with the
    vertices pushed out onto the surface of an enclosing sphere) to
    encode directions into a two byte value.
    
    See Also:
    
    DirectionEncoder
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRecursiveSphereDirectionEncoder, obj, update, **traits)
    
    recursion_depth = traits.Trait(6, traits.Range(0, 6, enter_set=True, auto_set=False), help=\
        """
        Set / Get the recursion depth for the subdivision. This indicates
        how many time one triangle on the initial 8-sided sphere model is
        replaced by four triangles formed by connecting triangle edge
        midpoints. A recursion level of 0 yields 8 triangles with 6
        unique vertices. The normals are the vectors from the sphere
        center through the vertices. The number of directions will be 11
        since the four normals with 0 z values will be duplicated in the
        table - once with +0 values and the other time with -0 values,
        and an addition index will be used to represent the (0,0,0)
        normal. If we instead choose a recursion level of 6 (the maximum
        that can fit within 2 bytes) the number of directions is 16643,
        with 16386 unique directions and a zero normal.
        """
    )
    def _recursion_depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRecursionDepth,
                        self.recursion_depth)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('recursion_depth',
    'GetRecursionDepth'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'recursion_depth'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RecursiveSphereDirectionEncoder, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RecursiveSphereDirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['recursion_depth']),
            title='Edit RecursiveSphereDirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RecursiveSphereDirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

