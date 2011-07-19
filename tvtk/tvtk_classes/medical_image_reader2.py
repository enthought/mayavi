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

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class MedicalImageReader2(ImageReader2):
    """
    MedicalImageReader2 - ImageReader2 with medical meta data.
    
    Superclass: ImageReader2
    
    MedicalImageReader2 is a parent class for medical image readers.
    It provides a place to store patient information that may be stored
    in the image header.
    
    See Also:
    
    ImageReader2 GESignaReader MedicalImageProperties
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMedicalImageReader2, obj, update, **traits)
    
    image_number = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _image_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageNumber,
                        self.image_number)

    series = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _series_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSeries,
                        self.series)

    study = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _study_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStudy,
                        self.study)

    patient_id = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _patient_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientID,
                        self.patient_id)

    patient_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _patient_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientName,
                        self.patient_name)

    date = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _date_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDate,
                        self.date)

    modality = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For backward compatibility, propagate calls to the
        medical_image_properties object.
        """
    )
    def _modality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModality,
                        self.modality)

    def _get_medical_image_properties(self):
        return wrap_vtk(self._vtk_obj.GetMedicalImageProperties())
    medical_image_properties = traits.Property(_get_medical_image_properties, help=\
        """
        Get the medical image properties object
        """
    )

    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('series', 'GetSeries'), ('data_byte_order', 'GetDataByteOrder'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('debug', 'GetDebug'), ('header_size', 'GetHeaderSize'),
    ('data_spacing', 'GetDataSpacing'), ('swap_bytes', 'GetSwapBytes'),
    ('date', 'GetDate'), ('patient_id', 'GetPatientID'), ('modality',
    'GetModality'), ('data_origin', 'GetDataOrigin'), ('file_lower_left',
    'GetFileLowerLeft'), ('file_name_slice_offset',
    'GetFileNameSliceOffset'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('data_extent', 'GetDataExtent'),
    ('study', 'GetStudy'), ('progress_text', 'GetProgressText'),
    ('patient_name', 'GetPatientName'), ('file_name_slice_spacing',
    'GetFileNameSliceSpacing'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('file_name',
    'GetFileName'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('image_number', 'GetImageNumber'),
    ('file_dimensionality', 'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'date', 'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'image_number', 'modality',
    'number_of_scalar_components', 'patient_id', 'patient_name',
    'progress_text', 'series', 'study'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MedicalImageReader2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MedicalImageReader2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'date',
            'file_dimensionality', 'file_name', 'file_name_slice_offset',
            'file_name_slice_spacing', 'file_pattern', 'file_prefix',
            'header_size', 'image_number', 'modality',
            'number_of_scalar_components', 'patient_id', 'patient_name', 'series',
            'study']),
            title='Edit MedicalImageReader2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MedicalImageReader2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

