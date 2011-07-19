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

from tvtk.tvtk_classes.button_source import ButtonSource


class RectangularButtonSource(ButtonSource):
    """
    RectangularButtonSource - create a rectangular button
    
    Superclass: ButtonSource
    
    RectangularButtonSource creates a rectangular shaped button with
    texture coordinates suitable for application of a texture map. This
    provides a way to make nice looking 3d buttons. The buttons are
    represented as PolyData that includes texture coordinates and
    normals. The button lies in the x-y plane.
    
    To use this class you must define its width, height and length. These
    measurements are all taken with respect to the shoulder of the
    button. The shoulder is defined as follows. Imagine a box sitting on
    the floor. The distance from the floor to the top of the box is the
    depth; the other directions are the length (x-direction) and height
    (y-direction). In this particular widget the box can have a smaller
    bottom than top. The ratio in size between bottom and top is called
    the box ratio (by default=1.0). The ratio of the texture region to
    the shoulder region is the texture ratio. And finally the texture
    region may be out of plane compared to the shoulder. The texture
    height ratio controls this.
    
    Caveats:
    
    The button is defined in the x-y plane. Use
    TransformPolyDataFilter or Glyph3D to orient the button in a
    different direction.
    
    See Also:
    
    ButtonSource EllipticalButtonSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectangularButtonSource, obj, update, **traits)
    
    box_ratio = traits.Trait(1.1, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the bottom of the button with the shoulder
        region. Numbers greater than one produce buttons with a wider
        bottom than shoulder; ratios less than one produce buttons that
        have a wider shoulder than bottom.
        """
    )
    def _box_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxRatio,
                        self.box_ratio)

    height = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the height of the button.
        """
    )
    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    width = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of the button.
        """
    )
    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    depth = traits.Trait(0.05, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
    )
    def _depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepth,
                        self.depth)

    texture_ratio = traits.Trait(0.9, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the texture region to the shoulder region.
        This number must be 0<=tr<=1. If the texture style is to fit the
        image, then satisfying the texture ratio may only be possible in
        one of the two directions (length or width) depending on the
        dimensions of the texture.
        """
    )
    def _texture_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureRatio,
                        self.texture_ratio)

    texture_height_ratio = traits.Trait(0.95, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the height of the texture region to the
        shoulder height. Values greater than 1.0 yield convex buttons
        with the texture region raised above the shoulder. Values less
        than 1.0 yield concave buttons with the texture region below the
        shoulder.
        """
    )
    def _texture_height_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureHeightRatio,
                        self.texture_height_ratio)

    _updateable_traits_ = \
    (('texture_style', 'GetTextureStyle'), ('texture_height_ratio',
    'GetTextureHeightRatio'), ('shoulder_texture_coordinate',
    'GetShoulderTextureCoordinate'), ('width', 'GetWidth'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'), ('box_ratio',
    'GetBoxRatio'), ('height', 'GetHeight'), ('texture_ratio',
    'GetTextureRatio'), ('texture_dimensions', 'GetTextureDimensions'),
    ('depth', 'GetDepth'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('two_sided',
    'GetTwoSided'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('center', 'GetCenter'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'two_sided', 'texture_style', 'box_ratio',
    'center', 'depth', 'height', 'progress_text',
    'shoulder_texture_coordinate', 'texture_dimensions',
    'texture_height_ratio', 'texture_ratio', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectangularButtonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['two_sided'], ['texture_style'], ['box_ratio',
            'center', 'depth', 'height', 'shoulder_texture_coordinate',
            'texture_dimensions', 'texture_height_ratio', 'texture_ratio',
            'width']),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

