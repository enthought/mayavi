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

from tvtk.tvtk_classes.data_set_writer import DataSetWriter


class MNITagPointWriter(DataSetWriter):
    """
    MNITagPointWriter - A writer for MNI tag point files.
    
    Superclass: DataSetWriter
    
    The MNI .tag file format is used to store tag points, for use in
    either registration or labelling of data volumes.  This file format
    was developed at the mc_connell Brain Imaging Centre at the Montreal
    Neurological Institute and is used by their software. Tag points can
    be stored for either one volume or two volumes, and this filter can
    take one or two inputs.  Alternatively, the points to be written can
    be specified by calling set_points().
    
    See Also:
    
    MINCImageReader MNIObjectReader MNITransformReader
    
    Thanks:
    
    Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMNITagPointWriter, obj, update, **traits)
    
    def _get_label_text(self):
        return wrap_vtk(self._vtk_obj.GetLabelText())
    def _set_label_text(self, arg):
        old_val = self._get_label_text()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetLabelText,
                        my_arg[0])
        self.trait_property_changed('label_text', old_val, arg)
    label_text = traits.Property(_get_label_text, _set_label_text, help=\
        """
        Set the labels (unless the input point_data has an array called
        label_text). Labels are optional.
        """
    )

    comments = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set comments to be added to the file.
        """
    )
    def _comments_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComments,
                        self.comments)

    def get_points(self, *args):
        """
        V.get_points(int) -> Points
        C++: virtual Points *GetPoints(int port)
        V.get_points() -> Points
        C++: virtual Points *GetPoints()
        Set the points (unless you set them as inputs).
        """
        ret = self._wrap_call(self._vtk_obj.GetPoints, *args)
        return wrap_vtk(ret)

    def set_points(self, *args):
        """
        V.set_points(int, Points)
        C++: virtual void SetPoints(int port, Points *points)
        V.set_points(Points)
        C++: virtual void SetPoints(Points *points)
        Set the points (unless you set them as inputs).
        """
        my_args = deref_array(args, [('int', 'vtkPoints'), ['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.SetPoints, *my_args)
        return ret

    def _get_weights(self):
        return wrap_vtk(self._vtk_obj.GetWeights())
    def _set_weights(self, arg):
        old_val = self._get_weights()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetWeights,
                        my_arg[0])
        self.trait_property_changed('weights', old_val, arg)
    weights = traits.Property(_get_weights, _set_weights, help=\
        """
        Set the weights (unless the input point_data has an array called
        Weights).  Weights are optional.
        """
    )

    def _get_patient_ids(self):
        return wrap_vtk(self._vtk_obj.GetPatientIds())
    def _set_patient_ids(self, arg):
        old_val = self._get_patient_ids()
        my_arg = deref_array([arg], [['vtkIntArray']])
        self._wrap_call(self._vtk_obj.SetPatientIds,
                        my_arg[0])
        self.trait_property_changed('patient_ids', old_val, arg)
    patient_ids = traits.Property(_get_patient_ids, _set_patient_ids, help=\
        """
        Set the structure ids (unless the input point_data has an array
        called patient_ids).  These are optional.
        """
    )

    def _get_structure_ids(self):
        return wrap_vtk(self._vtk_obj.GetStructureIds())
    def _set_structure_ids(self, arg):
        old_val = self._get_structure_ids()
        my_arg = deref_array([arg], [['vtkIntArray']])
        self._wrap_call(self._vtk_obj.SetStructureIds,
                        my_arg[0])
        self.trait_property_changed('structure_ids', old_val, arg)
    structure_ids = traits.Property(_get_structure_ids, _set_structure_ids, help=\
        """
        Set the structure ids (unless the input point_data has an array
        called structure_ids).  These are optional.
        """
    )

    def _get_descriptive_name(self):
        return self._vtk_obj.GetDescriptiveName()
    descriptive_name = traits.Property(_get_descriptive_name, help=\
        """
        Get the name of this file format.
        """
    )

    def _get_file_extensions(self):
        return self._vtk_obj.GetFileExtensions()
    file_extensions = traits.Property(_get_file_extensions, help=\
        """
        Get the entension for this file format.
        """
    )

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('global_ids_name',
    'GetGlobalIdsName'), ('tensors_name', 'GetTensorsName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lookup_table_name', 'GetLookupTableName'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('scalars_name',
    'GetScalarsName'), ('progress_text', 'GetProgressText'), ('comments',
    'GetComments'), ('header', 'GetHeader'), ('abort_execute',
    'GetAbortExecute'), ('t_coords_name', 'GetTCoordsName'),
    ('normals_name', 'GetNormalsName'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('field_data_name', 'GetFieldDataName'),
    ('pedigree_ids_name', 'GetPedigreeIdsName'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_type',
    'comments', 'field_data_name', 'file_name', 'global_ids_name',
    'header', 'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalars_name', 't_coords_name', 'tensors_name',
    'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MNITagPointWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MNITagPointWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['file_type'], ['comments',
            'field_data_name', 'file_name', 'global_ids_name', 'header',
            'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'scalars_name', 't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit MNITagPointWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MNITagPointWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

