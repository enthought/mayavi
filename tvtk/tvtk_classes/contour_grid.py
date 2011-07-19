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


class ContourGrid(PolyDataAlgorithm):
    """
    ContourGrid - generate isosurfaces/isolines from scalar values
    (specialized for unstructured grids)
    
    Superclass: PolyDataAlgorithm
    
    ContourGrid is a filter that takes as input datasets of type
    UnstructuredGrid and generates on output isosurfaces and/or
    isolines. The exact form of the output depends upon the
    dimensionality of the input data.  Data consisting of 3d cells will
    generate isosurfaces, data consisting of 2d cells will generate
    isolines, and data with 1d or 0d cells will generate isopoints.
    Combinations of output type are possible if the input dimension is
    mixed.
    
    To use this filter you must specify one or more contour values. You
    can either use the method set_value() to specify each contour value,
    or use generate_values() to generate a series of evenly spaced
    contours. It is also possible to accelerate the operation of this
    filter (at the cost of extra memory) by using a ScalarTree. A
    scalar tree is used to quickly locate cells that contain a contour
    surface. This is especially effective if multiple contours are being
    extracted. If you want to use a scalar tree, invoke the method
    use_scalar_tree_on().
    
    Caveats:
    
    For unstructured data or structured grids, normals and gradients are
    not computed. Use PolyDataNormals to compute the surface normals
    of the resulting isosurface.
    
    See Also:
    
    MarchingContourFilter KitwareContourFilter MarchingCubes
    SliceCubes DividingCubes MarchingSquares
    ImageMarchingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContourGrid, obj, update, **traits)
    
    use_scalar_tree = tvtk_base.false_bool_trait(help=\
        """
        Enable the use of a scalar tree to accelerate contour extraction.
        """
    )
    def _use_scalar_tree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseScalarTree,
                        self.use_scalar_tree_)

    compute_gradients = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the computation of gradients. Gradient computation is
        fairly expensive in both time and storage. Note that if
        compute_normals is on, gradients will have to be calculated, but
        will not be stored in the output dataset.  If the output data
        will be processed by filters that modify topology or geometry, it
        may be wise to turn Normals and Gradients off.
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

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default, an
        instance of MergePoints is used.
        """
    )

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Methods to set / get contour values.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Methods to set / get contour values.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Methods to set / get contour values.
        """
    )
    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Methods to set / get contour values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('use_scalar_tree', 'GetUseScalarTree'), ('progress_text',
    'GetProgressText'), ('compute_normals', 'GetComputeNormals'),
    ('compute_scalars', 'GetComputeScalars'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_contours',
    'GetNumberOfContours'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'global_warning_display',
    'release_data_flag', 'use_scalar_tree', 'number_of_contours',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContourGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContourGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_gradients', 'compute_normals',
            'compute_scalars', 'use_scalar_tree'], [], ['number_of_contours']),
            title='Edit ContourGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContourGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

