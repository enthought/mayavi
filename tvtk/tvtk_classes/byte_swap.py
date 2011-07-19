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

from tvtk.tvtk_classes.object import Object


class ByteSwap(Object):
    """
    ByteSwap - perform machine dependent byte swapping
    
    Superclass: Object
    
    ByteSwap is used by other classes to perform machine dependent
    byte swapping. Byte swapping is often used when reading or writing
    binary files.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkByteSwap, obj, update, **traits)
    
    def swap2_be(self):
        """
        V.swap2_be()
        C++: static void Swap2BE(void *p)
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ret = self._vtk_obj.Swap2BE()
        return ret
        

    def swap2_be_range(self, *args):
        """
        V.swap2_be_range(, int)
        C++: static void Swap2BERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap2BERange, *args)
        return ret

    def swap2_le(self):
        """
        V.swap2_le()
        C++: static void Swap2LE(void *p)
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ret = self._vtk_obj.Swap2LE()
        return ret
        

    def swap2_le_range(self, *args):
        """
        V.swap2_le_range(, int)
        C++: static void Swap2LERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap2LERange, *args)
        return ret

    def swap4_be(self):
        """
        V.swap4_be()
        C++: static void Swap4BE(void *p)
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ret = self._vtk_obj.Swap4BE()
        return ret
        

    def swap4_be_range(self, *args):
        """
        V.swap4_be_range(, int)
        C++: static void Swap4BERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap4BERange, *args)
        return ret

    def swap4_le(self):
        """
        V.swap4_le()
        C++: static void Swap4LE(void *p)
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ret = self._vtk_obj.Swap4LE()
        return ret
        

    def swap4_le_range(self, *args):
        """
        V.swap4_le_range(, int)
        C++: static void Swap4LERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap4LERange, *args)
        return ret

    def swap8_be(self):
        """
        V.swap8_be()
        C++: static void Swap8BE(void *p)
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ret = self._vtk_obj.Swap8BE()
        return ret
        

    def swap8_be_range(self, *args):
        """
        V.swap8_be_range(, int)
        C++: static void Swap8BERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap8BERange, *args)
        return ret

    def swap8_le(self):
        """
        V.swap8_le()
        C++: static void Swap8LE(void *p)
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ret = self._vtk_obj.Swap8LE()
        return ret
        

    def swap8_le_range(self, *args):
        """
        V.swap8_le_range(, int)
        C++: static void Swap8LERange(void *p, int num)
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ret = self._wrap_call(self._vtk_obj.Swap8LERange, *args)
        return ret

    def swap_void_range(self, *args):
        """
        V.swap_void_range(, int, int)
        C++: static void SwapVoidRange(void *buffer, int numWords,
            int wordSize)
        Swaps the bytes of a buffer.  Uses an arbitrary word size, but
        assumes the word size is divisible by two.
        """
        ret = self._wrap_call(self._vtk_obj.SwapVoidRange, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ByteSwap, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ByteSwap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ByteSwap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ByteSwap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

