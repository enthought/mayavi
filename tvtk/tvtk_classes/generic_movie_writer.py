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

from tvtk.tvtk_classes.process_object import ProcessObject


class GenericMovieWriter(ProcessObject):
    """
    GenericMovieWriter - an abstract movie writer class.
    
    Superclass: ProcessObject
    
    GenericMovieWriter is the abstract base class for several movie
    writers. The input type is a ImageData. The Start() method will
    open and create the file, the Write() method will output a frame to
    the file (i.e. the contents of the ImageData), End() will finalize
    and close the file.
    
    See Also:
    
    AVIWriter MPEG2Writer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericMovieWriter, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of avi file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_error(self):
        return self._vtk_obj.GetError()
    error = traits.Property(_get_error, help=\
        """
        Was there an error on the last write performed?
        """
    )

    def get_string_from_error_code(self, *args):
        """
        V.get_string_from_error_code(int) -> string
        C++: static const char *GetStringFromErrorCode(
            unsigned long event)
        Converts ErrorCodes and GenericMovieWriter errors to
        strings.
        """
        ret = self._wrap_call(self._vtk_obj.GetStringFromErrorCode, *args)
        return ret

    def end(self):
        """
        V.end()
        C++: virtual void End()
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
        """
        ret = self._vtk_obj.End()
        return ret
        

    def start(self):
        """
        V.start()
        C++: virtual void Start()
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
        """
        ret = self._vtk_obj.Start()
        return ret
        

    def write(self):
        """
        V.write()
        C++: virtual void Write()
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericMovieWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericMovieWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name']),
            title='Edit GenericMovieWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericMovieWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

