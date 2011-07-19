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

from tvtk.tvtk_classes.abstract_context_item import AbstractContextItem


class ContextTransform(AbstractContextItem):
    """
    ContextTransform - all children of this item are transformed
    
    Superclass: AbstractContextItem
    
    This class can be used to transform all child items of this class.
    The default transform is the identity.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextTransform, obj, update, **traits)
    
    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Access the Transform2D that controls object transformation.
        """
    )

    def rotate(self, *args):
        """
        V.rotate(float)
        C++: virtual void Rotate(float angle)
        Rotate the item by the specified angle.
        """
        ret = self._wrap_call(self._vtk_obj.Rotate, *args)
        return ret

    def scale(self, *args):
        """
        V.scale(float, float)
        C++: virtual void Scale(float dx, float dy)
        Scale the item by the specified amounts dx and dy in the x and y
        directions.
        """
        ret = self._wrap_call(self._vtk_obj.Scale, *args)
        return ret

    def translate(self, *args):
        """
        V.translate(float, float)
        C++: virtual void Translate(float dx, float dy)
        Translate the item by the specified amounts dx and dy in the x
        and y directions.
        """
        ret = self._wrap_call(self._vtk_obj.Translate, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('visible', 'GetVisible'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['visible']),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

