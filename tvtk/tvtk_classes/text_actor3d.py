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

from tvtk.tvtk_classes.prop3d import Prop3D


class TextActor3D(Prop3D):
    """
    TextActor3D - An actor that displays text.
    
    Superclass: Prop3D
    
    The input text is rendered into a buffer, which in turn is used as a
    texture applied onto a quad (a ImageActor is used under the hood).
    
    Warning:
    
    This class is experimental at the moment.
    - The orientation is not optimized, the quad should be oriented, not
      the text itself when it is rendered in the buffer (we end up with
      excessively big textures for 45 degrees angles). This will be fixed
    first.
    - No checking is done at the moment regarding hardware texture size
      limits.
    - Alignment is not supported (soon).
    - Multiline is not supported.
    - Need to fix angle out of 0<->360
    
    See Also:
    
    Prop3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextActor3D, obj, update, **traits)
    
    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the text string to be displayed.
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

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box([int, int, int, int]) -> int
        C++: int GetBoundingBox(int bbox[4])
        Get the Freetype-derived real bounding box for the given
        TextProperty and text string str.  Results are returned in the
        four element bbox int array.  This call can be used for sizing
        other elements.
        """
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'), ('orientation',
    'GetOrientation'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextActor3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale']),
            title='Edit TextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

