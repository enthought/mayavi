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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class TecplotReader(MultiBlockDataSetAlgorithm):
    """
    TecplotReader - A concrete class to read an ASCII Tecplot file.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    TecplotReader parses an ASCII Tecplot file to get a
    MultiBlockDataSet
     object made up of several DataSet objects, of which each is of
    type
     either StructuredGrid or UnstructuredGrid. Each DataSet
    object
     maintains the geometry, topology, and some associated attributes
    describing
     physical properties.
    
    
     Tecplot treats 3d coordinates (only one or two coordinates might be
     explicitly specified in a file) as varaibles too, whose names (e.g.,
     'X' / 'x' / 'I', 'Y' / 'y' / 'J', 'Z' / 'z' / 'K') are provided in
    the
     variables list (the 'VARIABLES' section). These names are then
    followed
     in the list by those of other traditional variables or attributes
    (node-
     based and / or cell-based data with the mode specified via token
    'VAR
     LOCATION', to be extracted to create PointData and / or
    CellData).
     Each zone described afterwards (in the 'ZONE's section) provides the
     specific values of the aforementioned variables (including 3d
    coordinates),
     in the same order as indicated by the variable-names list, through
    either
     POINT-packing (i.e., tuple-based storage) or BLOCK-packing
    (component-based
     storage). In particular, the first / description line of  each zone
    tells
     the type of all the  constituent cells as the connectivity /
    topology
     information. In other words, the entire dataset is made up of
    multiple zones
     (blocks), of which each maintains a set of cells of the same type
    ('BRICK',
     'TRIANGLE', 'QUADRILATERAL', 'TETRAHEDRON', and 'POINT' in Tecplot
    terms).
     In addition, the description line of each zone specifies the zone
    name,
     dimensionality information (size of each dimension for a structured
    zone),
     number of nodes, and number of cells. Information about the file
    format is
     available at http://download.tecplot.com/360/dataformat.pdf.
    
    Caveats:
    
    
     TecplotReader is currently a simplified ASCII Tecplot reader and
    some
     functionalities (e.g., extraction of sections 'GEOMETRY', 'TEXT',
    and 'DATA
     SETAUXDATA', access to multiple time steps, in addition to the
    construction
     of RectilinearGrid and ImageData objects) are not supported.
    
    Thanks:
    
    
     This class is a VTK implementation of vis_it's ASCII Tecplot reader.
    
    See Also:
    
    
     Points StructuredGrid UnstructuredGrid PointData
    CellData
     DataSet MultiBlockDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTecplotReader, obj, update, **traits)
    
    def get_data_array_status(self, *args):
        """
        V.get_data_array_status(string) -> int
        C++: int GetDataArrayStatus(const char *arayName)
        Get the status of a specific data array (0: un-selected; 1:
        selected).
        """
        ret = self._wrap_call(self._vtk_obj.GetDataArrayStatus, *args)
        return ret

    def set_data_array_status(self, *args):
        """
        V.set_data_array_status(string, int)
        C++: void SetDataArrayStatus(const char *arayName, int bChecked)
        Set the status of a specific data array (0: de-select; 1: select)
        specified by the name.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataArrayStatus, *args)
        return ret

    def get_block_name(self, *args):
        """
        V.get_block_name(int) -> string
        C++: const char *GetBlockName(int blockIdx)
        Get the name of a block specified by a zero-based index. NULL is
        returned for an invalid block index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockName, *args)
        return ret

    def get_data_array_name(self, *args):
        """
        V.get_data_array_name(int) -> string
        C++: const char *GetDataArrayName(int arrayIdx)
        Get the name of a data array specified by the zero-based index
        (array_idx).
        """
        ret = self._wrap_call(self._vtk_obj.GetDataArrayName, *args)
        return ret

    def get_data_attribute_name(self, *args):
        """
        V.get_data_attribute_name(int) -> string
        C++: const char *GetDataAttributeName(int attrIndx)
        Get the name of a zero-based data attribute (not 3d coordinates).
        NULL is returned for an invalid attribute index.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataAttributeName, *args)
        return ret

    def _get_data_title(self):
        return self._vtk_obj.GetDataTitle()
    data_title = traits.Property(_get_data_title, help=\
        """
        Get the Tecplot data title.
        """
    )

    def _get_number_of_blocks(self):
        return self._vtk_obj.GetNumberOfBlocks()
    number_of_blocks = traits.Property(_get_number_of_blocks, help=\
        """
        Get the number of blocks (i.e., zones in Tecplot terms).
        """
    )

    def _get_number_of_data_arrays(self):
        return self._vtk_obj.GetNumberOfDataArrays()
    number_of_data_arrays = traits.Property(_get_number_of_data_arrays, help=\
        """
        Get the number of all data attributes (point data and cell data).
        """
    )

    def _get_number_of_data_attributes(self):
        return self._vtk_obj.GetNumberOfDataAttributes()
    number_of_data_attributes = traits.Property(_get_number_of_data_attributes, help=\
        """
        Get the number of standard data attributes (node-based and
        cell-based), excluding 3d coordinates.
        """
    )

    def _get_number_of_variables(self):
        return self._vtk_obj.GetNumberOfVariables()
    number_of_variables = traits.Property(_get_number_of_variables, help=\
        """
        Get the number of all variables (including 3d coordinates).
        """
    )

    def is_data_attribute_cell_based(self, *args):
        """
        V.is_data_attribute_cell_based(string) -> int
        C++: int IsDataAttributeCellBased(const char *attrName)
        V.is_data_attribute_cell_based(int) -> int
        C++: int IsDataAttributeCellBased(int attrIndx)
        Get the type (0 for node-based and 1 for cell-based) of a
        specified data attribute (not 3d coordinates). -1 is returned for
        an invalid attribute name.
        """
        ret = self._wrap_call(self._vtk_obj.IsDataAttributeCellBased, *args)
        return ret

    def set_file_name(self, *args):
        """
        V.set_file_name(string)
        C++: void SetFileName(const char *fileName)
        Specify a Tecplot ASCII file for data loading.
        """
        ret = self._wrap_call(self._vtk_obj.SetFileName, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TecplotReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TecplotReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TecplotReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TecplotReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

