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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageChangeInformation(ImageAlgorithm):
    """
    ImageChangeInformation - modify spacing, origin and extent.
    
    Superclass: ImageAlgorithm
    
    ImageChangeInformation  modify the spacing, origin, or extent of
    the data without changing the data itself.  The data is not resampled
    by this filter, only the information accompanying the data is
    modified.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageChangeInformation, obj, update, **traits)
    
    center_image = tvtk_base.false_bool_trait(help=\
        """
        Set the Origin of the output so that image coordinate (0,0,0)
        lies at the Center of the data set.  This will override
        set_output_origin.  This is often a useful operation to apply
        before using ImageReslice to apply a transformation to an
        image.
        """
    )
    def _center_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenterImage,
                        self.center_image_)

    output_extent_start = traits.Array(shape=(3,), value=(2147483647, 2147483647, 2147483647), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_extent_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputExtentStart,
                        self.output_extent_start)

    origin_scale = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginScale,
                        self.origin_scale)

    spacing_scale = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _spacing_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacingScale,
                        self.spacing_scale)

    origin_translation = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginTranslation,
                        self.origin_translation)

    extent_translation = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _extent_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtentTranslation,
                        self.extent_translation)

    output_origin = traits.Array(shape=(3,), value=(1.0000000000000001e+299, 1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    def _set_information_input(self, arg):
        old_val = self._get_information_input()
        self._wrap_call(self._vtk_obj.SetInformationInput,
                        deref_vtk(arg))
        self.trait_property_changed('information_input', old_val, arg)
    information_input = traits.Property(_get_information_input, _set_information_input, help=\
        """
        Copy the information from another data set.  By default, the
        information is copied from the input.
        """
    )

    output_spacing = traits.Array(shape=(3,), value=(1.0000000000000001e+299, 1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    _updateable_traits_ = \
    (('origin_scale', 'GetOriginScale'), ('output_extent_start',
    'GetOutputExtentStart'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_spacing', 'GetOutputSpacing'),
    ('origin_translation', 'GetOriginTranslation'), ('progress_text',
    'GetProgressText'), ('spacing_scale', 'GetSpacingScale'),
    ('output_origin', 'GetOutputOrigin'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('center_image',
    'GetCenterImage'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('extent_translation', 'GetExtentTranslation'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'center_image', 'debug', 'global_warning_display',
    'release_data_flag', 'extent_translation', 'origin_scale',
    'origin_translation', 'output_extent_start', 'output_origin',
    'output_spacing', 'progress_text', 'spacing_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageChangeInformation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['center_image'], [], ['extent_translation',
            'origin_scale', 'origin_translation', 'output_extent_start',
            'output_origin', 'output_spacing', 'spacing_scale']),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

