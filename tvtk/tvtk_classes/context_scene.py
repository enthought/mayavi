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


class ContextScene(Object):
    """
    ContextScene - Provides a 2d scene for ContextItem objects.
    
    Superclass: Object
    
    Provides a 2d scene that ContextItem objects can be added to.
    Manages the items, ensures that they are rendered at the right times
    and passes on mouse events.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextScene, obj, update, **traits)
    
    scale_tiles = tvtk_base.true_bool_trait(help=\
        """
        Whether to scale the scene transform when tiling, for example
        when using WindowToImageFilter to take a large screenshot. The
        default is true.
        """
    )
    def _scale_tiles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleTiles,
                        self.scale_tiles_)

    geometry = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometry,
                        self.geometry)

    use_buffer_id = traits.Bool(True, help=\
        """
        Set whether the scene should use the color buffer. Default is
        true.
        """
    )
    def _use_buffer_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBufferId,
                        self.use_buffer_id)

    def _get_annotation_link(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLink())
    def _set_annotation_link(self, arg):
        old_val = self._get_annotation_link()
        self._wrap_call(self._vtk_obj.SetAnnotationLink,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_link', old_val, arg)
    annotation_link = traits.Property(_get_annotation_link, _set_annotation_link, help=\
        """
        Get the AnnotationLink for the chart.
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Get the transform for the scene.
        """
    )

    def _get_buffer_id(self):
        return wrap_vtk(self._vtk_obj.GetBufferId())
    buffer_id = traits.Property(_get_buffer_id, help=\
        """
        Return buffer id. Not part of the end-user API. Can be used by
        context items to initialize their own colorbuffer id (when a
        context item is a container).
        """
    )

    def get_item(self, *args):
        """
        V.get_item(int) -> AbstractContextItem
        C++: AbstractContextItem *GetItem(unsigned int index)
        Get the item at the specified index.
        \return the item at the specified index (null if index is
            invalid).
        """
        ret = self._wrap_call(self._vtk_obj.GetItem, *args)
        return wrap_vtk(ret)

    def _get_number_of_items(self):
        return self._vtk_obj.GetNumberOfItems()
    number_of_items = traits.Property(_get_number_of_items, help=\
        """
        Get the number of child items.
        """
    )

    def _get_scene_height(self):
        return self._vtk_obj.GetSceneHeight()
    scene_height = traits.Property(_get_scene_height, help=\
        """
        Get the height of the scene.
        """
    )

    def _get_scene_width(self):
        return self._vtk_obj.GetSceneWidth()
    scene_width = traits.Property(_get_scene_width, help=\
        """
        Get the width of the scene.
        """
    )

    def _get_view_height(self):
        return self._vtk_obj.GetViewHeight()
    view_height = traits.Property(_get_view_height, help=\
        """
        Get the height of the view
        """
    )

    def _get_view_width(self):
        return self._vtk_obj.GetViewWidth()
    view_width = traits.Property(_get_view_width, help=\
        """
        Get the width of the view
        """
    )

    def add_item(self, *args):
        """
        V.add_item(AbstractContextItem) -> int
        C++: unsigned int AddItem(AbstractContextItem *item)
        Add child items to this item. Increments reference count of item.
        \return the index of the child item.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddItem, *my_args)
        return ret

    def clear_items(self):
        """
        V.clear_items()
        C++: void ClearItems()
        Remove all child items from this item.
        """
        ret = self._vtk_obj.ClearItems()
        return ret
        

    def has_transform(self):
        """
        V.has_transform() -> bool
        C++: bool HasTransform()
        Check whether the scene has a transform.
        """
        ret = self._vtk_obj.HasTransform()
        return ret
        

    def paint(self, *args):
        """
        V.paint(Context2D) -> bool
        C++: virtual bool Paint(Context2D *painter)
        Paint event for the chart, called whenever the chart needs to be
        drawn
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Paint, *my_args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()
        Release graphics resources hold by the scene.
        """
        ret = self._vtk_obj.ReleaseGraphicsResources()
        return ret
        

    def remove_item(self, *args):
        """
        V.remove_item(AbstractContextItem) -> bool
        C++: bool RemoveItem(AbstractContextItem *item)
        V.remove_item(int) -> bool
        C++: bool RemoveItem(unsigned int index)
        Remove child item from this item. Decrements reference count of
        item.
        \param item the item to be removed.
        \return true on success, false otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveItem, *my_args)
        return ret

    def set_dirty(self, *args):
        """
        V.set_dirty(bool)
        C++: void SetDirty(bool isDirty)
        Inform the scene that something changed that requires a repaint
        of the scene. This should only be used by the ContextItem
        derived objects in a scene in their event handlers.
        """
        ret = self._wrap_call(self._vtk_obj.SetDirty, *args)
        return ret

    def set_interactor_style(self, *args):
        """
        V.set_interactor_style(InteractorStyle)
        C++: void SetInteractorStyle(InteractorStyle *interactor)
        Add the scene as an observer on the supplied interactor style.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInteractorStyle, *my_args)
        return ret

    def set_renderer(self, *args):
        """
        V.set_renderer(Renderer)
        C++: virtual void SetRenderer(Renderer *renderer)
        This should not be necessary as the context view should take care
        of rendering.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRenderer, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_buffer_id', 'GetUseBufferId'),
    ('geometry', 'GetGeometry'), ('debug', 'GetDebug'), ('scale_tiles',
    'GetScaleTiles'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scale_tiles', 'geometry',
    'use_buffer_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextScene, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scale_tiles'], [], ['geometry', 'use_buffer_id']),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

