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


class ImageMask(ThreadedImageAlgorithm):
    """
    ImageMask - Combines a mask and an image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMask combines a mask with an image.  Non zero mask implies
    the output pixel will be the same as the image. If a mask pixel is
    zero,  then the output pixel is set to "_masked_value".  The filter
    also has the option to pass the mask through a boolean not operation
    before processing the image. This reverses the passed and replaced
    pixels. The two inputs should have the same "_whole_extent". The mask
    input should be unsigned char, and the image scalar type is the same
    as the output scalar type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMask, obj, update, **traits)
    
    not_mask = tvtk_base.false_bool_trait(help=\
        """
        When Not Mask is on, the mask is passed through a boolean not
        before it is used to mask the image.  The effect is to pass the
        pixels where the input mask is zero, and replace the pixels where
        the input value is non zero.
        """
    )
    def _not_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNotMask,
                        self.not_mask_)

    mask_alpha = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the alpha blending value for the mask The input image is
        assumed to be at alpha = 1.0 and the mask image uses this alpha
        to blend using an over operator.
        """
    )
    def _mask_alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskAlpha,
                        self.mask_alpha)

    def _get_masked_output_value_length(self):
        return self._vtk_obj.GetMaskedOutputValueLength()
    masked_output_value_length = traits.Property(_get_masked_output_value_length, help=\
        """
        set_get the value of the output pixel replaced by mask.
        """
    )

    def set_image_input(self, *args):
        """
        V.set_image_input(ImageData)
        C++: void SetImageInput(ImageData *in)
        Set the input to be masked.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetImageInput, *my_args)
        return ret

    def set_input1(self, *args):
        """
        V.set_input1(DataObject)
        C++: virtual void SetInput1(DataObject *in)
        Set the two inputs to this filter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1, *my_args)
        return ret

    def set_input2(self, *args):
        """
        V.set_input2(DataObject)
        C++: virtual void SetInput2(DataObject *in)
        Set the two inputs to this filter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2, *my_args)
        return ret

    def set_mask_input(self, *args):
        """
        V.set_mask_input(ImageData)
        C++: void SetMaskInput(ImageData *in)
        Set the mask to be used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMaskInput, *my_args)
        return ret

    def set_masked_output_value(self, *args):
        """
        V.set_masked_output_value(float)
        C++: void SetMaskedOutputValue(double v)
        V.set_masked_output_value(float, float)
        C++: void SetMaskedOutputValue(double v1, double v2)
        V.set_masked_output_value(float, float, float)
        C++: void SetMaskedOutputValue(double v1, double v2, double v3)
        set_get the value of the output pixel replaced by mask.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaskedOutputValue, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('not_mask', 'GetNotMask'),
    ('debug', 'GetDebug'), ('mask_alpha', 'GetMaskAlpha'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'not_mask',
    'release_data_flag', 'mask_alpha', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMask, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['not_mask'], [], ['mask_alpha', 'number_of_threads']),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

