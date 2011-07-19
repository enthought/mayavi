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

from tvtk.tvtk_classes.unstructured_grid_volume_ray_integrator import UnstructuredGridVolumeRayIntegrator


class UnstructuredGridPartialPreIntegration(UnstructuredGridVolumeRayIntegrator):
    """
    UnstructuredGridPartialPreIntegration - performs piecewise linear
    ray integration.
    
    Superclass: UnstructuredGridVolumeRayIntegrator
    
    UnstructuredGridPartialPreIntegration performs piecewise linear
    ray integration.  This will give the same results as
    UnstructuredGridLinearRayIntegration (with potentially a error due
    to table lookup quantization), but should be notably faster.  The
    algorithm used is given by Moreland and Angel, "A Fast High Accuracy
    Volume Renderer for Unstructured Data."
    
    This class is thread safe only after the first instance is created.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridPartialPreIntegration, obj, update, **traits)
    
    def build_psi_table(self):
        """
        V.build_psi_table()
        C++: static void BuildPsiTable()
        Looks up Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data") in a table.  The
        table must be created first, which happens on the first
        instantiation of this class or when build_psi_table is first
        called.
        """
        ret = self._vtk_obj.BuildPsiTable()
        return ret
        

    def integrate_ray(self, *args):
        """
        V.integrate_ray(float, float, float, float, float, [float, float,
            float, float])
        C++: static void IntegrateRay(double length,
            double intensity_front, double attenuation_front,
            double intensity_back, double attenuation_back,
            float color[4])
        V.integrate_ray(float, (float, float, float), float, (float, float,
             float), float, [float, float, float, float])
        C++: static void IntegrateRay(double length,
            const double color_front[3], double attenuation_front,
            const double color_back[3], double attenuation_back,
            float color[4])
        Integrates a single ray segment.  color is blended with the
        result (with color in front).  The result is written back into
        color.
        """
        ret = self._wrap_call(self._vtk_obj.IntegrateRay, *args)
        return ret

    def psi(self, *args):
        """
        V.psi(float, float) -> float
        C++: static float Psi(float taufD, float taubD)
        Looks up Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data") in a table.  The
        table must be created first, which happens on the first
        instantiation of this class or when build_psi_table is first
        called.
        """
        ret = self._wrap_call(self._vtk_obj.Psi, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridPartialPreIntegration, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridPartialPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit UnstructuredGridPartialPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridPartialPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

