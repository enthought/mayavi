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


class Instantiator(Object):
    """
    Instantiator - create an instance of any VTK class from its name.
    
    Superclass: Object
    
    Instantiator provides an interface to create an instance of any
    VTK class from its name.  Instances are created through registered
    pointers to functions returning the objects.  New classes can also be
    registered with the creator.  VTK libraries automatically register
    their classes with the creator when they are loaded.  Instances are
    created using the static New() method, so the normal ObjectFactory
    mechanism is still invoked.
    
    When using this class from language wrappers (Tcl, Python, or Java),
    the Instantiator should be able to create any class from any kit
    that has been loaded.
    
    In C++ code, one should include the header for each kit from which
    one wishes to create instances through Instantiator.  This is
    necessary to ensure proper linking when building static libraries. Be
    careful, though, because including each kit's header means every
    class from that kit will be linked into your executable whether or
    not the class is used.  The headers are:
    
    
      Common          - CommonInstantiator.h
      Filtering       - FilteringInstantiator.h
      IO              - IOInstantiator.h
      Imaging         - ImagingInstantiator.h
      Graphics        - GraphicsInstantiator.h
      Rendering       - RenderingInstantiator.h
      VolumeRendering - VolumeRenderingInstantiator.h
      Hybrid          - HybridInstantiator.h
      Parallel        - ParallelInstantiator.h
    
    The VTK_MAKE_INSTANTIATOR() command in CMake is used to automatically
    generate the creator registration for each VTK library.  It can also
    be used to create registration code for VTK-style user libraries that
    are linked to Common.  After using this command to register
    classes from a new library, the generated header must be included.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInstantiator, obj, update, **traits)
    
    def create_instance(self, *args):
        """
        V.create_instance(string) -> Object
        C++: static Object *CreateInstance(const char *className)
        Create an instance of the class whose name is given.  If creation
        fails, a NULL pointer is returned.
        """
        ret = self._wrap_call(self._vtk_obj.CreateInstance, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Instantiator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Instantiator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Instantiator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Instantiator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

