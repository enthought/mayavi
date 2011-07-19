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

from tvtk.tvtk_classes.actor2d import Actor2D


class LegendBoxActor(Actor2D):
    """
    LegendBoxActor - draw symbols with text
    
    Superclass: Actor2D
    
    LegendBoxActor is used to associate a symbol with a text string.
    The user specifies a PolyData to use as the symbol, and a string
    associated with the symbol. The actor can then be placed in the scene
    in the same way that any other Actor2D can be used.
    
    To use this class, you must define the position of the legend box by
    using the superclasses' Actor2D::Position coordinate and Position2
    coordinate. Then define the set of symbols and text strings that make
    up the menu box. The font attributes of the entries can be set
    through the TextProperty associated to this actor. The class will
    scale the symbols and text to fit in the legend box defined by
    (Position,Position2). Optional features like turning on a border line
    and setting the spacing between the border and the symbols/text can
    also be set.
    
    See Also:
    
    XYPlotActor Actor2D GlyphSource2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLegendBoxActor, obj, update, **traits)
    
    box = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag that controls whether a box will be drawn/filled
        corresponding to the legend box.
        """
    )
    def _box_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBox,
                        self.box_)

    lock_border = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag that controls whether the border and legend
        placement is locked into the rectangle defined by
        (Position,Position2). If off, then the legend box will adjust its
        size so that the border fits nicely around the text and symbols.
        (The ivar is off by default.) Note: the legend box is guaranteed
        to lie within the original border definition.
        """
    )
    def _lock_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockBorder,
                        self.lock_border_)

    use_background = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off background.
        """
    )
    def _use_background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBackground,
                        self.use_background_)

    border = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that controls whether a border will be drawn
        around the legend box.
        """
    )
    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    scalar_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off flag to control whether the symbol's scalar data is
        used to color the symbol. If off, the color of the
        LegendBoxActor is used.
        """
    )
    def _scalar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarVisibility,
                        self.scalar_visibility_)

    number_of_entries = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of entries in the legend box.
        """
    )
    def _number_of_entries_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfEntries,
                        self.number_of_entries)

    def get_entry_symbol(self, *args):
        """
        V.get_entry_symbol(int) -> PolyData
        C++: PolyData *GetEntrySymbol(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetEntrySymbol, *args)
        return wrap_vtk(ret)

    def set_entry_symbol(self, *args):
        """
        V.set_entry_symbol(int, PolyData)
        C++: void SetEntrySymbol(int i, PolyData *symbol)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetEntrySymbol, *my_args)
        return ret

    entry_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _entry_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEntryString,
                        self.entry_string)

    padding = traits.Trait(3, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the padding between the legend entries and the border.
        The value is specified in pixels.
        """
    )
    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    def get_entry_color(self, *args):
        """
        V.get_entry_color(int) -> (float, float, float)
        C++: double *GetEntryColor(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetEntryColor, *args)
        return ret

    def set_entry_color(self, *args):
        """
        V.set_entry_color(int, [float, float, float])
        C++: void SetEntryColor(int i, double color[3])
        V.set_entry_color(int, float, float, float)
        C++: void SetEntryColor(int i, double r, double g, double b)"""
        ret = self._wrap_call(self._vtk_obj.SetEntryColor, *args)
        return ret

    background_color = tvtk_base.vtk_color_trait((0.29999999999999999, 0.29999999999999999, 0.29999999999999999), help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    background_opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get background opacity. Default is: 1.0
        """
    )
    def _background_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundOpacity,
                        self.background_opacity)

    def get_entry_icon(self, *args):
        """
        V.get_entry_icon(int) -> ImageData
        C++: ImageData *GetEntryIcon(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetEntryIcon, *args)
        return wrap_vtk(ret)

    def set_entry_icon(self, *args):
        """
        V.set_entry_icon(int, ImageData)
        C++: void SetEntryIcon(int i, ImageData *icon)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetEntryIcon, *my_args)
        return ret

    def _get_entry_text_property(self):
        return wrap_vtk(self._vtk_obj.GetEntryTextProperty())
    def _set_entry_text_property(self, arg):
        old_val = self._get_entry_text_property()
        self._wrap_call(self._vtk_obj.SetEntryTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('entry_text_property', old_val, arg)
    entry_text_property = traits.Property(_get_entry_text_property, _set_entry_text_property, help=\
        """
        Set/Get the text property.
        """
    )

    def _get_box_property(self):
        return wrap_vtk(self._vtk_obj.GetBoxProperty())
    box_property = traits.Property(_get_box_property, help=\
        """
        Get the box Property2D.
        """
    )

    def set_entry(self, *args):
        """
        V.set_entry(int, PolyData, string, [float, float, float])
        C++: void SetEntry(int i, PolyData *symbol, const char *string,
             double color[3])
        V.set_entry(int, ImageData, string, [float, float, float])
        C++: void SetEntry(int i, ImageData *symbol,
            const char *string, double color[3])
        V.set_entry(int, PolyData, ImageData, string, [float, float,
            float])
        C++: void SetEntry(int i, PolyData *symbol, ImageData *icon,
             const char *string, double color[3])
        Add an entry to the legend box. You must supply a PolyData to
        be used as a symbol (it can be NULL) and a text string (which
        also can be NULL). The PolyData is assumed to be defined in
        the x-y plane, and the text is assumed to be a single line in
        height. Note that when this method is invoked previous entries
        are deleted. Also supply a text string and optionally a color.
        (If a color is not specified, then the entry color is the same as
        this actor's color.) (Note: use the set methods when you use
        set_number_of_entries().)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetEntry, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('dragable',
    'GetDragable'), ('number_of_entries', 'GetNumberOfEntries'),
    ('visibility', 'GetVisibility'), ('height', 'GetHeight'), ('padding',
    'GetPadding'), ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('entry_string', 'GetEntryString'), ('scalar_visibility',
    'GetScalarVisibility'), ('background_color', 'GetBackgroundColor'),
    ('use_bounds', 'GetUseBounds'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('box',
    'GetBox'), ('layer_number', 'GetLayerNumber'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('position2',
    'GetPosition2'), ('lock_border', 'GetLockBorder'), ('border',
    'GetBorder'), ('use_background', 'GetUseBackground'), ('width',
    'GetWidth'), ('reference_count', 'GetReferenceCount'), ('position',
    'GetPosition'), ('pickable', 'GetPickable'), ('background_opacity',
    'GetBackgroundOpacity'))
    
    _full_traitnames_list_ = \
    (['border', 'box', 'debug', 'dragable', 'global_warning_display',
    'lock_border', 'pickable', 'scalar_visibility', 'use_background',
    'use_bounds', 'visibility', 'allocated_render_time',
    'background_color', 'background_opacity', 'entry_string',
    'estimated_render_time', 'height', 'layer_number',
    'number_of_entries', 'padding', 'position', 'position2',
    'render_time_multiplier', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LegendBoxActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LegendBoxActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['border', 'box', 'lock_border', 'scalar_visibility',
            'use_background', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'background_color', 'background_opacity',
            'entry_string', 'estimated_render_time', 'height', 'layer_number',
            'number_of_entries', 'padding', 'position', 'position2',
            'render_time_multiplier', 'width']),
            title='Edit LegendBoxActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LegendBoxActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

