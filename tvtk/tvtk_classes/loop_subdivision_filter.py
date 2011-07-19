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

from tvtk.tvtk_classes.approximating_subdivision_filter import ApproximatingSubdivisionFilter


class LoopSubdivisionFilter(ApproximatingSubdivisionFilter):
    """
    LoopSubdivisionFilter - generate a subdivision surface using the
    Loop Scheme
    
    Superclass: ApproximatingSubdivisionFilter
    
    LoopSubdivisionFilter is an approximating subdivision scheme that
    creates four new triangles for each triangle in the mesh. The user
    can specify the number_of_subdivisions. Loop's subdivision scheme is
    described in: Loop, C., "Smooth Subdivision surfaces based on
    triangles,", Masters Thesis, University of Utah, August 1987. For a
    nice summary of the technique see, Hoppe, H., et. al, "Piecewise
    Smooth Surface Reconstruction,:, Proceedings of Siggraph 94 (Orlando,
    Florida, July 24-29, 1994). In COmputer Graphics Proceedings, Annual
    COnference Series, 1994, ACM SIGGRAPH, pp. 295-302. <P> The filter
    only operates on triangles. Users should use the TriangleFilter to
    triangulate meshes that contain polygons or triangle strips. <P> The
    filter approximates point data using the same scheme. New triangles
    create at a subdivision step will have the cell data of their parent
    cell.
    
    See Also:
    
    ApproximatingSubdivisionFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLoopSubdivisionFilter, obj, update, **traits)
    
    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_subdivisions',
    'GetNumberOfSubdivisions'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_subdivisions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LoopSubdivisionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LoopSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_subdivisions']),
            title='Edit LoopSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LoopSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

