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


class VolumeReader(ImageAlgorithm):
    """
    VolumeReader - read image files
    
    Superclass: ImageAlgorithm
    
    VolumeReader is a source object that reads image files.
    
    volume_reader creates structured point datasets. The dimension of the
    dataset depends upon the number of files read. Reading a single file
    results in a 2d image, while reading more than one file results in a
    3d volume.
    
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
    swap_bytes, which turns on/off byte swapping. Consider using
    ImageReader as a replacement.
    
    See Also:
    
    SliceCubes MarchingCubes PNMReader Volume16Reader
    ImageReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeReader, obj, update, **traits)
    
    data_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    file_prefix = tvtk_base.vtk_file_prefix("", help=\
        """
        Specify file prefix for the image file(s).
        """
    )
    def _file_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePrefix,
                        self.file_prefix)

    data_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    image_range = traits.Array(shape=(2,), value=(1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _image_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageRange,
                        self.image_range)

    file_pattern = traits.String(r"%s.%d", enter_set=True, auto_set=False, help=\
        """
        The sprintf format used to build filename from file_prefix and
        number.
        """
    )
    def _file_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePattern,
                        self.file_pattern)

    def get_image(self, *args):
        """
        V.get_image(int) -> ImageData
        C++: virtual ImageData *GetImage(int ImageNumber)
        Other objects make use of this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetImage, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('file_pattern',
    'GetFilePattern'), ('file_prefix', 'GetFilePrefix'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'), ('data_spacing',
    'GetDataSpacing'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('image_range', 'GetImageRange'), ('data_origin', 'GetDataOrigin'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'data_origin', 'data_spacing', 'file_pattern',
    'file_prefix', 'image_range', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['data_origin', 'data_spacing', 'file_pattern',
            'file_prefix', 'image_range']),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

