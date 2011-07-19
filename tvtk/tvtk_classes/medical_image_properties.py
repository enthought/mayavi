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


class MedicalImageProperties(Object):
    """
    MedicalImageProperties - some medical image properties.
    
    Superclass: Object
    
    MedicalImageProperties is a helper class that can be used by
    medical image readers and applications to encapsulate medical
    image/acquisition properties. Later on, this should probably be
    extended to add any user-defined property.
    
    See Also:
    
    MedicalImageReader2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMedicalImageProperties, obj, update, **traits)
    
    image_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Image Time Format: hhmmss.frac (any trailing component(s) can be
        ommited) For ex: DICOM (0008,0033) = 162552.0705 or 230012, or
        0012
        """
    )
    def _image_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageTime,
                        self.image_time)

    study_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Study Time Format: hhmmss.frac (any trailing component(s) can be
        ommited) For ex: DICOM (0008,0030) = 162552.0705 or 230012, or
        0012
        """
    )
    def _study_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStudyTime,
                        self.study_time)

    patient_sex = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Patient sex For ex: DICOM (0010,0040) = M
        """
    )
    def _patient_sex_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientSex,
                        self.patient_sex)

    study_id = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Study ID For ex: DICOM (0020,0010) = 37481
        """
    )
    def _study_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStudyID,
                        self.study_id)

    repetition_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Repetition Time The period of time in msec between the beginning
        of a pulse sequence and the beginning of the succeeding
        (essentially identical) pulse sequence. For ex: DICOM (0018,0080)
        = 2040
        """
    )
    def _repetition_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepetitionTime,
                        self.repetition_time)

    def get_orientation_type(self, *args):
        """
        V.get_orientation_type(int) -> int
        C++: int GetOrientationType(int volumeidx)"""
        ret = self._wrap_call(self._vtk_obj.GetOrientationType, *args)
        return ret

    def set_orientation_type(self, *args):
        """
        V.set_orientation_type(int, int)
        C++: void SetOrientationType(int volumeidx, int orientation)"""
        ret = self._wrap_call(self._vtk_obj.SetOrientationType, *args)
        return ret

    image_date = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Image Date aka Content Date Format: yyyymmdd For ex: DICOM
        (0008,0023) = 20030617
        """
    )
    def _image_date_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageDate,
                        self.image_date)

    image_number = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Image number For ex: DICOM (0020,0013) = 1
        """
    )
    def _image_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageNumber,
                        self.image_number)

    series_number = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Series number For ex: DICOM (0020,0011) = 902
        """
    )
    def _series_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSeriesNumber,
                        self.series_number)

    slice_thickness = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Slice Thickness (Nominal reconstructed slice thickness, in mm)
        For ex: DICOM (0018,0050) = 0.273438
        """
    )
    def _slice_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceThickness,
                        self.slice_thickness)

    institution_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Institution Name For ex: DICOM (0008,0080) = foo_city Medical
        Center
        """
    )
    def _institution_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInstitutionName,
                        self.institution_name)

    gantry_tilt = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Gantry/Detector tilt (Nominal angle of tilt in degrees of the
        scanning gantry.) For ex: DICOM (0018,1120) = 15
        """
    )
    def _gantry_tilt_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGantryTilt,
                        self.gantry_tilt)

    patient_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Patient name For ex: DICOM (0010,0010) = DOE,JOHN
        """
    )
    def _patient_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientName,
                        self.patient_name)

    echo_train_length = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Echo Train Length (Number of lines in k-space acquired per
        excitation per image) For ex: DICOM (0018,0091) = 35
        """
    )
    def _echo_train_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEchoTrainLength,
                        self.echo_train_length)

    patient_age = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Patient age Format: nnn_d, nn_w, nnn_m or nnn_y (eventually nn_d, nn_w,
        nn_y)
                with D (day), M (month), W (week), Y (year) For ex: DICOM
        (0010,1010) = 031y
        """
    )
    def _patient_age_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientAge,
                        self.patient_age)

    nth_window_level_preset_comment = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
    )
    def _nth_window_level_preset_comment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNthWindowLevelPresetComment,
                        self.nth_window_level_preset_comment)

    manufacturer = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Manufacturer For ex: DICOM (0008,0070) = Siemens
        """
    )
    def _manufacturer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManufacturer,
                        self.manufacturer)

    exposure_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Exposure time (time of x-ray exposure in msec) For ex: DICOM
        (0018,1150) = 5
        """
    )
    def _exposure_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExposureTime,
                        self.exposure_time)

    study_date = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Study Date Format: yyyymmdd For ex: DICOM (0008,0020) = 20030617
        """
    )
    def _study_date_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStudyDate,
                        self.study_date)

    station_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Station Name For ex: DICOM (0008,1010) = LSPD_OC8
        """
    )
    def _station_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStationName,
                        self.station_name)

    series_description = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Series Description User provided description of the Series For
        ex: DICOM (0008,103e) = SCOUT
        """
    )
    def _series_description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSeriesDescription,
                        self.series_description)

    acquisition_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Acquisition time Format: hhmmss.frac (any trailing component(s)
        can be ommited) For ex: DICOM (0008,0032) = 162552.0705 or
        230012, or 0012
        """
    )
    def _acquisition_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAcquisitionTime,
                        self.acquisition_time)

    x_ray_tube_current = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        X-ray tube current (in m_a) For ex: DICOM (0018,1151) = 400
        """
    )
    def _x_ray_tube_current_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXRayTubeCurrent,
                        self.x_ray_tube_current)

    direction_cosine = traits.Array(shape=(6,), value=(1.0, 0.0, 0.0, 0.0, 1.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _direction_cosine_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirectionCosine,
                        self.direction_cosine)

    echo_time = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Echo Time (Time in ms between the middle of the excitation pulse
        and the peak of the echo produced) For ex: DICOM (0018,0081) =
        105
        """
    )
    def _echo_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEchoTime,
                        self.echo_time)

    acquisition_date = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Acquisition Date Format: yyyymmdd For ex: DICOM (0008,0022) =
        20030617
        """
    )
    def _acquisition_date_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAcquisitionDate,
                        self.acquisition_date)

    study_description = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Study description For ex: DICOM (0008,1030) = BRAIN/C-SP/FACIAL
        """
    )
    def _study_description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStudyDescription,
                        self.study_description)

    patient_id = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Patient ID For ex: DICOM (0010,0020) = 1933197
        """
    )
    def _patient_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientID,
                        self.patient_id)

    convolution_kernel = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Convolution Kernel (or algorithm used to reconstruct the data)
        For ex: DICOM (0018,1210) = Bone
        """
    )
    def _convolution_kernel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvolutionKernel,
                        self.convolution_kernel)

    patient_birth_date = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Patient birth date Format: yyyymmdd For ex: DICOM (0010,0030) =
        19680427
        """
    )
    def _patient_birth_date_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPatientBirthDate,
                        self.patient_birth_date)

    kvp = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Peak kilo voltage output of the (x-ray) generator used For ex:
        DICOM (0018,0060) = 120
        """
    )
    def _kvp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKVP,
                        self.kvp)

    manufacturer_model_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Manufacturer's Model Name For ex: DICOM (0008,1090) = light_speed
        QX/i
        """
    )
    def _manufacturer_model_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManufacturerModelName,
                        self.manufacturer_model_name)

    exposure = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Exposure (The exposure expressed in m_as, for example calculated
        from Exposure Time and X-ray Tube Current) For ex: DICOM
        (0018,1152) = 114
        """
    )
    def _exposure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExposure,
                        self.exposure)

    instance_uid_from_slice_id = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Mapping from a sliceidx within a volumeidx into a DICOM Instance
        UID Some DICOM reader can populate this structure so that later
        on from a slice index in a ImageData volume we can backtrack
        and find out which 2d slice it was coming from
        """
    )
    def _instance_uid_from_slice_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInstanceUIDFromSliceID,
                        self.instance_uid_from_slice_id)

    modality = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Modality For ex: DICOM (0008,0060)= CT
        """
    )
    def _modality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModality,
                        self.modality)

    def _get_acquisition_date_day(self):
        return self._vtk_obj.GetAcquisitionDateDay()
    acquisition_date_day = traits.Property(_get_acquisition_date_day, help=\
        """
        
        """
    )

    def _get_acquisition_date_month(self):
        return self._vtk_obj.GetAcquisitionDateMonth()
    acquisition_date_month = traits.Property(_get_acquisition_date_month, help=\
        """
        
        """
    )

    def _get_acquisition_date_year(self):
        return self._vtk_obj.GetAcquisitionDateYear()
    acquisition_date_year = traits.Property(_get_acquisition_date_year, help=\
        """
        
        """
    )

    def get_age_as_fields(self, *args):
        """
        V.get_age_as_fields(string, int, int, int, int) -> int
        C++: static int GetAgeAsFields(const char *age, int &year,
            int &month, int &week, int &day)
        Take as input a string in VR=AS (DICOM PS3.5) and extract either
        different fields namely: year month week day Return 0 on error, 1
        on success One can test fields if they are different from -1 upon
        success
        """
        ret = self._wrap_call(self._vtk_obj.GetAgeAsFields, *args)
        return ret

    def get_date_as_fields(self, *args):
        """
        V.get_date_as_fields(string, int, int, int) -> int
        C++: static int GetDateAsFields(const char *date, int &year,
            int &month, int &day)
        Take as input a string in ISO 8601 date (YYYY/MM/DD) and extract
        the different fields namely: year month day Return 0 on error, 1
        on success
        """
        ret = self._wrap_call(self._vtk_obj.GetDateAsFields, *args)
        return ret

    def get_date_as_locale(self, *args):
        """
        V.get_date_as_locale(string, string) -> int
        C++: static int GetDateAsLocale(const char *date, char *locale)
        Take as input a string in ISO 8601 date (YYYY/MM/DD) and
        construct a locale date based on the different fields (see
        get_date_as_fields to extract different fields) Return 0 on error, 1
        on success
        """
        ret = self._wrap_call(self._vtk_obj.GetDateAsLocale, *args)
        return ret

    def _get_gantry_tilt_as_double(self):
        return self._vtk_obj.GetGantryTiltAsDouble()
    gantry_tilt_as_double = traits.Property(_get_gantry_tilt_as_double, help=\
        """
        Gantry/Detector tilt (Nominal angle of tilt in degrees of the
        scanning gantry.) For ex: DICOM (0018,1120) = 15
        """
    )

    def _get_image_date_day(self):
        return self._vtk_obj.GetImageDateDay()
    image_date_day = traits.Property(_get_image_date_day, help=\
        """
        
        """
    )

    def _get_image_date_month(self):
        return self._vtk_obj.GetImageDateMonth()
    image_date_month = traits.Property(_get_image_date_month, help=\
        """
        
        """
    )

    def _get_image_date_year(self):
        return self._vtk_obj.GetImageDateYear()
    image_date_year = traits.Property(_get_image_date_year, help=\
        """
        
        """
    )

    def get_nth_window_level_preset(self, *args):
        """
        V.get_nth_window_level_preset(int) -> (float, float)
        C++: virtual double *GetNthWindowLevelPreset(int idx)
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._wrap_call(self._vtk_obj.GetNthWindowLevelPreset, *args)
        return ret

    def _get_number_of_user_defined_values(self):
        return self._vtk_obj.GetNumberOfUserDefinedValues()
    number_of_user_defined_values = traits.Property(_get_number_of_user_defined_values, help=\
        """
        
        """
    )

    def _get_number_of_window_level_presets(self):
        return self._vtk_obj.GetNumberOfWindowLevelPresets()
    number_of_window_level_presets = traits.Property(_get_number_of_window_level_presets, help=\
        """
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
    )

    def _get_patient_age_day(self):
        return self._vtk_obj.GetPatientAgeDay()
    patient_age_day = traits.Property(_get_patient_age_day, help=\
        """
        
        """
    )

    def _get_patient_age_month(self):
        return self._vtk_obj.GetPatientAgeMonth()
    patient_age_month = traits.Property(_get_patient_age_month, help=\
        """
        
        """
    )

    def _get_patient_age_week(self):
        return self._vtk_obj.GetPatientAgeWeek()
    patient_age_week = traits.Property(_get_patient_age_week, help=\
        """
        
        """
    )

    def _get_patient_age_year(self):
        return self._vtk_obj.GetPatientAgeYear()
    patient_age_year = traits.Property(_get_patient_age_year, help=\
        """
        
        """
    )

    def _get_patient_birth_date_day(self):
        return self._vtk_obj.GetPatientBirthDateDay()
    patient_birth_date_day = traits.Property(_get_patient_birth_date_day, help=\
        """
        
        """
    )

    def _get_patient_birth_date_month(self):
        return self._vtk_obj.GetPatientBirthDateMonth()
    patient_birth_date_month = traits.Property(_get_patient_birth_date_month, help=\
        """
        
        """
    )

    def _get_patient_birth_date_year(self):
        return self._vtk_obj.GetPatientBirthDateYear()
    patient_birth_date_year = traits.Property(_get_patient_birth_date_year, help=\
        """
        
        """
    )

    def get_slice_id_from_instance_uid(self, *args):
        """
        V.get_slice_id_from_instance_uid(int, string) -> int
        C++: int GetSliceIDFromInstanceUID(int &volumeidx,
            const char *uid)
        Provides the inverse mapping. Returns -1 if a slice for this uid
        is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetSliceIDFromInstanceUID, *args)
        return ret

    def _get_slice_thickness_as_double(self):
        return self._vtk_obj.GetSliceThicknessAsDouble()
    slice_thickness_as_double = traits.Property(_get_slice_thickness_as_double, help=\
        """
        Slice Thickness (Nominal reconstructed slice thickness, in mm)
        For ex: DICOM (0018,0050) = 0.273438
        """
    )

    def get_string_from_orientation_type(self, *args):
        """
        V.get_string_from_orientation_type(int) -> string
        C++: static const char *GetStringFromOrientationType(
            unsigned int type)"""
        ret = self._wrap_call(self._vtk_obj.GetStringFromOrientationType, *args)
        return ret

    def get_time_as_fields(self, *args):
        """
        V.get_time_as_fields(string, int, int, int) -> int
        C++: static int GetTimeAsFields(const char *time, int &hour,
            int &minute, int &second)
        Take as input a string in VR:TM format (HHMMSS) and extract the
        different fields namely: hour, minute and second Return 0 on
        error, 1 on success
        """
        ret = self._wrap_call(self._vtk_obj.GetTimeAsFields, *args)
        return ret

    def get_user_defined_name_by_index(self, *args):
        """
        V.get_user_defined_name_by_index(int) -> string
        C++: virtual const char *GetUserDefinedNameByIndex(
            unsigned int idx)"""
        ret = self._wrap_call(self._vtk_obj.GetUserDefinedNameByIndex, *args)
        return ret

    def get_user_defined_value(self, *args):
        """
        V.get_user_defined_value(string) -> string
        C++: virtual const char *GetUserDefinedValue(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetUserDefinedValue, *args)
        return ret

    def get_user_defined_value_by_index(self, *args):
        """
        V.get_user_defined_value_by_index(int) -> string
        C++: virtual const char *GetUserDefinedValueByIndex(
            unsigned int idx)"""
        ret = self._wrap_call(self._vtk_obj.GetUserDefinedValueByIndex, *args)
        return ret

    def get_window_level_preset_index(self, *args):
        """
        V.get_window_level_preset_index(float, float) -> int
        C++: virtual int GetWindowLevelPresetIndex(double w, double l)
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._wrap_call(self._vtk_obj.GetWindowLevelPresetIndex, *args)
        return ret

    def add_user_defined_value(self, *args):
        """
        V.add_user_defined_value(string, string)
        C++: virtual void AddUserDefinedValue(const char *name,
            const char *value)"""
        ret = self._wrap_call(self._vtk_obj.AddUserDefinedValue, *args)
        return ret

    def add_window_level_preset(self, *args):
        """
        V.add_window_level_preset(float, float) -> int
        C++: virtual int AddWindowLevelPreset(double w, double l)
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._wrap_call(self._vtk_obj.AddWindowLevelPreset, *args)
        return ret

    def clear(self):
        """
        V.clear()
        C++: virtual void Clear()
        Convenience method to reset all fields to an emptry string/value
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(MedicalImageProperties)
        C++: virtual void DeepCopy(MedicalImageProperties *p)
        Copy the contents of p to this instance.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def has_window_level_preset(self, *args):
        """
        V.has_window_level_preset(float, float) -> int
        C++: virtual int HasWindowLevelPreset(double w, double l)
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._wrap_call(self._vtk_obj.HasWindowLevelPreset, *args)
        return ret

    def remove_all_user_defined_values(self):
        """
        V.remove_all_user_defined_values()
        C++: virtual void RemoveAllUserDefinedValues()"""
        ret = self._vtk_obj.RemoveAllUserDefinedValues()
        return ret
        

    def remove_all_window_level_presets(self):
        """
        V.remove_all_window_level_presets()
        C++: virtual void RemoveAllWindowLevelPresets()
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._vtk_obj.RemoveAllWindowLevelPresets()
        return ret
        

    def remove_window_level_preset(self, *args):
        """
        V.remove_window_level_preset(float, float)
        C++: virtual void RemoveWindowLevelPreset(double w, double l)
        Add/Remove/Query the window/level presets that may have been
        associated to a medical image. Window is also known as 'width',
        level is also known as 'center'. The same window/level pair can
        not be added twice. As a convenience, a comment (aka Explanation)
        can be associated to a preset. For ex:
                 DICOM Window Center (0028,1050) = 00045\000470
                 DICOM Window Width  (0028,1051) = 0106\03412
                 DICOM Window Center Width Explanation (0028,1055) = WINDOW1\WINDOW2
         
        """
        ret = self._wrap_call(self._vtk_obj.RemoveWindowLevelPreset, *args)
        return ret

    _updateable_traits_ = \
    (('exposure_time', 'GetExposureTime'), ('echo_time', 'GetEchoTime'),
    ('gantry_tilt', 'GetGantryTilt'), ('acquisition_date',
    'GetAcquisitionDate'), ('patient_sex', 'GetPatientSex'),
    ('patient_name', 'GetPatientName'), ('image_date', 'GetImageDate'),
    ('modality', 'GetModality'), ('patient_birth_date',
    'GetPatientBirthDate'), ('acquisition_time', 'GetAcquisitionTime'),
    ('series_description', 'GetSeriesDescription'), ('image_time',
    'GetImageTime'), ('repetition_time', 'GetRepetitionTime'),
    ('slice_thickness', 'GetSliceThickness'), ('manufacturer',
    'GetManufacturer'), ('study_date', 'GetStudyDate'), ('patient_age',
    'GetPatientAge'), ('nth_window_level_preset_comment',
    'GetNthWindowLevelPresetComment'), ('study_description',
    'GetStudyDescription'), ('study_time', 'GetStudyTime'), ('debug',
    'GetDebug'), ('x_ray_tube_current', 'GetXRayTubeCurrent'),
    ('direction_cosine', 'GetDirectionCosine'), ('kvp', 'GetKVP'),
    ('station_name', 'GetStationName'), ('exposure', 'GetExposure'),
    ('convolution_kernel', 'GetConvolutionKernel'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('instance_uid_from_slice_id', 'GetInstanceUIDFromSliceID'),
    ('institution_name', 'GetInstitutionName'), ('patient_id',
    'GetPatientID'), ('study_id', 'GetStudyID'), ('image_number',
    'GetImageNumber'), ('manufacturer_model_name',
    'GetManufacturerModelName'), ('reference_count', 'GetReferenceCount'),
    ('series_number', 'GetSeriesNumber'), ('echo_train_length',
    'GetEchoTrainLength'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'acquisition_date',
    'acquisition_time', 'convolution_kernel', 'direction_cosine',
    'echo_time', 'echo_train_length', 'exposure', 'exposure_time',
    'gantry_tilt', 'image_date', 'image_number', 'image_time',
    'instance_uid_from_slice_id', 'institution_name', 'kvp',
    'manufacturer', 'manufacturer_model_name', 'modality',
    'nth_window_level_preset_comment', 'patient_age',
    'patient_birth_date', 'patient_id', 'patient_name', 'patient_sex',
    'repetition_time', 'series_description', 'series_number',
    'slice_thickness', 'station_name', 'study_date', 'study_description',
    'study_id', 'study_time', 'x_ray_tube_current'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MedicalImageProperties, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MedicalImageProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['acquisition_date', 'acquisition_time',
            'convolution_kernel', 'direction_cosine', 'echo_time',
            'echo_train_length', 'exposure', 'exposure_time', 'gantry_tilt',
            'image_date', 'image_number', 'image_time',
            'instance_uid_from_slice_id', 'institution_name', 'kvp',
            'manufacturer', 'manufacturer_model_name', 'modality',
            'nth_window_level_preset_comment', 'patient_age',
            'patient_birth_date', 'patient_id', 'patient_name', 'patient_sex',
            'repetition_time', 'series_description', 'series_number',
            'slice_thickness', 'station_name', 'study_date', 'study_description',
            'study_id', 'study_time', 'x_ray_tube_current']),
            title='Edit MedicalImageProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MedicalImageProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

