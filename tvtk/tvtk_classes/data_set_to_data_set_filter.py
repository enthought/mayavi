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

from tvtk.tvtk_classes.data_set_source import DataSetSource


class DataSetToDataSetFilter(DataSetSource):
    """
    DataSetToDataSetFilter - abstract filter class
    
    Superclass: DataSetSource
    
    DataSetToDataSetFilter is an abstract filter class. Subclasses of
    DataSetToDataSetFilter take a dataset as input and create a
    dataset as output. The form of the input geometry is not changed in
    these filters, only the point attributes (e.g. scalars, vectors,
    etc.).
    
    This is an abstract filter type. What that means is that the output
    of the filter is an abstract type (i.e., DataSet), no matter what
    the input of the filter is. This can cause problems connecting
    together filters due to the change in dataset type. (For example, in
    a series of filters processing PolyData, when a
    DataSetToDataSetFilter or subclass is introduced into the
    pipeline, if the filter downstream of it takes PolyData as input,
    the pipeline connection cannot be made.) To get around this problem,
    use one of the convenience methods to return a concrete type (e.g.,
    GetPolyDataOutput(), get_structured_points_output(), etc.).
    
    See Also:
    
    BrownianPoints ProbeFilter ThresholdTextureCoords Dicer
    ElevationFilter ImplicitTextureCoords TextureMapToPlane
    VectorDot VectorNorm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetToDataSetFilter, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Get the input data or filter.
        """
    )

    def _get_poly_data_output(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataOutput())
    poly_data_output = traits.Property(_get_poly_data_output, help=\
        """
        Get the output as PolyData.
        """
    )

    def _get_rectilinear_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearGridOutput())
    rectilinear_grid_output = traits.Property(_get_rectilinear_grid_output, help=\
        """
        Get the output as RectilinearGrid.
        """
    )

    def _get_structured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredGridOutput())
    structured_grid_output = traits.Property(_get_structured_grid_output, help=\
        """
        Get the output as StructuredGrid.
        """
    )

    def _get_structured_points_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredPointsOutput())
    structured_points_output = traits.Property(_get_structured_points_output, help=\
        """
        Get the output as StructuredPoints.
        """
    )

    def _get_unstructured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGridOutput())
    unstructured_grid_output = traits.Property(_get_unstructured_grid_output, help=\
        """
        Get the output as UnstructuredGrid.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetToDataSetFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['release_data_flag']),
            title='Edit DataSetToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

