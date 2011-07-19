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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class ProjectedTexture(DataSetAlgorithm):
    """
    ProjectedTexture - assign texture coordinates for a projected
    texture
    
    Superclass: DataSetAlgorithm
    
    ProjectedTexture assigns texture coordinates to a dataset as if
    the texture was projected from a slide projected located somewhere in
    the scene.  Methods are provided to position the projector and aim it
    at a location, to set the width of the projector's frustum, and to
    set the range of texture coordinates assigned to the dataset.
    
    Objects in the scene that appear behind the projector are also
    assigned texture coordinates; the projected image is left-right and
    top-bottom flipped, much as a lens' focus flips the rays of light
    that pass through it.  A warning is issued if a point in the dataset
    falls at the focus of the projector.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProjectedTexture, obj, update, **traits)
    
    camera_mode = traits.Trait('pinhole',
    tvtk_base.TraitRevPrefixMap({'pinhole': 0, 'two_mirror': 1}), help=\
        """
        Set/Get the camera mode of the projection -- pinhole projection
        or two mirror projection.
        """
    )
    def _camera_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCameraMode,
                        self.camera_mode_)

    s_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _s_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRange,
                        self.s_range)

    focal_point = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the focal point of the projector (a point that lies along
        the center axis of the projector's frustum).
        """
    )
    def _focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalPoint,
                        self.focal_point)

    up = traits.Array(shape=(3,), value=(0.0, 1.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _up_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUp,
                        self.up)

    mirror_separation = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the mirror separation for the two mirror system.
        """
    )
    def _mirror_separation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMirrorSeparation,
                        self.mirror_separation)

    position = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    aspect_ratio = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _aspect_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAspectRatio,
                        self.aspect_ratio)

    t_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _t_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTRange,
                        self.t_range)

    def _get_orientation(self):
        return self._vtk_obj.GetOrientation()
    orientation = traits.Property(_get_orientation, help=\
        """
        Get the normalized orientation vector of the projector.
        """
    )

    _updateable_traits_ = \
    (('s_range', 'GetSRange'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('mirror_separation',
    'GetMirrorSeparation'), ('progress_text', 'GetProgressText'), ('up',
    'GetUp'), ('debug', 'GetDebug'), ('focal_point', 'GetFocalPoint'),
    ('aspect_ratio', 'GetAspectRatio'), ('abort_execute',
    'GetAbortExecute'), ('t_range', 'GetTRange'), ('release_data_flag',
    'GetReleaseDataFlag'), ('position', 'GetPosition'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('camera_mode', 'GetCameraMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'camera_mode', 'aspect_ratio', 'focal_point',
    'mirror_separation', 'position', 'progress_text', 's_range',
    't_range', 'up'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProjectedTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProjectedTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['camera_mode'], ['aspect_ratio', 'focal_point',
            'mirror_separation', 'position', 's_range', 't_range', 'up']),
            title='Edit ProjectedTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProjectedTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

