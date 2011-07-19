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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageReader2(ImageAlgorithm):
    """
    ImageReader2 - Superclass of binary file readers.
    
    Superclass: ImageAlgorithm
    
    ImageReader2 is the parent class for ImageReader.  It is a good
    super class for streaming readers that do not require a mask or
    transform on the data.  ImageReader was implemented before
    ImageReader2, ImageReader2 is intended to have a simpler
    interface.
    
    See Also:
    
    JPEGReader PNGReader ImageReader GESignaReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReader2, obj, update, **traits)
    
    swap_bytes = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the byte swapping to explicitly swap the bytes of a file.
        """
    )
    def _swap_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapBytes,
                        self.swap_bytes_)

    file_lower_left = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether the data comes from the file starting in the
        lower left corner or upper left corner.
        """
    )
    def _file_lower_left_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileLowerLeft,
                        self.file_lower_left_)

    def get_data_scalar_type(self):
        """
        V.get_data_scalar_type() -> int
        C++: int GetDataScalarType()
        Get the file format.  Pixels are this type in the file.
        """
        ret = self._vtk_obj.GetDataScalarType()
        return ret
        

    def set_data_scalar_type(self, *args):
        """
        V.set_data_scalar_type(int)
        C++: virtual void SetDataScalarType(int type)
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataScalarType, *args)
        return ret

    def set_data_scalar_type_to_char(self):
        """
        V.set_data_scalar_type_to_char()
        C++: virtual void SetDataScalarTypeToChar()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToChar()

    def set_data_scalar_type_to_double(self):
        """
        V.set_data_scalar_type_to_double()
        C++: virtual void SetDataScalarTypeToDouble()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToDouble()

    def set_data_scalar_type_to_float(self):
        """
        V.set_data_scalar_type_to_float()
        C++: virtual void SetDataScalarTypeToFloat()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToFloat()

    def set_data_scalar_type_to_int(self):
        """
        V.set_data_scalar_type_to_int()
        C++: virtual void SetDataScalarTypeToInt()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToInt()

    def set_data_scalar_type_to_short(self):
        """
        V.set_data_scalar_type_to_short()
        C++: virtual void SetDataScalarTypeToShort()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToShort()

    def set_data_scalar_type_to_signed_char(self):
        """
        V.set_data_scalar_type_to_signed_char()
        C++: virtual void SetDataScalarTypeToSignedChar()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToSignedChar()

    def set_data_scalar_type_to_unsigned_char(self):
        """
        V.set_data_scalar_type_to_unsigned_char()
        C++: virtual void SetDataScalarTypeToUnsignedChar()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedChar()

    def set_data_scalar_type_to_unsigned_int(self):
        """
        V.set_data_scalar_type_to_unsigned_int()
        C++: virtual void SetDataScalarTypeToUnsignedInt()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedInt()

    def set_data_scalar_type_to_unsigned_short(self):
        """
        V.set_data_scalar_type_to_unsigned_short()
        C++: virtual void SetDataScalarTypeToUnsignedShort()
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedShort()

    data_byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        These methods should be used instead of the swap_bytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a big_endian file on a big_endian
        machine will result in no swapping. Trying to read the same file
        on a little_endian machine will result in swapping. As a quick
        note most UNIX machines are big_endian while PC's and VAX tend to
        be little_endian. So if the file you are reading in was generated
        on a VAX or PC, set_data_byte_order_to_little_endian otherwise
        set_data_byte_order_to_big_endian.
        """
    )
    def _data_byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataByteOrder,
                        self.data_byte_order_)

    data_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataExtent,
                        self.data_extent)

    file_prefix = tvtk_base.vtk_file_prefix("", help=\
        """
        Specify file prefix for the image file or files.  This can be
        used in place of set_file_name or set_file_names if the filenames
        follow a specific naming pattern, but you must explicitly set the
        data_extent so that the reader will know what range of slices to
        load.
        """
    )
    def _file_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePrefix,
                        self.file_prefix)

    file_name_slice_spacing = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When reading files which have regular, but non contiguous slices
        (eg filename.1,filename.3,filename.5) a spacing can be specified
        to skip missing files (default = 1)
        """
    )
    def _file_name_slice_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileNameSliceSpacing,
                        self.file_name_slice_spacing)

    file_name_slice_offset = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When reading files which start at an unusual index, this can be
        added to the slice number when generating the file name (default
        = 0)
        """
    )
    def _file_name_slice_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileNameSliceOffset,
                        self.file_name_slice_offset)

    number_of_scalar_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of scalar components
        """
    )
    def _number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfScalarComponents,
                        self.number_of_scalar_components)

    file_dimensionality = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        The number of dimensions stored in a file. This defaults to two.
        """
    )
    def _file_dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileDimensionality,
                        self.file_dimensionality)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name for the image file. If the data is stored in
        multiple files, then use set_file_names or set_file_prefix instead.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    data_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    file_pattern = traits.String(r"%s.%d", enter_set=True, auto_set=False, help=\
        """
        The sprintf-style format string used to build filename from
        file_prefix and slice number.
        """
    )
    def _file_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePattern,
                        self.file_pattern)

    data_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    def _get_file_names(self):
        return wrap_vtk(self._vtk_obj.GetFileNames())
    def _set_file_names(self, arg):
        old_val = self._get_file_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetFileNames,
                        my_arg[0])
        self.trait_property_changed('file_names', old_val, arg)
    file_names = traits.Property(_get_file_names, _set_file_names, help=\
        """
        Specify a list of file names.  Each file must be a single slice,
        and each slice must be of the same size. The files must be in the
        correct order. Use set_file_name when reading a volume (multiple
        slice), since data_extent will be modified after a set_file_names
        call.
        """
    )

    header_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If there is a tail on the file, you want to explicitly set the
        header size.
        """
    )
    def _header_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeaderSize,
                        self.header_size)

    def _get_data_increments(self):
        return self._vtk_obj.GetDataIncrements()
    data_increments = traits.Property(_get_data_increments, help=\
        """
        
        """
    )

    def _get_descriptive_name(self):
        return self._vtk_obj.GetDescriptiveName()
    descriptive_name = traits.Property(_get_descriptive_name, help=\
        """
        Return a descriptive name for the file format that might be
        useful in a GUI.
        """
    )

    def _get_file_extensions(self):
        return self._vtk_obj.GetFileExtensions()
    file_extensions = traits.Property(_get_file_extensions, help=\
        """
        Get the file extensions for this format. Returns a string with a
        space separated list of extensions in the format .extension
        """
    )

    def _get_internal_file_name(self):
        return self._vtk_obj.GetInternalFileName()
    internal_file_name = traits.Property(_get_internal_file_name, help=\
        """
        Set/Get the internal file name
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: virtual int CanReadFile(const char *fname)
        Return non zero if the reader can read the given file name.
        Should be implemented by all sub-classes of ImageReader2. For
        non zero return values the following values are to be used
          1 - I think I can read the file but I cannot prove it
          2 - I definitely can read the file
          3 - I can read the file and I have validated that I am the
              correct reader for this file
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def compute_internal_file_name(self, *args):
        """
        V.compute_internal_file_name(int)
        C++: virtual void ComputeInternalFileName(int slice)
        Set/Get the internal file name
        """
        ret = self._wrap_call(self._vtk_obj.ComputeInternalFileName, *args)
        return ret

    def open_file(self):
        """
        V.open_file() -> int
        C++: virtual int OpenFile()"""
        ret = self._vtk_obj.OpenFile()
        return ret
        

    def seek_file(self, *args):
        """
        V.seek_file(int, int, int)
        C++: virtual void SeekFile(int i, int j, int k)"""
        ret = self._wrap_call(self._vtk_obj.SeekFile, *args)
        return ret

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
            return super(ImageReader2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReader2 properties', scrollable=True, resizable=True,
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
            title='Edit ImageReader2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReader2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

