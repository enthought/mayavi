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

from tvtk.tvtk_classes.abstract_transform import AbstractTransform


class GeoTransform(AbstractTransform):
    """
    GeoTransform - A transformation between two geographic coordinate
    systems
    
    Superclass: AbstractTransform
    
    This class takes two geographic projections and transforms point
    coordinates between them.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTransform, obj, update, **traits)
    
    def _get_source_projection(self):
        return wrap_vtk(self._vtk_obj.GetSourceProjection())
    def _set_source_projection(self, arg):
        old_val = self._get_source_projection()
        self._wrap_call(self._vtk_obj.SetSourceProjection,
                        deref_vtk(arg))
        self.trait_property_changed('source_projection', old_val, arg)
    source_projection = traits.Property(_get_source_projection, _set_source_projection, help=\
        """
        The source geographic projection.
        """
    )

    def _get_destination_projection(self):
        return wrap_vtk(self._vtk_obj.GetDestinationProjection())
    def _set_destination_projection(self, arg):
        old_val = self._get_destination_projection()
        self._wrap_call(self._vtk_obj.SetDestinationProjection,
                        deref_vtk(arg))
        self.trait_property_changed('destination_projection', old_val, arg)
    destination_projection = traits.Property(_get_destination_projection, _set_destination_projection, help=\
        """
        The target geographic projection.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GeoTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

