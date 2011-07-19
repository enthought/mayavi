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


class Tensor(Object):
    """
    Tensor - supporting class to enable assignment and referencing of
    tensors
    
    Superclass: Object
    
    Tensor is a floating point representation of an nxn tensor.
    Tensor provides methods for assignment and reference of tensor
    components. It does it in such a way as to minimize data copying.
    
    Caveats:
    
    Tensor performs its operations using pointer reference. You are
    responsible for supplying data storage (if necessary) if local copies
    of data are being made.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTensor, obj, update, **traits)
    
    def get_component(self, *args):
        """
        V.get_component(int, int) -> float
        C++: double GetComponent(int i, int j)
        Get the tensor component (i,j).
        """
        ret = self._wrap_call(self._vtk_obj.GetComponent, *args)
        return ret

    def set_component(self, *args):
        """
        V.set_component(int, int, float)
        C++: void SetComponent(int i, int j, double v)
        Set the value of the tensor component (i,j).
        """
        ret = self._wrap_call(self._vtk_obj.SetComponent, *args)
        return ret

    def add_component(self, *args):
        """
        V.add_component(int, int, float)
        C++: void AddComponent(int i, int j, double v)
        Add to the value of the tensor component at location (i,j).
        """
        ret = self._wrap_call(self._vtk_obj.AddComponent, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Tensor)
        C++: void DeepCopy(Tensor *t)
        Deep copy of one tensor to another tensor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Initialize tensor components to 0.0.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Tensor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Tensor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Tensor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Tensor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

