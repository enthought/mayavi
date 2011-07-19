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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class PerlinNoise(ImplicitFunction):
    """
    PerlinNoise - an implicit function that implements Perlin noise
    
    Superclass: ImplicitFunction
    
    PerlinNoise computes a Perlin noise field as an implicit function.
    PerlinNoise is a concrete implementation of ImplicitFunction.
    Perlin noise, originally described by Ken Perlin, is a non-periodic
    and continuous noise function useful for modeling real-world objects.
    
    The amplitude and frequency of the noise pattern are adjustable. 
    This implementation of Perlin noise is derived closely from Greg
    Ward's version in Graphics Gems II.
    
    See Also:
    
    ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPerlinNoise, obj, update, **traits)
    
    phase = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _phase_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhase,
                        self.phase)

    frequency = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _frequency_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrequency,
                        self.frequency)

    amplitude = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the amplitude of the noise function. Amplitude can be
        negative. The noise function varies randomly between -|Amplitude|
        and |Amplitude|. Therefore the range of values is 2*|Amplitude|
        large. The initial amplitude is 1.
        """
    )
    def _amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmplitude,
                        self.amplitude)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('frequency',
    'GetFrequency'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('amplitude', 'GetAmplitude'), ('phase',
    'GetPhase'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'amplitude', 'frequency',
    'phase'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PerlinNoise, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PerlinNoise properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['amplitude', 'frequency', 'phase']),
            title='Edit PerlinNoise properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PerlinNoise properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

