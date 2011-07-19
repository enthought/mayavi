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


class TextCodecFactory(Object):
    """
    TextCodecFactory - maintain a list of text codecs and return
    instances
    
    Superclass: Object
    
    A single class to hold registered codecs and return instances of them
    based on either a decriptive name (UTF16 or latin-1) or by asking who
    can handle a given vtkstd::vector<unsigned char>
    
    Thanks:
    
    Thanks to Tim Shed from Sandia National Laboratories for his work on
    the concepts and to Marcus Hanwell and Jeff Baumes of Kitware for
    keeping me out of the weeds
    
    See Also:
    
    TextCodec
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextCodecFactory, obj, update, **traits)
    
    def codec_for_name(self, *args):
        """
        V.codec_for_name(string) -> TextCodec
        C++: static TextCodec *CodecForName(const char *CodecName)
        Given a codec/storage name try to find one of our registered
        codecs that can handle it.  This is non-deterministic, very messy
        and should not be your first thing to try. The registered
        callbacks are tried in the order they are registered.
        """
        ret = self._wrap_call(self._vtk_obj.CodecForName, *args)
        return wrap_vtk(ret)

    def initialize(self):
        """
        V.initialize()
        C++: static void Initialize()
        Initialize core text codecs - needed for the static compilation
        case.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def un_register_all_create_callbacks(self):
        """
        V.un_register_all_create_callbacks()
        C++: static void UnRegisterAllCreateCallbacks()
        Provides mechanism to register/unregister additional callbacks to
        create concrete subclasses of TextCodecFactory to handle
        different protocols. The registered callbacks are tried in the
        order they are registered.
        """
        ret = self._vtk_obj.UnRegisterAllCreateCallbacks()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextCodecFactory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextCodecFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TextCodecFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextCodecFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

