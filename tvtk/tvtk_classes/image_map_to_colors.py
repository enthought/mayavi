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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageMapToColors(ThreadedImageAlgorithm):
    """
    ImageMapToColors - map the input image through a lookup table
    
    Superclass: ThreadedImageAlgorithm
    
    The ImageMapToColors filter will take an input image of any valid
    scalar type, and map the first component of the image through a
    lookup table.  The result is an image of type VTK_UNSIGNED_CHAR. If
    the lookup table is not set, or is set to NULL, then the input data
    will be passed through if it is already of type VTK_UNSIGNED_CHAR.
    
    See Also:
    
    LookupTable ScalarsToColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMapToColors, obj, update, **traits)
    
    pass_alpha_to_output = tvtk_base.false_bool_trait(help=\
        """
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
        """
    )
    def _pass_alpha_to_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassAlphaToOutput,
                        self.pass_alpha_to_output_)

    output_format = traits.Trait('rgba',
    tvtk_base.TraitRevPrefixMap({'luminance_alpha': 2, 'rgb': 3, 'luminance': 1, 'rgba': 4}), help=\
        """
        Set the output format, the default is RGBA.
        """
    )
    def _output_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputFormat,
                        self.output_format_)

    active_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the component to map for multi-component images (default: 0)
        """
    )
    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set the lookup table.
        """
    )

    _updateable_traits_ = \
    (('pass_alpha_to_output', 'GetPassAlphaToOutput'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_format', 'GetOutputFormat'), ('progress_text',
    'GetProgressText'), ('active_component', 'GetActiveComponent'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_alpha_to_output', 'release_data_flag', 'output_format',
    'active_component', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMapToColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_alpha_to_output'], ['output_format'],
            ['active_component', 'number_of_threads']),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

