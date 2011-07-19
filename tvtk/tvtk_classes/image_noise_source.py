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


class ImageNoiseSource(ImageAlgorithm):
    """
    ImageNoiseSource - Create an image filled with noise.
    
    Superclass: ImageAlgorithm
    
    ImageNoiseSource just produces images filled with noise.  The only
    option now is uniform noise specified by a min and a max.  There is
    one major problem with this source. Every time it executes, it will
    output different pixel values.  This has important implications when
    a stream requests overlapping regions.  The same pixels will have
    different values on different updates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageNoiseSource, obj, update, **traits)
    
    minimum = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum and maximum values for the generated noise.
        """
    )
    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum)

    maximum = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum and maximum values for the generated noise.
        """
    )
    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(int, int, int, int, int, int)
        C++: void SetWholeExtent(int xMinx, int xMax, int yMin, int yMax,
            int zMin, int zMax)
        V.set_whole_extent((int, int, int, int, int, int))
        C++: void SetWholeExtent(const int ext[6])
        Set how large of an image to generate.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('maximum', 'GetMaximum'),
    ('debug', 'GetDebug'), ('minimum', 'GetMinimum'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum', 'minimum', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageNoiseSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['maximum', 'minimum']),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

