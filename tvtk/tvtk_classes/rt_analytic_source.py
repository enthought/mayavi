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


class RTAnalyticSource(ImageAlgorithm):
    """
    RTAnalyticSource - Create an image for regression testing
    
    Superclass: ImageAlgorithm
    
    RTAnalyticSource just produces images with pixel values determined
    by a Maximum*Gaussian*XMag*sin(XFreq*x)*sin(YFreq*y)*cos(ZFreq*z)
    Values are float scalars on point data with name "RTData".
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRTAnalyticSource, obj, update, **traits)
    
    subsample_rate = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the sub-sample rate. Initial value is 1.
        """
    )
    def _subsample_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubsampleRate,
                        self.subsample_rate)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    x_mag = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in x. Initial value is 10.
        """
    )
    def _x_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMag,
                        self.x_mag)

    whole_extent = traits.Array(shape=(6,), value=(-10, 10, -10, 10, -10, 10), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the extent of the whole output image. Initial value is
        {-10,10,-10,10,-10,10}
        """
    )
    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    standard_deviation = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the standard deviation of the function. Initial value is
        0.5.
        """
    )
    def _standard_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStandardDeviation,
                        self.standard_deviation)

    maximum = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Maximum value of the function. Initial value is
        255.0.
        """
    )
    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    x_freq = traits.Float(60.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in x. Initial value is 60.
        """
    )
    def _x_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXFreq,
                        self.x_freq)

    y_freq = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in y. Initial value is 30.
        """
    )
    def _y_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYFreq,
                        self.y_freq)

    z_mag = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in z. Initial value is 5.
        """
    )
    def _z_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZMag,
                        self.z_mag)

    y_mag = traits.Float(18.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in y. Initial value is 18.
        """
    )
    def _y_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYMag,
                        self.y_mag)

    z_freq = traits.Float(40.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in z. Initial value is 40.
        """
    )
    def _z_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZFreq,
                        self.z_freq)

    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('subsample_rate',
    'GetSubsampleRate'), ('y_freq', 'GetYFreq'), ('center', 'GetCenter'),
    ('x_mag', 'GetXMag'), ('x_freq', 'GetXFreq'), ('progress_text',
    'GetProgressText'), ('maximum', 'GetMaximum'), ('debug', 'GetDebug'),
    ('z_freq', 'GetZFreq'), ('z_mag', 'GetZMag'), ('y_mag', 'GetYMag'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('standard_deviation',
    'GetStandardDeviation'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'maximum', 'progress_text',
    'standard_deviation', 'subsample_rate', 'whole_extent', 'x_freq',
    'x_mag', 'y_freq', 'y_mag', 'z_freq', 'z_mag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RTAnalyticSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'maximum', 'standard_deviation',
            'subsample_rate', 'whole_extent', 'x_freq', 'x_mag', 'y_freq',
            'y_mag', 'z_freq', 'z_mag']),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

