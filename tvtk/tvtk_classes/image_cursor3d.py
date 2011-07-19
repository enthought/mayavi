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

from tvtk.tvtk_classes.image_in_place_filter import ImageInPlaceFilter


class ImageCursor3D(ImageInPlaceFilter):
    """
    ImageCursor3D - Paints a cursor on top of an image or volume.
    
    Superclass: ImageInPlaceFilter
    
    ImageCursor3D will draw a cursor on a 2d image or 3d volume.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageCursor3D, obj, update, **traits)
    
    cursor_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cursor_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorPosition,
                        self.cursor_position)

    cursor_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Sets/Gets what pixel value to draw the cursor in.
        """
    )
    def _cursor_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorValue,
                        self.cursor_value)

    cursor_radius = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Sets/Gets the radius of the cursor. The radius determines how far
        the axis lines project out from the cursors center.
        """
    )
    def _cursor_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorRadius,
                        self.cursor_radius)

    _updateable_traits_ = \
    (('cursor_value', 'GetCursorValue'), ('cursor_position',
    'GetCursorPosition'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('cursor_radius', 'GetCursorRadius'),
    ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'cursor_position', 'cursor_radius',
    'cursor_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageCursor3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageCursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cursor_position', 'cursor_radius',
            'cursor_value']),
            title='Edit ImageCursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageCursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

