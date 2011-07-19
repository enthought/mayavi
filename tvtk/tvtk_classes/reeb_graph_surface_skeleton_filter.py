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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ReebGraphSurfaceSkeletonFilter(DataObjectAlgorithm):
    """
    ReebGraphSurfaceSkeletonFilter - compute a skeletal embedding of
    the
    
    Superclass: DataObjectAlgorithm
    
    The filter takes a PolyData as an input (port 0), along with a
    ReebGraph (port 1). The filter samples each arc of the Reeb graph
    and embeds the samples on the barycenter of the corresponding field
    contour. The number of (evenly distributed) arc samples  can be
    defined with set_number_of_samples() (default value: 10). The skeleton
    can be optionally smoothed with set_number_of_smoothing_iterations()
    (default value: 10). The filter will first try to pull as a scalar
    field the DataArray with Id '_field_id' of the PolyData, see
    set_field_id() (default: 0). The filter will abort if this field does
    not exist.
    
    The filter outputs a Table of points (double[3]). Each column
    contains the samples (sorted by function value) of the corresponding
    arc. The first and the last entry of the column corresponds to the
    critical nodes at the extremity of the arc (each column has
    number_of_samples + 2 entries).
    
    The skeleton can be rendered by linking the samples with geometrical
    primitives (for instance, spheres at critical nodes and cylinders
    between intermediary samples, see
    graphics/_testing/_cxx/_test_reeb_graph.cxx).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReebGraphSurfaceSkeletonFilter, obj, update, **traits)
    
    number_of_samples = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the number of samples along each arc of the Reeb graph
        Default value: 5
        """
    )
    def _number_of_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSamples,
                        self.number_of_samples)

    field_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the scalar field Id Default value: 0
        """
    )
    def _field_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldId,
                        self.field_id)

    number_of_smoothing_iterations = traits.Int(30, enter_set=True, auto_set=False, help=\
        """
        Set the number of optional smoothing iterations Default value: 30
        """
    )
    def _number_of_smoothing_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSmoothingIterations,
                        self.number_of_smoothing_iterations)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_samples', 'GetNumberOfSamples'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('number_of_smoothing_iterations', 'GetNumberOfSmoothingIterations'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('field_id', 'GetFieldId'), ('progress_text', 'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'field_id', 'number_of_samples',
    'number_of_smoothing_iterations', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReebGraphSurfaceSkeletonFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ReebGraphSurfaceSkeletonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['field_id', 'number_of_samples',
            'number_of_smoothing_iterations']),
            title='Edit ReebGraphSurfaceSkeletonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReebGraphSurfaceSkeletonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

