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

from tvtk.tvtk_classes.abstract_mapper import AbstractMapper


class Mapper2D(AbstractMapper):
    """
    Mapper2D - abstract class specifies interface for objects which
    render 2d actors
    
    Superclass: AbstractMapper
    
    Mapper2D is an abstract class which defines the interface for
    objects which render two dimensional actors (vtk_actor2d).
    
    See Also:
    
    Actor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMapper2D, obj, update, **traits)
    
    def has_translucent_polygonal_geometry(self):
        """
        V.has_translucent_polygonal_geometry() -> int
        C++: virtual int HasTranslucentPolygonalGeometry()"""
        ret = self._vtk_obj.HasTranslucentPolygonalGeometry()
        return ret
        

    def render_opaque_geometry(self, *args):
        """
        V.render_opaque_geometry(Viewport, Actor2D)
        C++: virtual void RenderOpaqueGeometry(Viewport *,
            Actor2D *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderOpaqueGeometry, *my_args)
        return ret

    def render_overlay(self, *args):
        """
        V.render_overlay(Viewport, Actor2D)
        C++: virtual void RenderOverlay(Viewport *, Actor2D *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderOverlay, *my_args)
        return ret

    def render_translucent_polygonal_geometry(self, *args):
        """
        V.render_translucent_polygonal_geometry(Viewport, Actor2D)
        C++: virtual void RenderTranslucentPolygonalGeometry(
            Viewport *, Actor2D *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentPolygonalGeometry, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Mapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Mapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Mapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Mapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

