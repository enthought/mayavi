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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageIdealHighPass(ThreadedImageAlgorithm):
    """
    ImageIdealHighPass - Simple frequency domain band pass.
    
    Superclass: ThreadedImageAlgorithm
    
    This filter only works on an image after it has been converted to
    frequency domain by a ImageFFT filter.  A ImageRFFT filter can
    be used to convert the output back into the spatial domain.
    ImageIdealHighPass just sets a portion of the image to zero.  The
    sharp cutoff in the frequence domain produces ringing in the spatial
    domain. Input and Output must be doubles.  Dimensionality is set when
    the axes are set.  Defaults to 2d on X and Y axes.
    
    See Also:
    
    ImageButterworthHighPass ImageIdealLowPass ImageFFT
    ImageRFFT
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageIdealHighPass, obj, update, **traits)
    
    x_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )
    def _x_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXCutOff,
                        self.x_cut_off)

    cut_off = traits.Array(shape=(3,), value=(1.0000000000000001e+299, 1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutOff,
                        self.cut_off)

    y_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )
    def _y_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYCutOff,
                        self.y_cut_off)

    z_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )
    def _z_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCutOff,
                        self.z_cut_off)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('x_cut_off', 'GetXCutOff'), ('progress_text',
    'GetProgressText'), ('cut_off', 'GetCutOff'), ('abort_execute',
    'GetAbortExecute'), ('z_cut_off', 'GetZCutOff'), ('number_of_threads',
    'GetNumberOfThreads'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('y_cut_off', 'GetYCutOff'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'cut_off', 'number_of_threads', 'progress_text',
    'x_cut_off', 'y_cut_off', 'z_cut_off'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageIdealHighPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageIdealHighPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cut_off', 'number_of_threads', 'x_cut_off',
            'y_cut_off', 'z_cut_off']),
            title='Edit ImageIdealHighPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageIdealHighPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

