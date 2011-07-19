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


class VoxelContoursToSurfaceFilter(PolyDataAlgorithm):
    """
    VoxelContoursToSurfaceFilter - create surface from contours
    
    Superclass: PolyDataAlgorithm
    
    VoxelContoursToSurfaceFilter is a filter that takes contours and
    produces surfaces. There are some restrictions for the contours:
    
    - The contours are input as PolyData, with the contours being
      polys in the PolyData.
    - The contours lie on XY planes - each contour has a constant Z
    - The contours are ordered in the polys of the PolyData such that
      all contours on the first (lowest) XY plane are first, then
      continuing in order of increasing Z value.
    - The X, Y and Z coordinates are all integer values.
    - The desired sampling of the contour data is 1x1x1 - Aspect can be
      used to control the aspect ratio in the output polygonal dataset.
    
    This filter takes the contours and produces a structured points
    dataset of signed floating point number indicating distance from a
    contour. A contouring filter is then applied to generate 3d surfaces
    from a stack of 2d contour distance slices. This is done in a
    streaming fashion so as not to use to much memory.
    
    See Also:
    
    PolyDataAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVoxelContoursToSurfaceFilter, obj, update, **traits)
    
    memory_limit_in_bytes = traits.Int(10000000, enter_set=True, auto_set=False, help=\
        """
        Set / Get the memory limit in bytes for this filter. This is the
        limit of the size of the structured points data set that is
        created for intermediate processing. The data will be streamed
        through this volume in as many pieces as necessary.
        """
    )
    def _memory_limit_in_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMemoryLimitInBytes,
                        self.memory_limit_in_bytes)

    spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('spacing', 'GetSpacing'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('memory_limit_in_bytes', 'GetMemoryLimitInBytes'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'memory_limit_in_bytes', 'progress_text',
    'spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VoxelContoursToSurfaceFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VoxelContoursToSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['memory_limit_in_bytes', 'spacing']),
            title='Edit VoxelContoursToSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VoxelContoursToSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

