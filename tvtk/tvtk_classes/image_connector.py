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


class ImageConnector(Object):
    """
    ImageConnector - Create a binary image of a sphere.
    
    Superclass: Object
    
    ImageConnector is a helper class for connectivity filters. It is
    not meant to be used directly. It implements a stack and breadth
    first search necessary for some connectivity filters.  Filtered axes
    sets the dimensionality of the neighbor comparison, and cannot be
    more than three dimensions. As implemented, only voxels which share
    faces are considered neighbors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageConnector, obj, update, **traits)
    
    connected_value = traits.Int(255, enter_set=True, auto_set=False, help=\
        """
        Values used by the mark_region method
        """
    )
    def _connected_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConnectedValue,
                        self.connected_value)

    unconnected_value = traits.Int(128, enter_set=True, auto_set=False, help=\
        """
        Values used by the mark_region method
        """
    )
    def _unconnected_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnconnectedValue,
                        self.unconnected_value)

    def mark_data(self, *args):
        """
        V.mark_data(ImageData, int, [int, int, int, int, int, int])
        C++: void MarkData(ImageData *data, int dimensionality,
            int ext[6])
        Input a data of 0's and "_unconnected_value"s. Seeds of this object
        are used to find connected pixels.  All pixels connected to seeds
        are set to connected_value.  The data has to be unsigned char.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MarkData, *my_args)
        return ret

    def remove_all_seeds(self):
        """
        V.remove_all_seeds()
        C++: void RemoveAllSeeds()"""
        ret = self._vtk_obj.RemoveAllSeeds()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('unconnected_value',
    'GetUnconnectedValue'), ('connected_value', 'GetConnectedValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'connected_value',
    'unconnected_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageConnector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageConnector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['connected_value', 'unconnected_value']),
            title='Edit ImageConnector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageConnector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

