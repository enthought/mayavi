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

from tvtk.tvtk_classes.mapper2d import Mapper2D


class TextMapper(Mapper2D):
    """
    TextMapper - 2d text annotation
    
    Superclass: Mapper2D
    
    TextMapper provides 2d text annotation support for VTK.  It is a
    Mapper2D that can be associated with a Actor2D and placed into
    a Renderer.
    
    To use TextMapper, specify an input text string.
    
    See Also:
    
    Mapper2D Actor2D LegendBoxActor CaptionActor2D
    VectorText TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextMapper, obj, update, **traits)
    
    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the input text string to the mapper.  The mapper recognizes
        "\n" as a carriage return/linefeed (line separator).
        """
    )

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property.
        """
    )

    def get_height(self, *args):
        """
        V.get_height(Viewport) -> int
        C++: virtual int GetHeight(Viewport *v)
        Return the size[2]/width/height of the rectangle required to draw
        this mapper (in pixels).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetHeight, *my_args)
        return ret

    def _get_number_of_lines(self):
        return self._vtk_obj.GetNumberOfLines()
    number_of_lines = traits.Property(_get_number_of_lines, help=\
        """
        Determine the number of lines in the input string (delimited by
        "\n").
        """
    )

    def get_size(self, *args):
        """
        V.get_size(Viewport, [int, int])
        C++: virtual void GetSize(Viewport *, int size[2])
        Return the size[2]/width/height of the rectangle required to draw
        this mapper (in pixels).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetSize, *my_args)
        return ret

    def get_system_font_size(self, *args):
        """
        V.get_system_font_size(int) -> int
        C++: virtual int GetSystemFontSize(int size)
        Get the available system font size matching a font size.
        """
        ret = self._wrap_call(self._vtk_obj.GetSystemFontSize, *args)
        return ret

    def get_width(self, *args):
        """
        V.get_width(Viewport) -> int
        C++: virtual int GetWidth(Viewport *v)
        Return the size[2]/width/height of the rectangle required to draw
        this mapper (in pixels).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetWidth, *my_args)
        return ret

    def set_constrained_font_size(self, *args):
        """
        V.set_constrained_font_size(Viewport, int, int) -> int
        C++: virtual int SetConstrainedFontSize(Viewport *,
            int targetWidth, int targetHeight)
        V.set_constrained_font_size(TextMapper, Viewport, int, int)
            -> int
        C++: static int SetConstrainedFontSize(TextMapper *,
            Viewport *, int targetWidth, int targetHeight)
        Set and return the font size required to make this mapper fit in
        a given target rectangle (width x height, in pixels). A static
        version of the method is also available for convenience to other
        classes (e.g., widgets).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetConstrainedFontSize, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TextMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

