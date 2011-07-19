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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageThreshold(ThreadedImageAlgorithm):
    """
    ImageThreshold -  Flexible threshold
    
    Superclass: ThreadedImageAlgorithm
    
    ImageThreshold can do binary or continuous thresholding for lower,
    upper or a range of data.  The output data type may be different than
    the output, but defaults to the same type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageThreshold, obj, update, **traits)
    
    replace_in = tvtk_base.false_bool_trait(help=\
        """
        Determines whether to replace the pixel in range with in_value
        """
    )
    def _replace_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceIn,
                        self.replace_in_)

    replace_out = tvtk_base.false_bool_trait(help=\
        """
        Determines whether to replace the pixel out of range with
        out_value
        """
    )
    def _replace_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceOut,
                        self.replace_out_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the desired output scalar type to cast to
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        Set the desired output scalar type to cast to
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_signed_char(self):
        """
        V.set_output_scalar_type_to_signed_char()
        C++: void SetOutputScalarTypeToSignedChar()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToSignedChar()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    in_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Replace the in range pixels with this value.
        """
    )
    def _in_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInValue,
                        self.in_value)

    out_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Replace the in range pixels with this value.
        """
    )
    def _out_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutValue,
                        self.out_value)

    def _get_lower_threshold(self):
        return self._vtk_obj.GetLowerThreshold()
    lower_threshold = traits.Property(_get_lower_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _get_upper_threshold(self):
        return self._vtk_obj.GetUpperThreshold()
    upper_threshold = traits.Property(_get_upper_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        The values in a range (inclusive) match
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double thresh)
        The values less than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double thresh)
        The values greater than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('in_value', 'GetInValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('replace_out', 'GetReplaceOut'), ('replace_in', 'GetReplaceIn'),
    ('debug', 'GetDebug'), ('out_value', 'GetOutValue'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'replace_in', 'replace_out', 'in_value',
    'number_of_threads', 'out_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageThreshold, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['replace_in', 'replace_out'], [], ['in_value',
            'number_of_threads', 'out_value']),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

