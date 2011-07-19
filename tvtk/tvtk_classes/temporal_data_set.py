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

from tvtk.tvtk_classes.composite_data_set import CompositeDataSet


class TemporalDataSet(CompositeDataSet):
    """
    TemporalDataSet - Composite dataset that holds multiple times
    
    Superclass: CompositeDataSet
    
    TemporalDataSet is a CompositeDataSet that stores multiple time
    steps of data.
    
    See Also:
    
    CompositeDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalDataSet, obj, update, **traits)
    
    def get_time_step(self, *args):
        """
        V.get_time_step(int) -> DataObject
        C++: DataObject *GetTimeStep(unsigned int timestep)
        Get a timestep.
        """
        ret = self._wrap_call(self._vtk_obj.GetTimeStep, *args)
        return wrap_vtk(ret)

    def set_time_step(self, *args):
        """
        V.set_time_step(int, DataObject)
        C++: void SetTimeStep(unsigned int timestep, DataObject *dobj)
        Set a data object as a timestep. Cannot be TemporalDataSet.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTimeStep, *my_args)
        return ret

    number_of_time_steps = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of time steps in theis dataset
        """
    )
    def _number_of_time_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTimeSteps,
                        self.number_of_time_steps)

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('number_of_time_steps',
    'GetNumberOfTimeSteps'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'number_of_time_steps', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'number_of_time_steps',
            'update_extent', 'update_ghost_level', 'update_number_of_pieces',
            'update_piece', 'whole_bounding_box', 'whole_extent']),
            title='Edit TemporalDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

