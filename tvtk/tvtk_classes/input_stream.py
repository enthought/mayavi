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


class InputStream(Object):
    """
    InputStream - Wraps a binary input stream with a VTK interface.
    
    Superclass: Object
    
    InputStream provides a VTK-style interface wrapping around a
    standard input stream.  The access methods are virtual so that
    subclasses can transparently provide decoding of an encoded stream.
    Data lengths for Seek and Read calls refer to the length of the input
    data.  The actual length in the stream may differ for subclasses that
    implement an encoding scheme.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInputStream, obj, update, **traits)
    
    def end_reading(self):
        """
        V.end_reading()
        C++: virtual void EndReading()
        Called after all desired calls to Seek and Read have been made.
        After this call, the caller is free to change the position of the
        stream.  Additional reads should not be done until after another
        call to start_reading.
        """
        ret = self._vtk_obj.EndReading()
        return ret
        

    def read(self, *args):
        """
        V.read(string, int) -> int
        C++: unsigned long Read(char *data, unsigned long length)
        Read input data of the given length.  Returns amount actually
        read.
        """
        ret = self._wrap_call(self._vtk_obj.Read, *args)
        return ret

    def seek(self, *args):
        """
        V.seek(int) -> int
        C++: virtual int Seek(unsigned long offset)
        Seek to the given offset in the input data.  Returns 1 for
        success, 0 for failure.
        """
        ret = self._wrap_call(self._vtk_obj.Seek, *args)
        return ret

    def start_reading(self):
        """
        V.start_reading()
        C++: virtual void StartReading()
        Called after the stream position has been set by the caller, but
        before any Seek or Read calls.  The stream position should not be
        adjusted by the caller until after an end_reading call.
        """
        ret = self._vtk_obj.StartReading()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InputStream, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit InputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

