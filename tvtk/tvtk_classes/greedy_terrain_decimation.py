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


class GreedyTerrainDecimation(PolyDataAlgorithm):
    """
    GreedyTerrainDecimation - reduce height field (represented as
    image) to reduced TIN
    
    Superclass: PolyDataAlgorithm
    
    GreedyTerrainDecimation approximates a height field with a
    triangle mesh (triangulated irregular network - TIN) using a greedy
    insertion algorithm similar to that described by Garland and Heckbert
    in their paper "Fast Polygonal Approximations of Terrain and Height
    Fields" (Technical Report CMU-CS-95-181).  The input to the filter is
    a height field (represented by a image whose scalar values are
    height) and the output of the filter is polygonal data consisting of
    triangles. The number of triangles in the output is reduced in number
    as compared to a naive tessellation of the input height field. This
    filter copies point data from the input to the output for those
    points present in the output.
    
    An brief description of the algorithm is as follows. The algorithm
    uses a top-down decimation approach that initially represents the
    height field with two triangles (whose vertices are at the four
    corners of the image). These two triangles form a Delaunay
    triangulation. In an iterative fashion, the point in the image with
    the greatest error (as compared to the original height field) is
    injected into the triangulation. (Note that the single point with the
    greatest error per triangle is identified and placed into a priority
    queue. As the triangulation is modified, the errors from the deleted
    triangles are removed from the queue, error values from the new
    triangles are added.) The point whose error is at the top of the
    queue is added to the triangulaion modifying it using the standard
    incremental Delaunay point insertion (see Delaunay2D) algorithm.
    Points are repeatedly inserted until the appropriate (user-specified)
    error criterion is met.
    
    To use this filter, set the input and specify the error measure to be
    used.  The error measure options are 1) the absolute number of
    triangles to be produced; 2) a fractional reduction of the mesh
    (num_tris/max_tris) where max_tris is the largest possible number of
    triangles 2*(dims[0]-1)*(dims[1]-1); 3) an absolute measure on error
    (maximum difference in height field to reduced TIN); and 4) relative
    error (the absolute error is normalized by the diagonal of the
    bounding box of the height field).
    
    Caveats:
    
    This algorithm requires the entire input dataset to be in memory,
    hence it may not work for extremely large images. Invoking
    boundary_vertex_deletion_off will allow you to stitch together images
    with matching boundaries.
    
    The input height image is assumed to be positioned in the x-y plane
    so the scalar value is the z-coordinate, height value.
    
    See Also:
    
    DecimatePro QuadricDecimation QuadricClustering
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGreedyTerrainDecimation, obj, update, **traits)
    
    compute_normals = tvtk_base.false_bool_trait(help=\
        """
        Compute normals based on the input image. Off by default.
        """
    )
    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    boundary_vertex_deletion = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the deletion of vertices on the boundary of a mesh.
        This may limit the maximum reduction that may be achieved.
        """
    )
    def _boundary_vertex_deletion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundaryVertexDeletion,
                        self.boundary_vertex_deletion_)

    error_measure = traits.Trait('specified_reduction',
    tvtk_base.TraitRevPrefixMap({'number_of_triangles': 0, 'specified_reduction': 1, 'relative_error': 3, 'absolute_error': 2}), help=\
        """
        Specify how to terminate the algorithm: either as an absolute
        number of triangles, a relative number of triangles (normalized
        by the full resolution mesh), an absolute error (in the height
        field), or relative error (normalized by the length of the
        diagonal of the image).
        """
    )
    def _error_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErrorMeasure,
                        self.error_measure_)

    number_of_triangles = traits.Trait(1000, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of triangles to produce on output. (It is a
        good idea to make sure this is less than a tessellated mesh at
        full resolution.) You need to set this value only when the error
        measure is set to number_of_triangles.
        """
    )
    def _number_of_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTriangles,
                        self.number_of_triangles)

    reduction = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the reduction of the mesh (represented as a fraction). 
        Note that a value of 0.10 means a 10% reduction.  You need to set
        this value only when the error measure is set to
        specified_reduction.
        """
    )
    def _reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReduction,
                        self.reduction)

    absolute_error = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the absolute error of the mesh; that is, the error in
        height between the decimated mesh and the original height field. 
        You need to set this value only when the error measure is set to
        absolute_error.
        """
    )
    def _absolute_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbsoluteError,
                        self.absolute_error)

    relative_error = traits.Trait(0.01, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the relative error of the mesh; that is, the error in
        height between the decimated mesh and the original height field
        normalized by the diagonal of the image.  You need to set this
        value only when the error measure is set to relative_error.
        """
    )
    def _relative_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRelativeError,
                        self.relative_error)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('error_measure', 'GetErrorMeasure'), ('debug', 'GetDebug'),
    ('progress_text', 'GetProgressText'), ('compute_normals',
    'GetComputeNormals'), ('reference_count', 'GetReferenceCount'),
    ('reduction', 'GetReduction'), ('abort_execute', 'GetAbortExecute'),
    ('relative_error', 'GetRelativeError'), ('absolute_error',
    'GetAbsoluteError'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('number_of_triangles', 'GetNumberOfTriangles'), ('progress',
    'GetProgress'), ('boundary_vertex_deletion',
    'GetBoundaryVertexDeletion'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'boundary_vertex_deletion', 'compute_normals',
    'debug', 'global_warning_display', 'release_data_flag',
    'error_measure', 'absolute_error', 'number_of_triangles',
    'progress_text', 'reduction', 'relative_error'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GreedyTerrainDecimation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GreedyTerrainDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['boundary_vertex_deletion', 'compute_normals'],
            ['error_measure'], ['absolute_error', 'number_of_triangles',
            'reduction', 'relative_error']),
            title='Edit GreedyTerrainDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GreedyTerrainDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

