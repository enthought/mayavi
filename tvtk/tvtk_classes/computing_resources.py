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


class ComputingResources(Object):
    """
    ComputingResources - Definition of computing resource
    
    Superclass: Object
    
    This is a class for distribute the number of threads to a network of
    modules
    
    See Also:
    
    ExecutionScheduler
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkComputingResources, obj, update, **traits)
    
    def clear(self):
        """
        V.clear()
        C++: void Clear()
        Set resources to an empty states
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def collect(self, *args):
        """
        V.collect(ComputingResources)
        C++: void Collect(ComputingResources *res)
        Add an amount of computing resources to this object
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Collect, *my_args)
        return ret

    def deploy(self, *args):
        """
        V.deploy(ThreadedStreamingPipeline, Information)
        C++: void Deploy(ThreadedStreamingPipeline *exec,
            Information *info)
        Assign the resources and information of this object to an
        executive, i.e., set the number of threads of the algorithm the
        executive is pointing to
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Deploy, *my_args)
        return ret

    def obtain_maximum_resources(self):
        """
        V.obtain_maximum_resources()
        C++: void ObtainMaximumResources()
        Assign a maximum amount of usable resources to this object
        """
        ret = self._vtk_obj.ObtainMaximumResources()
        return ret
        

    def obtain_minimum_resources(self):
        """
        V.obtain_minimum_resources()
        C++: void ObtainMinimumResources()
        Assign a minimum amount of usable resources to this object, e.g.
        1 thread
        """
        ret = self._vtk_obj.ObtainMinimumResources()
        return ret
        

    def reserve(self, *args):
        """
        V.reserve(ComputingResources) -> bool
        C++: bool Reserve(ComputingResources *res)
        Take an amount of computing resources out of this object. Return
        true if it is successful.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Reserve, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ComputingResources, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ComputingResources properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ComputingResources properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ComputingResources properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

