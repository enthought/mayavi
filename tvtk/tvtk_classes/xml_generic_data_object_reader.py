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

from tvtk.tvtk_classes.xml_data_reader import XMLDataReader


class XMLGenericDataObjectReader(XMLDataReader):
    """
    XMLGenericDataObjectReader - Read any type of vtk data object
    
    Superclass: XMLDataReader
    
    XMLGenericDataObjectReader reads any type of vtk data object
    encoded in XML format.
    
    See Also:
    
    GenericDataObjectReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLGenericDataObjectReader, obj, update, **traits)
    
    def _get_hierarchical_box_data_set_output(self):
        return wrap_vtk(self._vtk_obj.GetHierarchicalBoxDataSetOutput())
    hierarchical_box_data_set_output = traits.Property(_get_hierarchical_box_data_set_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_hyper_octree_output(self):
        return wrap_vtk(self._vtk_obj.GetHyperOctreeOutput())
    hyper_octree_output = traits.Property(_get_hyper_octree_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_image_data_output(self):
        return wrap_vtk(self._vtk_obj.GetImageDataOutput())
    image_data_output = traits.Property(_get_image_data_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_multi_block_data_set_output(self):
        return wrap_vtk(self._vtk_obj.GetMultiBlockDataSetOutput())
    multi_block_data_set_output = traits.Property(_get_multi_block_data_set_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> DataObject
        C++: DataObject *GetOutput()
        V.get_output(int) -> DataObject
        C++: DataObject *GetOutput(int idx)
        Get the reader's output.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def _get_poly_data_output(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataOutput())
    poly_data_output = traits.Property(_get_poly_data_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_rectilinear_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearGridOutput())
    rectilinear_grid_output = traits.Property(_get_rectilinear_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_structured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredGridOutput())
    structured_grid_output = traits.Property(_get_structured_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_unstructured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGridOutput())
    unstructured_grid_output = traits.Property(_get_unstructured_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def read_output_type(self, *args):
        """
        V.read_output_type(string, bool) -> int
        C++: virtual int ReadOutputType(const char *name, bool &parallel)
        This method can be used to find out the type of output expected
        without needing to read the whole file.
        """
        ret = self._wrap_call(self._vtk_obj.ReadOutputType, *args)
        return ret

    def setup_empty_output(self):
        """
        V.setup_empty_output()
        C++: void SetupEmptyOutput()
        Overridden method. Not Used. Delegated.
        """
        ret = self._vtk_obj.SetupEmptyOutput()
        return ret
        

    _updateable_traits_ = \
    (('file_name', 'GetFileName'), ('time_step_range',
    'GetTimeStepRange'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('time_step',
    'GetTimeStep'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLGenericDataObjectReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLGenericDataObjectReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'time_step', 'time_step_range']),
            title='Edit XMLGenericDataObjectReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLGenericDataObjectReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

