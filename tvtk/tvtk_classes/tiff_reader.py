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

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class TIFFReader(ImageReader2):
    """
    TIFFReader - read TIFF files
    
    Superclass: ImageReader2
    
    TIFFReader is a source object that reads TIFF files. It should be
    able to read almost any TIFF file
    
    See Also:
    
    TIFFWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTIFFReader, obj, update, **traits)
    
    origin_specified_flag = tvtk_base.false_bool_trait(help=\
        """
        Set/get methods to see if manual Origin/Spacing have been set.
        """
    )
    def _origin_specified_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginSpecifiedFlag,
                        self.origin_specified_flag_)

    spacing_specified_flag = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _spacing_specified_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacingSpecifiedFlag,
                        self.spacing_specified_flag_)

    orientation_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set orientation type ORIENTATION_TOPLEFT         1       (row 0
        top, col 0 lhs) ORIENTATION_TOPRIGHT        2       (row 0 top,
        col 0 rhs) ORIENTATION_BOTRIGHT        3       (row 0 bottom, col
        0 rhs) ORIENTATION_BOTLEFT         4       (row 0 bottom, col 0
        lhs) ORIENTATION_LEFTTOP         5       (row 0 lhs, col 0 top)
        ORIENTATION_RIGHTTOP        6       (row 0 rhs, col 0 top)
        ORIENTATION_RIGHTBOT        7       (row 0 rhs, col 0 bottom)
        ORIENTATION_LEFTBOT         8       (row 0 lhs, col 0 bottom)
        User need to explicitely include vtk_tiff.h header to have access
        to those #define
        """
    )
    def _orientation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationType,
                        self.orientation_type)

    def _get_orientation_type_specified_flag(self):
        return self._vtk_obj.GetOrientationTypeSpecifiedFlag()
    orientation_type_specified_flag = traits.Property(_get_orientation_type_specified_flag, help=\
        """
        Get method to check if orientation type is specified
        """
    )

    def initialize_colors(self):
        """
        V.initialize_colors()
        C++: void InitializeColors()
        Auxilary methods used by the reader internally.
        """
        ret = self._vtk_obj.InitializeColors()
        return ret
        

    def read_tiles(self):
        """
        V.read_tiles()
        C++: virtual void ReadTiles(void *buffer)
        Reads 3d data from tiled tiff
        """
        ret = self._vtk_obj.ReadTiles()
        return ret
        

    def read_volume(self):
        """
        V.read_volume()
        C++: virtual void ReadVolume(void *buffer)
        Reads 3d data from multi-pages tiff.
        """
        ret = self._vtk_obj.ReadVolume()
        return ret
        

    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('file_name', 'GetFileName'), ('data_byte_order', 'GetDataByteOrder'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('debug', 'GetDebug'), ('header_size', 'GetHeaderSize'),
    ('data_spacing', 'GetDataSpacing'), ('swap_bytes', 'GetSwapBytes'),
    ('data_origin', 'GetDataOrigin'), ('file_lower_left',
    'GetFileLowerLeft'), ('file_name_slice_offset',
    'GetFileNameSliceOffset'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('spacing_specified_flag',
    'GetSpacingSpecifiedFlag'), ('data_extent', 'GetDataExtent'),
    ('origin_specified_flag', 'GetOriginSpecifiedFlag'), ('progress_text',
    'GetProgressText'), ('file_name_slice_spacing',
    'GetFileNameSliceSpacing'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('orientation_type', 'GetOrientationType'), ('file_dimensionality',
    'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'origin_specified_flag',
    'release_data_flag', 'spacing_specified_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'number_of_scalar_components', 'orientation_type',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TIFFReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'origin_specified_flag',
            'spacing_specified_flag', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'file_dimensionality',
            'file_name', 'file_name_slice_offset', 'file_name_slice_spacing',
            'file_pattern', 'file_prefix', 'header_size',
            'number_of_scalar_components', 'orientation_type']),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

