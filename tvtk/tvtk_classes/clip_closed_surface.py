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


class ClipClosedSurface(PolyDataAlgorithm):
    """
    ClipClosedSurface - Clip a closed surface with a plane collection
    
    Superclass: PolyDataAlgorithm
    
    ClipClosedSurface will clip a closed polydata surface with a
    collection of clipping planes.  It will produce a new closed surface
    by creating new polygonal faces where the input data was clipped. If
    generate_outline is on, it will also generate an outline wherever the
    clipping planes intersect the data.  The scalar_mode option will add
    cell scalars to the output, so that the generated faces can be
    visualized in a different color from the original surface.
    
    Caveats:
    
    The triangulation of new faces is done in O(n) time for simple convex
    inputs, but for non-convex inputs the worst-case time is O(n^2*m^2)
    where n is the number of points and m is the number of 3d cavities.
    The best triangulation algorithms, in contrast, are O(n log n). There
    are also rare cases where the triangulation will fail to produce a
    watertight output.  Turn on triangulation_error_display to be notified
    of these failures.
    
    See Also:
    
    OutlineFilter OutlineSource VolumeOutlineSource
    
    Thanks:
    
    Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkClipClosedSurface, obj, update, **traits)
    
    generate_faces = tvtk_base.true_bool_trait(help=\
        """
        Set whether to generate polygonal faces for the output.  This is
        on by default.  If it is off, then the output will have no polys.
        """
    )
    def _generate_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFaces,
                        self.generate_faces_)

    generate_color_scalars = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _generate_color_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateColorScalars,
                        self.generate_color_scalars_)

    pass_point_data = tvtk_base.false_bool_trait(help=\
        """
        Pass the point data to the output.  Point data will be
        interpolated when new points are generated.  This is off by
        default.
        """
    )
    def _pass_point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPointData,
                        self.pass_point_data_)

    triangulation_error_display = tvtk_base.false_bool_trait(help=\
        """
        Generate errors when the triangulation fails.  Usually the
        triangulation errors are too small to see, but they result in a
        surface that is not watertight.  This option has no impact on
        performance.
        """
    )
    def _triangulation_error_display_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTriangulationErrorDisplay,
                        self.triangulation_error_display_)

    generate_outline = tvtk_base.false_bool_trait(help=\
        """
        Set whether to generate an outline wherever an input face was cut
        by a plane.  This is off by default.
        """
    )
    def _generate_outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateOutline,
                        self.generate_outline_)

    scalar_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'labels': 2, 'colors': 1}), help=\
        """
        Set whether to add cell scalars, so that new faces and outlines
        can be distinguished from original faces and lines.  The options
        are "None", "Colors", and "Labels".  For the "Labels" option, a
        scalar value of "0" indicates an original cell, "1" indicates a
        new cell on a cut face, and "2" indicates a new cell on the
        active_plane as set by the set_active_plane() method.  The default
        scalar mode is "None".
        """
    )
    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    base_color = tvtk_base.vtk_color_trait((1.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _base_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBaseColor,
                        self.base_color, False)

    active_plane_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the active plane, so that the clipping from that plane can be
        displayed in a different color.  Set this to -1 if there is no
        active plane.  The default value is -1.
        """
    )
    def _active_plane_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActivePlaneId,
                        self.active_plane_id)

    active_plane_color = tvtk_base.vtk_color_trait((1.0, 1.0, 0.0), help=\
        """
        
        """
    )
    def _active_plane_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActivePlaneColor,
                        self.active_plane_color, False)

    clip_color = tvtk_base.vtk_color_trait((1.0, 0.5, 0.0), help=\
        """
        
        """
    )
    def _clip_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipColor,
                        self.clip_color, False)

    tolerance = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        Set the tolerance for creating new points while clipping.  If the
        tolerance is too small, then degenerate triangles might be
        produced. The default tolerance is 1e-6.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_clipping_planes(self):
        return wrap_vtk(self._vtk_obj.GetClippingPlanes())
    def _set_clipping_planes(self, arg):
        old_val = self._get_clipping_planes()
        self._wrap_call(self._vtk_obj.SetClippingPlanes,
                        deref_vtk(arg))
        self.trait_property_changed('clipping_planes', old_val, arg)
    clipping_planes = traits.Property(_get_clipping_planes, _set_clipping_planes, help=\
        """
        Set the PlaneCollection that holds the clipping planes.
        """
    )

    _updateable_traits_ = \
    (('scalar_mode', 'GetScalarMode'), ('base_color', 'GetBaseColor'),
    ('clip_color', 'GetClipColor'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('active_plane_id', 'GetActivePlaneId'),
    ('debug', 'GetDebug'), ('triangulation_error_display',
    'GetTriangulationErrorDisplay'), ('progress_text', 'GetProgressText'),
    ('generate_faces', 'GetGenerateFaces'), ('generate_color_scalars',
    'GetGenerateColorScalars'), ('generate_outline',
    'GetGenerateOutline'), ('abort_execute', 'GetAbortExecute'),
    ('pass_point_data', 'GetPassPointData'), ('release_data_flag',
    'GetReleaseDataFlag'), ('active_plane_color', 'GetActivePlaneColor'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_color_scalars',
    'generate_faces', 'generate_outline', 'global_warning_display',
    'pass_point_data', 'release_data_flag', 'triangulation_error_display',
    'scalar_mode', 'active_plane_color', 'active_plane_id', 'base_color',
    'clip_color', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ClipClosedSurface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ClipClosedSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_color_scalars', 'generate_faces',
            'generate_outline', 'pass_point_data', 'triangulation_error_display'],
            ['scalar_mode'], ['active_plane_color', 'active_plane_id',
            'base_color', 'clip_color', 'tolerance']),
            title='Edit ClipClosedSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ClipClosedSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

