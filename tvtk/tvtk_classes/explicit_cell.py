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

from tvtk.tvtk_classes.non_linear_cell import NonLinearCell


class ExplicitCell(NonLinearCell):
    """
    ExplicitCell - abstract superclass for cells requiring an explicit
    representation
    
    Superclass: NonLinearCell
    
    ExplicitCell is an abstract superclass for cells that cannot be
    represented implicitly. An implicit representation requires only a
    cell type and connectivity list (e.g., triangle). Explicit cells
    require information beyond this; e.g., a NURBS surface or cells that
    require explicit face/edge descriptions. Most cells in VTK are
    implicitly represented.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExplicitCell, obj, update, **traits)
    
    cell_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cell id. This is necessary for explicit cells because
        they often need to keep extra information (typically contained in
        the cell data of a point set). This information might be things
        like knot points/weights, boundaries, etc.
        """
    )
    def _cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellId,
                        self.cell_id)

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Set/Get the mesh that owns this cell. This is necessary for
        explicit cells because they often need to keep extra information
        (typically contained in the cell data of a point set). This
        information might be things like knot points/weights, boundaries,
        etc.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('cell_id', 'GetCellId'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cell_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExplicitCell, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExplicitCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cell_id']),
            title='Edit ExplicitCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExplicitCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

