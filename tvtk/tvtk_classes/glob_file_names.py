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


class GlobFileNames(Object):
    """
    GlobFileNames - find files that match a wildcard pattern
    
    Superclass: Object
    
    GlobFileNames is a utility for finding files and directories that
    match a given wildcard pattern.  Allowed wildcards are
    *, ?, [...], [!...]. The "*" wildcard matches any substring, the "?"
       matches any single character, the [...] matches any one of the
       enclosed characters, e.g. [abc] will match one of a, b, or c,
       while [0-9] will match any digit, and [!...] will match any single
       character except for the ones within the brackets.  Special
       treatment is given to "/" (or "\" on Windows) because these are
       path separators.  These are never matched by a wildcard, they are
       only matched with another file separator.
    
    Caveats:
    
    This function performs case-sensitive matches on UNIX and
    case-insensitive matches on Windows.
    
    See Also:
    
    Directory
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlobFileNames, obj, update, **traits)
    
    recurse = tvtk_base.false_bool_trait(help=\
        """
        Recurse into subdirectories.
        """
    )
    def _recurse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRecurse,
                        self.recurse_)

    directory = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the directory in which to perform the glob.  If this is not
        set, then the current directory will be used.  Also, if you use a
        glob pattern that contains absolute path (one that starts with
        "/" or a drive letter) then that absolute path will be used and
        Directory will be ignored.
        """
    )
    def _directory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirectory,
                        self.directory)

    def _get_file_names(self):
        return wrap_vtk(self._vtk_obj.GetFileNames())
    file_names = traits.Property(_get_file_names, help=\
        """
        Get an array that contains all the file names.
        """
    )

    def get_nth_file_name(self, *args):
        """
        V.get_nth_file_name(int) -> string
        C++: const char *GetNthFileName(int index)
        Return the file at the given index, the indexing is 0 based.
        """
        ret = self._wrap_call(self._vtk_obj.GetNthFileName, *args)
        return ret

    def _get_number_of_file_names(self):
        return self._vtk_obj.GetNumberOfFileNames()
    number_of_file_names = traits.Property(_get_number_of_file_names, help=\
        """
        Return the number of files found.
        """
    )

    def add_file_names(self, *args):
        """
        V.add_file_names(string) -> int
        C++: int AddFileNames(const char *pattern)
        Search for all files that match the given expression, sort them,
        and add them to the output.  This method can be called repeatedly
        to add files matching additional patterns. Returns 1 if
        successful, otherwise returns zero.
        """
        ret = self._wrap_call(self._vtk_obj.AddFileNames, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the glob by clearing the list of output filenames.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('directory', 'GetDirectory'), ('reference_count',
    'GetReferenceCount'), ('recurse', 'GetRecurse'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'recurse', 'directory'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GlobFileNames, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GlobFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['recurse'], [], ['directory']),
            title='Edit GlobFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GlobFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

