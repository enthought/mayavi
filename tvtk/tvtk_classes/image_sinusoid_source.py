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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageSinusoidSource(ImageAlgorithm):
    """
    ImageSinusoidSource - Create an image with sinusoidal pixel values.
    
    Superclass: ImageAlgorithm
    
    ImageSinusoidSource just produces images with pixel values
    determined by a sinusoid.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSinusoidSource, obj, update, **traits)
    
    phase = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the phase: 0->_2_pi.  0 => Cosine, pi/2 => Sine.
        """
    )
    def _phase_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhase,
                        self.phase)

    direction = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the direction vector which determines the sinusoidal
        orientation. The magnitude is ignored.
        """
    )
    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction)

    period = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the period of the sinusoid in pixels.
        """
    )
    def _period_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPeriod,
                        self.period)

    amplitude = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude of the sinusoid.
        """
    )
    def _amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmplitude,
                        self.amplitude)

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(int, int, int, int, int, int)
        C++: void SetWholeExtent(int xMinx, int xMax, int yMin, int yMax,
            int zMin, int zMax)
        Set/Get the extent of the whole output image.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *args)
        return ret

    _updateable_traits_ = \
    (('direction', 'GetDirection'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('period', 'GetPeriod'), ('reference_count',
    'GetReferenceCount'), ('abort_execute', 'GetAbortExecute'),
    ('amplitude', 'GetAmplitude'), ('release_data_flag',
    'GetReleaseDataFlag'), ('phase', 'GetPhase'), ('progress',
    'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'amplitude', 'direction', 'period', 'phase',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSinusoidSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['amplitude', 'direction', 'period', 'phase']),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

