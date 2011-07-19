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


class VolumeRayCastFunction(Object):
    """
    VolumeRayCastFunction - a superclass for ray casting functions
    
    Superclass: Object
    
    VolumeRayCastFunction is a superclass for ray casting functions
    that can be used within a VolumeRayCastMapper. This includes for
    example, VolumeRayCastCompositeFunction,
    VolumeRayCastMIPFunction, and VolumeRayCastIsosurfaceFunction.
    
    See Also:
    
    VolumeRayCastCompositeFunction VolumeRayCastMIPFunction
    VolumeRayCastIsosurfaceFunction VolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastFunction, obj, update, **traits)
    
    def get_zero_opacity_threshold(self, *args):
        """
        V.get_zero_opacity_threshold(Volume) -> float
        C++: virtual float GetZeroOpacityThreshold(Volume *vol)
        Get the value below which all scalar values are considered to
        have 0 opacity.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetZeroOpacityThreshold, *my_args)
        return ret

    def cast_ray(self, *args):
        """
        V.cast_ray(VolumeRayCastDynamicInfo, VolumeRayCastStaticInfo)
        C++: virtual void CastRay(
            VolumeRayCastDynamicInfo *dynamicInfo,
            VolumeRayCastStaticInfo *staticInfo)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CastRay, *my_args)
        return ret

    def function_initialize(self, *args):
        """
        V.function_initialize(Renderer, Volume,
            VolumeRayCastStaticInfo)
        C++: void FunctionInitialize(Renderer *ren, Volume *vol,
            VolumeRayCastStaticInfo *staticInfo)
        Do the basic initialization. This includes saving the parameters
        passed in into local variables, as well as grabbing some useful
        info from the volume property and normal encoder. This initialize
        routine is called once per render. It also calls the
        specific_function_initialize of the subclass function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FunctionInitialize, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit VolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

