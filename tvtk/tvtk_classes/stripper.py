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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class Stripper(PolyDataAlgorithm):
    """
    Stripper - create triangle strips and/or poly-lines
    
    Superclass: PolyDataAlgorithm
    
    Caveats:
    
    If triangle strips or poly-lines exist in the input data they will be
    passed through to the output data. This filter will only construct
    triangle strips if triangle polygons are available; and will only
    construct poly-lines if lines are available.
    
    See Also:
    
    TriangleFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStripper, obj, update, **traits)
    
    pass_through_cell_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for picking. The default is off
        to conserve memory.
        """
    )
    def _pass_through_cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughCellIds,
                        self.pass_through_cell_ids_)

    pass_through_point_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a pointdata array
        that holds the point index of the original vertex that produced
        each output vertex. This is useful for picking. The default is
        off to conserve memory.
        """
    )
    def _pass_through_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughPointIds,
                        self.pass_through_point_ids_)

    pass_cell_data_as_field_data = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable passing of the cell_data in the input to the output
        as field_data. Note the field data is tranformed.
        """
    )
    def _pass_cell_data_as_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellDataAsFieldData,
                        self.pass_cell_data_as_field_data_)

    maximum_length = traits.Trait(1000, traits.Range(4, 100000, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum number of triangles in a triangle strip,
        and/or the maximum number of lines in a poly-line.
        """
    )
    def _maximum_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLength,
                        self.maximum_length)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('pass_through_point_ids',
    'GetPassThroughPointIds'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('pass_cell_data_as_field_data',
    'GetPassCellDataAsFieldData'), ('release_data_flag',
    'GetReleaseDataFlag'), ('maximum_length', 'GetMaximumLength'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('pass_through_cell_ids', 'GetPassThroughCellIds'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_cell_data_as_field_data', 'pass_through_cell_ids',
    'pass_through_point_ids', 'release_data_flag', 'maximum_length',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Stripper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_cell_data_as_field_data',
            'pass_through_cell_ids', 'pass_through_point_ids'], [],
            ['maximum_length']),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

