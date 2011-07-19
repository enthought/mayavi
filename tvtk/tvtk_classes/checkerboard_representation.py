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


class CheckerboardRepresentation(WidgetRepresentation):
    """
    CheckerboardRepresentation - represent the CheckerboardWidget
    
    Superclass: WidgetRepresentation
    
    The CheckerboardRepresentation is used to implement the
    representation of the CheckerboardWidget. The user can adjust the
    number of divisions in each of the i-j directions in a 2d image. A
    frame appears around the ImageActor with sliders along each side
    of the frame. The user can interactively adjust the sliders to the
    desired number of checkerboard subdivisions. The representation uses
    four instances of SliderRepresentation3D to implement itself.
    
    See Also:
    
    CheckerboardWidget ImageCheckerboard ImageActor
    SliderWidget RectilinearWipeWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCheckerboardRepresentation, obj, update, **traits)
    
    def _get_bottom_representation(self):
        return wrap_vtk(self._vtk_obj.GetBottomRepresentation())
    def _set_bottom_representation(self, arg):
        old_val = self._get_bottom_representation()
        self._wrap_call(self._vtk_obj.SetBottomRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('bottom_representation', old_val, arg)
    bottom_representation = traits.Property(_get_bottom_representation, _set_bottom_representation, help=\
        """
        Set and get the instances of SliderRepresention used to
        implement this representation. Normally default representations
        are created, but you can specify the ones you want to use.
        """
    )

    def _get_left_representation(self):
        return wrap_vtk(self._vtk_obj.GetLeftRepresentation())
    def _set_left_representation(self, arg):
        old_val = self._get_left_representation()
        self._wrap_call(self._vtk_obj.SetLeftRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('left_representation', old_val, arg)
    left_representation = traits.Property(_get_left_representation, _set_left_representation, help=\
        """
        Set and get the instances of SliderRepresention used to
        implement this representation. Normally default representations
        are created, but you can specify the ones you want to use.
        """
    )

    def _get_top_representation(self):
        return wrap_vtk(self._vtk_obj.GetTopRepresentation())
    def _set_top_representation(self, arg):
        old_val = self._get_top_representation()
        self._wrap_call(self._vtk_obj.SetTopRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('top_representation', old_val, arg)
    top_representation = traits.Property(_get_top_representation, _set_top_representation, help=\
        """
        Set and get the instances of SliderRepresention used to
        implement this representation. Normally default representations
        are created, but you can specify the ones you want to use.
        """
    )

    def _get_checkerboard(self):
        return wrap_vtk(self._vtk_obj.GetCheckerboard())
    def _set_checkerboard(self, arg):
        old_val = self._get_checkerboard()
        self._wrap_call(self._vtk_obj.SetCheckerboard,
                        deref_vtk(arg))
        self.trait_property_changed('checkerboard', old_val, arg)
    checkerboard = traits.Property(_get_checkerboard, _set_checkerboard, help=\
        """
        Specify an instance of ImageCheckerboard to manipulate.
        """
    )

    corner_offset = traits.Trait(0.0, traits.Range(0.0, 0.40000000000000002, enter_set=True, auto_set=False), help=\
        """
        Specify the offset of the ends of the sliders (on the boundary
        edges of the image) from the corner of the image. The offset is
        expressed as a normalized fraction of the border edges.
        """
    )
    def _corner_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerOffset,
                        self.corner_offset)

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    def _set_image_actor(self, arg):
        old_val = self._get_image_actor()
        self._wrap_call(self._vtk_obj.SetImageActor,
                        deref_vtk(arg))
        self.trait_property_changed('image_actor', old_val, arg)
    image_actor = traits.Property(_get_image_actor, _set_image_actor, help=\
        """
        Specify an instance of ImageActor to decorate.
        """
    )

    def _get_right_representation(self):
        return wrap_vtk(self._vtk_obj.GetRightRepresentation())
    def _set_right_representation(self, arg):
        old_val = self._get_right_representation()
        self._wrap_call(self._vtk_obj.SetRightRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('right_representation', old_val, arg)
    right_representation = traits.Property(_get_right_representation, _set_right_representation, help=\
        """
        Set and get the instances of SliderRepresention used to
        implement this representation. Normally default representations
        are created, but you can specify the ones you want to use.
        """
    )

    def slider_value_changed(self, *args):
        """
        V.slider_value_changed(int)
        C++: void SliderValueChanged(int sliderNum)
        This method is invoked by the CheckerboardWidget() when a
        value of some slider has changed.
        """
        ret = self._wrap_call(self._vtk_obj.SliderValueChanged, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('corner_offset', 'GetCornerOffset'),
    ('need_to_render', 'GetNeedToRender'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'corner_offset', 'estimated_render_time', 'handle_size',
    'place_factor', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CheckerboardRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CheckerboardRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'corner_offset', 'estimated_render_time',
            'handle_size', 'place_factor', 'render_time_multiplier']),
            title='Edit CheckerboardRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CheckerboardRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

