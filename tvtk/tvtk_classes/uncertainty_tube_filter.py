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


class UncertaintyTubeFilter(PolyDataAlgorithm):
    """
    UncertaintyTubeFilter - generate uncertainty tubes along a polyline
    
    Superclass: PolyDataAlgorithm
    
    UncertaintyTubeFilter is a filter that generates ellipsoidal (in
    cross section) tubes that follows a polyline. The input is a
    PolyData with polylines that have associated vector point data.
    The vector data represents the uncertainty of the polyline in the
    x-y-z directions.
    
    Caveats:
    
    The vector uncertainty values define an axis-aligned ellipsoid at
    each polyline point. The uncertainty tubes can be envisioned as the
    interpolation of these ellipsoids between the points defining the
    polyline (or rather, the interpolation of the cross section of the
    ellipsoids alog the polyline).
    
    See Also:
    
    TensorGlyph Streamer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUncertaintyTubeFilter, obj, update, **traits)
    
    number_of_sides = traits.Trait(12, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set / get the number of sides for the tube. At a minimum, the
        number of sides is 3.
        """
    )
    def _number_of_sides_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSides,
                        self.number_of_sides)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_sides', 'GetNumberOfSides'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_sides', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UncertaintyTubeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UncertaintyTubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_sides']),
            title='Edit UncertaintyTubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UncertaintyTubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

