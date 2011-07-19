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

from tvtk.tvtk_classes.geo_tree_node import GeoTreeNode


class GeoImageNode(GeoTreeNode):
    """
    GeoImageNode - A node in a multi-resolution image tree.
    
    Superclass: GeoTreeNode
    
    GeoImageNode contains an image tile in a multi-resolution image
    tree, along with metadata about that image's extents.
    
    See Also:
    
    GeoTreeNode GeoTerrainNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoImageNode, obj, update, **traits)
    
    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    def _set_image(self, arg):
        old_val = self._get_image()
        self._wrap_call(self._vtk_obj.SetImage,
                        deref_vtk(arg))
        self.trait_property_changed('image', old_val, arg)
    image = traits.Property(_get_image, _set_image, help=\
        """
        Get the image tile.
        """
    )

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    def _set_texture(self, arg):
        old_val = self._get_texture()
        self._wrap_call(self._vtk_obj.SetTexture,
                        deref_vtk(arg))
        self.trait_property_changed('texture', old_val, arg)
    texture = traits.Property(_get_texture, _set_texture, help=\
        """
        Get the image tile.
        """
    )

    def get_child(self, *args):
        """
        V.get_child(int) -> GeoImageNode
        C++: GeoImageNode *GetChild(int idx)"""
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return wrap_vtk(ret)

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    parent = traits.Property(_get_parent, help=\
        """
        
        """
    )

    def load_an_image(self, *args):
        """
        V.load_an_image(string)
        C++: void LoadAnImage(const char *prefix)
        This loads the image from a tile database at the specified
        location.
        """
        ret = self._wrap_call(self._vtk_obj.LoadAnImage, *args)
        return ret

    _updateable_traits_ = \
    (('latitude_range', 'GetLatitudeRange'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('longitude_range', 'GetLongitudeRange'), ('level', 'GetLevel'),
    ('reference_count', 'GetReferenceCount'), ('id', 'GetId'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'id', 'latitude_range', 'level',
    'longitude_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoImageNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['id', 'latitude_range', 'level',
            'longitude_range']),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

