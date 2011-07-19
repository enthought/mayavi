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


class GlyphSource2D(PolyDataAlgorithm):
    """
    GlyphSource2D - create 2d glyphs represented by PolyData
    
    Superclass: PolyDataAlgorithm
    
    GlyphSource2D can generate a family of 2d glyphs each of which
    lies in the x-y plane (i.e., the z-coordinate is zero). The class is
    a helper class to be used with Glyph2D and XYPlotActor.
    
    To use this class, specify the glyph type to use and its attributes.
    Attributes include its position (i.e., center point), scale, color,
    and whether the symbol is filled or not (a polygon or closed line
    sequence). You can also put a short line through the glyph running
    from -x to +x (the glyph looks like it's on a line), or a cross.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyphSource2D, obj, update, **traits)
    
    dash = tvtk_base.false_bool_trait(help=\
        """
        Specify whether a short line segment is drawn through the glyph.
        (This is in addition to the glyph. If the glyph type is set to
        "Dash" there is no need to enable this flag.)
        """
    )
    def _dash_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDash,
                        self.dash_)

    cross = tvtk_base.false_bool_trait(help=\
        """
        Specify whether a cross is drawn as part of the glyph. (This is
        in addition to the glyph. If the glyph type is set to "Cross"
        there is no need to enable this flag.)
        """
    )
    def _cross_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCross,
                        self.cross_)

    filled = tvtk_base.true_bool_trait(help=\
        """
        Specify whether the glyph is filled (a polygon) or not (a closed
        polygon defined by line segments). This only applies to 2d closed
        glyphs.
        """
    )
    def _filled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilled,
                        self.filled_)

    glyph_type = traits.Trait('vertex',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'diamond': 8, 'triangle': 5, 'thick_cross': 4, 'vertex': 1, 'cross': 3, 'dash': 2, 'thick_arrow': 10, 'square': 6, 'hooked_arrow': 11, 'arrow': 9, 'circle': 7, 'edge_arrow': 12}), help=\
        """
        Specify the type of glyph to generate.
        """
    )
    def _glyph_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphType,
                        self.glyph_type_)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    rotation_angle = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify an angle (in degrees) to rotate the glyph around the
        z-axis. Using this ivar, it is possible to generate rotated
        glyphs (e.g., crosses, arrows, etc.)
        """
    )
    def _rotation_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationAngle,
                        self.rotation_angle)

    scale = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the scale of the glyph. Note that the glyphs are designed to
        fit in the (1,1) rectangle.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    scale2 = traits.Trait(1.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the scale of optional portions of the glyph (e.g., the dash
        and cross is dash_on() and cross_on()).
        """
    )
    def _scale2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale2,
                        self.scale2)

    _updateable_traits_ = \
    (('rotation_angle', 'GetRotationAngle'), ('glyph_type',
    'GetGlyphType'), ('scale', 'GetScale'), ('center', 'GetCenter'),
    ('scale2', 'GetScale2'), ('color', 'GetColor'), ('progress_text',
    'GetProgressText'), ('cross', 'GetCross'), ('dash', 'GetDash'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('filled',
    'GetFilled'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cross', 'dash', 'debug', 'filled',
    'global_warning_display', 'release_data_flag', 'glyph_type', 'center',
    'color', 'progress_text', 'rotation_angle', 'scale', 'scale2'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GlyphSource2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cross', 'dash', 'filled'], ['glyph_type'], ['center',
            'color', 'rotation_angle', 'scale', 'scale2']),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

