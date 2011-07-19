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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class TimeSourceExample(UnstructuredGridAlgorithm):
    """
    TimeSource - creates a simple time varying data set.
    
    Superclass: UnstructuredGridAlgorithm
    
    Creates a small easily understood time varying data set for testing.
    The output is a UntructuredGrid in which the point and cell values
    vary over time in a sin wave. The analytic ivar controls whether the
    output corresponds to a step function over time or is continuous. The
    X and Y Amplitude ivars make the output move in the X and Y
    directions over time. The Growing ivar makes the number of cells in
    the output grow and then shrink over time.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTimeSourceExample, obj, update, **traits)
    
    growing = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _growing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGrowing,
                        self.growing_)

    analytic = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _analytic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnalytic,
                        self.analytic_)

    x_amplitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _x_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAmplitude,
                        self.x_amplitude)

    y_amplitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _y_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAmplitude,
                        self.y_amplitude)

    def _get_analytic_max_value(self):
        return self._vtk_obj.GetAnalyticMaxValue()
    analytic_max_value = traits.Property(_get_analytic_max_value, help=\
        """
        
        """
    )

    def _get_analytic_min_value(self):
        return self._vtk_obj.GetAnalyticMinValue()
    analytic_min_value = traits.Property(_get_analytic_min_value, help=\
        """
        
        """
    )

    def _get_growing_max_value(self):
        return self._vtk_obj.GetGrowingMaxValue()
    growing_max_value = traits.Property(_get_growing_max_value, help=\
        """
        
        """
    )

    def _get_growing_min_value(self):
        return self._vtk_obj.GetGrowingMinValue()
    growing_min_value = traits.Property(_get_growing_min_value, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('y_amplitude', 'GetYAmplitude'), ('growing', 'GetGrowing'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'), ('x_amplitude',
    'GetXAmplitude'), ('analytic', 'GetAnalytic'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'analytic', 'debug', 'global_warning_display',
    'growing', 'release_data_flag', 'progress_text', 'x_amplitude',
    'y_amplitude'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TimeSourceExample, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['analytic', 'growing'], [], ['x_amplitude',
            'y_amplitude']),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

