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


class SortFileNames(Object):
    """
    SortFileNames - Group and sort a set of filenames
    
    Superclass: Object
    
    SortFileNames will take a list of filenames (e.g. from a file load
    dialog) and sort them into one or more series.  If the input list of
    filenames contains any directories, these can be removed before
    sorting using the skip_directories flag.  This class should be used
    where information about the series groupings can be determined by the
    filenames, but it might not be successful in cases where the
    information about the series groupings is stored in the files
    themselves (e.g DICOM).
    
    See Also:
    
    ImageReader2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSortFileNames, obj, update, **traits)
    
    ignore_case = tvtk_base.false_bool_trait(help=\
        """
        Ignore case when sorting.  This flag is honored by both the
        sorting and the grouping. This is off by default.
        """
    )
    def _ignore_case_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIgnoreCase,
                        self.ignore_case_)

    numeric_sort = tvtk_base.false_bool_trait(help=\
        """
        Sort the files numerically, rather than lexicographically. For
        filenames that contain numbers, this means the order will be
        ["file8.dat", "file9.dat", "file10.dat"] instead of the usual
        alphabetic sorting order ["file10.dat" "file8.dat", "file9.dat"].
        numeric_sort is off by default.
        """
    )
    def _numeric_sort_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumericSort,
                        self.numeric_sort_)

    skip_directories = tvtk_base.false_bool_trait(help=\
        """
        Skip directories. If this flag is set, any input item that is a
        directory rather than a file will not be included in the output. 
        This is off by default.
        """
    )
    def _skip_directories_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSkipDirectories,
                        self.skip_directories_)

    grouping = tvtk_base.false_bool_trait(help=\
        """
        Sort the file names into groups, according to similarity in
        filename name and path.  Files in different directories, or with
        different extensions, or which do not fit into the same numbered
        series will be placed into different groups.  This is off by
        default.
        """
    )
    def _grouping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGrouping,
                        self.grouping_)

    def _get_input_file_names(self):
        return wrap_vtk(self._vtk_obj.GetInputFileNames())
    def _set_input_file_names(self, arg):
        old_val = self._get_input_file_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetInputFileNames,
                        my_arg[0])
        self.trait_property_changed('input_file_names', old_val, arg)
    input_file_names = traits.Property(_get_input_file_names, _set_input_file_names, help=\
        """
        Set a list of file names to group and sort.
        """
    )

    def _get_file_names(self):
        return wrap_vtk(self._vtk_obj.GetFileNames())
    file_names = traits.Property(_get_file_names, help=\
        """
        Get the full list of sorted filenames.
        """
    )

    def get_nth_group(self, *args):
        """
        V.get_nth_group(int) -> StringArray
        C++: virtual StringArray *GetNthGroup(int i)
        Get the Nth group of file names.  This method should only be used
        if grouping is on.  If grouping is off, it will always return
        null.
        """
        ret = self._wrap_call(self._vtk_obj.GetNthGroup, *args)
        return wrap_vtk(ret)

    def _get_number_of_groups(self):
        return self._vtk_obj.GetNumberOfGroups()
    number_of_groups = traits.Property(_get_number_of_groups, help=\
        """
        Get the number of groups that the names were split into, if
        grouping is on.  The filenames are automatically split into
        groups, where the filenames in each group will be identical
        except for their series numbers.  If grouping is not on, this
        method will return zero.
        """
    )

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Update the output filenames from the input filenames. This method
        is called automatically by get_file_names() and get_number_of_groups()
        if the input names have changed.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('ignore_case', 'GetIgnoreCase'),
    ('numeric_sort', 'GetNumericSort'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('skip_directories', 'GetSkipDirectories'), ('grouping',
    'GetGrouping'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'grouping', 'ignore_case',
    'numeric_sort', 'skip_directories'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SortFileNames, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SortFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['grouping', 'ignore_case', 'numeric_sort',
            'skip_directories'], [], []),
            title='Edit SortFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SortFileNames properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

