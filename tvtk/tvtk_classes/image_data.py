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

from tvtk.tvtk_classes.data_set import DataSet


class ImageData(DataSet):
    """
    ImageData - topologically and geometrically regular array of data
    
    Superclass: DataSet
    
    ImageData is a data object that is a concrete implementation of
    DataSet. ImageData represents a geometric structure that is a
    topological and geometrical regular array of points. Examples include
    volumes (voxel data) and pixmaps.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageData, obj, update, **traits)
    
    scalar_type = traits.Trait('double', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    tvtk_base.TraitRevPrefixMap({'short': 4, 'signed_char': 15, 'int': 6, 'double': 11, 'float': 10, 'unsigned_long': 9, 'long': 8, 'char': 2, 'unsigned_int': 7, 'unsigned_char': 3, 'unsigned_short': 5}), help=\
        """
        Set/Get the data scalar type (i.e VTK_DOUBLE). Note that these
        methods are setting and getting the pipeline scalar type. i.e.
        they are setting the type that the image data will be once it has
        executed. Until the REQUEST_DATA pass the actual scalars may be
        of some other type. This is for backwards compatibility
        """
    )
    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    dimensions = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        \deprecated{This is for backward compatibility only - use
        set_extent().} Same as set_extent(_0, i-1, 0, j-1, 0, k-1)
        """
    )
    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    number_of_scalar_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of scalar components for points. As with the
        set_scalar_type method this is setting pipeline info.
        """
    )
    def _number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfScalarComponents,
                        self.number_of_scalar_components)

    spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    def get_axis_update_extent(self, *args):
        """
        V.get_axis_update_extent(int, int, int)
        C++: virtual void GetAxisUpdateExtent(int axis, int &min,
            int &max)
        Set / Get the extent on just one axis
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisUpdateExtent, *args)
        return ret

    def set_axis_update_extent(self, *args):
        """
        V.set_axis_update_extent(int, int, int)
        C++: virtual void SetAxisUpdateExtent(int axis, int min, int max)
        Set / Get the extent on just one axis
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisUpdateExtent, *args)
        return ret

    extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the extent. On each axis, the extent is defined by the
        index of the first point and the index of the last point.  The
        extent should be set before the "Scalars" are set or allocated. 
        The Extent is stored in the order (X, Y, Z). The dataset extent
        does not have to start at (0,0,0). (0,0,0) is just the extent of
        the origin. The first point (the one with Id=0) is at extent
        (Extent[0],Extent[2],Extent[4]). As for any dataset, a data array
        on point data starts at Id=0.
        """
    )
    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    def get_array_increments(self, *args):
        """
        V.get_array_increments(DataArray, [int, int, int])
        C++: void GetArrayIncrements(DataArray *array,
            IdType increments[3])
        Since various arrays have different number of components, the
        will have different increments.
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayIncrements, *my_args)
        return ret

    def get_array_pointer(self, *args):
        """
        V.get_array_pointer(DataArray, [int, int, int]) ->
        C++: void *GetArrayPointer(DataArray *array,
            int coordinates[3])
        These are convenience methods for getting a pointer from any
        filed array.  It is a start at expanding image filters to process
        any array (not just scalars).
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayPointer, *my_args)
        return ret

    def get_array_pointer_for_extent(self, *args):
        """
        V.get_array_pointer_for_extent(DataArray, [int, int, int, int, int,
             int]) ->
        C++: void *GetArrayPointerForExtent(DataArray *array,
            int extent[6])
        These are convenience methods for getting a pointer from any
        filed array.  It is a start at expanding image filters to process
        any array (not just scalars).
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int', 'int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayPointerForExtent, *my_args)
        return ret

    def get_continuous_increments(self, *args):
        """
        V.get_continuous_increments([int, int, int, int, int, int], int,
            int, int)
        C++: virtual void GetContinuousIncrements(int extent[6],
            IdType &incX, IdType &incY, IdType &incZ)
        Different ways to get the increments for moving around the data.
        inc_x is always returned with 0.  inc_y is returned with the
        increment needed to move from the end of one X scanline of data
        to the start of the next line.  inc_z is filled in with the
        increment needed to move from the end of one image to the start
        of the next.  The proper way to use these values is to for a loop
        over Z, Y, X, C, incrementing the pointer by 1 after each
        component.  When the end of the component is reached, the pointer
        is set to the beginning of the next pixel, thus inc_x is properly
        set to 0.
        """
        ret = self._wrap_call(self._vtk_obj.GetContinuousIncrements, *args)
        return ret

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Return the dimensionality of the data.
        """
    )

    def _get_increments(self):
        return self._vtk_obj.GetIncrements()
    increments = traits.Property(_get_increments, help=\
        """
        Different ways to get the increments for moving around the data.
        get_increments() calls compute_increments() to ensure the
        increments are up to date.
        """
    )

    def get_point_gradient(self, *args):
        """
        V.get_point_gradient(int, int, int, DataArray, [float, float,
            float])
        C++: virtual void GetPointGradient(int i, int j, int k,
            DataArray *s, double g[3])
        Given structured coordinates (i,j,k) for a point in a structured
        point dataset, compute the gradient vector from the scalar data
        at that point. The scalars s are the scalars from which the
        gradient is to be computed. This method will treat structured
        point datasets of any dimension.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'vtkDataArray', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.GetPointGradient, *my_args)
        return ret

    def get_scalar_component_as_double(self, *args):
        """
        V.get_scalar_component_as_double(int, int, int, int) -> float
        C++: virtual double GetScalarComponentAsDouble(int x, int y,
            int z, int component)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentAsDouble, *args)
        return ret

    def get_scalar_component_as_float(self, *args):
        """
        V.get_scalar_component_as_float(int, int, int, int) -> float
        C++: virtual float GetScalarComponentAsFloat(int x, int y, int z,
            int component)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentAsFloat, *args)
        return ret

    def _get_scalar_pointer(self):
        return self._vtk_obj.GetScalarPointer()
    scalar_pointer = traits.Property(_get_scalar_pointer, help=\
        """
        Access the native pointer for the scalar data
        """
    )

    def get_scalar_pointer_for_extent(self, *args):
        """
        V.get_scalar_pointer_for_extent([int, int, int, int, int, int]) ->
        C++: virtual void *GetScalarPointerForExtent(int extent[6])
        Access the native pointer for the scalar data
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarPointerForExtent, *args)
        return ret

    def _get_scalar_size(self):
        return self._vtk_obj.GetScalarSize()
    scalar_size = traits.Property(_get_scalar_size, help=\
        """
        Get the size of the scalar type in bytes.
        """
    )

    def _get_scalar_type_max(self):
        return self._vtk_obj.GetScalarTypeMax()
    scalar_type_max = traits.Property(_get_scalar_type_max, help=\
        """
        These returns the minimum and maximum values the scalar_type can
        hold without overflowing.
        """
    )

    def _get_scalar_type_min(self):
        return self._vtk_obj.GetScalarTypeMin()
    scalar_type_min = traits.Property(_get_scalar_type_min, help=\
        """
        These returns the minimum and maximum values the scalar_type can
        hold without overflowing.
        """
    )

    def get_voxel_gradient(self, *args):
        """
        V.get_voxel_gradient(int, int, int, DataArray, DataArray)
        C++: virtual void GetVoxelGradient(int i, int j, int k,
            DataArray *s, DataArray *g)
        Given structured coordinates (i,j,k) for a voxel cell, compute
        the eight gradient values for the voxel corners. The order in
        which the gradient vectors are arranged corresponds to the
        ordering of the voxel points. Gradient vector is computed by
        central differences (except on edges of volume where forward
        difference is used). The scalars s are the scalars from which the
        gradient is to be computed. This method will treat only 3d
        structured point datasets (i.e., volumes).
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.GetVoxelGradient, *my_args)
        return ret

    def allocate_scalars(self):
        """
        V.allocate_scalars()
        C++: virtual void AllocateScalars()
        Allocate the Scalars object associated with this object.
        """
        ret = self._vtk_obj.AllocateScalars()
        return ret
        

    def compute_cell_id(self, *args):
        """
        V.compute_cell_id([int, int, int]) -> int
        C++: virtual IdType ComputeCellId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        cell id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellId, *args)
        return ret

    def compute_point_id(self, *args):
        """
        V.compute_point_id([int, int, int]) -> int
        C++: virtual IdType ComputePointId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        point id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointId, *args)
        return ret

    def compute_structured_coordinates(self, *args):
        """
        V.compute_structured_coordinates([float, float, float], [int, int,
            int], [float, float, float]) -> int
        C++: virtual int ComputeStructuredCoordinates(double x[3],
            int ijk[3], double pcoords[3])
        Convenience function computes the structured coordinates for a
        point x[3]. The voxel is specified by the array ijk[3], and the
        parametric coordinates in the cell are specified with pcoords[3].
        The function returns a 0 if the point x is outside of the volume,
        and a 1 if inside the volume.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeStructuredCoordinates, *args)
        return ret

    def copy_and_cast_from(self, *args):
        """
        V.copy_and_cast_from(ImageData, [int, int, int, int, int, int])
        C++: virtual void CopyAndCastFrom(ImageData *inData,
            int extent[6])
        V.copy_and_cast_from(ImageData, int, int, int, int, int, int)
        C++: virtual void CopyAndCastFrom(ImageData *inData, int x0,
            int x1, int y0, int y1, int z0, int z1)
        This method is passed a input and output region, and executes the
        filter algorithm to fill the output from the input. It just
        executes a switch statement to call the correct function for the
        regions data types.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAndCastFrom, *my_args)
        return ret

    def set_scalar_component_from_double(self, *args):
        """
        V.set_scalar_component_from_double(int, int, int, int, float)
        C++: virtual void SetScalarComponentFromDouble(int x, int y,
            int z, int component, double v)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarComponentFromDouble, *args)
        return ret

    def set_scalar_component_from_float(self, *args):
        """
        V.set_scalar_component_from_float(int, int, int, int, float)
        C++: virtual void SetScalarComponentFromFloat(int x, int y, int z,
             int component, float v)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarComponentFromFloat, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('dimensions', 'GetDimensions'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('spacing',
    'GetSpacing'), ('update_extent', 'GetUpdateExtent'), ('debug',
    'GetDebug'), ('update_piece', 'GetUpdatePiece'), ('extent',
    'GetExtent'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('scalar_type',
    'GetScalarType'), ('whole_extent', 'GetWholeExtent'),
    ('request_exact_extent', 'GetRequestExactExtent'),
    ('whole_bounding_box', 'GetWholeBoundingBox'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'scalar_type',
    'dimensions', 'extent', 'maximum_number_of_pieces',
    'number_of_scalar_components', 'origin', 'spacing', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            ['scalar_type'], ['dimensions', 'extent', 'maximum_number_of_pieces',
            'number_of_scalar_components', 'origin', 'spacing', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

