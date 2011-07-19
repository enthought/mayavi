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


class GraphToGlyphs(PolyDataAlgorithm):
    """
    GraphToGlyphs - create glyphs for graph vertices
    
    Superclass: PolyDataAlgorithm
    
    Converts a Graph to a PolyData containing a glyph for each
    vertex. This assumes that the points of the graph have already been
    filled (perhaps by GraphLayout). The glyphs will automatically be
    scaled to be the same size in screen coordinates. To do this the
    filter requires a pointer to the renderer into which the glyphs will
    be rendered.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphToGlyphs, obj, update, **traits)
    
    filled = tvtk_base.true_bool_trait(help=\
        """
        Whether to fill the glyph, or to just render the outline.
        """
    )
    def _filled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilled,
                        self.filled_)

    scaling = traits.Bool(False, help=\
        """
        Whether to use the input array to process in order to scale the
        vertices.
        """
    )
    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling)

    glyph_type = traits.Int(7, enter_set=True, auto_set=False, help=\
        """
        The glyph type, specified as one of the enumerated values in this
        class. VERTEX is a special glyph that cannot be scaled, but
        instead is rendered as an open_gl vertex primitive. This may
        appear as a box or circle depending on the hardware.
        """
    )
    def _glyph_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphType,
                        self.glyph_type)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        The renderer in which the glyphs will be placed.
        """
    )

    screen_size = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the desired screen size of each glyph. If you are using
        scaling, this will be the size of the glyph when rendering an
        object with scaling value 1.0.
        """
    )
    def _screen_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenSize,
                        self.screen_size)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('screen_size', 'GetScreenSize'), ('progress_text',
    'GetProgressText'), ('scaling', 'GetScaling'), ('debug', 'GetDebug'),
    ('glyph_type', 'GetGlyphType'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('filled', 'GetFilled'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'filled', 'global_warning_display',
    'release_data_flag', 'glyph_type', 'progress_text', 'scaling',
    'screen_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphToGlyphs, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphToGlyphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['filled'], [], ['glyph_type', 'scaling',
            'screen_size']),
            title='Edit GraphToGlyphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphToGlyphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

