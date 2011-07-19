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

from tvtk.tvtk_classes.edge_subdivision_criterion import EdgeSubdivisionCriterion


class DataSetEdgeSubdivisionCriterion(EdgeSubdivisionCriterion):
    """
    DataSetEdgeSubdivisionCriterion - a subclass of
    EdgeSubdivisionCriterion for DataSet objects.
    
    Superclass: EdgeSubdivisionCriterion
    
    This is a subclass of EdgeSubdivisionCriterion that is used for
    tessellating cells of a DataSet, particularly nonlinear cells.
    
    It provides functions for setting the current cell being tessellated
    and a convenience routine, evaluate_fields() to evaluate field values
    at a point. You should call evaluate_fields() from inside
    evaluate_edge() whenever the result of evaluate_edge() will be true.
    Otherwise, do not call evaluate_fields() as the midpoint is about to
    be discarded. (Implementor's note</i>: This isn't true if
    UGLY_ASPECT_RATIO_HACK has been defined. But in that case, we don't
    want the exact field values; we need the linearly interpolated ones
    at the midpoint for continuity.)
    
    See Also:
    
    EdgeSubdivisionCriterion
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetEdgeSubdivisionCriterion, obj, update, **traits)
    
    def _get_mesh(self):
        return wrap_vtk(self._vtk_obj.GetMesh())
    def _set_mesh(self, arg):
        old_val = self._get_mesh()
        self._wrap_call(self._vtk_obj.SetMesh,
                        deref_vtk(arg))
        self.trait_property_changed('mesh', old_val, arg)
    mesh = traits.Property(_get_mesh, _set_mesh, help=\
        """
        
        """
    )

    def get_field_error2(self, *args):
        """
        V.get_field_error2(int) -> float
        C++: double GetFieldError2(int s)
        Get/Set the square of the allowable error magnitude for the
        scalar field s at any edge's midpoint. A value less than or equal
        to 0 indicates that the field should not be used as a criterion
        for subdivision.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldError2, *args)
        return ret

    def set_field_error2(self, *args):
        """
        V.set_field_error2(int, float)
        C++: virtual void SetFieldError2(int s, double err)
        Get/Set the square of the allowable error magnitude for the
        scalar field s at any edge's midpoint. A value less than or equal
        to 0 indicates that the field should not be used as a criterion
        for subdivision.
        """
        ret = self._wrap_call(self._vtk_obj.SetFieldError2, *args)
        return ret

    cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellId,
                        self.cell_id)

    chord_error2 = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        Get/Set the square of the allowable chord error at any edge's
        midpoint. This value is used by evaluate_edge.
        """
    )
    def _chord_error2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChordError2,
                        self.chord_error2)

    def _get_active_field_criteria(self):
        return self._vtk_obj.GetActiveFieldCriteria()
    active_field_criteria = traits.Property(_get_active_field_criteria, help=\
        """
        Return a bitfield specifying which field_error2 criteria are
        positive (i.e., actively used to decide edge subdivisions). This
        is stored as separate state to make subdivisions go faster.
        """
    )

    def _get_cell(self):
        return wrap_vtk(self._vtk_obj.GetCell())
    cell = traits.Property(_get_cell, help=\
        """
        
        """
    )

    def reset_field_error2(self):
        """
        V.reset_field_error2()
        C++: virtual void ResetFieldError2()
        Tell the subdivider not to use any field values as subdivision
        criteria. Effectively calls set_field_error2( a, -1. ) for all
        fields.
        """
        ret = self._vtk_obj.ResetFieldError2()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('chord_error2',
    'GetChordError2'), ('cell_id', 'GetCellId'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cell_id', 'chord_error2'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetEdgeSubdivisionCriterion, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetEdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cell_id', 'chord_error2']),
            title='Edit DataSetEdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetEdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

