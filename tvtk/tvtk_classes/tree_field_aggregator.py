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

from tvtk.tvtk_classes.tree_algorithm import TreeAlgorithm


class TreeFieldAggregator(TreeAlgorithm):
    """
    TreeFieldAggregator - aggregate field values from the leaves up
    the tree
    
    Superclass: TreeAlgorithm
    
    TreeFieldAggregator may be used to assign sizes to all the
    vertices in the tree, based on the sizes of the leaves.  The size of
    a vertex will equal the sum of the sizes of the child vertices.  If
    you have a data array with values for all leaves, you may specify
    that array, and the values will be filled in for interior tree
    vertices.  If you do not yet have an array, you may tell the filter
    to create a new array, assuming that the size of each leaf vertex is
    1.  You may optionally set a flag to first take the log of all leaf
    values before aggregating.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeFieldAggregator, obj, update, **traits)
    
    log_scale = tvtk_base.false_bool_trait(help=\
        """
        If set, the leaf values in the tree will be logarithmically
        scaled (base 10).
        """
    )
    def _log_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogScale,
                        self.log_scale_)

    leaf_vertex_unit_size = tvtk_base.true_bool_trait(help=\
        """
        If set, the algorithm will assume a size of 1 for each leaf
        vertex.
        """
    )
    def _leaf_vertex_unit_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeafVertexUnitSize,
                        self.leaf_vertex_unit_size_)

    field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The field to aggregate.  If this is a string array, the entries
        are converted to double. TODO: Remove this field and use the
        array_to_process in Algorithm.
        """
    )
    def _field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetField,
                        self.field)

    min_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If the value of the vertex is less than min_value then consider
        it's value to be min_val.
        """
    )
    def _min_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinValue,
                        self.min_value)

    _updateable_traits_ = \
    (('log_scale', 'GetLogScale'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('min_value',
    'GetMinValue'), ('progress_text', 'GetProgressText'), ('field',
    'GetField'), ('leaf_vertex_unit_size', 'GetLeafVertexUnitSize'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'leaf_vertex_unit_size', 'log_scale', 'release_data_flag', 'field',
    'min_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeFieldAggregator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeFieldAggregator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['leaf_vertex_unit_size', 'log_scale'], [], ['field',
            'min_value']),
            title='Edit TreeFieldAggregator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeFieldAggregator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

