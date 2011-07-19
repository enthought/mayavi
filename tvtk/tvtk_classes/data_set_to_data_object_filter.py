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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class DataSetToDataObjectFilter(DataObjectAlgorithm):
    """
    DataSetToDataObjectFilter - map dataset into data object (i.e., a
    field)
    
    Superclass: DataObjectAlgorithm
    
    DataSetToDataObjectFilter is an class that transforms a dataset
    into data object (i.e., a field). The field will have labeled data
    arrays corresponding to the topology, geometry, field data, and point
    and cell attribute data.
    
    You can control what portions of the dataset are converted into the
    output data object's field data. The instance variables Geometry,
    Topology, field_data, point_data, and cell_data are flags that control
    whether the dataset's geometry (e.g., points, spacing, origin);
    topology (e.g., cell connectivity, dimensions); the field data
    associated with the dataset's superclass data object; the dataset's
    point data attributes; and the dataset's cell data attributes. (Note:
    the data attributes include scalars, vectors, tensors, normals,
    texture coordinates, and field data.)
    
    The names used to create the field data are as follows. For
    PolyData, "Points", "Verts", "Lines", "Polys", and "Strips". For
    UnstructuredGrid, "Cells" and "_cell_types". For
    StructuredPoints, "Dimensions", "Spacing", and "Origin". For
    StructuredGrid, "Points" and "Dimensions". For RectilinearGrid,
    "XCoordinates", "YCoordinates", and "ZCoordinates". for point
    attribute data, "_point_scalars", "_point_vectors", etc. For cell
    attribute data, "_cell_scalars", "_cell_vectors", etc. Field data arrays
    retain their original name.
    
    See Also:
    
    DataObject FieldData DataObjectToDataSetFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetToDataObjectFilter, obj, update, **traits)
    
    geometry = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the conversion of dataset geometry to a data object.
        """
    )
    def _geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometry,
                        self.geometry_)

    point_data = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the conversion of dataset point data to a data
        object.
        """
    )
    def _point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointData,
                        self.point_data_)

    cell_data = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the conversion of dataset cell data to a data object.
        """
    )
    def _cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellData,
                        self.cell_data_)

    field_data = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the conversion of dataset field data to a data
        object.
        """
    )
    def _field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldData,
                        self.field_data_)

    topology = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the conversion of dataset topology to a data object.
        """
    )
    def _topology_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTopology,
                        self.topology_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('geometry',
    'GetGeometry'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('field_data',
    'GetFieldData'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('cell_data', 'GetCellData'),
    ('point_data', 'GetPointData'), ('topology', 'GetTopology'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cell_data', 'debug', 'field_data', 'geometry',
    'global_warning_display', 'point_data', 'release_data_flag',
    'topology', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetToDataObjectFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetToDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cell_data', 'field_data', 'geometry', 'point_data',
            'topology'], [], []),
            title='Edit DataSetToDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetToDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

