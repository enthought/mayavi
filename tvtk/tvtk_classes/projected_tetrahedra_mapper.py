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


class ProjectedTetrahedraMapper(UnstructuredGridVolumeMapper):
    """
    ProjectedTetrahedraMapper - Unstructured grid volume renderer.
    
    Superclass: UnstructuredGridVolumeMapper
    
    ProjectedTetrahedraMapper is an implementation of the classic
    Projected Tetrahedra algorithm presented by Shirley and Tuchman in "A
    Polygonal Approximation to Direct Scalar Volume Rendering" in
    Computer Graphics, December 1990.
    
    Bugs:
    
    This mapper relies highly on the implementation of the open_gl
    pipeline. A typical hardware driver has lots of options and some
    settings can cause this mapper to produce artifacts.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProjectedTetrahedraMapper, obj, update, **traits)
    
    def _get_visibility_sort(self):
        return wrap_vtk(self._vtk_obj.GetVisibilitySort())
    def _set_visibility_sort(self, arg):
        old_val = self._get_visibility_sort()
        self._wrap_call(self._vtk_obj.SetVisibilitySort,
                        deref_vtk(arg))
        self.trait_property_changed('visibility_sort', old_val, arg)
    visibility_sort = traits.Property(_get_visibility_sort, _set_visibility_sort, help=\
        """
        
        """
    )

    def map_scalars_to_colors(self, *args):
        """
        V.map_scalars_to_colors(DataArray, VolumeProperty,
            DataArray)
        C++: static void MapScalarsToColors(DataArray *colors,
            VolumeProperty *property, DataArray *scalars)"""
        my_args = deref_array(args, [('vtkDataArray', 'vtkVolumeProperty', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.MapScalarsToColors, *my_args)
        return ret

    def transform_points(self, *args):
        """
        V.transform_points(Points, (float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float), (float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float), FloatArray)
        C++: static void TransformPoints(Points *inPoints,
            const float projection_mat[16], const float modelview_mat[16],
             FloatArray *outPoints)"""
        my_args = deref_array(args, [('vtkPoints', ('float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float'), ('float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float'), 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.TransformPoints, *my_args)
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
            return super(ProjectedTetrahedraMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProjectedTetrahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['blend_mode', 'scalar_mode'], []),
            title='Edit ProjectedTetrahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProjectedTetrahedraMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

