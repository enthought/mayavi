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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class ImplicitSelectionLoop(ImplicitFunction):
    """
    ImplicitSelectionLoop - implicit function for a selection loop
    
    Superclass: ImplicitFunction
    
    ImplicitSelectionLoop computes the implicit function value and
    function gradient for a irregular, cylinder-like object whose cross
    section is defined by a set of points forming a loop. The loop need
    not be convex nor its points coplanar. However, the loop must be
    non-self-intersecting when projected onto the plane defined by the
    accumulated cross product around the loop (i.e., the axis of the
    loop). (Alternatively, you can specify the normal to use.)
    
    The following procedure is used to compute the implicit function
    value for a point x. Each point of the loop is first projected onto
    the plane defined by the loop normal. This forms a polygon. Then, to
    evaluate the implicit function value, inside/outside tests are used
    to determine if x is inside the polygon, and the distance to the loop
    boundary is computed (negative values are inside the loop).
    
    One example application of this implicit function class is to draw a
    loop on the surface of a mesh, and use the loop to clip or extract
    cells from within the loop. Remember, the selection loop is
    "infinite" in length, you can use a plane (in boolean combination) to
    cap the extent of the selection loop. Another trick is to use a
    connectivity filter to extract the closest region to a given point
    (i.e., one of the points used to define the selection loop).
    
    See Also:
    
    ImplicitFunction ImplicitBoolean ExtractGeometry
    ClipPolyData ConnectivityFilter PolyDataConnectivityFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitSelectionLoop, obj, update, **traits)
    
    automatic_normal_generation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off automatic normal generation. By default, the normal
        is computed from the accumulated cross product of the edges. You
        can also specify the normal to use.
        """
    )
    def _automatic_normal_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticNormalGeneration,
                        self.automatic_normal_generation_)

    def _get_loop(self):
        return wrap_vtk(self._vtk_obj.GetLoop())
    def _set_loop(self, arg):
        old_val = self._get_loop()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetLoop,
                        my_arg[0])
        self.trait_property_changed('loop', old_val, arg)
    loop = traits.Property(_get_loop, _set_loop, help=\
        """
        Set/Get the array of point coordinates defining the loop. There
        must be at least three points used to define a loop.
        """
    )

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('automatic_normal_generation', 'GetAutomaticNormalGeneration'),
    ('normal', 'GetNormal'))
    
    _full_traitnames_list_ = \
    (['automatic_normal_generation', 'debug', 'global_warning_display',
    'normal'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitSelectionLoop, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitSelectionLoop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_normal_generation'], [], ['normal']),
            title='Edit ImplicitSelectionLoop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitSelectionLoop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

