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


class AbstractContextItem(Object):
    """
    AbstractContextItem - base class for items that are part of a
    
    Superclass: Object
    
    This class is the common base for all context scene items. You should
    generally derive from ContextItem, rather than this class, as it
    provides most of the commonly used API.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractContextItem, obj, update, **traits)
    
    visible = traits.Bool(True, help=\
        """
        Set the visibility of the item (should it be drawn). Visible by
        default.
        """
    )
    def _visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVisible,
                        self.visible)

    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Get the ContextScene for the item, always set for an item in a
        scene.
        """
    )

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Get the parent item. The parent will be set for all items except
        top level items in a tree.
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
        

    def paint(self, *args):
        """
        V.paint(Context2D) -> bool
        C++: virtual bool Paint(Context2D *painter)
        Paint event for the item, called whenever the item needs to be
        drawn.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Paint, *my_args)
        return ret

    def paint_children(self, *args):
        """
        V.paint_children(Context2D) -> bool
        C++: bool PaintChildren(Context2D *painter)
        Paint the children of the item, should be called whenever the
        children need to be rendered.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PaintChildren, *my_args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: virtual void ReleaseGraphicsResources()
        Release graphics resources hold by the item. The default
        implementation is empty.
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

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Perform any updates to the item that may be necessary before
        rendering. The scene should take care of calling this on all
        items before their Paint function is invoked.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('visible', 'GetVisible'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractContextItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['visible']),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

