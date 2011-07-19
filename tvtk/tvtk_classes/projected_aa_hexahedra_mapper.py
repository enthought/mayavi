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

from tvtk.tvtk_classes.unstructured_grid_volume_mapper import UnstructuredGridVolumeMapper


class ProjectedAAHexahedraMapper(UnstructuredGridVolumeMapper):
    """
    ProjectedAAHexahedraMapper - volume mapper for axis-aligned
    hexahedra
    
    Superclass: UnstructuredGridVolumeMapper
    
    High quality volume renderer for axis-aligned hexahedra
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProjectedAAHexahedraMapper, obj, update, **traits)
    
    def _get_visibility_sort(self):
        return wrap_vtk(self._vtk_obj.GetVisibilitySort())
    def _set_visibility_sort(self, arg):
        old_val = self._get_visibility_sort()
        self._wrap_call(self._vtk_obj.SetVisibilitySort,
                        deref_vtk(arg))
        self.trait_property_changed('visibility_sort', old_val, arg)
    visibility_sort = traits.Property(_get_visibility_sort, _set_visibility_sort, help=\
        """
        Algorithm used to sort the cells according to viewpoint of the
        camera. Initial value is a CellCenterDepthSort object.
        """
    )

    def is_render_supported(self, *args):
        """
        V.is_render_supported(RenderWindow) -> bool
        C++: virtual bool IsRenderSupported(RenderWindow *w)
        Check if the required open_gl extensions are supported by the
        open_gl context attached to the render window `w'.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsRenderSupported, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('scalar_mode',
    'GetScalarMode'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('blend_mode', 'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'scalar_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProjectedAAHexahedraMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProjectedAAHexahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['blend_mode', 'scalar_mode'], []),
            title='Edit ProjectedAAHexahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProjectedAAHexahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

