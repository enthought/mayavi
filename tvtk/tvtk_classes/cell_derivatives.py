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


class CellDerivatives(DataSetAlgorithm):
    """
    CellDerivatives - compute derivatives of scalars and vectors
    
    Superclass: DataSetAlgorithm
    
    CellDerivatives is a filter that computes derivatives of scalars
    and vectors at the center of cells. You can choose to generate
    different output including the scalar gradient (a vector), computed
    tensor vorticity (a vector), gradient of input vectors (a tensor),
    and strain matrix of the input vectors (a tensor); or you may choose
    to pass data through to the output.
    
    Note that it is assumed that on input scalars and vector point data
    is available, which are then used to generate cell vectors and
    tensors. (The interpolation functions of the cells are used to
    compute the derivatives which is why point data is required.)
    
    Caveats:
    
    The computed derivatives are cell attribute data; you can convert
    them to point attribute data by using the CellDataToPointData
    filter. Note that, due to the interpolation function used (obtained
    using 1/r**2 normalized sum), the derivatives calculated for polygons
    with more than 4 vertices are inaccurate in most cases.
    
    The point data is passed through the filter to the output.
    
    See Also:
    
    VectorNorm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellDerivatives, obj, update, **traits)
    
    tensor_mode = traits.Trait('compute_gradient',
    tvtk_base.TraitRevPrefixMap({'compute_gradient': 1, 'pass_tensors': 0, 'compute_strain': 2}), help=\
        """
        Control how the filter works to generate tensor cell data. You
        can choose to pass the input cell tensors, compute the gradient
        of the input vectors, or compute the strain tensor of the vector
        gradient tensor. By default (_tensor_mode_to_compute_gradient), the
        filter will take the gradient of the vector data to construct a
        tensor.
        """
    )
    def _tensor_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorMode,
                        self.tensor_mode_)

    vector_mode = traits.Trait('compute_gradient',
    tvtk_base.TraitRevPrefixMap({'compute_gradient': 1, 'pass_vectors': 0, 'compute_vorticity': 2}), help=\
        """
        Control how the filter works to generate vector cell data. You
        can choose to pass the input cell vectors, compute the gradient
        of the input scalars, or extract the vorticity of the computed
        vector gradient tensor. By default (_vector_mode_to_compute_gradient),
        the filter will take the gradient of the input scalar data.
        """
    )
    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode_)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('vector_mode',
    'GetVectorMode'), ('tensor_mode', 'GetTensorMode'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'tensor_mode', 'vector_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellDerivatives, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellDerivatives properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['tensor_mode', 'vector_mode'], []),
            title='Edit CellDerivatives properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellDerivatives properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

