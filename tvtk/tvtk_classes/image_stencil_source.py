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

from tvtk.tvtk_classes.image_stencil_algorithm import ImageStencilAlgorithm


class ImageStencilSource(ImageStencilAlgorithm):
    """
    ImageStencilSource - generate an image stencil
    
    Superclass: ImageStencilAlgorithm
    
    ImageStencilSource is a superclass for filters that generate image
    stencils.  Given a clipping object such as a ImplicitFunction, it
    will set up a list of clipping extents for each x-row through the
    image data.  The extents for each x-row can be retrieved via the
    get_next_extent() method after the extent lists have been built with
    the build_extents() method.  For large images, using clipping extents
    is much more memory efficient (and slightly more time-efficient) than
    building a mask.  This class can be subclassed to allow clipping with
    objects other than ImplicitFunction.
    
    See Also:
    
    ImplicitFunction ImageStencil PolyDataToImageStencil
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencilSource, obj, update, **traits)
    
    output_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    output_whole_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputWholeExtent,
                        self.output_whole_extent)

    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    def _set_information_input(self, arg):
        old_val = self._get_information_input()
        self._wrap_call(self._vtk_obj.SetInformationInput,
                        deref_vtk(arg))
        self.trait_property_changed('information_input', old_val, arg)
    information_input = traits.Property(_get_information_input, _set_information_input, help=\
        """
        Set a ImageData that has the Spacing, Origin, and whole_extent
        that will be used for the stencil.  This input should be set to
        the image that you wish to apply the stencil to.  If you use this
        method, then any values set with the set_output_spacing,
        set_output_origin, and set_output_whole_extent methods will be
        ignored.
        """
    )

    output_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    def report_references(self, *args):
        """
        V.report_references(GarbageCollector)
        C++: virtual void ReportReferences(GarbageCollector *)
        Report object referenced by instances of this class.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReportReferences, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('output_whole_extent', 'GetOutputWholeExtent'), ('release_data_flag',
    'GetReleaseDataFlag'), ('output_spacing', 'GetOutputSpacing'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('output_origin',
    'GetOutputOrigin'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencilSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['output_origin', 'output_spacing',
            'output_whole_extent']),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

