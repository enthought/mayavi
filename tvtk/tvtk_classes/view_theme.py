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

from tvtk.tvtk_classes.object import Object


class ViewTheme(Object):
    """
    ViewTheme - Sets theme colors for a graphical view.
    
    Superclass: Object
    
    This may be set on any subclass of View.  The view class will
    attempt to use the values set in the theme to customize the view. 
    Views will not generally use every aspect of the theme. NOTICE: This
    class will be deprecated in favor of a more robust solution based on
    style sheets.  Do not become overly-dependent on the functionality of
    themes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkViewTheme, obj, update, **traits)
    
    scale_cell_lookup_table = tvtk_base.true_bool_trait(help=\
        """
        Whether to scale the lookup table to fit the range of the data.
        """
    )
    def _scale_cell_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleCellLookupTable,
                        self.scale_cell_lookup_table_)

    scale_point_lookup_table = tvtk_base.true_bool_trait(help=\
        """
        Whether to scale the lookup table to fit the range of the data.
        """
    )
    def _scale_point_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalePointLookupTable,
                        self.scale_point_lookup_table_)

    def get_point_hue_range(self, *args):
        """
        V.get_point_hue_range(float, float)
        C++: virtual void GetPointHueRange(double &mn, double &mx)
        V.get_point_hue_range([float, float])
        C++: virtual void GetPointHueRange(double rng[2])
        The ranges to use in the point lookup table. You may also do this
        by accessing the point lookup table directly with
        get_point_lookup_table() and calling these methods.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointHueRange, *args)
        return ret

    def set_point_hue_range(self, *args):
        """
        V.set_point_hue_range(float, float)
        C++: virtual void SetPointHueRange(double mn, double mx)
        V.set_point_hue_range([float, float])
        C++: virtual void SetPointHueRange(double rng[2])
        The ranges to use in the point lookup table. You may also do this
        by accessing the point lookup table directly with
        get_point_lookup_table() and calling these methods.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointHueRange, *args)
        return ret

    def get_point_alpha_range(self, *args):
        """
        V.get_point_alpha_range(float, float)
        C++: virtual void GetPointAlphaRange(double &mn, double &mx)
        V.get_point_alpha_range([float, float])
        C++: virtual void GetPointAlphaRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetPointAlphaRange, *args)
        return ret

    def set_point_alpha_range(self, *args):
        """
        V.set_point_alpha_range(float, float)
        C++: virtual void SetPointAlphaRange(double mn, double mx)
        V.set_point_alpha_range([float, float])
        C++: virtual void SetPointAlphaRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetPointAlphaRange, *args)
        return ret

    cell_opacity = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        The color and opacity of cells or edges when not mapped through a
        lookup table.
        """
    )
    def _cell_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellOpacity,
                        self.cell_opacity)

    selected_cell_color = tvtk_base.vtk_color_trait((1.0, 0.0, 1.0), help=\
        """
        
        """
    )
    def _selected_cell_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedCellColor,
                        self.selected_cell_color, False)

    def get_cell_hue_range(self, *args):
        """
        V.get_cell_hue_range(float, float)
        C++: virtual void GetCellHueRange(double &mn, double &mx)
        V.get_cell_hue_range([float, float])
        C++: virtual void GetCellHueRange(double rng[2])
        The ranges to use in the cell lookup table. You may also do this
        by accessing the cell lookup table directly with
        get_cell_lookup_table() and calling these methods.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellHueRange, *args)
        return ret

    def set_cell_hue_range(self, *args):
        """
        V.set_cell_hue_range(float, float)
        C++: virtual void SetCellHueRange(double mn, double mx)
        V.set_cell_hue_range([float, float])
        C++: virtual void SetCellHueRange(double rng[2])
        The ranges to use in the cell lookup table. You may also do this
        by accessing the cell lookup table directly with
        get_cell_lookup_table() and calling these methods.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellHueRange, *args)
        return ret

    def _get_point_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetPointLookupTable())
    def _set_point_lookup_table(self, arg):
        old_val = self._get_point_lookup_table()
        self._wrap_call(self._vtk_obj.SetPointLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('point_lookup_table', old_val, arg)
    point_lookup_table = traits.Property(_get_point_lookup_table, _set_point_lookup_table, help=\
        """
        Set/Get the point lookup table.
        """
    )

    def get_cell_alpha_range(self, *args):
        """
        V.get_cell_alpha_range(float, float)
        C++: virtual void GetCellAlphaRange(double &mn, double &mx)
        V.get_cell_alpha_range([float, float])
        C++: virtual void GetCellAlphaRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetCellAlphaRange, *args)
        return ret

    def set_cell_alpha_range(self, *args):
        """
        V.set_cell_alpha_range(float, float)
        C++: virtual void SetCellAlphaRange(double mn, double mx)
        V.set_cell_alpha_range([float, float])
        C++: virtual void SetCellAlphaRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetCellAlphaRange, *args)
        return ret

    selected_point_color = tvtk_base.vtk_color_trait((1.0, 0.0, 1.0), help=\
        """
        
        """
    )
    def _selected_point_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedPointColor,
                        self.selected_point_color, False)

    line_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The width of lines or edges
        """
    )
    def _line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineWidth,
                        self.line_width)

    point_size = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        The size of points or vertices
        """
    )
    def _point_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointSize,
                        self.point_size)

    def _get_cell_text_property(self):
        return wrap_vtk(self._vtk_obj.GetCellTextProperty())
    def _set_cell_text_property(self, arg):
        old_val = self._get_cell_text_property()
        self._wrap_call(self._vtk_obj.SetCellTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('cell_text_property', old_val, arg)
    cell_text_property = traits.Property(_get_cell_text_property, _set_cell_text_property, help=\
        """
        The text property to use for labelling edges/cells.
        """
    )

    selected_point_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The color of selected points or vertices.
        """
    )
    def _selected_point_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedPointOpacity,
                        self.selected_point_opacity)

    point_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The color and opacity of points or vertices when not mapped
        through a lookup table.
        """
    )
    def _point_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointOpacity,
                        self.point_opacity)

    def get_point_value_range(self, *args):
        """
        V.get_point_value_range(float, float)
        C++: virtual void GetPointValueRange(double &mn, double &mx)
        V.get_point_value_range([float, float])
        C++: virtual void GetPointValueRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetPointValueRange, *args)
        return ret

    def set_point_value_range(self, *args):
        """
        V.set_point_value_range(float, float)
        C++: virtual void SetPointValueRange(double mn, double mx)
        V.set_point_value_range([float, float])
        C++: virtual void SetPointValueRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetPointValueRange, *args)
        return ret

    selected_cell_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The color of selected cells or edges.
        """
    )
    def _selected_cell_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedCellOpacity,
                        self.selected_cell_opacity)

    def get_cell_value_range(self, *args):
        """
        V.get_cell_value_range(float, float)
        C++: virtual void GetCellValueRange(double &mn, double &mx)
        V.get_cell_value_range([float, float])
        C++: virtual void GetCellValueRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetCellValueRange, *args)
        return ret

    def set_cell_value_range(self, *args):
        """
        V.set_cell_value_range(float, float)
        C++: virtual void SetCellValueRange(double mn, double mx)
        V.set_cell_value_range([float, float])
        C++: virtual void SetCellValueRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetCellValueRange, *args)
        return ret

    def get_point_saturation_range(self, *args):
        """
        V.get_point_saturation_range(float, float)
        C++: virtual void GetPointSaturationRange(double &mn, double &mx)
        V.get_point_saturation_range([float, float])
        C++: virtual void GetPointSaturationRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetPointSaturationRange, *args)
        return ret

    def set_point_saturation_range(self, *args):
        """
        V.set_point_saturation_range(float, float)
        C++: virtual void SetPointSaturationRange(double mn, double mx)
        V.set_point_saturation_range([float, float])
        C++: virtual void SetPointSaturationRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetPointSaturationRange, *args)
        return ret

    def _get_point_text_property(self):
        return wrap_vtk(self._vtk_obj.GetPointTextProperty())
    def _set_point_text_property(self, arg):
        old_val = self._get_point_text_property()
        self._wrap_call(self._vtk_obj.SetPointTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('point_text_property', old_val, arg)
    point_text_property = traits.Property(_get_point_text_property, _set_point_text_property, help=\
        """
        The text property to use for labelling points/vertices.
        """
    )

    def get_vertex_label_color(self, *args):
        """
        V.get_vertex_label_color(float, float, float)
        C++: virtual void GetVertexLabelColor(double &r, double &g,
            double &b)
        V.get_vertex_label_color([float, float, float])
        C++: virtual void GetVertexLabelColor(double c[3])
        The color to use for labelling graph vertices. This is
        deprecated. Use get_point_text_property()->_set_color() instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetVertexLabelColor, *args)
        return ret

    def set_vertex_label_color(self, *args):
        """
        V.set_vertex_label_color(float, float, float)
        C++: virtual void SetVertexLabelColor(double r, double g,
            double b)
        V.set_vertex_label_color([float, float, float])
        C++: virtual void SetVertexLabelColor(double c[3])
        The color to use for labelling graph vertices. This is
        deprecated. Use get_point_text_property()->_set_color() instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetVertexLabelColor, *args)
        return ret

    def _get_cell_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetCellLookupTable())
    def _set_cell_lookup_table(self, arg):
        old_val = self._get_cell_lookup_table()
        self._wrap_call(self._vtk_obj.SetCellLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('cell_lookup_table', old_val, arg)
    cell_lookup_table = traits.Property(_get_cell_lookup_table, _set_cell_lookup_table, help=\
        """
        Set/Get the cell lookup table.
        """
    )

    background_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    point_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _point_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointColor,
                        self.point_color, False)

    cell_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _cell_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellColor,
                        self.cell_color, False)

    outline_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _outline_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineColor,
                        self.outline_color, False)

    background_color2 = tvtk_base.vtk_color_trait((0.29999999999999999, 0.29999999999999999, 0.29999999999999999), help=\
        """
        
        """
    )
    def _background_color2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor2,
                        self.background_color2, False)

    def get_edge_label_color(self, *args):
        """
        V.get_edge_label_color(float, float, float)
        C++: virtual void GetEdgeLabelColor(double &r, double &g,
            double &b)
        V.get_edge_label_color([float, float, float])
        C++: virtual void GetEdgeLabelColor(double c[3])
        The color to use for labelling graph edges. This is deprecated.
        Use get_cell_text_property()->_set_color() instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeLabelColor, *args)
        return ret

    def set_edge_label_color(self, *args):
        """
        V.set_edge_label_color(float, float, float)
        C++: virtual void SetEdgeLabelColor(double r, double g, double b)
        V.set_edge_label_color([float, float, float])
        C++: virtual void SetEdgeLabelColor(double c[3])
        The color to use for labelling graph edges. This is deprecated.
        Use get_cell_text_property()->_set_color() instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetEdgeLabelColor, *args)
        return ret

    def get_cell_saturation_range(self, *args):
        """
        V.get_cell_saturation_range(float, float)
        C++: virtual void GetCellSaturationRange(double &mn, double &mx)
        V.get_cell_saturation_range([float, float])
        C++: virtual void GetCellSaturationRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.GetCellSaturationRange, *args)
        return ret

    def set_cell_saturation_range(self, *args):
        """
        V.set_cell_saturation_range(float, float)
        C++: virtual void SetCellSaturationRange(double mn, double mx)
        V.set_cell_saturation_range([float, float])
        C++: virtual void SetCellSaturationRange(double rng[2])"""
        ret = self._wrap_call(self._vtk_obj.SetCellSaturationRange, *args)
        return ret

    def create_mellow_theme(self):
        """
        V.create_mellow_theme() -> ViewTheme
        C++: static ViewTheme *CreateMellowTheme()
        Convenience methods for creating some default view themes. The
        return reference is reference-counted, so you will have to call
        Delete() on the reference when you are finished with it.
        """
        ret = wrap_vtk(self._vtk_obj.CreateMellowTheme())
        return ret
        

    def create_neon_theme(self):
        """
        V.create_neon_theme() -> ViewTheme
        C++: static ViewTheme *CreateNeonTheme()
        Convenience methods for creating some default view themes. The
        return reference is reference-counted, so you will have to call
        Delete() on the reference when you are finished with it.
        """
        ret = wrap_vtk(self._vtk_obj.CreateNeonTheme())
        return ret
        

    def create_ocean_theme(self):
        """
        V.create_ocean_theme() -> ViewTheme
        C++: static ViewTheme *CreateOceanTheme()
        Convenience methods for creating some default view themes. The
        return reference is reference-counted, so you will have to call
        Delete() on the reference when you are finished with it.
        """
        ret = wrap_vtk(self._vtk_obj.CreateOceanTheme())
        return ret
        

    def lookup_matches_cell_theme(self, *args):
        """
        V.lookup_matches_cell_theme(ScalarsToColors) -> bool
        C++: bool LookupMatchesCellTheme(ScalarsToColors *s2c)
        Whether a given lookup table matches the point or cell theme of
        this theme.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.LookupMatchesCellTheme, *my_args)
        return ret

    def lookup_matches_point_theme(self, *args):
        """
        V.lookup_matches_point_theme(ScalarsToColors) -> bool
        C++: bool LookupMatchesPointTheme(ScalarsToColors *s2c)
        Whether a given lookup table matches the point or cell theme of
        this theme.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.LookupMatchesPointTheme, *my_args)
        return ret

    _updateable_traits_ = \
    (('line_width', 'GetLineWidth'), ('outline_color', 'GetOutlineColor'),
    ('point_size', 'GetPointSize'), ('point_color', 'GetPointColor'),
    ('background_color2', 'GetBackgroundColor2'), ('selected_point_color',
    'GetSelectedPointColor'), ('selected_cell_opacity',
    'GetSelectedCellOpacity'), ('cell_opacity', 'GetCellOpacity'),
    ('scale_point_lookup_table', 'GetScalePointLookupTable'),
    ('cell_color', 'GetCellColor'), ('selected_point_opacity',
    'GetSelectedPointOpacity'), ('reference_count', 'GetReferenceCount'),
    ('scale_cell_lookup_table', 'GetScaleCellLookupTable'),
    ('selected_cell_color', 'GetSelectedCellColor'), ('background_color',
    'GetBackgroundColor'), ('point_opacity', 'GetPointOpacity'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scale_cell_lookup_table',
    'scale_point_lookup_table', 'background_color', 'background_color2',
    'cell_color', 'cell_opacity', 'line_width', 'outline_color',
    'point_color', 'point_opacity', 'point_size', 'selected_cell_color',
    'selected_cell_opacity', 'selected_point_color',
    'selected_point_opacity'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ViewTheme, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ViewTheme properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scale_cell_lookup_table',
            'scale_point_lookup_table'], [], ['background_color',
            'background_color2', 'cell_color', 'cell_opacity', 'line_width',
            'outline_color', 'point_color', 'point_opacity', 'point_size',
            'selected_cell_color', 'selected_cell_opacity',
            'selected_point_color', 'selected_point_opacity']),
            title='Edit ViewTheme properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ViewTheme properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

