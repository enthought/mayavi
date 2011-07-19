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


class UnstructuredGridVolumeRayIntegrator(Object):
    """
    UnstructuredGridVolumeRayIntegrator - a superclass for volume ray
    integration functions
    
    Superclass: Object
    
    UnstructuredGridVolumeRayIntegrator is a superclass for ray
    integration functions that can be used within a
    UnstructuredGridVolumeRayCastMapper.
    
    See Also:
    
    UnstructuredGridVolumeRayCastMapper
    UnstructuredGridVolumeRayCastFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridVolumeRayIntegrator, obj, update, **traits)
    
    def initialize(self, *args):
        """
        V.initialize(Volume, DataArray)
        C++: virtual void Initialize(Volume *volume,
            DataArray *scalars)
        Set up the integrator with the given properties and scalars.
        """
        my_args = deref_array(args, [('vtkVolume', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def integrate(self, *args):
        """
        V.integrate(DoubleArray, DataArray, DataArray, [float,
            float, float, float])
        C++: virtual void Integrate(DoubleArray *intersectionLengths,
            DataArray *nearIntersections,
            DataArray *farIntersections, float color[4])
        Given a set of intersections (defined by the three arrays),
        compute the peicewise integration of the array in front to back
        order. /c intersection_lengths holds the lengths of each peicewise
        segment. /c near_intersections and /c far_intersections hold the
        scalar values at the front and back of each segment.  /c color
        should contain the RGBA value of the volume in front of the
        segments passed in, and the result will be placed back into /c
        color.
        """
        my_args = deref_array(args, [('vtkDoubleArray', 'vtkDataArray', 'vtkDataArray', ['float', 'float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.Integrate, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridVolumeRayIntegrator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridVolumeRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit UnstructuredGridVolumeRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridVolumeRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

