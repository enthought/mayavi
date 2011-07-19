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


class DecimatePolylineFilter(PolyDataAlgorithm):
    """
    DecimatePolylineFilter - reduce the number of lines in a polyline
    
    Superclass: PolyDataAlgorithm
    
    DecimatePolylineFilter is a filter to reduce the number of lines
    in a polyline. The algorithm functions by evaluating an error metric
    for each vertex (i.e., the distance of the vertex to a line defined
    from the two vertices on either side of the vertex). Then, these
    vertices are placed into a priority queue, and those with larger
    errors are deleted first. The decimation continues until the target
    reduction is reached.
    
    Caveats:
    
    This algorithm is a very simple implementation that overlooks some
    potential complexities. First, if a vertex is multiply connected,
    meaning that it is used by multiple polylines, then the extra
    topological constraints are ignored. Second, the error is not updated
    as vertices are deleted (similar to iteratively computing a quadric
    error metric). Thus, once calculated, the error is used to determine
    which vertices are removed. This can produce less than optimal
    results.
    
    See Also:
    
    Decimate DecimateProp QuadricClustering QuadricDecimation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDecimatePolylineFilter, obj, update, **traits)
    
    target_reduction = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the desired reduction in the total number of polygons
        (e.g., if target_reduction is set to 0.9, this filter will try to
        reduce the data set to 10% of its original size).
        """
    )
    def _target_reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetReduction,
                        self.target_reduction)

    _updateable_traits_ = \
    (('target_reduction', 'GetTargetReduction'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'target_reduction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DecimatePolylineFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['target_reduction']),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

