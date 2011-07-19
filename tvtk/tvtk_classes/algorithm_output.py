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


class AlgorithmOutput(Object):
    """
    AlgorithmOutput - Proxy object to connect input/output ports.
    
    Superclass: Object
    
    AlgorithmOutput is a proxy object returned by the get_output_port
    method of Algorithm.  It may be passed to the set_input_connection,
    add_input_connection, or remove_input_connection methods of another
    Algorithm to establish a connection between an output and input
    port.  The connection is not stored in the proxy object: it is simply
    a convenience for creating or removing connections.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAlgorithmOutput, obj, update, **traits)
    
    index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndex,
                        self.index)

    def _get_producer(self):
        return wrap_vtk(self._vtk_obj.GetProducer())
    def _set_producer(self, arg):
        old_val = self._get_producer()
        self._wrap_call(self._vtk_obj.SetProducer,
                        deref_vtk(arg))
        self.trait_property_changed('producer', old_val, arg)
    producer = traits.Property(_get_producer, _set_producer, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('index', 'GetIndex'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'index'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AlgorithmOutput, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AlgorithmOutput properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['index']),
            title='Edit AlgorithmOutput properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AlgorithmOutput properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

