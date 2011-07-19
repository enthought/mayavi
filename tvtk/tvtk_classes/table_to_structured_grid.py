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

from tvtk.tvtk_classes.structured_grid_algorithm import StructuredGridAlgorithm


class TableToStructuredGrid(StructuredGridAlgorithm):
    """
    TableToStructuredGrid - converts Table to a StructuredGrid.
    
    Superclass: StructuredGridAlgorithm
    
    TableToStructuredGrid is a filter that converts an input Table
    to a StructuredGrid. It provides API to select columns to use as
    points in the output structured grid. The specified dimensions of the
    output (specified using set_whole_extent()) must match the number of
    rows in the input table.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToStructuredGrid, obj, update, **traits)
    
    x_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the X coordinate for the
        points.
        """
    )
    def _x_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXColumn,
                        self.x_column)

    whole_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    z_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the Z coordinate for the
        points. Default is 0.
        """
    )
    def _z_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZColumn,
                        self.z_column)

    z_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_z_column()
        to use as the Zcoordinate in case the column is a multi-component
        array.
        """
    )
    def _z_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZComponent,
                        self.z_component)

    x_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_x_column()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
    )
    def _x_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXComponent,
                        self.x_component)

    y_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_y_column()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
    )
    def _y_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYComponent,
                        self.y_component)

    y_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the Y coordinate for the
        points. Default is 0.
        """
    )
    def _y_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYColumn,
                        self.y_column)

    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('z_component', 'GetZComponent'),
    ('y_component', 'GetYComponent'), ('z_column', 'GetZColumn'),
    ('x_column', 'GetXColumn'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('y_column', 'GetYColumn'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('x_component', 'GetXComponent'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'whole_extent', 'x_column',
    'x_component', 'y_column', 'y_component', 'z_column', 'z_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToStructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['whole_extent', 'x_column', 'x_component',
            'y_column', 'y_component', 'z_column', 'z_component']),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

