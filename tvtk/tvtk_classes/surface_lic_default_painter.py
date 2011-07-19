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

from tvtk.tvtk_classes.default_painter import DefaultPainter


class SurfaceLICDefaultPainter(DefaultPainter):
    """
    SurfaceLICDefaultPainter - DefaultPainter replacement that
    
    Superclass: DefaultPainter
    
    SurfaceLICDefaultPainter is a DefaultPainter replacement
     that inserts the SurfaceLICPainter at the correct position in the
    painter
     chain.
    
    See Also:
    
    
     DefaultPainter SurfaceLICPainter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSurfaceLICDefaultPainter, obj, update, **traits)
    
    def _get_surface_lic_painter(self):
        return wrap_vtk(self._vtk_obj.GetSurfaceLICPainter())
    def _set_surface_lic_painter(self, arg):
        old_val = self._get_surface_lic_painter()
        self._wrap_call(self._vtk_obj.SetSurfaceLICPainter,
                        deref_vtk(arg))
        self.trait_property_changed('surface_lic_painter', old_val, arg)
    surface_lic_painter = traits.Property(_get_surface_lic_painter, _set_surface_lic_painter, help=\
        """
        Get/Set the Surface LIC painter.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SurfaceLICDefaultPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SurfaceLICDefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SurfaceLICDefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SurfaceLICDefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

