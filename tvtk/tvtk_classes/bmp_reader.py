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

from tvtk.tvtk_classes.image_reader import ImageReader


class BMPReader(ImageReader):
    """
    BMPReader - read Windows BMP files
    
    Superclass: ImageReader
    
    BMPReader is a source object that reads Windows BMP files. This
    includes indexed and 24bit bitmaps Usually, all BMPs are converted to
    24bit RGB, but BMPs may be output as 8bit images with a lookup_table
    if the allow8_bit_bmp flag is set.
    
    BMPReader creates structured point datasets. The dimension of the
    dataset depends upon the number of files read. Reading a single file
    results in a 2d image, while reading more than one file results in a
    3d volume.
    
    To read a volume, files must be of the form "_file_name.<number>"
    (e.g., foo.bmp.0, foo.bmp.1, ...). You must also specify the image
    range. This range specifies the beginning and ending files to read
    (range can be any pair of non-negative numbers).
    
    The default behavior is to read a single file. In this case, the form
    of the file is simply "_file_name" (e.g., foo.bmp).
    
    See Also:
    
    BMPWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBMPReader, obj, update, **traits)
    
    allow8_bit_bmp = tvtk_base.false_bool_trait(help=\
        """
        If this flag is set and the BMP reader encounters an 8bit file,
        the data will be kept as unsigned chars and a lookuptable will be
        exported
        """
    )
    def _allow8_bit_bmp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllow8BitBMP,
                        self.allow8_bit_bmp_)

    def _get_depth(self):
        return self._vtk_obj.GetDepth()
    depth = traits.Property(_get_depth, help=\
        """
        Returns the depth of the BMP, either 8 or 24.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    lookup_table = traits.Property(_get_lookup_table, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('data_voi', 'GetDataVOI'), ('file_name', 'GetFileName'),
    ('data_mask', 'GetDataMask'), ('data_byte_order', 'GetDataByteOrder'),
    ('scalar_array_name', 'GetScalarArrayName'), ('file_prefix',
    'GetFilePrefix'), ('file_pattern', 'GetFilePattern'), ('debug',
    'GetDebug'), ('header_size', 'GetHeaderSize'), ('data_spacing',
    'GetDataSpacing'), ('swap_bytes', 'GetSwapBytes'), ('data_origin',
    'GetDataOrigin'), ('file_lower_left', 'GetFileLowerLeft'),
    ('file_name_slice_offset', 'GetFileNameSliceOffset'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('data_extent',
    'GetDataExtent'), ('progress_text', 'GetProgressText'),
    ('file_name_slice_spacing', 'GetFileNameSliceSpacing'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('allow8_bit_bmp', 'GetAllow8BitBMP'),
    ('file_dimensionality', 'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'allow8_bit_bmp', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_mask', 'data_origin',
    'data_spacing', 'data_voi', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'number_of_scalar_components',
    'progress_text', 'scalar_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BMPReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BMPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow8_bit_bmp', 'file_lower_left', 'swap_bytes'],
            ['data_byte_order'], ['data_extent', 'data_mask', 'data_origin',
            'data_spacing', 'data_voi', 'file_dimensionality', 'file_name',
            'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
            'file_prefix', 'header_size', 'number_of_scalar_components',
            'scalar_array_name']),
            title='Edit BMPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BMPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

