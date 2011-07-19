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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class IdFilter(DataSetAlgorithm):
    """
    IdFilter - generate scalars or field data from point and cell ids
    
    Superclass: DataSetAlgorithm
    
    IdFilter is a filter to that generates scalars or field data using
    cell and point ids. That is, the point attribute data scalars or
    field data are generated from the point ids, and the cell attribute
    data scalars or field data are generated from the the cell ids.
    
    Typically this filter is used with LabeledDataMapper (and possibly
    SelectVisiblePoints) to create labels for points and cells, or
    labels for the point or cell data scalar values.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIdFilter, obj, update, **traits)
    
    point_ids = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the generation of point ids. Default is on.
        """
    )
    def _point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointIds,
                        self.point_ids_)

    cell_ids = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the generation of point ids. Default is on.
        """
    )
    def _cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellIds,
                        self.cell_ids_)

    field_data = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which controls whether to generate scalar data
        or field data. If this flag is off, scalar data is generated.
        Otherwise, field data is generated. Default is off.
        """
    )
    def _field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldData,
                        self.field_data_)

    ids_array_name = traits.String(r"vtkIdFilter_Ids", enter_set=True, auto_set=False, help=\
        """
        Set/Get the name of the Ids array if generated. By default the
        Ids are named "vtk_id_filter__ids", but this can be changed with
        this function.
        """
    )
    def _ids_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdsArrayName,
                        self.ids_array_name)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('ids_array_name', 'GetIdsArrayName'), ('field_data', 'GetFieldData'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('cell_ids', 'GetCellIds'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('point_ids',
    'GetPointIds'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cell_ids', 'debug', 'field_data',
    'global_warning_display', 'point_ids', 'release_data_flag',
    'ids_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IdFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IdFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cell_ids', 'field_data', 'point_ids'], [],
            ['ids_array_name']),
            title='Edit IdFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IdFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

