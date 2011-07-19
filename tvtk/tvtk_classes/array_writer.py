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

from tvtk.tvtk_classes.writer import Writer


class ArrayWriter(Writer):
    """
    ArrayWriter - Serialize sparse and dense arrays to a file or
    stream.
    
    Superclass: Writer
    
    ArrayWriter serializes sparse and dense array data using a
    text-based format that is human-readable and easily parsed (default
    option).  The write_binary array option can be used to serialize the
    sparse and dense array data using a binary format that is optimized
    for rapid throughput.
    
    ArrayWriter can be used in two distinct ways: first, it can be
    used as a normal pipeline filter, which writes its inputs to a file. 
    Alternatively, static methods are provided for writing Array
    instances to files or arbitrary c++ streams.
    
    Inputs:
      Input port 0: (required) ArrayData object containing a single
    sparse or dense
                               array.
    
    Output Format:
      See
    http://www.kitware.com/_infovis_wiki/index.php/_n-_way__array__file__formats
    for
      details on how ArrayWriter encodes data.
    
    See Also:
    
    ArrayReader
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayWriter, obj, update, **traits)
    
    binary = tvtk_base.false_bool_trait(help=\
        """
        Get / set whether data will be written in binary format (when
        used as a filter).
        """
    )
    def _binary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinary,
                        self.binary_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get / set the filename where data will be stored (when used as a
        filter).
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('binary', 'GetBinary'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'binary', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['binary'], [], ['file_name']),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

