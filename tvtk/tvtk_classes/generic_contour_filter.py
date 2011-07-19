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


class GenericContourFilter(PolyDataAlgorithm):
    """
    GenericContourFilter - generate isocontours from input dataset
    
    Superclass: PolyDataAlgorithm
    
    GenericContourFilter is a filter that takes as input any (generic)
    dataset and generates on output isosurfaces and/or isolines. The
    exact form of the output depends upon the dimensionality of the input
    data. Data consisting of 3d cells will generate isosurfaces, data
    consisting of 2d cells will generate isolines, and data with 1d or 0d
    cells will generate isopoints. Combinations of output type are
    possible if the input dimension is mixed.
    
    To use this filter you must specify one or more contour values. You
    can either use the method set_value() to specify each contour value,
    or use generate_values() to generate a series of evenly spaced
    contours. You can use compute_normals_on to compute the normals without
    the need of a PolyDataNormals
    
    This filter has been implemented to operate on generic datasets,
    rather than the typical DataSet (and subclasses).
    GenericDataSet is a more complex cousin of DataSet, typically
    consisting of nonlinear, higher-order cells. To process this type of
    data, generic cells are automatically tessellated into linear cells
    prior to isocontouring.
    
    See Also:
    
    ContourFilter GenericDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericContourFilter, obj, update, **traits)
    
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
        C++: void SetValue(int i, float value)
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

    def _get_input_scalars_selection(self):
        return self._vtk_obj.GetInputScalarsSelection()
    input_scalars_selection = traits.Property(_get_input_scalars_selection, help=\
        """
        If you want to contour by an arbitrary scalar attribute, then set
        its name here. By default this in NULL and the filter will use
        the active scalar array.
        """
    )

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

    def select_input_scalars(self, *args):
        """
        V.select_input_scalars(string)
        C++: virtual void SelectInputScalars(const char *fieldName)
        If you want to contour by an arbitrary scalar attribute, then set
        its name here. By default this in NULL and the filter will use
        the active scalar array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectInputScalars, *args)
        return ret

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
            return super(GenericContourFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_gradients', 'compute_normals',
            'compute_scalars'], [], ['number_of_contours']),
            title='Edit GenericContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

