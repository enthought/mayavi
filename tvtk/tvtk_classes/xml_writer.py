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

from tvtk.tvtk_classes.algorithm import Algorithm


class XMLWriter(Algorithm):
    """
    XMLWriter - Superclass for VTK's XML file writers.
    
    Superclass: Algorithm
    
    XMLWriter provides methods implementing most of the functionality
    needed to write VTK XML file formats.  Concrete subclasses provide
    actual writer implementations calling upon this functionality.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLWriter, obj, update, **traits)
    
    encode_appended_data = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether the appended data section is base64 encoded.  If
        encoded, reading and writing will be slower, but the file will be
        fully valid XML and text-only.  If not encoded, the XML
        specification will be violated, but reading and writing will be
        fast.  The default is to do the encoding.
        """
    )
    def _encode_appended_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEncodeAppendedData,
                        self.encode_appended_data_)

    id_type = traits.Trait('int64',
    tvtk_base.TraitRevPrefixMap({'int32': 32, 'int64': 32}), help=\
        """
        Get/Set the size of the IdType values stored in the file.  The
        default is the real size of IdType.
        """
    )
    def _id_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdType,
                        self.id_type_)

    data_mode = traits.Trait('appended',
    tvtk_base.TraitRevPrefixMap({'binary': 1, 'appended': 2, 'ascii': 0}), help=\
        """
        Get/Set the data mode used for the file's data.  The options are
        XMLWriter::Ascii, XMLWriter::Binary, and
        XMLWriter::Appended.
        """
    )
    def _data_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataMode,
                        self.data_mode_)

    byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        Get/Set the byte order of data written to the file.  The default
        is the machine's hardware byte order.
        """
    )
    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    time_step_range = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    block_size = traits.Int(32768, enter_set=True, auto_set=False, help=\
        """
        Get/Set the block size used in compression.  When reading, this
        controls the granularity of how much extra information must be
        read when only part of the data are requested.  The value should
        be a multiple of the largest scalar data type.
        """
    )
    def _block_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlockSize,
                        self.block_size)

    number_of_time_steps = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of time steps
        """
    )
    def _number_of_time_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTimeSteps,
                        self.number_of_time_steps)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the output file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_compressor(self):
        return wrap_vtk(self._vtk_obj.GetCompressor())
    def _set_compressor(self, arg):
        old_val = self._get_compressor()
        self._wrap_call(self._vtk_obj.SetCompressor,
                        deref_vtk(arg))
        self.trait_property_changed('compressor', old_val, arg)
    compressor = traits.Property(_get_compressor, _set_compressor, help=\
        """
        Get/Set the compressor used to compress binary and appended data
        before writing to the file.  Default is a ZLibDataCompressor.
        """
    )

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Which time_step to write.
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Set/Get an input of this algorithm. You should not override these
        methods because they are not the only way to connect a pipeline
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(DataObject)
        C++: void SetInput(DataObject *)
        V.set_input(int, DataObject)
        C++: void SetInput(int, DataObject *)
        Set/Get an input of this algorithm. You should not override these
        methods because they are not the only way to connect a pipeline
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def _get_default_file_extension(self):
        return self._vtk_obj.GetDefaultFileExtension()
    default_file_extension = traits.Property(_get_default_file_extension, help=\
        """
        Get the default file extension for files written by this writer.
        """
    )

    def set_compressor_type(self, *args):
        """
        V.set_compressor_type(int)
        C++: void SetCompressorType(int compressorType)
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._wrap_call(self._vtk_obj.SetCompressorType, *args)
        return ret

    def set_compressor_type_to_none(self):
        """
        V.set_compressor_type_to_none()
        C++: void SetCompressorTypeToNone()
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._vtk_obj.SetCompressorTypeToNone()
        return ret
        

    def set_compressor_type_to_z_lib(self):
        """
        V.set_compressor_type_to_z_lib()
        C++: void SetCompressorTypeToZLib()
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._vtk_obj.SetCompressorTypeToZLib()
        return ret
        

    def start(self):
        """
        V.start()
        C++: void Start()
        API to interface an outside the VTK pipeline control
        """
        ret = self._vtk_obj.Start()
        return ret
        

    def stop(self):
        """
        V.stop()
        C++: void Stop()
        API to interface an outside the VTK pipeline control
        """
        ret = self._vtk_obj.Stop()
        return ret
        

    def write(self):
        """
        V.write() -> int
        C++: int Write()
        Invoke the writer.  Returns 1 for success, 0 for failure.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    def write_next_time(self, *args):
        """
        V.write_next_time(float)
        C++: void WriteNextTime(double time)
        API to interface an outside the VTK pipeline control
        """
        ret = self._wrap_call(self._vtk_obj.WriteNextTime, *args)
        return ret

    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('data_mode', 'GetDataMode'), ('time_step_range', 'GetTimeStepRange'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'),
    ('encode_appended_data', 'GetEncodeAppendedData'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('time_step',
    'GetTimeStep'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('block_size', 'GetBlockSize'), ('abort_execute',
    'GetAbortExecute'), ('id_type', 'GetIdType'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'byte_order',
    'data_mode', 'id_type', 'block_size', 'file_name',
    'number_of_time_steps', 'progress_text', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['encode_appended_data'], ['byte_order', 'data_mode',
            'id_type'], ['block_size', 'file_name', 'number_of_time_steps',
            'time_step', 'time_step_range']),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

