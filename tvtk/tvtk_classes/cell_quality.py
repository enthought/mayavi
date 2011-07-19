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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class CellQuality(DataSetAlgorithm):
    """
    CellQuality - Calculate functions of quality of the elements
    
    Superclass: DataSetAlgorithm
    
    CellQuality computes one or more functions of (geometric) quality
    for each cell of a mesh.  The per-cell quality is added to the mesh's
    cell data, in an array named "Quality." Cell types not supported by
    this filter or undefined quality of supported cell types will have an
    entry of 0.
    
    Caveats:
    
    Most quadrilateral quality functions are intended for planar
    quadrilaterals only.  The minimal angle is not, strictly speaking, a
    quality function, but it is provided because of its useage by many
    authors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellQuality, obj, update, **traits)
    
    quality_measure = traits.Trait('area',
    tvtk_base.TraitRevPrefixMap({'aspect_frobenius': 3, 'aspect_beta': 2, 'distortion': 10, 'shape': 23, 'radius_ratio': 20, 'shear_and_size': 26, 'relative_size_squared': 21, 'shape_and_size': 24, 'taper': 29, 'med_aspect_frobenius': 16, 'area': 1, 'stretch': 28, 'skew': 27, 'warpage': 31, 'min_angle': 17, 'jacobian': 12, 'shear': 25, 'max_edge_ratio': 15, 'diagonal': 8, 'volume': 30, 'scaled_jacobian': 22, 'aspect_gamma': 4, 'condition': 7, 'max_angle': 13, 'oddy': 19, 'collapse_ratio': 6, 'max_aspect_frobenius': 14, 'aspect_ratio': 5, 'dimension': 9}), help=\
        """
        Set/Get the particular estimator used to function the quality of
        all supported geometries. For qualities that are not defined for
        certain geometries, later program logic ensures that
        cell_quality_none static function will be used so that a predefined
        value is returned for the request. There is no default value for
        this call and valid values include all possible qualities
        supported by this class.
        """
    )
    def _quality_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQualityMeasure,
                        self.quality_measure_)

    unsupported_geometry = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the return value for unsupported geometry. Unsupported
        geometry are geometries that are not supported by this filter
        currently, future implementation might include support for them.
        The defalut value for unsupported_geometry is -1.
        """
    )
    def _unsupported_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnsupportedGeometry,
                        self.unsupported_geometry)

    undefined_quality = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the return value for undefined quality. Undefined quality
        are qualities that could be addressed by this filter but is not
        well defined for the particular geometry of cell in question,
        e.g. a volume query for a triangle. Undefined quality will always
        be undefined. The default value for undefined_quality is -1.
        """
    )
    def _undefined_quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUndefinedQuality,
                        self.undefined_quality)

    def pixel_area(self, *args):
        """
        V.pixel_area(Cell) -> float
        C++: double PixelArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PixelArea, *my_args)
        return ret

    def polygon_area(self, *args):
        """
        V.polygon_area(Cell) -> float
        C++: double PolygonArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PolygonArea, *my_args)
        return ret

    def triangle_strip_area(self, *args):
        """
        V.triangle_strip_area(Cell) -> float
        C++: double TriangleStripArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleStripArea, *my_args)
        return ret

    _updateable_traits_ = \
    (('unsupported_geometry', 'GetUnsupportedGeometry'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('quality_measure',
    'GetQualityMeasure'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('undefined_quality', 'GetUndefinedQuality'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'quality_measure', 'progress_text',
    'undefined_quality', 'unsupported_geometry'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellQuality, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['quality_measure'], ['undefined_quality',
            'unsupported_geometry']),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

