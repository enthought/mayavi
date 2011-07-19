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


class ImplicitModeller(ImageAlgorithm):
    """
    ImplicitModeller - compute distance from input geometry on
    structured point dataset
    
    Superclass: ImageAlgorithm
    
    ImplicitModeller is a filter that computes the distance from the
    input geometry to the points of an output structured point set. This
    distance function can then be "contoured" to generate new, offset
    surfaces from the original geometry. An important feature of this
    object is "capping". If capping is turned on, after the implicit
    model is created, the values on the boundary of the structured points
    dataset are set to the cap value. This is used to force closure of
    the resulting contoured surface. Note, however, that large cap values
    can generate weird surface normals in those cells adjacent to the
    boundary of the dataset. Using smaller cap value will reduce this
    effect. <P> Another important ivar is maximum_distance. This controls
    how far into the volume the distance function is computed from the
    input geometry.  Small values give significant increases in
    performance. However, there can strange sampling effects at the
    extreme range of the maximum_distance. <P> In order to properly
    execute and sample the input data, a rectangular region in space must
    be defined (this is the ivar model_bounds).  If not explicitly
    defined, the model bounds will be computed. Note that to avoid
    boundary effects, it is possible to adjust the model bounds (i.e.,
    using the adjust_bounds and adjust_distance ivars) to strictly contain
    the sampled data. <P> This filter has one other unusual capability:
    it is possible to append data in a sequence of operations to generate
    a single output. This is useful when you have multiple datasets and
    want to create a conglomeration of all the data.  However, the user
    must be careful to either specify the model_bounds or specify the
    first item such that its bounds completely contain all other items. 
    This is because the rectangular region of the output can not be
    changed after the 1st Append. <P> The process_mode ivar controls the
    method used within the Append function (where the actual work is done
    regardless if the Append function is explicitly called) to compute
    the implicit model.  If set to work in voxel mode, each voxel is
    visited once.  If set to cell mode, each cell is visited once.  Tests
    have shown once per voxel to be faster when there are a lot of cells
    (at least a thousand?); relative performance improvement increases
    with addition cells. Primitives should not be stripped for best
    performance of the voxel mode.  Also, if explicitly using the Append
    feature many times, the cell mode will probably be better because
    each voxel will be visited each Append.  Append the data before input
    if possible when using the voxel mode.  Do not switch between voxel
    and cell mode between execution of start_append and end_append. <P>
    Further performance improvement is now possible using the per_voxel
    process mode on multi-processor machines (the mode is now
    multithreaded).  Each thread processes a different "slab" of the
    output.  Also, if the input is PolyData, it is appropriately
    clipped for each thread; that is, each thread only considers the
    input which could affect its slab of the output. <P> This filter can
    now produce output of any type supported by ImageData. However to
    support this change, additional sqrts must be executed during the
    Append step.  Previously, the output was initialized to the squared
    cap_value in start_append, the output was updated with squared distance
    values during the Append, and then the sqrt of the distances was
    computed in end_append. To support different scalar types in the
    output (largely to reduce memory requirements as an
    ImageShiftScale and/or ImageCast could have achieved the same
    result), we can't "afford" to save squared value in the output,
    because then we could only represent up to the sqrt of the scalar max
    for an integer type in the output; 1 (instead of 255) for an unsigned
    char; 11 for a char (instead of 127).  Thus this change may result in
    a minor performance degradation.  Non-float output types can be
    scaled to the cap_value by turning scale_to_maximum_distance On.
    
    See Also:
    
    SampleFunction ContourFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitModeller, obj, update, **traits)
    
    adjust_bounds = tvtk_base.true_bool_trait(help=\
        """
        Control how the model bounds are computed. If the ivar
        adjust_bounds is set, then the bounds specified (or computed
        automatically) is modified by the fraction given by
        adjust_distance. This means that the model bounds is expanded in
        each of the x-y-z directions.
        """
    )
    def _adjust_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustBounds,
                        self.adjust_bounds_)

    scale_to_maximum_distance = tvtk_base.false_bool_trait(help=\
        """
        If a non-floating output type is specified, the output distances
        can be scaled to use the entire positive scalar range of the
        output type specified (up to the cap_value which is equal to the
        max for the type unless modified by the user).  For example, if
        scale_to_maximum_distance is On and the output_scalar_type is
        unsigned_char the distances saved in the output would be linearly
        scaled between 0 (for distances "very close" to the surface) and
        255 (at the specifed maximum distance)... assuming the cap_value
        is not changed from 255.
        """
    )
    def _scale_to_maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleToMaximumDistance,
                        self.scale_to_maximum_distance_)

    capping = tvtk_base.true_bool_trait(help=\
        """
        The outer boundary of the structured point set can be assigned a
        particular value. This can be used to close or "cap" all
        surfaces.
        """
    )
    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    process_mode = traits.Trait('per_cell',
    tvtk_base.TraitRevPrefixMap({'per_cell': 1, 'per_voxel': 0}), help=\
        """
        Specify whether to visit each cell once per append or each voxel
        once per append.  Some tests have shown once per voxel to be
        faster when there are a lot of cells (at least a thousand?);
        relative performance improvement increases with addition cells. 
        Primitives should not be stripped for best performance of the
        voxel mode.
        """
    )
    def _process_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessMode,
                        self.process_mode_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the desired output scalar type.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int type)
        Set the desired output scalar type.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_char(self):
        """
        V.set_output_scalar_type_to_char()
        C++: void SetOutputScalarTypeToChar()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToChar()

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set the desired output scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    locator_max_level = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Specify the level of the locator to use when using the per voxel
        process mode.
        """
    )
    def _locator_max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLocatorMaxLevel,
                        self.locator_max_level)

    adjust_distance = traits.Trait(0.0125, traits.Range(-1.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the amount to grow the model bounds (if the ivar
        adjust_bounds is set). The value is a fraction of the maximum
        length of the sides of the box specified by the model bounds.
        """
    )
    def _adjust_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustDistance,
                        self.adjust_distance)

    sample_dimensions = traits.Array(shape=(3,), value=(50, 50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the i-j-k dimensions on which to sample distance
        function.
        """
    )
    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    model_bounds = traits.Array(shape=(6,), value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    number_of_threads = traits.Trait(2, traits.Range(1, 32, enter_set=True, auto_set=False), help=\
        """
        Set / Get the number of threads used during Per-Voxel processing
        mode
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    maximum_distance = traits.Trait(0.1, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / get the distance away from surface of input geometry to
        sample. Smaller values make large increases in performance.
        """
    )
    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    cap_value = traits.Float(9.99999968029e+37, enter_set=True, auto_set=False, help=\
        """
        Specify the capping value to use. The cap_value is also used as an
        initial distance value at each point in the dataset.
        """
    )
    def _cap_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapValue,
                        self.cap_value)

    def append(self, *args):
        """
        V.append(DataSet)
        C++: void Append(DataSet *input)
        Append a data set to the existing output. To use this function,
        you'll have to invoke the start_append() method before doing
        successive appends. It's also a good idea to specify the model
        bounds; otherwise the input model bounds is used. When you've
        finished appending, use the end_append() method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds(DataSet) -> float
        C++: double ComputeModelBounds(DataSet *input=NULL)
        Compute model_bounds from input geometry. If input is not
        specified, the input of the filter will be used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *my_args)
        return ret

    def end_append(self):
        """
        V.end_append()
        C++: void EndAppend()
        Method completes the append process.
        """
        ret = self._vtk_obj.EndAppend()
        return ret
        

    def start_append(self):
        """
        V.start_append()
        C++: void StartAppend()
        Initialize the filter for appending data. You must invoke the
        start_append() method before doing successive Appends(). It's also
        a good idea to manually specify the model bounds; otherwise the
        input bounds for the data will be used.
        """
        ret = self._vtk_obj.StartAppend()
        return ret
        

    _updateable_traits_ = \
    (('scale_to_maximum_distance', 'GetScaleToMaximumDistance'),
    ('model_bounds', 'GetModelBounds'), ('maximum_distance',
    'GetMaximumDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('adjust_distance', 'GetAdjustDistance'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('process_mode',
    'GetProcessMode'), ('adjust_bounds', 'GetAdjustBounds'),
    ('progress_text', 'GetProgressText'), ('capping', 'GetCapping'),
    ('debug', 'GetDebug'), ('locator_max_level', 'GetLocatorMaxLevel'),
    ('number_of_threads', 'GetNumberOfThreads'), ('cap_value',
    'GetCapValue'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('sample_dimensions', 'GetSampleDimensions'),
    ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'adjust_bounds', 'capping', 'debug',
    'global_warning_display', 'release_data_flag',
    'scale_to_maximum_distance', 'process_mode', 'adjust_distance',
    'cap_value', 'locator_max_level', 'maximum_distance', 'model_bounds',
    'number_of_threads', 'progress_text', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitModeller, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['adjust_bounds', 'capping',
            'scale_to_maximum_distance'], ['process_mode'], ['adjust_distance',
            'cap_value', 'locator_max_level', 'maximum_distance', 'model_bounds',
            'number_of_threads', 'sample_dimensions']),
            title='Edit ImplicitModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

