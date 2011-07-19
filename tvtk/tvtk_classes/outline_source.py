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


class OutlineSource(PolyDataAlgorithm):
    """
    OutlineSource - create wireframe outline around bounding box
    
    Superclass: PolyDataAlgorithm
    
    OutlineSource creates a wireframe outline around a user-specified
    bounding box.  The outline may be created aligned with the {x,y,z}
    axis - in which case it is defined by the 6 bounds
    {xmin,xmax,ymin,ymax,zmin,zmax} via set_bounds(). Alternatively, the
    box may be arbitrarily aligned, in which case it should be set via
    the set_corners() member.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutlineSource, obj, update, **traits)
    
    generate_faces = tvtk_base.false_bool_trait(help=\
        """
        Generate solid faces for the box. This is off by default.
        """
    )
    def _generate_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFaces,
                        self.generate_faces_)

    box_type = traits.Trait('axis_aligned',
    tvtk_base.TraitRevPrefixMap({'oriented': 1, 'axis_aligned': 0}), help=\
        """
        Set box type to axis_aligned (default) or Oriented. Use the method
        set_bounds() with axis_aligned mode, and set_corners() with Oriented
        mode.
        """
    )
    def _box_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxType,
                        self.box_type_)

    corners = traits.Array(shape=(24,), value=(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the corners of the outline when in Oriented mode, the
        values are supplied as 8*3 double values The correct corner
        ordering is using {x,y,z} convention for the unit cube as
        follows:
        {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}.
        """
    )
    def _corners_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCorners,
                        self.corners)

    bounds = traits.Array(shape=(6,), value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('corners',
    'GetCorners'), ('progress_text', 'GetProgressText'), ('bounds',
    'GetBounds'), ('box_type', 'GetBoxType'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('generate_faces', 'GetGenerateFaces'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_faces',
    'global_warning_display', 'release_data_flag', 'box_type', 'bounds',
    'corners', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OutlineSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_faces'], ['box_type'], ['bounds',
            'corners']),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

