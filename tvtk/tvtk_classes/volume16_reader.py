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

from tvtk.tvtk_classes.volume_reader import VolumeReader


class Volume16Reader(VolumeReader):
    """
    Volume16Reader - read 16 bit image files
    
    Superclass: VolumeReader
    
    Volume16Reader is a source object that reads 16 bit image files.
    
    volume16_reader creates structured point datasets. The dimension of
    the dataset depends upon the number of files read. Reading a single
    file results in a 2d image, while reading more than one file results
    in a 3d volume.
    
    File names are created using file_pattern and file_prefix as follows:
    sprintf (filename, file_pattern, file_prefix, number); where number is
    in the range image_range[_0] to image_range[_1]. If image_range[_1] <=
    image_range[_0], then slice number image_range[_0] is read. Thus to read
    an image set image_range[_0] = image_range[_1] = slice number. The
    default behavior is to read a single file (i.e., image slice 1).
    
    The data_mask instance variable is used to read data files with
    imbedded connectivity or segmentation information. For example, some
    data has the high order bit set to indicate connected surface. The
    data_mask allows you to select this data. Other important ivars
    include header_size, which allows you to skip over initial info, and
    swap_bytes, which turns on/off byte swapping.
    
    The Transform instance variable specifies a permutation
    transformation to map slice space into world space. ImageReader
    has replaced the functionality of this class and should be used
    instead.
    
    See Also:
    
    SliceCubes MarchingCubes ImageReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolume16Reader, obj, update, **traits)
    
    swap_bytes = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off byte swapping.
        """
    )
    def _swap_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapBytes,
                        self.swap_bytes_)

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

    data_mask = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify a mask used to eliminate data in the data file (e.g.,
        connectivity bits).
        """
    )
    def _data_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataMask,
                        self.data_mask)

    data_dimensions = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataDimensions,
                        self.data_dimensions)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set/Get transformation matrix to transform the data from slice
        space into world space. This matrix must be a permutation matrix.
        To qualify, the sums of the rows must be + or - 1.
        """
    )

    header_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of bytes to seek over at start of image.
        """
    )
    def _header_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeaderSize,
                        self.header_size)

    _updateable_traits_ = \
    (('data_byte_order', 'GetDataByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('data_mask', 'GetDataMask'),
    ('swap_bytes', 'GetSwapBytes'), ('progress_text', 'GetProgressText'),
    ('file_pattern', 'GetFilePattern'), ('header_size', 'GetHeaderSize'),
    ('data_dimensions', 'GetDataDimensions'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('file_prefix',
    'GetFilePrefix'), ('data_spacing', 'GetDataSpacing'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('image_range',
    'GetImageRange'), ('data_origin', 'GetDataOrigin'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'swap_bytes', 'data_byte_order',
    'data_dimensions', 'data_mask', 'data_origin', 'data_spacing',
    'file_pattern', 'file_prefix', 'header_size', 'image_range',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Volume16Reader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Volume16Reader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['swap_bytes'], ['data_byte_order'],
            ['data_dimensions', 'data_mask', 'data_origin', 'data_spacing',
            'file_pattern', 'file_prefix', 'header_size', 'image_range']),
            title='Edit Volume16Reader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Volume16Reader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

