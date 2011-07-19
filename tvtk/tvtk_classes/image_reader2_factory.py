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


class ImageReader2Factory(Object):
    """
    ImageReader2Factory - Superclass of binary file readers.
    
    Superclass: Object
    
    ImageReader2Factory: This class is used to create a
    ImageReader2 object given a path name to a file.  It calls
    can_read_file on all available readers until one of them returns true. 
    The available reader list comes from three places.  In the
    initialize_readers function of this class, built-in VTK classes are
    added to the list, users can call register_reader, or users can create
    a ObjectFactory that has create_object method that returns a new
    ImageReader2 sub class when given the string
    "vtk_image_reader_object".  This way applications can be extended with
    new readers via a plugin dll or by calling register_reader. Of course
    all of the readers that are part of the vtk release are made
    automatically available.
    
    See Also:
    
    ImageReader2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReader2Factory, obj, update, **traits)
    
    def get_registered_readers(self, *args):
        """
        V.get_registered_readers(ImageReader2Collection)
        C++: static void GetRegisteredReaders(ImageReader2Collection *)
        The caller must allocate the ImageReader2Collection and pass
        in the pointer to this method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetRegisteredReaders, *my_args)
        return ret

    def create_image_reader2(self, *args):
        """
        V.create_image_reader2(string) -> ImageReader2
        C++: static ImageReader2 *CreateImageReader2(const char *path)"""
        ret = self._wrap_call(self._vtk_obj.CreateImageReader2, *args)
        return wrap_vtk(ret)

    def register_reader(self, *args):
        """
        V.register_reader(ImageReader2)
        C++: static void RegisterReader(ImageReader2 *r)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegisterReader, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageReader2Factory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReader2Factory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ImageReader2Factory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReader2Factory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

