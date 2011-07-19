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


class ImageReader(ImageReader2):
    """
    ImageReader - Superclass of transformable binary file readers.
    
    Superclass: ImageReader2
    
    ImageReader provides methods needed to read a region from a file.
    It supports both transforms and masks on the input data, but as a
    result is more complicated and slower than its parent class
    ImageReader2.
    
    See Also:
    
    BMPReader PNMReader TIFFReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReader, obj, update, **traits)
    
    data_mask = traits.Long(4294967295, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Data mask.  The data mask is a simply integer whose
        bits are treated as a mask to the bits read from disk.  That is,
        the data mask is bitwise-and'ed to the numbers read from disk. 
        This ivar is stored as 64 bits, the largest mask you will need. 
        The mask will be truncated to the data size required to be read
        (using the least significant bits).
        """
    )
    def _data_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataMask,
                        self.data_mask)

    data_voi = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_voi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataVOI,
                        self.data_voi)

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

    scalar_array_name = traits.String(r"ImageFile", enter_set=True, auto_set=False, help=\
        """
        Set/get the scalar array name for this data set.
        """
    )
    def _scalar_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArrayName,
                        self.scalar_array_name)

    def compute_inverse_transformed_extent(self, *args):
        """
        V.compute_inverse_transformed_extent([int, int, int, int, int, int],
            [int, int, int, int, int, int])
        C++: void ComputeInverseTransformedExtent(int inExtent[6],
            int outExtent[6])"""
        ret = self._wrap_call(self._vtk_obj.ComputeInverseTransformedExtent, *args)
        return ret

    def compute_inverse_transformed_increments(self, *args):
        """
        V.compute_inverse_transformed_increments([int, int, int], [int, int,
            int])
        C++: void ComputeInverseTransformedIncrements(IdType inIncr[3],
             IdType outIncr[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeInverseTransformedIncrements, *args)
        return ret

    def open_and_seek_file(self, *args):
        """
        V.open_and_seek_file([int, int, int, int, int, int], int) -> int
        C++: int OpenAndSeekFile(int extent[6], int slice)"""
        ret = self._wrap_call(self._vtk_obj.OpenAndSeekFile, *args)
        return ret

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
            return super(ImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReader properties', scrollable=True, resizable=True,
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
            title='Edit ImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

