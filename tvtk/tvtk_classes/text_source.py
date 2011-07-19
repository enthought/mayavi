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


class TextSource(PolyDataAlgorithm):
    """
    TextSource - create polygonal text
    
    Superclass: PolyDataAlgorithm
    
    TextSource converts a text string into polygons.  This way you can
    insert text into your renderings. It uses the 9x15 font from X
    Windows. You can specify if you want the background to be drawn or
    not. The characters are formed by scan converting the raster font
    into quadrilaterals. Colors are assigned to the letters using scalar
    data. To set the color of the characters with the source's actor
    property, set backing_off on the text source and scalar_visibility_off
    on the associated PolyDataMapper. Then, the color can be set using
    the associated actor's property.
    
    VectorText generates higher quality polygonal representations of
    characters.
    
    See Also:
    
    VectorText
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextSource, obj, update, **traits)
    
    backing = tvtk_base.true_bool_trait(help=\
        """
        Controls whether or not a background is drawn with the text.
        """
    )
    def _backing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBacking,
                        self.backing_)

    text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the text to be drawn.
        """
    )
    def _text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetText,
                        self.text)

    foreground_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _foreground_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForegroundColor,
                        self.foreground_color, False)

    background_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('backing',
    'GetBacking'), ('text', 'GetText'), ('progress_text',
    'GetProgressText'), ('foreground_color', 'GetForegroundColor'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('background_color', 'GetBackgroundColor'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'backing', 'debug', 'global_warning_display',
    'release_data_flag', 'background_color', 'foreground_color',
    'progress_text', 'text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['backing'], [], ['background_color',
            'foreground_color', 'text']),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

