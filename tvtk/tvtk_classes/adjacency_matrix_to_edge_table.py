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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class AdjacencyMatrixToEdgeTable(TableAlgorithm):
    """
    AdjacencyMatrixToEdgeTable
    
    Superclass: TableAlgorithm
    
    Treats a dense 2-way array of doubles as an adacency matrix and
    converts it into a Table suitable for use as an edge table with
    TableToGraph.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAdjacencyMatrixToEdgeTable, obj, update, **traits)
    
    value_array_name = traits.String(r"value", enter_set=True, auto_set=False, help=\
        """
        Controls the name of the output table column that contains edge
        weights. Default: "value"
        """
    )
    def _value_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueArrayName,
                        self.value_array_name)

    minimum_count = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specifies the minimum number of adjacent edges to include for
        each source vertex. Default: 0
        """
    )
    def _minimum_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumCount,
                        self.minimum_count)

    source_dimension = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specifies whether rows or columns become the "source" in the
        output edge table. 0 = rows, 1 = columns.  Default: 0
        """
    )
    def _source_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSourceDimension,
                        self.source_dimension)

    minimum_threshold = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Specifies a minimum threshold that an edge weight must exceed to
        be included in the output. Default: 0.5
        """
    )
    def _minimum_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumThreshold,
                        self.minimum_threshold)

    _updateable_traits_ = \
    (('minimum_threshold', 'GetMinimumThreshold'), ('progress_text',
    'GetProgressText'), ('minimum_count', 'GetMinimumCount'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('source_dimension', 'GetSourceDimension'), ('value_array_name',
    'GetValueArrayName'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'minimum_count', 'minimum_threshold',
    'progress_text', 'source_dimension', 'value_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AdjacencyMatrixToEdgeTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AdjacencyMatrixToEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['minimum_count', 'minimum_threshold',
            'source_dimension', 'value_array_name']),
            title='Edit AdjacencyMatrixToEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AdjacencyMatrixToEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

