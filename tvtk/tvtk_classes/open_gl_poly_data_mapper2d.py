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

from tvtk.tvtk_classes.poly_data_mapper2d import PolyDataMapper2D


class OpenGLPolyDataMapper2D(PolyDataMapper2D):
    """
    OpenGLPolyDataMapper2D - 2d poly_data support for open_gl
    
    Superclass: PolyDataMapper2D
    
    OpenGLPolyDataMapper2D provides 2d poly_data annotation support for
    vtk under open_gl.  Normally the user should use PolyDataMapper2D
    which in turn will use this class.
    
    See Also:
    
    PolyDataMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLPolyDataMapper2D, obj, update, **traits)
    
    _updateable_traits_ = \
    (('color_mode', 'GetColorMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('scalar_mode',
    'GetScalarMode'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('scalar_visibility',
    'GetScalarVisibility'), ('scalar_range', 'GetScalarRange'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_visibility',
    'use_lookup_table_scalar_range', 'color_mode', 'scalar_mode',
    'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLPolyDataMapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scalar_visibility', 'use_lookup_table_scalar_range'],
            ['color_mode', 'scalar_mode'], ['scalar_range']),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

