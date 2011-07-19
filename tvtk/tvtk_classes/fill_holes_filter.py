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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class FillHolesFilter(PolyDataAlgorithm):
    """
    FillHolesFilter - identify and fill holes in meshes
    
    Superclass: PolyDataAlgorithm
    
    FillHolesFilter is a filter that identifies and fills holes in
    input PolyData meshes. Holes are identified by locating boundary
    edges, linking them together into loops, and then triangulating the
    resulting loops. Note that you can specify an approximate limit to
    the size of the hole that can be filled.
    
    Caveats:
    
    Note that any mesh with boundary edges by definition has a
    topological hole. This even includes a reactangular grid (e.g., the
    output of PlaneSource). In such situations, if the outer hole is
    filled, retriangulation of the hole will cause geometric overlap of
    the mesh. This can be prevented by using the hole size instance
    variable to prevent the larger holes from being triangulated.
    
    Note this filter only operates on polygons and triangle strips.
    Vertices and polylines are passed through untouched.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFillHolesFilter, obj, update, **traits)
    
    hole_size = traits.Trait(1.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum hole size to fill. This is represented as a
        radius to the bounding circumsphere containing the hole.  Note
        that this is an approximate area; the actual area cannot be
        computed without first triangulating the hole.
        """
    )
    def _hole_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHoleSize,
                        self.hole_size)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('hole_size',
    'GetHoleSize'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'hole_size', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FillHolesFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FillHolesFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['hole_size']),
            title='Edit FillHolesFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FillHolesFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

