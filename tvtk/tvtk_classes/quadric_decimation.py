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


class QuadricDecimation(PolyDataAlgorithm):
    """
    QuadricDecimation - reduce the number of triangles in a mesh
    
    Superclass: PolyDataAlgorithm
    
    QuadricDecimation is a filter to reduce the number of triangles in
    a triangle mesh, forming a good approximation to the original
    geometry. The input to QuadricDecimation is a PolyData object,
    and only triangles are treated. If you desire to decimate polygonal
    meshes, first triangulate the polygons with TriangleFilter.
    
    The algorithm is based on repeated edge collapses until the requested
    mesh reduction is achieved. Edges are placed in a priority queue
    based on the "cost" to delete the edge. The cost is an approximate
    measure of error (distance to the original surface)--described by the
    so-called quadric error measure. The quadric error measure is
    associated with each vertex of the mesh and represents a matrix of
    planes incident on that vertex. The distance of the planes to the
    vertex is the error in the position of the vertex (originally the
    vertex error iz zero). As edges are deleted, the quadric error
    measure associated with the two end points of the edge are summed
    (this combines the plane equations) and an optimal collapse point can
    be computed. Edges connected to the collapse point are then
    reinserted into the queue after computing the new cost to delete
    them. The process continues until the desired reduction level is
    reached or topological constraints prevent further reduction. Note
    that this basic algorithm can be extended to higher dimensions by
    taking into account variation in attributes (i.e., scalars, vectors,
    and so on).
    
    This paper is based on the work of Garland and Heckbert who first
    presented the quadric error measure at Siggraph '97 "Surface
    Simplification Using Quadric Error Metrics". For details of the
    algorithm Michael Garland's Ph.D. thesis is also recommended. Hughues
    Hoppe's Vis '99 paper, "New Quadric Metric for Simplifying Meshes
    with Appearance Attributes" is also a good take on the subject
    especially as it pertains to the error metric applied to attributes.
    
    Thanks:
    
    Thanks to Bradley Lowekamp of the National Library of Medicine/NIH
    for contributing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadricDecimation, obj, update, **traits)
    
    normals_attribute = tvtk_base.true_bool_trait(help=\
        """
        If attribute errors are to be included in the metric (i.e.,
        attribute_error_metric is on), then the following flags control
        which attributes are to be included in the error calculation. By
        default all of these are on.
        """
    )
    def _normals_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsAttribute,
                        self.normals_attribute_)

    t_coords_attribute = tvtk_base.true_bool_trait(help=\
        """
        If attribute errors are to be included in the metric (i.e.,
        attribute_error_metric is on), then the following flags control
        which attributes are to be included in the error calculation. By
        default all of these are on.
        """
    )
    def _t_coords_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordsAttribute,
                        self.t_coords_attribute_)

    tensors_attribute = tvtk_base.true_bool_trait(help=\
        """
        If attribute errors are to be included in the metric (i.e.,
        attribute_error_metric is on), then the following flags control
        which attributes are to be included in the error calculation. By
        default all of these are on.
        """
    )
    def _tensors_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorsAttribute,
                        self.tensors_attribute_)

    attribute_error_metric = tvtk_base.false_bool_trait(help=\
        """
        Decide whether to include data attributes in the error metric. If
        off, then only geometric error is used to control the decimation.
        By default the attribute errors are off.
        """
    )
    def _attribute_error_metric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeErrorMetric,
                        self.attribute_error_metric_)

    vectors_attribute = tvtk_base.true_bool_trait(help=\
        """
        If attribute errors are to be included in the metric (i.e.,
        attribute_error_metric is on), then the following flags control
        which attributes are to be included in the error calculation. By
        default all of these are on.
        """
    )
    def _vectors_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorsAttribute,
                        self.vectors_attribute_)

    scalars_attribute = tvtk_base.true_bool_trait(help=\
        """
        If attribute errors are to be included in the metric (i.e.,
        attribute_error_metric is on), then the following flags control
        which attributes are to be included in the error calculation. By
        default all of these are on.
        """
    )
    def _scalars_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsAttribute,
                        self.scalars_attribute_)

    scalars_weight = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling weight contribution of the attribute. These
        values are used to weight the contribution of the attributes
        towards the error metric.
        """
    )
    def _scalars_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsWeight,
                        self.scalars_weight)

    vectors_weight = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling weight contribution of the attribute. These
        values are used to weight the contribution of the attributes
        towards the error metric.
        """
    )
    def _vectors_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorsWeight,
                        self.vectors_weight)

    target_reduction = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the desired reduction (expressed as a fraction of the
        original number of triangles). The actual reduction may be less
        depending on triangulation and topological constraints.
        """
    )
    def _target_reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetReduction,
                        self.target_reduction)

    t_coords_weight = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling weight contribution of the attribute. These
        values are used to weight the contribution of the attributes
        towards the error metric.
        """
    )
    def _t_coords_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordsWeight,
                        self.t_coords_weight)

    normals_weight = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling weight contribution of the attribute. These
        values are used to weight the contribution of the attributes
        towards the error metric.
        """
    )
    def _normals_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsWeight,
                        self.normals_weight)

    tensors_weight = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling weight contribution of the attribute. These
        values are used to weight the contribution of the attributes
        towards the error metric.
        """
    )
    def _tensors_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorsWeight,
                        self.tensors_weight)

    def _get_actual_reduction(self):
        return self._vtk_obj.GetActualReduction()
    actual_reduction = traits.Property(_get_actual_reduction, help=\
        """
        Get the actual reduction. This value is only valid after the
        filter has executed.
        """
    )

    _updateable_traits_ = \
    (('scalars_attribute', 'GetScalarsAttribute'), ('scalars_weight',
    'GetScalarsWeight'), ('target_reduction', 'GetTargetReduction'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('tensors_weight', 'GetTensorsWeight'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('tensors_attribute',
    'GetTensorsAttribute'), ('t_coords_weight', 'GetTCoordsWeight'),
    ('attribute_error_metric', 'GetAttributeErrorMetric'),
    ('vectors_attribute', 'GetVectorsAttribute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('vectors_weight', 'GetVectorsWeight'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('normals_attribute', 'GetNormalsAttribute'), ('abort_execute',
    'GetAbortExecute'), ('t_coords_attribute', 'GetTCoordsAttribute'),
    ('normals_weight', 'GetNormalsWeight'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'attribute_error_metric', 'debug',
    'global_warning_display', 'normals_attribute', 'release_data_flag',
    'scalars_attribute', 't_coords_attribute', 'tensors_attribute',
    'vectors_attribute', 'normals_weight', 'progress_text',
    'scalars_weight', 't_coords_weight', 'target_reduction',
    'tensors_weight', 'vectors_weight'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuadricDecimation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['attribute_error_metric', 'normals_attribute',
            'scalars_attribute', 't_coords_attribute', 'tensors_attribute',
            'vectors_attribute'], [], ['normals_weight', 'scalars_weight',
            't_coords_weight', 'target_reduction', 'tensors_weight',
            'vectors_weight']),
            title='Edit QuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

