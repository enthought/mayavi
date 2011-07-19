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


class ImageOrthoPlanes(Object):
    """
    ImageOrthoPlanes - Connect three ImagePlaneWidgets together
    
    Superclass: Object
    
    ImageOrthoPlanes is an event observer class that listens to the
    events from three ImagePlaneWidgets and keeps their orientations
    and scales synchronized.
    
    See Also:
    
    ImagePlaneWidget
    
    Thanks:
    
    Thanks to Atamai Inc. for developing and contributing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageOrthoPlanes, obj, update, **traits)
    
    def get_plane(self, *args):
        """
        V.get_plane(int) -> ImagePlaneWidget
        C++: ImagePlaneWidget *GetPlane(int i)
        You must set three planes for the widget.
        """
        ret = self._wrap_call(self._vtk_obj.GetPlane, *args)
        return wrap_vtk(ret)

    def set_plane(self, *args):
        """
        V.set_plane(int, ImagePlaneWidget)
        C++: void SetPlane(int i, ImagePlaneWidget *imagePlaneWidget)
        You must set three planes for the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlane, *my_args)
        return ret

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Get the transform for the planes.
        """
    )

    def handle_plane_event(self, *args):
        """
        V.handle_plane_event(ImagePlaneWidget)
        C++: void HandlePlaneEvent(ImagePlaneWidget *imagePlaneWidget)
        A public method to be used only by the event callback.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HandlePlaneEvent, *my_args)
        return ret

    def reset_planes(self):
        """
        V.reset_planes()
        C++: void ResetPlanes()
        Reset the planes to original scale, rotation, and location.
        """
        ret = self._vtk_obj.ResetPlanes()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageOrthoPlanes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageOrthoPlanes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ImageOrthoPlanes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageOrthoPlanes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

