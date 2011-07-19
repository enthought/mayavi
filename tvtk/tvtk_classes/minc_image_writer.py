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

from tvtk.tvtk_classes.image_writer import ImageWriter


class MINCImageWriter(ImageWriter):
    """
    MINCImageWriter - A writer for MINC files.
    
    Superclass: ImageWriter
    
    MINC is a net_cdf-based medical image file format that was developed
    at the Montreal Neurological Institute in 1992. The data is written
    slice-by-slice, and this writer is therefore suitable for streaming
    MINC data that is larger than the memory size through VTK.  This
    writer can also produce files with up to 4 dimensions, where the
    fourth dimension is provided by using add_input() to specify multiple
    input data sets.  If you want to set header information for the file,
    you must supply a MINCImageAttributes
    
    See Also:
    
    MINCImageReader MINCImageAttributes
    
    Thanks:
    
    Thanks to David Gobbi for writing this class and Atamai Inc. for
    contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMINCImageWriter, obj, update, **traits)
    
    strict_validation = tvtk_base.true_bool_trait(help=\
        """
        Set whether to validate that all variable attributes that have
        been set are ones that are listed in the MINC standard.
        """
    )
    def _strict_validation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStrictValidation,
                        self.strict_validation_)

    rescale_intercept = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the slope and intercept for rescaling the intensities.  The
        default values are zero, which indicates to the reader that no
        rescaling is to be performed.
        """
    )
    def _rescale_intercept_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRescaleIntercept,
                        self.rescale_intercept)

    def _get_image_attributes(self):
        return wrap_vtk(self._vtk_obj.GetImageAttributes())
    def _set_image_attributes(self, arg):
        old_val = self._get_image_attributes()
        self._wrap_call(self._vtk_obj.SetImageAttributes,
                        deref_vtk(arg))
        self.trait_property_changed('image_attributes', old_val, arg)
    image_attributes = traits.Property(_get_image_attributes, _set_image_attributes, help=\
        """
        Set the image attributes, which contain patient information and
        other useful metadata.
        """
    )

    rescale_slope = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the slope and intercept for rescaling the intensities.  The
        default values are zero, which indicates to the reader that no
        rescaling is to be performed.
        """
    )
    def _rescale_slope_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRescaleSlope,
                        self.rescale_slope)

    def _get_direction_cosines(self):
        return wrap_vtk(self._vtk_obj.GetDirectionCosines())
    def _set_direction_cosines(self, arg):
        old_val = self._get_direction_cosines()
        self._wrap_call(self._vtk_obj.SetDirectionCosines,
                        deref_vtk(arg))
        self.trait_property_changed('direction_cosines', old_val, arg)
    direction_cosines = traits.Property(_get_direction_cosines, _set_direction_cosines, help=\
        """
        Set a matrix that describes the orientation of the data.  The
        three columns of this matrix should give the unit-vector
        directions for the VTK x, y and z dimensions respectively. The
        writer will use this information to determine how to map the VTK
        dimensions to the canonical MINC dimensions, and if necessary,
        the writer will re-order one or more dimensions back-to-front to
        ensure that no MINC dimension ends up with a direction cosines
        vector whose dot product with the canonical unit vector for that
        dimension is negative.
        """
    )

    history_addition = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set a string value to append to the history of the file.  This
        string should describe, briefly, how the file was processed.
        """
    )
    def _history_addition_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHistoryAddition,
                        self.history_addition)

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
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'),
    ('rescale_intercept', 'GetRescaleIntercept'), ('rescale_slope',
    'GetRescaleSlope'), ('file_pattern', 'GetFilePattern'), ('debug',
    'GetDebug'), ('history_addition', 'GetHistoryAddition'),
    ('file_prefix', 'GetFilePrefix'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('strict_validation', 'GetStrictValidation'), ('file_dimensionality',
    'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'strict_validation', 'file_dimensionality',
    'file_name', 'file_pattern', 'file_prefix', 'history_addition',
    'progress_text', 'rescale_intercept', 'rescale_slope'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MINCImageWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MINCImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['strict_validation'], [], ['file_dimensionality',
            'file_name', 'file_pattern', 'file_prefix', 'history_addition',
            'rescale_intercept', 'rescale_slope']),
            title='Edit MINCImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MINCImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

