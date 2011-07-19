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


class ImageDataGeometryFilter(PolyDataAlgorithm):
    """
    ImageDataGeometryFilter - extract geometry for structured points
    
    Superclass: PolyDataAlgorithm
    
    ImageDataGeometryFilter is a filter that extracts geometry from a
    structured points dataset. By specifying appropriate i-j-k indices
    (via the "Extent" instance variable), it is possible to extract a
    point, a line, a plane (i.e., image), or a "volume" from dataset.
    (Since the output is of type polydata, the volume is actually a (n x
    m x o) region of points.)
    
    The extent specification is zero-offset. That is, the first k-plane
    in a 50x50x50 volume is given by (0,49, 0,49, 0,0).
    
    Caveats:
    
    If you don't know the dimensions of the input dataset, you can use a
    large number to specify extent (the number will be clamped
    appropriately). For example, if the dataset dimensions are 50x50x50,
    and you want a the fifth k-plane, you can use the extents (0,100,
    0,100, 4,4). The 100 will automatically be clamped to 49.
    
    See Also:
    
    GeometryFilter StructuredGridSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDataGeometryFilter, obj, update, **traits)
    
    output_triangles = tvtk_base.false_bool_trait(help=\
        """
        Set output_triangles to true if you wish to generate triangles
        instead of quads when extracting cells from 2d imagedata
        Currently this functionality is only implemented for 2d imagedata
        """
    )
    def _output_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputTriangles,
                        self.output_triangles_)

    threshold_cells = tvtk_base.false_bool_trait(help=\
        """
        Set threshold_cells to true if you wish to skip any voxel/pixels
        which have scalar values less than the specified threshold.
        Currently this functionality is only implemented for 2d imagedata
        """
    )
    def _threshold_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThresholdCells,
                        self.threshold_cells_)

    threshold_value = tvtk_base.false_bool_trait(help=\
        """
        Set threshold_value to the scalar value by which to threshhold
        cells when extracting geometry when threshold_cells is true. Cells
        with scalar values greater than the threshold will be output.
        """
    )
    def _threshold_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThresholdValue,
                        self.threshold_value_)

    def set_extent(self, *args):
        """
        V.set_extent([int, int, int, int, int, int])
        C++: void SetExtent(int extent[6])
        V.set_extent(int, int, int, int, int, int)
        C++: void SetExtent(int iMin, int iMax, int jMin, int jMax,
            int kMin, int kMax)
        Set / get the extent (imin,imax, jmin,jmax, kmin,kmax) indices.
        """
        ret = self._wrap_call(self._vtk_obj.SetExtent, *args)
        return ret

    _updateable_traits_ = \
    (('threshold_value', 'GetThresholdValue'), ('output_triangles',
    'GetOutputTriangles'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'), ('threshold_cells',
    'GetThresholdCells'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'output_triangles', 'release_data_flag', 'threshold_cells',
    'threshold_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDataGeometryFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['output_triangles', 'threshold_cells',
            'threshold_value'], [], []),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

