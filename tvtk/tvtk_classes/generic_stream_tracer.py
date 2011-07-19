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


class GenericStreamTracer(PolyDataAlgorithm):
    """
    GenericStreamTracer - Streamline generator
    
    Superclass: PolyDataAlgorithm
    
    GenericStreamTracer is a filter that integrates a vector field to
    generate streamlines. The integration is performed using the provided
    integrator. The default is second order Runge-Kutta.
    
    GenericStreamTracer generate polylines as output. Each cell
    (polyline) corresponds to one streamline. The values associated with
    each streamline are stored in the cell data whereas the values
    associated with points are stored in point data.
    
    Note that GenericStreamTracer can integrate both forward and
    backward. The length of the streamline is controlled by specifying
    either a maximum value in the units of length, cell length or elapsed
    time (the elapsed time is the time each particle would have traveled
    if flow were steady). Otherwise, the integration terminates after
    exiting the dataset or if the particle speed is reduced to a value
    less than the terminal speed or when a maximum number of steps is
    reached. The reason for the termination is stored in a cell array
    named reason_for_termination.
    
    The quality of integration can be controlled by setting integration
    step (_initial_integration_step) and in the case of adaptive solvers the
    maximum error, the minimum integration step and the maximum
    integration step. All of these can have units of length, cell length
    or elapsed time.
    
    The integration time, vorticity, rotation and angular velocity are
    stored in point arrays named "_integration_time", "Vorticity",
    "Rotation" and "_angular_velocity" respectively (vorticity, rotation
    and angular velocity are computed only when compute_vorticity is on).
    All point attributes in the source data set are interpolated on the
    new streamline points.
    
    GenericStreamTracer integrates through any type of dataset. As a
    result, if the dataset contains 2d cells such as polygons or
    triangles, the integration is constrained to lie on the surface
    defined by the 2d cells.
    
    The starting point of traces may be defined in two different ways.
    Starting from global x-y-z "position" allows you to start a single
    trace at a specified x-y-z coordinate. If you specify a source
    object, a trace will be generated for each point in the source that
    is inside the dataset.
    
    See Also:
    
    RibbonFilter RuledSurfaceFilter InitialValueProblemSolver
    RungeKutta2 RungeKutta4 RungeKutta45
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericStreamTracer, obj, update, **traits)
    
    compute_vorticity = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _compute_vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeVorticity,
                        self.compute_vorticity_)

    maximum_propagation_unit = traits.Trait('length_unit',
    tvtk_base.TraitRevPrefixMap({'length_unit': 1, 'cell_length_unit': 2, 'time_unit': 0}), help=\
        """
        Specify the maximum length of the streamlines expressed in one of
        the: TIME_UNIT        = 0 LENGTH_UNIT      = 1 CELL_LENGTH_UNIT =
        2
        """
    )
    def _maximum_propagation_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPropagationUnit,
                        self.maximum_propagation_unit_)

    initial_integration_step_unit = traits.Trait('cell_length_unit',
    tvtk_base.TraitRevPrefixMap({'length_unit': 1, 'cell_length_unit': 2, 'time_unit': 0}), help=\
        """
        Specify the initial step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 If the integrator is not adaptive, this is
        the actual step used.
        """
    )
    def _initial_integration_step_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialIntegrationStepUnit,
                        self.initial_integration_step_unit_)

    integrator_type = traits.Trait('runge_kutta2',
    tvtk_base.TraitRevPrefixMap({'runge_kutta4': 1, 'runge_kutta45': 2, 'runge_kutta2': 0}), help=\
        """
        Set/get the integrator type to be used in the stream line
        calculation. The object passed is not actually used but is cloned
        with new_instance in the process of integration (prototype
        pattern). The default is 2nd order Runge Kutta. The integrator
        can also be changed using set_integrator_type. The recognized
        solvers are: RUNGE_KUTTA2  = 0 RUNGE_KUTTA4  = 1 RUNGE_KUTTA45 =
        2
        """
    )
    def _integrator_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegratorType,
                        self.integrator_type_)

    maximum_integration_step_unit = traits.Trait('cell_length_unit',
    tvtk_base.TraitRevPrefixMap({'length_unit': 1, 'cell_length_unit': 2, 'time_unit': 0}), help=\
        """
        Specify the maximum step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators.
        """
    )
    def _maximum_integration_step_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumIntegrationStepUnit,
                        self.maximum_integration_step_unit_)

    integration_direction = traits.Trait('forward',
    tvtk_base.TraitRevPrefixMap({'forward': 0, 'both': 2, 'backward': 1}), help=\
        """
        Specify whether the streamtrace will be generated in the upstream
        or downstream direction.
        """
    )
    def _integration_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationDirection,
                        self.integration_direction_)

    minimum_integration_step_unit = traits.Trait('cell_length_unit',
    tvtk_base.TraitRevPrefixMap({'length_unit': 1, 'cell_length_unit': 2, 'time_unit': 0}), help=\
        """
        Specify the minimum step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators.
        """
    )
    def _minimum_integration_step_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumIntegrationStepUnit,
                        self.minimum_integration_step_unit_)

    maximum_integration_step = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators.
        """
    )
    def _maximum_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumIntegrationStep,
                        self.maximum_integration_step)

    rotation_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _rotation_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationScale,
                        self.rotation_scale)

    maximum_error = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _maximum_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumError,
                        self.maximum_error)

    maximum_propagation = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum length of the streamlines expressed in one of
        the: TIME_UNIT        = 0 LENGTH_UNIT      = 1 CELL_LENGTH_UNIT =
        2
        """
    )
    def _maximum_propagation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPropagation,
                        self.maximum_propagation)

    start_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _start_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPosition,
                        self.start_position)

    def _get_integrator(self):
        return wrap_vtk(self._vtk_obj.GetIntegrator())
    def _set_integrator(self, arg):
        old_val = self._get_integrator()
        self._wrap_call(self._vtk_obj.SetIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('integrator', old_val, arg)
    integrator = traits.Property(_get_integrator, _set_integrator, help=\
        """
        Set/get the integrator type to be used in the stream line
        calculation. The object passed is not actually used but is cloned
        with new_instance in the process of integration (prototype
        pattern). The default is 2nd order Runge Kutta. The integrator
        can also be changed using set_integrator_type. The recognized
        solvers are: RUNGE_KUTTA2  = 0 RUNGE_KUTTA4  = 1 RUNGE_KUTTA45 =
        2
        """
    )

    initial_integration_step = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Specify the initial step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 If the integrator is not adaptive, this is
        the actual step used.
        """
    )
    def _initial_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialIntegrationStep,
                        self.initial_integration_step)

    terminal_speed = traits.Float(1e-12, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _terminal_speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminalSpeed,
                        self.terminal_speed)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Specify the source object used to generate starting points.
        """
    )

    minimum_integration_step = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Specify the minimum step used in the integration expressed in one
        of the: TIME_UNIT        = 0 LENGTH_UNIT      = 1
        CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators.
        """
    )
    def _minimum_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumIntegrationStep,
                        self.minimum_integration_step)

    maximum_number_of_steps = traits.Int(2000, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _maximum_number_of_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSteps,
                        self.maximum_number_of_steps)

    def _get_input_vectors_selection(self):
        return self._vtk_obj.GetInputVectorsSelection()
    input_vectors_selection = traits.Property(_get_input_vectors_selection, help=\
        """
        If you want to generate traces using an arbitrary vector array,
        then set its name here. By default this in NULL and the filter
        will use the active vector array.
        """
    )

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def select_input_vectors(self, *args):
        """
        V.select_input_vectors(string)
        C++: void SelectInputVectors(const char *fieldName)
        If you want to generate traces using an arbitrary vector array,
        then set its name here. By default this in NULL and the filter
        will use the active vector array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectInputVectors, *args)
        return ret

    def set_interpolator_prototype(self, *args):
        """
        V.set_interpolator_prototype(GenericInterpolatedVelocityField)
        C++: void SetInterpolatorPrototype(
            GenericInterpolatedVelocityField *ivf)
        The object used to interpolate the velocity field during
        integration is of the same class as this prototype.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInterpolatorPrototype, *my_args)
        return ret

    _updateable_traits_ = \
    (('minimum_integration_step_unit', 'GetMinimumIntegrationStepUnit'),
    ('maximum_propagation', 'GetMaximumPropagation'),
    ('initial_integration_step_unit', 'GetInitialIntegrationStepUnit'),
    ('reference_count', 'GetReferenceCount'), ('initial_integration_step',
    'GetInitialIntegrationStep'), ('maximum_propagation_unit',
    'GetMaximumPropagationUnit'), ('start_position', 'GetStartPosition'),
    ('compute_vorticity', 'GetComputeVorticity'),
    ('maximum_number_of_steps', 'GetMaximumNumberOfSteps'),
    ('maximum_integration_step', 'GetMaximumIntegrationStep'),
    ('terminal_speed', 'GetTerminalSpeed'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('minimum_integration_step', 'GetMinimumIntegrationStep'),
    ('abort_execute', 'GetAbortExecute'), ('maximum_error',
    'GetMaximumError'), ('integration_direction',
    'GetIntegrationDirection'), ('release_data_flag',
    'GetReleaseDataFlag'), ('integrator_type', 'GetIntegratorType'),
    ('debug', 'GetDebug'), ('progress', 'GetProgress'),
    ('maximum_integration_step_unit', 'GetMaximumIntegrationStepUnit'),
    ('rotation_scale', 'GetRotationScale'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_vorticity', 'debug',
    'global_warning_display', 'release_data_flag',
    'initial_integration_step_unit', 'integration_direction',
    'integrator_type', 'maximum_integration_step_unit',
    'maximum_propagation_unit', 'minimum_integration_step_unit',
    'initial_integration_step', 'maximum_error',
    'maximum_integration_step', 'maximum_number_of_steps',
    'maximum_propagation', 'minimum_integration_step', 'progress_text',
    'rotation_scale', 'start_position', 'terminal_speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericStreamTracer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_vorticity'],
            ['initial_integration_step_unit', 'integration_direction',
            'integrator_type', 'maximum_integration_step_unit',
            'maximum_propagation_unit', 'minimum_integration_step_unit'],
            ['initial_integration_step', 'maximum_error',
            'maximum_integration_step', 'maximum_number_of_steps',
            'maximum_propagation', 'minimum_integration_step', 'rotation_scale',
            'start_position', 'terminal_speed']),
            title='Edit GenericStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

