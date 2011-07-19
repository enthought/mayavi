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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class ImplicitHalo(ImplicitFunction):
    """
    ImplicitHalo - implicit function for an halo
    
    Superclass: ImplicitFunction
    
    ImplicitHalo evaluates to 1.0 for each position in the sphere of a
    given center and radius radius*(_1-_fade_out). It evaluates to 0.0 for
    each position out the sphere of a given Center and radius Radius. It
    fades out linearly from 1.0 to 0.0 for points in a radius from
    radius*(_1-_fade_out) to Radius. ImplicitHalo is a concrete
    implementation of ImplicitFunction. It is useful as an input to
    SampleFunction to generate an 2d image of an halo. It is used this
    way by ShadowMapPass.
    
    Caveats:
    
    It does not implement the gradient.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitHalo, obj, update, **traits)
    
    fade_out = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        fade_out ratio. Valid values are between 0.0 and 1.0.
        """
    )
    def _fade_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFadeOut,
                        self.fade_out)

    radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Radius of the sphere.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('radius', 'GetRadius'), ('center',
    'GetCenter'), ('fade_out', 'GetFadeOut'), ('reference_count',
    'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'center', 'fade_out', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitHalo, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitHalo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'fade_out', 'radius']),
            title='Edit ImplicitHalo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitHalo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

