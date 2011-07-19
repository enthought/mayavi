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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class BalloonRepresentation(WidgetRepresentation):
    """
    BalloonRepresentation - represent the BalloonWidget
    
    Superclass: WidgetRepresentation
    
    The BalloonRepresentation is used to represent the
    BalloonWidget. This representation is defined by two items: a text
    string and an image. At least one of these two items must be defined,
    but it is allowable to specify both, or just an image or just text.
    If both the text and image are specified, then methods are available
    for positioning the text and image with respect to each other.
    
    The balloon representation consists of three parts: text, a
    rectangular frame behind the text, and an image placed next to the
    frame and sized to match the frame.
    
    The size of the balloon is ultimately controlled by the text
    properties (i.e., font size). This representation uses a layout
    policy as follows.
    
    If there is just text and no image, then the text properties and
    padding are used to control the size of the balloon.
    
    If there is just an image and no text, then the image_size[_2] member
    is used to control the image size. (The image will fit into this
    rectangle, but will not necessarily fill the whole rectangle, i.e.,
    the image is not stretched).
    
    If there is text and an image, the following approach ia used. First,
    based on the font size and other related properties (e.g., padding),
    determine the size of the frame. Second, depending on the layout of
    the image and text frame, control the size of the neighboring image
    (since the frame and image share a common edge). However, if this
    results in an image that is smaller than image_size[_2], then the image
    size will be set to image_size[_2] and the frame will be adjusted
    accordingly. The text is always placed in the center of the frame if
    the frame is resized.
    
    See Also:
    
    BalloonWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBalloonRepresentation, obj, update, **traits)
    
    balloon_layout = traits.Trait('text_bottom',
    tvtk_base.TraitRevPrefixMap({'text_bottom': 3, 'image_bottom': 2, 'text_right': 0, 'text_top': 2, 'text_left': 1, 'image_left': 0, 'image_top': 3, 'image_right': 1}), help=\
        """
        Specify the layout of the image and text within the balloon. Note
        that there are reduncies in these methods, for example
        set_balloon_layout_to_image_left() results in the same effect as
        set_balloon_layout_to_text_right(). If only text is specified, or only
        an image is specified, then it doesn't matter how the layout is
        specified.
        """
    )
    def _balloon_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBalloonLayout,
                        self.balloon_layout_)

    image_size = traits.Array(shape=(2,), value=(50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _image_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSize,
                        self.image_size)

    def _get_frame_property(self):
        return wrap_vtk(self._vtk_obj.GetFrameProperty())
    def _set_frame_property(self, arg):
        old_val = self._get_frame_property()
        self._wrap_call(self._vtk_obj.SetFrameProperty,
                        deref_vtk(arg))
        self.trait_property_changed('frame_property', old_val, arg)
    frame_property = traits.Property(_get_frame_property, _set_frame_property, help=\
        """
        Set/get the frame property (relevant only if text is shown). The
        frame lies behind the text.
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
        Set/get the text property (relevant only if text is shown).
        """
    )

    def _get_image_property(self):
        return wrap_vtk(self._vtk_obj.GetImageProperty())
    def _set_image_property(self, arg):
        old_val = self._get_image_property()
        self._wrap_call(self._vtk_obj.SetImageProperty,
                        deref_vtk(arg))
        self.trait_property_changed('image_property', old_val, arg)
    image_property = traits.Property(_get_image_property, _set_image_property, help=\
        """
        Set/get the image property (relevant only if an image is shown).
        """
    )

    padding = traits.Trait(5, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the padding (in pixels) that is used between the text and
        the frame.
        """
    )
    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    offset = traits.Array(shape=(2,), value=(15, -30), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    def _get_balloon_image(self):
        return wrap_vtk(self._vtk_obj.GetBalloonImage())
    def _set_balloon_image(self, arg):
        old_val = self._get_balloon_image()
        self._wrap_call(self._vtk_obj.SetBalloonImage,
                        deref_vtk(arg))
        self.trait_property_changed('balloon_image', old_val, arg)
    balloon_image = traits.Property(_get_balloon_image, _set_balloon_image, help=\
        """
        Specify/retrieve the image to display in the balloon.
        """
    )

    balloon_text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify/retrieve the text to display in the balloon.
        """
    )
    def _balloon_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBalloonText,
                        self.balloon_text)

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('balloon_layout', 'GetBalloonLayout'),
    ('handle_size', 'GetHandleSize'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('offset', 'GetOffset'), ('visibility',
    'GetVisibility'), ('padding', 'GetPadding'), ('reference_count',
    'GetReferenceCount'), ('image_size', 'GetImageSize'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('balloon_text', 'GetBalloonText'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('place_factor', 'GetPlaceFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'balloon_layout',
    'allocated_render_time', 'balloon_text', 'estimated_render_time',
    'handle_size', 'image_size', 'offset', 'padding', 'place_factor',
    'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BalloonRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BalloonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'],
            ['balloon_layout'], ['allocated_render_time', 'balloon_text',
            'estimated_render_time', 'handle_size', 'image_size', 'offset',
            'padding', 'place_factor', 'render_time_multiplier']),
            title='Edit BalloonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BalloonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

