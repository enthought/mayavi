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


class MetaImageReader(ImageReader2):
    """
    MetaImageReader - read binary UNC meta image data
    
    Superclass: ImageReader2
    
    One of the formats for which a reader is already available in the
    toolkit is the meta_image file format. This is a fairly simple yet
    powerful format consisting of a text header and a binary data
    section. The following instructions describe how you can write a
    meta_image header for the data that you download from the brain_web
    page.
    
    The minimal structure of the meta_image header is the following:
    
    
       NDims = 3
       dim_size = 181 217 181
       element_type = MET_UCHAR
       element_spacing = 1.0 1.0 1.0
       element_byte_order_msb = False
       element_data_file = brainweb1.raw
    
    * NDims indicate that this is a 3d image. ITK can handle images of
      arbitrary dimension.
    * dim_size indicates the size of the volume in pixels along each
      direction.
    * element_type indicate the primitive type used for pixels. In this
      case is "unsigned char", implying that the data is digitized in 8
      bits / pixel.
    * element_spacing indicates the physical separation between the center
    of one pixel and the center of the next pixel along each direction in
    space. The units used are millimeters.
    * element_byte_order_msb indicates is the data is encoded in little or
      big endian order. You might want to play with this value when
      moving data between different computer platforms.
    * element_data_file is the name of the file containing the raw binary
      data of the image. This file must be in the same directory as the
      header.
    
    meta_image headers are expected to have extension: ".mha" or ".mhd"
    
    Once you write this header text file, it should be possible to read
    the image into your ITK based application using the
    itk::_file_io_to_image_filter class.
    
    Caveats:
    
    See Also:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMetaImageReader, obj, update, **traits)
    
    def _get_anatomical_orientation(self):
        return self._vtk_obj.GetAnatomicalOrientation()
    anatomical_orientation = traits.Property(_get_anatomical_orientation, help=\
        """
        
        """
    )

    def _get_bits_allocated(self):
        return self._vtk_obj.GetBitsAllocated()
    bits_allocated = traits.Property(_get_bits_allocated, help=\
        """
        
        """
    )

    def _get_date(self):
        return self._vtk_obj.GetDate()
    date = traits.Property(_get_date, help=\
        """
        
        """
    )

    def _get_distance_units(self):
        return self._vtk_obj.GetDistanceUnits()
    distance_units = traits.Property(_get_distance_units, help=\
        """
        
        """
    )

    def _get_gantry_angle(self):
        return self._vtk_obj.GetGantryAngle()
    gantry_angle = traits.Property(_get_gantry_angle, help=\
        """
        
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        
        """
    )

    def _get_image_number(self):
        return self._vtk_obj.GetImageNumber()
    image_number = traits.Property(_get_image_number, help=\
        """
        
        """
    )

    def _get_modality(self):
        return self._vtk_obj.GetModality()
    modality = traits.Property(_get_modality, help=\
        """
        
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        
        """
    )

    def _get_patient_id(self):
        return self._vtk_obj.GetPatientID()
    patient_id = traits.Property(_get_patient_id, help=\
        """
        
        """
    )

    def _get_patient_name(self):
        return self._vtk_obj.GetPatientName()
    patient_name = traits.Property(_get_patient_name, help=\
        """
        
        """
    )

    def _get_pixel_representation(self):
        return self._vtk_obj.GetPixelRepresentation()
    pixel_representation = traits.Property(_get_pixel_representation, help=\
        """
        
        """
    )

    def _get_rescale_offset(self):
        return self._vtk_obj.GetRescaleOffset()
    rescale_offset = traits.Property(_get_rescale_offset, help=\
        """
        
        """
    )

    def _get_rescale_slope(self):
        return self._vtk_obj.GetRescaleSlope()
    rescale_slope = traits.Property(_get_rescale_slope, help=\
        """
        
        """
    )

    def _get_series(self):
        return self._vtk_obj.GetSeries()
    series = traits.Property(_get_series, help=\
        """
        
        """
    )

    def _get_study_id(self):
        return self._vtk_obj.GetStudyID()
    study_id = traits.Property(_get_study_id, help=\
        """
        
        """
    )

    def _get_study_uid(self):
        return self._vtk_obj.GetStudyUID()
    study_uid = traits.Property(_get_study_uid, help=\
        """
        
        """
    )

    def _get_transfer_syntax_uid(self):
        return self._vtk_obj.GetTransferSyntaxUID()
    transfer_syntax_uid = traits.Property(_get_transfer_syntax_uid, help=\
        """
        
        """
    )

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('file_name_slice_offset', 'GetFileNameSliceOffset'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('data_extent',
    'GetDataExtent'), ('file_name', 'GetFileName'), ('data_byte_order',
    'GetDataByteOrder'), ('swap_bytes', 'GetSwapBytes'), ('progress_text',
    'GetProgressText'), ('file_pattern', 'GetFilePattern'),
    ('file_prefix', 'GetFilePrefix'), ('debug', 'GetDebug'),
    ('file_name_slice_spacing', 'GetFileNameSliceSpacing'),
    ('abort_execute', 'GetAbortExecute'), ('header_size',
    'GetHeaderSize'), ('data_spacing', 'GetDataSpacing'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('file_lower_left',
    'GetFileLowerLeft'), ('data_origin', 'GetDataOrigin'),
    ('file_dimensionality', 'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'number_of_scalar_components', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MetaImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MetaImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'file_dimensionality',
            'file_name', 'file_name_slice_offset', 'file_name_slice_spacing',
            'file_pattern', 'file_prefix', 'header_size',
            'number_of_scalar_components']),
            title='Edit MetaImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MetaImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

