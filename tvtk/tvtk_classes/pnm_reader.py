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


class PNMReader(ImageReader):
    """
    PNMReader - read pnm (i.e., portable anymap) files
    
    Superclass: ImageReader
    
    PNMReader is a source object that reads pnm (portable anymap)
    files. This includes .pbm (bitmap), .pgm (grayscale), and .ppm
    (pixmap) files. (Currently this object only reads binary versions of
    these files.)
    
    PNMReader creates structured point datasets. The dimension of the
    dataset depends upon the number of files read. Reading a single file
    results in a 2d image, while reading more than one file results in a
    3d volume.
    
    To read a volume, files must be of the form "_file_name.<number>"
    (e.g., foo.ppm.0, foo.ppm.1, ...). You must also specify the
    data_extent.  The fifth and sixth values of the data_extent specify the
    beginning and ending files to read.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPNMReader, obj, update, **traits)
    
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
    ('progress', 'GetProgress'), ('file_dimensionality',
    'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_mask', 'data_origin',
    'data_spacing', 'data_voi', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'number_of_scalar_components',
    'progress_text', 'scalar_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PNMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PNMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_mask', 'data_origin', 'data_spacing',
            'data_voi', 'file_dimensionality', 'file_name',
            'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
            'file_prefix', 'header_size', 'number_of_scalar_components',
            'scalar_array_name']),
            title='Edit PNMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PNMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

