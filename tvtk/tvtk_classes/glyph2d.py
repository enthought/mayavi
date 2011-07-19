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

from tvtk.tvtk_classes.glyph3d import Glyph3D


class Glyph2D(Glyph3D):
    """
    Glyph2D - copy oriented and scaled glyph geometry to every input
    point (_2d specialization)
    
    Superclass: Glyph3D
    
    This subclass of Glyph3D is a specialization to 2d.
    Transformations (i.e., translation, scaling, and rotation) are
    constrained to the plane. For example, rotations due to a vector are
    computed from the x-y coordinates of the vector only, and are assumed
    to occur around the z-axis. (See Glyph3D for documentation on the
    interface to this class.)
    
    See Also:
    
    TensorGlyph Glyph3D ProgrammableGlyphFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyph2D, obj, update, **traits)
    
    _updateable_traits_ = \
    (('color_mode', 'GetColorMode'), ('fill_cell_data',
    'GetFillCellData'), ('scale_factor', 'GetScaleFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_point_ids', 'GetGeneratePointIds'), ('scale_mode',
    'GetScaleMode'), ('progress_text', 'GetProgressText'),
    ('point_ids_name', 'GetPointIdsName'), ('scaling', 'GetScaling'),
    ('debug', 'GetDebug'), ('range', 'GetRange'), ('abort_execute',
    'GetAbortExecute'), ('index_mode', 'GetIndexMode'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('vector_mode',
    'GetVectorMode'), ('clamping', 'GetClamping'), ('orient',
    'GetOrient'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug', 'fill_cell_data',
    'generate_point_ids', 'global_warning_display', 'orient',
    'release_data_flag', 'scaling', 'color_mode', 'index_mode',
    'scale_mode', 'vector_mode', 'point_ids_name', 'progress_text',
    'range', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Glyph2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamping', 'fill_cell_data', 'generate_point_ids',
            'orient', 'scaling'], ['color_mode', 'index_mode', 'scale_mode',
            'vector_mode'], ['point_ids_name', 'range', 'scale_factor']),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

