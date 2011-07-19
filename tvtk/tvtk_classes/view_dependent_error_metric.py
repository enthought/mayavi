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

from tvtk.tvtk_classes.generic_subdivision_error_metric import GenericSubdivisionErrorMetric


class ViewDependentErrorMetric(GenericSubdivisionErrorMetric):
    """
    ViewDependentErrorMetric - Objects that compute a
    
    Superclass: GenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on a geometric criterium in the
    screen space: the variation of the projected edge from a projected
    straight line
    
    See Also:
    
    GenericCellTessellator GenericSubdivisionErrorMetric
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkViewDependentErrorMetric, obj, update, **traits)
    
    pixel_tolerance = traits.Float(0.25, enter_set=True, auto_set=False, help=\
        """
        Set the squared screen-based geometric accuracy measured in
        pixels. Subdivision will be required if the square distance
        between the projection of the real point and the straight line
        passing through the projection of the vertices of the edge is
        greater than `value'. For instance, 0.25 will give better result
        than 1.
        \pre positive_value: value>0
        """
    )
    def _pixel_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelTolerance,
                        self.pixel_tolerance)

    def _get_viewport(self):
        return wrap_vtk(self._vtk_obj.GetViewport())
    def _set_viewport(self, arg):
        old_val = self._get_viewport()
        self._wrap_call(self._vtk_obj.SetViewport,
                        deref_vtk(arg))
        self.trait_property_changed('viewport', old_val, arg)
    viewport = traits.Property(_get_viewport, _set_viewport, help=\
        """
        Set/Get the renderer with `renderer' on which the error metric is
        based. The error metric use the active camera of the renderer.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pixel_tolerance', 'GetPixelTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pixel_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ViewDependentErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ViewDependentErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['pixel_tolerance']),
            title='Edit ViewDependentErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ViewDependentErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

