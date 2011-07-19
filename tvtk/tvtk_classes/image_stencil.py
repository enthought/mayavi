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


class ImageStencil(ThreadedImageAlgorithm):
    """
    ImageStencil - combine images via a cookie-cutter operation
    
    Superclass: ThreadedImageAlgorithm
    
    ImageStencil will combine two images together using a stencil. The
    stencil should be provided in the form of a ImageStencilData,
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencil, obj, update, **traits)
    
    reverse_stencil = tvtk_base.false_bool_trait(help=\
        """
        Reverse the stencil.
        """
    )
    def _reverse_stencil_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseStencil,
                        self.reverse_stencil_)

    background_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the default output value to use when the second input is not
        set.
        """
    )
    def _background_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundValue,
                        self.background_value)

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    def _set_stencil(self, arg):
        old_val = self._get_stencil()
        self._wrap_call(self._vtk_obj.SetStencil,
                        deref_vtk(arg))
        self.trait_property_changed('stencil', old_val, arg)
    stencil = traits.Property(_get_stencil, _set_stencil, help=\
        """
        Specify the stencil to use.  The stencil can be created from a
        ImplicitFunction or a PolyData.
        """
    )

    background_color = traits.Array(shape=(4,), value=(1.0, 1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color)

    def _get_background_input(self):
        return wrap_vtk(self._vtk_obj.GetBackgroundInput())
    def _set_background_input(self, arg):
        old_val = self._get_background_input()
        self._wrap_call(self._vtk_obj.SetBackgroundInput,
                        deref_vtk(arg))
        self.trait_property_changed('background_input', old_val, arg)
    background_input = traits.Property(_get_background_input, _set_background_input, help=\
        """
        Set the second input.  This image will be used for the 'outside'
        of the stencil.  If not set, the output voxels will be filled
        with background_value instead.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reverse_stencil', 'GetReverseStencil'), ('background_value',
    'GetBackgroundValue'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('background_color',
    'GetBackgroundColor'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reverse_stencil', 'background_color',
    'background_value', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['reverse_stencil'], [], ['background_color',
            'background_value', 'number_of_threads']),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

