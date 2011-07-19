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


class AreaContourSpectrumFilter(DataObjectAlgorithm):
    """
    AreaContourSpectrumFilter - compute an approximation of the area
    
    Superclass: DataObjectAlgorithm
    
    The filter takes a PolyData as an input (port 0), along with a
    ReebGraph (port 1). The Reeb graph arc to consider can be
    specified with set_arc_id() (default: 0). The number of (evenly
    distributed) samples of the signature can be defined with
    set_number_of_samples() (default value: 100). The filter will first try
    to pull as a scalar field the DataArray with Id '_field_id' of the
    PolyData, see set_field_id (default: 0). The filter will abort if
    this field does not exist.
    
    The filter outputs a Table with the area contour signature
    approximation, each sample being evenly distributed in the function
    span of the arc.
    
    This filter is a typical example for designing your own contour
    signature filter (with customized metrics). It also shows typical
    ReebGraph traversals.
    
    Reference: C. Bajaj, V. Pascucci, D. Schikore, "The contour
    spectrum", IEEE Visualization, 167-174, 1997.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAreaContourSpectrumFilter, obj, update, **traits)
    
    arc_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the arc Id for which the contour signature has to be
        computed. Default value: 0
        """
    )
    def _arc_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcId,
                        self.arc_id)

    field_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the scalar field Id Default value: 0
        """
    )
    def _field_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldId,
                        self.field_id)

    number_of_samples = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Set the number of samples in the output signature Default value:
        100
        """
    )
    def _number_of_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSamples,
                        self.number_of_samples)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_samples', 'GetNumberOfSamples'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('field_id',
    'GetFieldId'), ('arc_id', 'GetArcId'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'arc_id', 'field_id', 'number_of_samples',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AreaContourSpectrumFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['arc_id', 'field_id', 'number_of_samples']),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

