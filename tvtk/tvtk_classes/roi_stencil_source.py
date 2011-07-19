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


class ROIStencilSource(ImageStencilSource):
    """
    ROIStencilSource - create simple mask shapes
    
    Superclass: ImageStencilSource
    
    ROIStencilSource will create an image stencil with a simple shape
    like a box, a sphere, or a cylinder.  Its output can be used with
    ImageStecil or other vtk classes that apply a stencil to an image.
    
    See Also:
    
    ImplicitFunctionToImageStencil LassooStencilSource
    
    Thanks:
    
    Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkROIStencilSource, obj, update, **traits)
    
    shape = traits.Trait('box',
    tvtk_base.TraitRevPrefixMap({'box': 0, 'cylinder_x': 2, 'cylinder_z': 4, 'cylinder_y': 3, 'ellipsoid': 1}), help=\
        """
        The shape of the region of interest.  Cylinders can be oriented
        along the X, Y, or Z axes.  The default shape is "Box".
        """
    )
    def _shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShape,
                        self.shape_)

    bounds = traits.Array(shape=(6,), value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    _updateable_traits_ = \
    (('output_whole_extent', 'GetOutputWholeExtent'), ('output_spacing',
    'GetOutputSpacing'), ('progress_text', 'GetProgressText'), ('bounds',
    'GetBounds'), ('output_origin', 'GetOutputOrigin'), ('debug',
    'GetDebug'), ('shape', 'GetShape'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'shape', 'bounds', 'output_origin',
    'output_spacing', 'output_whole_extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ROIStencilSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['shape'], ['bounds', 'output_origin',
            'output_spacing', 'output_whole_extent']),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

