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

from tvtk.tvtk_classes.parametric_function import ParametricFunction


class ParametricRandomHills(ParametricFunction):
    """
    ParametricRandomHills - Generate a surface covered with randomly
    placed hills.
    
    Superclass: ParametricFunction
    
    ParametricRandomHills generates a surface covered with randomly
    placed hills.
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/documents.php in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    Thanks:
    
    Andrew Maclean a.maclean@cas.edu.au for creating and contributing the
    class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricRandomHills, obj, update, **traits)
    
    allow_random_generation = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the random generation flag. A value of 0 will disable the
        generation of random hills on the surface. This allows a
        reproducible shape to be generated. Any other value means that
        the generation of the hills will be done randomly. Default is 1.
        """
    )
    def _allow_random_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowRandomGeneration,
                        self.allow_random_generation_)

    amplitude_scale_factor = traits.Float(0.333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the amplitude. Default is 1/3.
        """
    )
    def _amplitude_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmplitudeScaleFactor,
                        self.amplitude_scale_factor)

    random_seed = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Seed for the random number generator, a value of 1
        will initialize the random number generator, a negative value
        will initialize it with the system time. Default is 1.
        """
    )
    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    x_variance_scale_factor = traits.Float(0.333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the variance in the x-direction.
        Default is 1/3.
        """
    )
    def _x_variance_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXVarianceScaleFactor,
                        self.x_variance_scale_factor)

    hill_amplitude = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill amplitude (height). Default is 2.
        """
    )
    def _hill_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillAmplitude,
                        self.hill_amplitude)

    y_variance_scale_factor = traits.Float(0.333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the variance in the y-direction.
        Default is 1/3.
        """
    )
    def _y_variance_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYVarianceScaleFactor,
                        self.y_variance_scale_factor)

    number_of_hills = traits.Int(30, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of hills. Default is 30.
        """
    )
    def _number_of_hills_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHills,
                        self.number_of_hills)

    hill_x_variance = traits.Float(2.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill variance in the x-direction. Default is 2.5.
        """
    )
    def _hill_x_variance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillXVariance,
                        self.hill_x_variance)

    hill_y_variance = traits.Float(2.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill variance in the y-direction. Default is 2.5.
        """
    )
    def _hill_y_variance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillYVariance,
                        self.hill_y_variance)

    def generate_the_hills(self):
        """
        V.generate_the_hills()
        C++: void GenerateTheHills(void)
        Generate the centers of the hills, their standard deviations and
        their amplitudes. This function creates a series of vectors
        representing the u, v coordinates of each hill, its variance in
        the u, v directions and the amplitude.
        
        NOTE: This function must be called whenever any of the parameters
        are changed.
        """
        ret = self._vtk_obj.GenerateTheHills()
        return ret
        

    _updateable_traits_ = \
    (('number_of_hills', 'GetNumberOfHills'), ('random_seed',
    'GetRandomSeed'), ('minimum_v', 'GetMinimumV'),
    ('derivatives_available', 'GetDerivativesAvailable'), ('join_v',
    'GetJoinV'), ('join_u', 'GetJoinU'), ('allow_random_generation',
    'GetAllowRandomGeneration'), ('twist_v', 'GetTwistV'), ('twist_u',
    'GetTwistU'), ('minimum_u', 'GetMinimumU'), ('hill_y_variance',
    'GetHillYVariance'), ('minimum_w', 'GetMinimumW'),
    ('amplitude_scale_factor', 'GetAmplitudeScaleFactor'),
    ('x_variance_scale_factor', 'GetXVarianceScaleFactor'), ('maximum_v',
    'GetMaximumV'), ('maximum_w', 'GetMaximumW'), ('maximum_u',
    'GetMaximumU'), ('clockwise_ordering', 'GetClockwiseOrdering'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('y_variance_scale_factor', 'GetYVarianceScaleFactor'), ('debug',
    'GetDebug'), ('hill_amplitude', 'GetHillAmplitude'),
    ('reference_count', 'GetReferenceCount'), ('hill_x_variance',
    'GetHillXVariance'))
    
    _full_traitnames_list_ = \
    (['allow_random_generation', 'clockwise_ordering', 'debug',
    'derivatives_available', 'global_warning_display', 'join_u', 'join_v',
    'twist_u', 'twist_v', 'amplitude_scale_factor', 'hill_amplitude',
    'hill_x_variance', 'hill_y_variance', 'maximum_u', 'maximum_v',
    'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w', 'number_of_hills',
    'random_seed', 'x_variance_scale_factor', 'y_variance_scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricRandomHills, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_random_generation', 'clockwise_ordering',
            'derivatives_available', 'join_u', 'join_v', 'twist_u', 'twist_v'],
            [], ['amplitude_scale_factor', 'hill_amplitude', 'hill_x_variance',
            'hill_y_variance', 'maximum_u', 'maximum_v', 'maximum_w', 'minimum_u',
            'minimum_v', 'minimum_w', 'number_of_hills', 'random_seed',
            'x_variance_scale_factor', 'y_variance_scale_factor']),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

