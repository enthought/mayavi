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


class TextureMapToPlane(DataSetAlgorithm):
    """
    TextureMapToPlane - generate texture coordinates by mapping points
    to plane
    
    Superclass: DataSetAlgorithm
    
    TextureMapToPlane is a filter that generates 2d texture
    coordinates by mapping input dataset points onto a plane. The plane
    can either be user specified or generated automatically. (A least
    squares method is used to generate the plane automatically.)
    
    There are two ways you can specify the plane. The first is to provide
    a plane normal. In this case the points are projected to a plane, and
    the points are then mapped into the user specified s-t coordinate
    range. For more control, you can specify a plane with three points:
    an origin and two points defining the two axes of the plane. (This is
    compatible with the PlaneSource.) Using the second method, the
    SRange and TRange vectors are ignored, since the presumption is that
    the user does not want to scale the texture coordinates; and you can
    adjust the origin and axes points to achieve the texture coordinate
    scaling you need. Note also that using the three point method the
    axes do not have to be orthogonal.
    
    See Also:
    
    
     PlaneSource TextureMapToCylinder TextureMapToSphere
    ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureMapToPlane, obj, update, **traits)
    
    automatic_plane_generation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off automatic plane generation.
        """
    )
    def _automatic_plane_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticPlaneGeneration,
                        self.automatic_plane_generation_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    s_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _s_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRange,
                        self.s_range)

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    point1 = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    t_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _t_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTRange,
                        self.t_range)

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('s_range', 'GetSRange'),
    ('automatic_plane_generation', 'GetAutomaticPlaneGeneration'),
    ('normal', 'GetNormal'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('point1', 'GetPoint1'), ('point2', 'GetPoint2'),
    ('abort_execute', 'GetAbortExecute'), ('t_range', 'GetTRange'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_plane_generation', 'debug',
    'global_warning_display', 'release_data_flag', 'normal', 'origin',
    'point1', 'point2', 'progress_text', 's_range', 't_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureMapToPlane, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_plane_generation'], [], ['normal',
            'origin', 'point1', 'point2', 's_range', 't_range']),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

