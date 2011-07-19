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


class GradientFilter(DataSetAlgorithm):
    """
    GradientFilter - A general filter for gradient estimation.
    
    Superclass: DataSetAlgorithm
    
    Estimates the gradient of a field in a data set.  The gradient
    calculation is dependent on the input dataset type.  The created
    gradient array is of the same type as the array it is calculated from
    (e.g. point data or cell data) as well as data type (e.g. float,
    double).  At the boundary the gradient is not central differencing. 
    The output array has 3*number of components of the input data array. 
    The ordering for the output tuple will be {du/dx, du/dy, du/dz,
    dv/dx, dv/dy, dv/dz, dw/dx, dw/dy, dw/dz} for an input array {u, v,
    w}.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGradientFilter, obj, update, **traits)
    
    compute_vorticity = tvtk_base.false_bool_trait(help=\
        """
        Set the resultant array to be vorticity/curl of the input array. 
        The input array must have 3 components.
        """
    )
    def _compute_vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeVorticity,
                        self.compute_vorticity_)

    faster_approximation = tvtk_base.false_bool_trait(help=\
        """
        When this flag is on (default is off), the gradient filter will
        provide a less accurate (but close) algorithm that performs fewer
        derivative calculations (and is therefore faster).  The error
        contains some smoothing of the output data and some possible
        errors on the boundary.  This parameter has no effect when
        performing the gradient of cell data. This only applies if the
        input grid is a UnstructuredGrid or a PolyData.
        """
    )
    def _faster_approximation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFasterApproximation,
                        self.faster_approximation_)

    result_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the name of the resulting array to create.  If NULL (the
        default) then the output array will be named "Gradients".
        """
    )
    def _result_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResultArrayName,
                        self.result_array_name)

    def set_input_scalars(self, *args):
        """
        V.set_input_scalars(int, string)
        C++: virtual void SetInputScalars(int fieldAssociation,
            const char *name)
        V.set_input_scalars(int, int)
        C++: virtual void SetInputScalars(int fieldAssociation,
            int fieldAttributeType)
        These are basically a convenience method that calls
        set_input_array_to_process to set the array used as the input
        scalars.  The field_association comes from the
        DataObject::FieldAssocations enum.  The field_attribute_type
        comes from the DataSetAttributes::AttributeTypes enum.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputScalars, *args)
        return ret

    _updateable_traits_ = \
    (('faster_approximation', 'GetFasterApproximation'),
    ('result_array_name', 'GetResultArrayName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('compute_vorticity',
    'GetComputeVorticity'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_vorticity', 'debug',
    'faster_approximation', 'global_warning_display', 'release_data_flag',
    'progress_text', 'result_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GradientFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_vorticity', 'faster_approximation'], [],
            ['result_array_name']),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

