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

from tvtk.tvtk_classes.writer import Writer


class AbstractParticleWriter(Writer):
    """
    AbstractParticleWriter - abstract class to write particle data to
    file
    
    Superclass: Writer
    
    AbstractParticleWriter is an abstract class which is used by
    TemporalStreamTracer to write particles out during simulations.
    This class is abstract and provides a time_step and file_name.
    Subclasses of this should provide the necessary IO.
    
    Caveats:
    
    See Writer
    
    See Also:
    
    TemporalStreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractParticleWriter, obj, update, **traits)
    
    collective_io = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When running in parallel, this writer may be capable of
        Collective IO operations (HDF5). By default, this is off.
        """
    )
    def _collective_io_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCollectiveIO,
                        self.collective_io)

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the time_step that is being written
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    time_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Before writing the current data out, set the time_value (optional)
        The time_value is a float/double value that corresonds to the real
        time of the data, it may not be regular, whereas the time_steps
        are simple increments.
        """
    )
    def _time_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeValue,
                        self.time_value)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/get the file_name that is being written to
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def close_file(self):
        """
        V.close_file()
        C++: virtual void CloseFile()
        Close the file after a write. This is optional but may protect
        against data loss in between steps
        """
        ret = self._vtk_obj.CloseFile()
        return ret
        

    def set_write_mode_to_collective(self):
        """
        V.set_write_mode_to_collective()
        C++: void SetWriteModeToCollective()
        When running in parallel, this writer may be capable of
        Collective IO operations (HDF5). By default, this is off.
        """
        ret = self._vtk_obj.SetWriteModeToCollective()
        return ret
        

    def set_write_mode_to_independent(self):
        """
        V.set_write_mode_to_independent()
        C++: void SetWriteModeToIndependent()
        When running in parallel, this writer may be capable of
        Collective IO operations (HDF5). By default, this is off.
        """
        ret = self._vtk_obj.SetWriteModeToIndependent()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('time_value', 'GetTimeValue'), ('release_data_flag',
    'GetReleaseDataFlag'), ('time_step', 'GetTimeStep'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('abort_execute', 'GetAbortExecute'), ('collective_io',
    'GetCollectiveIO'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'collective_io', 'file_name', 'progress_text',
    'time_step', 'time_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractParticleWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractParticleWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['collective_io', 'file_name', 'time_step',
            'time_value']),
            title='Edit AbstractParticleWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractParticleWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

