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


class ImageMarchingCubes(PolyDataAlgorithm):
    """
    ImageMarchingCubes - generate isosurface(s) from volume/images
    
    Superclass: PolyDataAlgorithm
    
    ImageMarchingCubes is a filter that takes as input images (e.g.,
    3d image region) and generates on output one or more isosurfaces. One
    or more contour values must be specified to generate the isosurfaces.
    Alternatively, you can specify a min/max scalar range and the number
    of contours to generate a series of evenly spaced contour values.
    This filter can stream, so that the entire volume need not be loaded
    at once.  Streaming is controlled using the instance variable
    input_memory_limit, which has units KBytes.
    
    Caveats:
    
    This filter is specialized to volumes. If you are interested in
    contouring other types of data, use the general ContourFilter. If
    you want to contour an image (i.e., a volume slice), use
    MarchingSquares.
    
    See Also:
    
    ContourFilter SliceCubes MarchingSquares
    SynchronizedTemplates3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMarchingCubes, obj, update, **traits)
    
    compute_gradients = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the computation of gradients. Gradient computation is
        fairly expensive in both time and storage. Note that if
        compute_normals is on, gradients will have to be calculated, but
        will not be stored in the output dataset. If the output data will
        be processed by filters that modify topology or geometry, it may
        be wise to turn Normals and Gradients off.
        """
    )
    def _compute_gradients_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradients,
                        self.compute_gradients_)

    compute_normals = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the computation of normals. Normal computation is fairly
        expensive in both time and storage. If the output data will be
        processed by filters that modify topology or geometry, it may be
        wise to turn Normals and Gradients off.
        """
    )
    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    compute_scalars = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the computation of scalars.
        """
    )
    def _compute_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeScalars,
                        self.compute_scalars_)

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Methods to set contour values
        """
    )
    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    input_memory_limit = traits.Int(10240, enter_set=True, auto_set=False, help=\
        """
        The input_memory_limit determines the chunk size (the number of
        slices requested at each iteration).  The units of this limit is
        kilo_bytes. For now, only the Z axis is split.
        """
    )
    def _input_memory_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputMemoryLimit,
                        self.input_memory_limit)

    def get_locator_point(self, *args):
        """
        V.get_locator_point(int, int, int) -> int
        C++: int GetLocatorPoint(int cellX, int cellY, int edge)"""
        ret = self._wrap_call(self._vtk_obj.GetLocatorPoint, *args)
        return ret

    def add_locator_point(self, *args):
        """
        V.add_locator_point(int, int, int, int)
        C++: void AddLocatorPoint(int cellX, int cellY, int edge,
            int ptId)"""
        ret = self._wrap_call(self._vtk_obj.AddLocatorPoint, *args)
        return ret

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    def increment_locator_z(self):
        """
        V.increment_locator_z()
        C++: void IncrementLocatorZ()"""
        ret = self._vtk_obj.IncrementLocatorZ()
        return ret
        

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('compute_normals',
    'GetComputeNormals'), ('compute_scalars', 'GetComputeScalars'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_contours', 'GetNumberOfContours'), ('input_memory_limit',
    'GetInputMemoryLimit'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'global_warning_display',
    'release_data_flag', 'input_memory_limit', 'number_of_contours',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMarchingCubes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_gradients', 'compute_normals',
            'compute_scalars'], [], ['input_memory_limit', 'number_of_contours']),
            title='Edit ImageMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

