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


class ArrowSource(PolyDataAlgorithm):
    """
    ArrowSource - Appends a cylinder to a cone to form an arrow.
    
    Superclass: PolyDataAlgorithm
    
    ArrowSource was intended to be used as the source for a glyph. The
    shaft base is always at (0,0,0). The arrow tip is always at (1,0,0).
    If "Invert" is true, then the ends are flipped i.e. tip is at (0,0,0)
    while base is at (1, 0, 0). The resolution of the cone and shaft can
    be set and default to 6. The radius of the cone and shaft can be set
    and default to 0.03 and 0.1. The length of the tip can also be set,
    and defaults to 0.35.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrowSource, obj, update, **traits)
    
    invert = tvtk_base.false_bool_trait(help=\
        """
        Inverts the arrow direction. When set to true, base is at (1, 0,
        0) while the tip is at (0, 0, 0). The default is false, i.e. base
        at (0, 0, 0) and the tip at (1, 0, 0).
        """
    )
    def _invert_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInvert,
                        self.invert_)

    tip_radius = traits.Trait(0.1, traits.Range(0.0, 10.0, enter_set=True, auto_set=False), help=\
        """
        Set the length, and radius of the tip.  They default to 0.35 and
        0.1
        """
    )
    def _tip_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTipRadius,
                        self.tip_radius)

    tip_resolution = traits.Trait(6, traits.Range(1, 128, enter_set=True, auto_set=False), help=\
        """
        Set the resolution of the tip.  The tip behaves the same as a
        cone. Resoultion 1 gives a single triangle, 2 gives two crossed
        triangles.
        """
    )
    def _tip_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTipResolution,
                        self.tip_resolution)

    shaft_radius = traits.Trait(0.03, traits.Range(0.0, 5.0, enter_set=True, auto_set=False), help=\
        """
        Set the radius of the shaft.  Defaults to 0.03.
        """
    )
    def _shaft_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShaftRadius,
                        self.shaft_radius)

    tip_length = traits.Trait(0.35, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the length, and radius of the tip.  They default to 0.35 and
        0.1
        """
    )
    def _tip_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTipLength,
                        self.tip_length)

    shaft_resolution = traits.Trait(6, traits.Range(0, 128, enter_set=True, auto_set=False), help=\
        """
        Set the resolution of the shaft.  2 gives a rectangle. I would
        like to extend the cone to produce a line, but this is not an
        option now.
        """
    )
    def _shaft_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShaftResolution,
                        self.shaft_resolution)

    _updateable_traits_ = \
    (('tip_resolution', 'GetTipResolution'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('tip_radius', 'GetTipRadius'),
    ('shaft_resolution', 'GetShaftResolution'), ('invert', 'GetInvert'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('shaft_radius', 'GetShaftRadius'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('tip_length', 'GetTipLength'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'invert',
    'release_data_flag', 'progress_text', 'shaft_radius',
    'shaft_resolution', 'tip_length', 'tip_radius', 'tip_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrowSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrowSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['invert'], [], ['shaft_radius', 'shaft_resolution',
            'tip_length', 'tip_radius', 'tip_resolution']),
            title='Edit ArrowSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrowSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

