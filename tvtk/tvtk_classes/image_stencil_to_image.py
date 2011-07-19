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


class ImageStencilToImage(ImageAlgorithm):
    """
    ImageStencilToImage - Convert an image stencil into an image
    
    Superclass: ImageAlgorithm
    
    ImageStencilToImage will convert an image stencil into a binary
    image.  The default output will be an 8-bit image with a value of 1
    inside the stencil and 0 outside.  When used in combination with
    PolyDataToImageStencil or ImplicitFunctionToImageStencil, this
    can be used to create a binary image from a mesh or a function.
    
    See Also:
    
    ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencilToImage, obj, update, **traits)
    
    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        The desired output scalar type.  The default is unsigned char.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        The desired output scalar type.  The default is unsigned char.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_char(self):
        """
        V.set_output_scalar_type_to_char()
        C++: void SetOutputScalarTypeToChar()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToChar()

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        The desired output scalar type.  The default is unsigned char.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    outside_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The value to use outside the stencil.  The default is 0.
        """
    )
    def _outside_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutsideValue,
                        self.outside_value)

    inside_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The value to use inside the stencil.  The default is 1.
        """
    )
    def _inside_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideValue,
                        self.inside_value)

    _updateable_traits_ = \
    (('inside_value', 'GetInsideValue'), ('outside_value',
    'GetOutsideValue'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'inside_value', 'outside_value',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencilToImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencilToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['inside_value', 'outside_value']),
            title='Edit ImageStencilToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencilToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

