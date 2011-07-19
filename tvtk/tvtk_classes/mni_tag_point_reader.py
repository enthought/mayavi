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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class MNITagPointReader(PolyDataAlgorithm):
    """
    MNITagPointReader - A reader for MNI tag files.
    
    Superclass: PolyDataAlgorithm
    
    The MNI .tag file format is used to store labeled points, it can
    store either one or two point sets.  All point sets must have the
    same number of points and they will share the same labels.  This file
    format was developed at the mc_connell Brain Imaging Centre at the
    Montreal Neurological Institute and is used by their software. The
    labels are stored as a StringArray in the point_data of the output
    dataset, which is a PolyData.
    
    See Also:
    
    MINCImageReader MNIObjectReader MNITransformReader
    
    Thanks:
    
    Thanks to David Gobbi for contributing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMNITagPointReader, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_comments(self):
        return self._vtk_obj.GetComments()
    comments = traits.Property(_get_comments, help=\
        """
        Get any comments that are included in the file.
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

    def _get_label_text(self):
        return wrap_vtk(self._vtk_obj.GetLabelText())
    label_text = traits.Property(_get_label_text, help=\
        """
        Get the labels.  These same labels are provided in the output
        point sets, as the point_data data array named "_label_text". This
        will return NULL if there were no labels in the file.
        """
    )

    def _get_number_of_volumes(self):
        return self._vtk_obj.GetNumberOfVolumes()
    number_of_volumes = traits.Property(_get_number_of_volumes, help=\
        """
        Get the number of volumes specified by the file, which will be
        equal to one or two.  There will be an output point set for each
        volume, so really, this parameter just tells you the number of
        outputs to expect from this reader.
        """
    )

    def _get_patient_ids(self):
        return wrap_vtk(self._vtk_obj.GetPatientIds())
    patient_ids = traits.Property(_get_patient_ids, help=\
        """
        Get the patient ids.  These are also provided in the output point
        sets, as the point_data data array named "_patient_ids". This will
        return NULL if there were no ids in the file.
        """
    )

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    points = traits.Property(_get_points, help=\
        """
        Get the points.  These are also provided in the first and second
        output ports of the reader.  This method will return NULL if
        there is no data.
        """
    )

    def _get_structure_ids(self):
        return wrap_vtk(self._vtk_obj.GetStructureIds())
    structure_ids = traits.Property(_get_structure_ids, help=\
        """
        Get the structure ids.  These are also provided in the output
        point sets, as the point_data data array named "_structure_ids".
        This will return NULL if there were no ids in the file.
        """
    )

    def _get_weights(self):
        return wrap_vtk(self._vtk_obj.GetWeights())
    weights = traits.Property(_get_weights, help=\
        """
        Get the weights.  These are also provided in the output point
        sets, as the point_data data array named "Weights". This will
        return NULL if there were no weights in the file.
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: virtual int CanReadFile(const char *name)
        Test whether the specified file can be read.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
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
            return super(MNITagPointReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MNITagPointReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name']),
            title='Edit MNITagPointReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MNITagPointReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

