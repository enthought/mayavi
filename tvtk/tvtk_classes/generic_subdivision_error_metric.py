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


class GenericSubdivisionErrorMetric(Object):
    """
    GenericSubdivisionErrorMetric - Objects that compute
    
    Superclass: Object
    
    Objects of that class answer the following question during the cell
    subdivision: "does the edge need to be subdivided?" through
    requires_edge_subdivision(). The answer depends on the criterium
    actually used in the subclass of this abstract class: a
    geometric-based error metric (variation of edge from a straight
    line), an attribute-based error metric (variation of the active
    attribute/component value from a linear ramp) , a view-depend error
    metric, ... Cell subdivision is performed in the context of the
    adaptor framework: higher-order, or complex cells, are automatically
    tessellated into simplices so that they can be processed with
    conventional visualization algorithms.
    
    See Also:
    
    GenericCellTessellator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericSubdivisionErrorMetric, obj, update, **traits)
    
    def _get_generic_cell(self):
        return wrap_vtk(self._vtk_obj.GetGenericCell())
    def _set_generic_cell(self, arg):
        old_val = self._get_generic_cell()
        self._wrap_call(self._vtk_obj.SetGenericCell,
                        deref_vtk(arg))
        self.trait_property_changed('generic_cell', old_val, arg)
    generic_cell = traits.Property(_get_generic_cell, _set_generic_cell, help=\
        """
        The cell that the edge belongs to.
        """
    )

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Set/Get the dataset to be tessellated.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericSubdivisionErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

