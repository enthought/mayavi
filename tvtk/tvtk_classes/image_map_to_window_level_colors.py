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

from tvtk.tvtk_classes.image_map_to_colors import ImageMapToColors


class ImageMapToWindowLevelColors(ImageMapToColors):
    """
    ImageMapToWindowLevelColors - map the input image through a lookup
    table and window / level it
    
    Superclass: ImageMapToColors
    
    The ImageMapToWindowLevelColors filter will take an input image of
    any valid scalar type, and map the first component of the image
    through a lookup table.  This resulting color will be modulated with
    value obtained by a window / level operation. The result is an image
    of type VTK_UNSIGNED_CHAR. If the lookup table is not set, or is set
    to NULL, then the input data will be passed through if it is already
    of type UNSIGNED_CHAR.
    
    See Also:
    
    LookupTable ScalarsToColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMapToWindowLevelColors, obj, update, **traits)
    
    window = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the Window to use -> modulation will be performed on
        the color based on (S - (L - W/2))/W where S is the scalar value,
        L is the level and W is the window.
        """
    )
    def _window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindow,
                        self.window)

    level = traits.Float(127.5, enter_set=True, auto_set=False, help=\
        """
        Set / Get the Level to use -> modulation will be performed on the
        color based on (S - (L - W/2))/W where S is the scalar value, L
        is the level and W is the window.
        """
    )
    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

    _updateable_traits_ = \
    (('pass_alpha_to_output', 'GetPassAlphaToOutput'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('level',
    'GetLevel'), ('output_format', 'GetOutputFormat'), ('progress_text',
    'GetProgressText'), ('active_component', 'GetActiveComponent'),
    ('debug', 'GetDebug'), ('window', 'GetWindow'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_alpha_to_output', 'release_data_flag', 'output_format',
    'active_component', 'level', 'number_of_threads', 'progress_text',
    'window'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMapToWindowLevelColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMapToWindowLevelColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_alpha_to_output'], ['output_format'],
            ['active_component', 'level', 'number_of_threads', 'window']),
            title='Edit ImageMapToWindowLevelColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMapToWindowLevelColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

