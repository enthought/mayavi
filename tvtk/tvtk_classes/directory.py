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


class Directory(Object):
    """
    Directory - OS independent class for access and manipulation of
    system directories
    
    Superclass: Object
    
    Directory provides a portable way of finding the names of the
    files in a system directory.  It also provides methods of
    manipulating directories.
    
    Caveats:
    
    Directory works with windows and unix only.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDirectory, obj, update, **traits)
    
    def get_current_working_directory(self, *args):
        """
        V.get_current_working_directory(string, int) -> string
        C++: static const char *GetCurrentWorkingDirectory(char *buf,
            unsigned int len)
        Get the current working directory.
        """
        ret = self._wrap_call(self._vtk_obj.GetCurrentWorkingDirectory, *args)
        return ret

    def get_file(self, *args):
        """
        V.get_file(int) -> string
        C++: const char *GetFile(IdType index)
        Return the file at the given index, the indexing is 0 based
        """
        ret = self._wrap_call(self._vtk_obj.GetFile, *args)
        return ret

    def _get_files(self):
        return wrap_vtk(self._vtk_obj.GetFiles())
    files = traits.Property(_get_files, help=\
        """
        Get an array that contains all the file names.
        """
    )

    def _get_number_of_files(self):
        return self._vtk_obj.GetNumberOfFiles()
    number_of_files = traits.Property(_get_number_of_files, help=\
        """
        Return the number of files in the current directory.
        """
    )

    def create_directory(self, *args):
        """
        V.create_directory(string) -> int
        C++: static int CreateDirectory(const char *dir)
        @deprecated Replaced by Directory::MakeDirectory() as of VTK
        5.0.
        """
        ret = self._wrap_call(self._vtk_obj.CreateDirectory, *args)
        return ret

    def delete_directory(self, *args):
        """
        V.delete_directory(string) -> int
        C++: static int DeleteDirectory(const char *dir)
        Remove a directory.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteDirectory, *args)
        return ret

    def file_is_directory(self, *args):
        """
        V.file_is_directory(string) -> int
        C++: int FileIsDirectory(const char *name)
        Return true if the file is a directory.  If the file is not an
        absolute path, it is assumed to be relative to the opened
        directory. If no directory has been opened, it is assumed to be
        relative to the current working directory.
        """
        ret = self._wrap_call(self._vtk_obj.FileIsDirectory, *args)
        return ret

    def make_directory(self, *args):
        """
        V.make_directory(string) -> int
        C++: static int MakeDirectory(const char *dir)
        Create directory.
        """
        ret = self._wrap_call(self._vtk_obj.MakeDirectory, *args)
        return ret

    def open(self, *args):
        """
        V.open(string) -> int
        C++: int Open(const char *dir)
        Open the specified directory and load the names of the files in
        that directory. 0 is returned if the directory can not be opened,
        1 if it is opened.
        """
        ret = self._wrap_call(self._vtk_obj.Open, *args)
        return ret

    def rename(self, *args):
        """
        V.rename(string, string) -> int
        C++: static int Rename(const char *oldname, const char *newname)
        Rename a file or directory.
        """
        ret = self._wrap_call(self._vtk_obj.Rename, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Directory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Directory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Directory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Directory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

