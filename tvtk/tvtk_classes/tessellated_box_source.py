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


class TessellatedBoxSource(PolyDataAlgorithm):
    """
    TessellatedBoxSource - Create a polygonal representation of a box
    
    Superclass: PolyDataAlgorithm
    
    TessellatedBoxSource creates a axis-aligned box defined by its
    bounds and a level of subdivision. Connectivity is strong: points of
    the vertices and inside the edges are shared between faces. In other
    words, faces are connected. Each face looks like a grid of quads,
    each quad is composed of 2 triangles. Given a level of subdivision `l', each edge has
    `l'+2 points, `l' of them are internal edge points, the 2 other ones
    are the vertices. Each face has a total of (`l'+2)*(`l'+2) points, 4
    of them are vertices, 4*`l' are internal edge points, it remains
    `l'^2 internal face points.
    
    This source only generate geometry, no data_arrays like normals or
    texture coordinates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTessellatedBoxSource, obj, update, **traits)
    
    duplicate_shared_points = tvtk_base.false_bool_trait(help=\
        """
        Flag to tell the source to duplicate points shared between faces
        (vertices of the box and internal edge points). Initial value is
        false. Implementation note: duplicating points is an easier
        method to implement than a minimal number of points.
        """
    )
    def _duplicate_shared_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDuplicateSharedPoints,
                        self.duplicate_shared_points_)

    quads = tvtk_base.false_bool_trait(help=\
        """
        Flag to tell the source to generate either a quad or two triangle
        for a set of four points. Initial value is false (generate
        triangles).
        """
    )
    def _quads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuads,
                        self.quads_)

    bounds = traits.Array(shape=(6,), value=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the level of subdivision of the faces.
        \pre positive_level: level>=0
        """
    )
    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

    _updateable_traits_ = \
    (('quads', 'GetQuads'), ('duplicate_shared_points',
    'GetDuplicateSharedPoints'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('level', 'GetLevel'), ('progress_text',
    'GetProgressText'), ('bounds', 'GetBounds'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'duplicate_shared_points',
    'global_warning_display', 'quads', 'release_data_flag', 'bounds',
    'level', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TessellatedBoxSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TessellatedBoxSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['duplicate_shared_points', 'quads'], [], ['bounds',
            'level']),
            title='Edit TessellatedBoxSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TessellatedBoxSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

