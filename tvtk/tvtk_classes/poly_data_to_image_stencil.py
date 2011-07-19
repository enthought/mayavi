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

from tvtk.tvtk_classes.image_stencil_source import ImageStencilSource


class PolyDataToImageStencil(ImageStencilSource):
    """
    PolyDataToImageStencil - use polydata to mask an image
    
    Superclass: ImageStencilSource
    
    The PolyDataToImageStencil class will convert polydata into an
    image stencil.  The polydata can either be a closed surface mesh or a
    series of polyline contours (one contour per slice).
    
    Caveats:
    
    If contours are provided, the contours must be aligned with the Z
    planes.  Other contour orientations are not supported.
    
    See Also:
    
    ImageStencil ImageAccumulate ImageBlend ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataToImageStencil, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Specify the implicit function to convert into a stencil.
        """
    )

    tolerance = traits.Trait(0.001, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The tolerance to apply in when determining whether a voxel is
        inside the stencil, given as a fraction of a voxel. Only used in
        X and Y, not in Z.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    _updateable_traits_ = \
    (('output_whole_extent', 'GetOutputWholeExtent'), ('output_spacing',
    'GetOutputSpacing'), ('progress_text', 'GetProgressText'),
    ('output_origin', 'GetOutputOrigin'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('tolerance', 'GetTolerance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataToImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['output_origin', 'output_spacing',
            'output_whole_extent', 'tolerance']),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

