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

from tvtk.tvtk_classes.geo_source import GeoSource


class GeoFileTerrainSource(GeoSource):
    """
    GeoFileTerrainSource - A source for tiled geometry on disk.
    
    Superclass: GeoSource
    
    GeoFileTerrainSource reads geometry tiles as .vtp files from a
    directory that follow a certain naming convention containing the
    level of the patch and the position within that level. Use
    GeoTerrain's save_database method to create a database of files in
    this format.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoFileTerrainSource, obj, update, **traits)
    
    path = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The path the tiled geometry database.
        """
    )
    def _path_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPath,
                        self.path)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('path', 'GetPath'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'path'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoFileTerrainSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoFileTerrainSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['path']),
            title='Edit GeoFileTerrainSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoFileTerrainSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

