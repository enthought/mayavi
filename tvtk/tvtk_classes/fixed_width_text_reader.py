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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class FixedWidthTextReader(TableAlgorithm):
    """
    FixedWidthTextReader - reader for pulling in text files with
    fixed-width fields
    
    Superclass: TableAlgorithm
    
    FixedWidthTextReader reads in a table from a text file where each
    column occupies a certain number of characters.
    
    This class emits progress_event for every 100 lines it reads.
    
    Caveats:
    
    This first version of the reader will assume that all fields have the
    same width.  It also assumes that the first line in the file has at
    least as many fields (i.e. at least as many characters) as any other
    line in the file.
    
    Thanks:
    
    Thanks to Andy Wilson from Sandia National Laboratories for
    implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFixedWidthTextReader, obj, update, **traits)
    
    strip_white_space = tvtk_base.false_bool_trait(help=\
        """
        If set, this flag will cause the reader to strip whitespace from
        the beginning and ending of each field.  Defaults to off.
        """
    )
    def _strip_white_space_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStripWhiteSpace,
                        self.strip_white_space_)

    have_headers = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether to treat the first line of the file as headers.
        """
    )
    def _have_headers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHaveHeaders,
                        self.have_headers_)

    field_width = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Set/get the field width
        """
    )
    def _field_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldWidth,
                        self.field_width)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('field_width', 'GetFieldWidth'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('have_headers', 'GetHaveHeaders'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('strip_white_space', 'GetStripWhiteSpace'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'have_headers',
    'release_data_flag', 'strip_white_space', 'field_width', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FixedWidthTextReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['have_headers', 'strip_white_space'], [],
            ['field_width', 'file_name']),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

