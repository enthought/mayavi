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

from tvtk.tvtk_classes.marching_cubes import MarchingCubes


class DiscreteMarchingCubes(MarchingCubes):
    """
    DiscreteMarchingCubes - generate object boundaries from
    
    Superclass: MarchingCubes
    
    takes as input a volume (e.g., 3d structured point set) of
    segmentation labels and generates on output one or more models
    representing the boundaries between the specified label and the
    adjacent structures.  One or more label values must be specified to
    generate the models.  The boundary positions are always defined to be
    half-way between adjacent voxels. This filter works best with
    integral scalar values. If compute_scalars is on (the default), each
    output cell will have cell data that corresponds to the scalar value
    (segmentation label) of the corresponding cube. Note that this
    differs from MarchingCubes, which stores the scalar value as point
    data. The rationale for this difference is that cell vertices may be
    shared between multiple cells. This also means that the resultant
    polydata may be non-manifold (cell faces may be coincident). To
    further process the polydata, users should either: 1) extract cells
    that have a common scalar value using Threshold, or 2) process the
    data with filters that can handle non-manifold polydata (e.g.
    WindowedSincPolyDataFilter). Also note, Normals and Gradients are
    not computed.
    
    Caveats:
    
    This filter is specialized to volumes. If you are interested in
    contouring other types of data, use the general ContourFilter. If
    you want to contour an image (i.e., a volume slice), use
    MarchingSquares.
    
    See Also:
    
    ContourFilter SliceCubes MarchingSquares DividingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiscreteMarchingCubes, obj, update, **traits)
    
    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('compute_normals',
    'GetComputeNormals'), ('compute_scalars', 'GetComputeScalars'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_contours', 'GetNumberOfContours'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiscreteMarchingCubes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_gradients', 'compute_normals',
            'compute_scalars'], [], ['number_of_contours']),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

