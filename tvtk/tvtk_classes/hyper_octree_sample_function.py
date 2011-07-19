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

from tvtk.tvtk_classes.hyper_octree_algorithm import HyperOctreeAlgorithm


class HyperOctreeSampleFunction(HyperOctreeAlgorithm):
    """
    HyperOctreeSampleFunction - sample an implicit function over an
    
    Superclass: HyperOctreeAlgorithm
    
    HyperOctreeSampleFunction is a source object that evaluates an
    implicit function to drive the subdivision process. The user can
    specify the threshold over which a subdivision occurs, the maximum
    and minimum level of subdivisions and the dimension of the
    hyperoctree.
    
    See Also:
    
    SampleFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeSampleFunction, obj, update, **traits)
    
    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set what type of scalar data this source should generate.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        Set what type of scalar data this source should generate.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_char(self):
        """
        V.set_output_scalar_type_to_char()
        C++: void SetOutputScalarTypeToChar()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToChar()

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    min_levels = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the minimal number of levels of systematic subdivision.
        \pre positive_min_levels: min_levels>=_0
        \post is_set: this->_get_min_levels()==min_levels
        """
    )
    def _min_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinLevels,
                        self.min_levels)

    height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the length along the y-axis. Relevant only if
        get_dimension()>=_2
        \pre positive_height: height>0
        \post height_is_set: get_height()==height
        """
    )
    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the length along the x-axis.
        \pre positive_width: width>0
        \post width_is_set: get_width()==width
        """
    )
    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    depth = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Return the length along the z-axis. Relevant only if
        get_dimension()>=_3
        \pre positive_depth: depth>0
        \post depth_is_set: get_depth()==depth
        """
    )
    def _depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepth,
                        self.depth)

    levels = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the maximum number of levels of the hyperoctree. If
        get_min_levels()>=levels, get_min_levels() is changed to levels-1.
        \pre positive_levels: levels>=1
        \post is_set: this->_get_levels()==levels
        \post min_is_valid: this->_get_min_levels()<this->_get_levels()
        """
    )
    def _levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevels,
                        self.levels)

    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function to use to generate data.
        """
    )

    threshold = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set the threshold over which a subdivision is required.
        \pre positive_threshold: threshold>=0
        \post is_set: this->_get_threshold()==threshold
        """
    )
    def _threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreshold,
                        self.threshold)

    dimension = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    size = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('min_levels', 'GetMinLevels'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'), ('progress_text',
    'GetProgressText'), ('height', 'GetHeight'), ('width', 'GetWidth'),
    ('depth', 'GetDepth'), ('levels', 'GetLevels'), ('threshold',
    'GetThreshold'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('dimension', 'GetDimension'), ('size', 'GetSize'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'depth', 'dimension', 'height', 'levels',
    'min_levels', 'origin', 'progress_text', 'size', 'threshold',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeSampleFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeSampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['depth', 'dimension', 'height', 'levels',
            'min_levels', 'origin', 'size', 'threshold', 'width']),
            title='Edit HyperOctreeSampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeSampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

