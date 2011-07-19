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

from tvtk.tvtk_classes.collection import Collection


class SocketCollection(Collection):
    """
    SocketCollection -  a collection for sockets.
    
    Superclass: Collection
    
    Apart from being Collection subclass for sockets, this class
    provides means to wait for activity on all the sockets in the
    collection simultaneously.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSocketCollection, obj, update, **traits)
    
    def _get_last_selected_socket(self):
        return wrap_vtk(self._vtk_obj.GetLastSelectedSocket())
    last_selected_socket = traits.Property(_get_last_selected_socket, help=\
        """
        Returns the socket selected during the last select_sockets(), if
        any. NULL otherwise.
        """
    )

    def select_sockets(self, *args):
        """
        V.select_sockets(int) -> int
        C++: int SelectSockets(unsigned long msec=0)
        Select all Connected sockets in the collection. If msec is
        specified, it timesout after msec milliseconds on inactivity.
        Returns 0 on timeout, -1 on error; 1 is a socket was selected.
        The selected socket can be retrieved by get_last_selected_socket().
        """
        ret = self._wrap_call(self._vtk_obj.SelectSockets, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SocketCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SocketCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SocketCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SocketCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

