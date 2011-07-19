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

from tvtk.tvtk_classes.prop3d import Prop3D


class AxesActor(Prop3D):
    """
    AxesActor - a 3d axes representation
    
    Superclass: Prop3D
    
    AxesActor is a hybrid 2d/_3d actor used to represent 3d axes in a
    scene. The user can define the geometry to use for the shaft or the
    tip, and the user can set the text for the three axes. The text will
    appear to follow the camera since it is implemented by means of
    CaptionActor2D.  All of the functionality of the underlying
    CaptionActor2D objects are accessable so that, for instance, the
    font attributes of the axes text can be manipulated through
    TextProperty. Since this class inherits from Prop3D, one can
    apply a user transform to the underlying geometry and the positioning
    of the labels. For example, a rotation transform could be used to
    generate a left-handed axes representation.
    
    Caveats:
    
    AxesActor is primarily intended for use with
    OrientationMarkerWidget. The bounds of this actor are calculated
    as though the geometry of the axes were symmetric: that is, although
    only positive axes are visible, bounds are calculated as though
    negative axes are present too.  This is done intentionally to
    implement functionality of the camera update mechanism in
    OrientationMarkerWidget.
    
    See Also:
    
    AnnotatedCubeActor OrientationMarkerWidget CaptionActor2D
    TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxesActor, obj, update, **traits)
    
    axis_labels = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable drawing the axis labels.
        """
    )
    def _axis_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisLabels,
                        self.axis_labels_)

    tip_type = traits.Trait('cone',
    tvtk_base.TraitRevPrefixMap({'sphere': 1, 'cone': 0, 'user_defined': 1}), help=\
        """
        Set the type of the tip to a cone, sphere, or user defined
        geometry.
        """
    )
    def _tip_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTipType,
                        self.tip_type_)

    shaft_type = traits.Trait('user_defined',
    tvtk_base.TraitRevPrefixMap({'line': 1, 'cylinder': 0, 'user_defined': 1}), help=\
        """
        Set the type of the shaft to a cylinder, line, or user defined
        geometry.
        """
    )
    def _shaft_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShaftType,
                        self.shaft_type_)

    total_length = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the total length of the axes in 3 dimensions.
        """
    )
    def _total_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTotalLength,
                        self.total_length)

    cylinder_resolution = traits.Trait(16, traits.Range(3, 128, enter_set=True, auto_set=False), help=\
        """
        Set/get the resolution of the pieces of the axes actor.
        """
    )
    def _cylinder_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCylinderResolution,
                        self.cylinder_resolution)

    normalized_tip_length = traits.Array(shape=(3,), value=(0.20000000000000001, 0.20000000000000001, 0.20000000000000001), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the normalized (0-1) length of the tip.  Normally, this would
        be 1 - the normalized length of the shaft.
        """
    )
    def _normalized_tip_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizedTipLength,
                        self.normalized_tip_length)

    z_axis_label_text = traits.String(r"Z", enter_set=True, auto_set=False, help=\
        """
        Set/get the label text.
        """
    )
    def _z_axis_label_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisLabelText,
                        self.z_axis_label_text)

    y_axis_label_text = traits.String(r"Y", enter_set=True, auto_set=False, help=\
        """
        Set/get the label text.
        """
    )
    def _y_axis_label_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisLabelText,
                        self.y_axis_label_text)

    sphere_radius = traits.Trait(0.5, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/get the radius of the pieces of the axes actor.
        """
    )
    def _sphere_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphereRadius,
                        self.sphere_radius)

    x_axis_label_text = traits.String(r"X", enter_set=True, auto_set=False, help=\
        """
        Set/get the label text.
        """
    )
    def _x_axis_label_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisLabelText,
                        self.x_axis_label_text)

    cone_radius = traits.Trait(0.4, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/get the radius of the pieces of the axes actor.
        """
    )
    def _cone_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConeRadius,
                        self.cone_radius)

    sphere_resolution = traits.Trait(16, traits.Range(3, 128, enter_set=True, auto_set=False), help=\
        """
        Set/get the resolution of the pieces of the axes actor.
        """
    )
    def _sphere_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphereResolution,
                        self.sphere_resolution)

    def _get_user_defined_shaft(self):
        return wrap_vtk(self._vtk_obj.GetUserDefinedShaft())
    def _set_user_defined_shaft(self, arg):
        old_val = self._get_user_defined_shaft()
        self._wrap_call(self._vtk_obj.SetUserDefinedShaft,
                        deref_vtk(arg))
        self.trait_property_changed('user_defined_shaft', old_val, arg)
    user_defined_shaft = traits.Property(_get_user_defined_shaft, _set_user_defined_shaft, help=\
        """
        Set the user defined shaft polydata.
        """
    )

    normalized_shaft_length = traits.Array(shape=(3,), value=(0.80000000000000004, 0.80000000000000004, 0.80000000000000004), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the normalized (0-1) length of the shaft.
        """
    )
    def _normalized_shaft_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizedShaftLength,
                        self.normalized_shaft_length)

    normalized_label_position = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the normalized (0-1) position of the label along the length
        of the shaft.  A value > 1 is permissible.
        """
    )
    def _normalized_label_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizedLabelPosition,
                        self.normalized_label_position)

    cylinder_radius = traits.Trait(0.05, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/get the radius of the pieces of the axes actor.
        """
    )
    def _cylinder_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCylinderRadius,
                        self.cylinder_radius)

    cone_resolution = traits.Trait(16, traits.Range(3, 128, enter_set=True, auto_set=False), help=\
        """
        Set/get the resolution of the pieces of the axes actor.
        """
    )
    def _cone_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConeResolution,
                        self.cone_resolution)

    def _get_user_defined_tip(self):
        return wrap_vtk(self._vtk_obj.GetUserDefinedTip())
    def _set_user_defined_tip(self, arg):
        old_val = self._get_user_defined_tip()
        self._wrap_call(self._vtk_obj.SetUserDefinedTip,
                        deref_vtk(arg))
        self.trait_property_changed('user_defined_tip', old_val, arg)
    user_defined_tip = traits.Property(_get_user_defined_tip, _set_user_defined_tip, help=\
        """
        Set the user defined tip polydata.
        """
    )

    def _get_x_axis_caption_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetXAxisCaptionActor2D())
    x_axis_caption_actor2d = traits.Property(_get_x_axis_caption_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def _get_x_axis_shaft_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxisShaftProperty())
    x_axis_shaft_property = traits.Property(_get_x_axis_shaft_property, help=\
        """
        Get the shaft properties.
        """
    )

    def _get_x_axis_tip_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxisTipProperty())
    x_axis_tip_property = traits.Property(_get_x_axis_tip_property, help=\
        """
        Get the tip properties.
        """
    )

    def _get_y_axis_caption_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetYAxisCaptionActor2D())
    y_axis_caption_actor2d = traits.Property(_get_y_axis_caption_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def _get_y_axis_shaft_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxisShaftProperty())
    y_axis_shaft_property = traits.Property(_get_y_axis_shaft_property, help=\
        """
        Get the shaft properties.
        """
    )

    def _get_y_axis_tip_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxisTipProperty())
    y_axis_tip_property = traits.Property(_get_y_axis_tip_property, help=\
        """
        Get the tip properties.
        """
    )

    def _get_z_axis_caption_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetZAxisCaptionActor2D())
    z_axis_caption_actor2d = traits.Property(_get_z_axis_caption_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def _get_z_axis_shaft_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxisShaftProperty())
    z_axis_shaft_property = traits.Property(_get_z_axis_shaft_property, help=\
        """
        Get the shaft properties.
        """
    )

    def _get_z_axis_tip_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxisTipProperty())
    z_axis_tip_property = traits.Property(_get_z_axis_tip_property, help=\
        """
        Get the tip properties.
        """
    )

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('x_axis_label_text', 'GetXAxisLabelText'),
    ('allocated_render_time', 'GetAllocatedRenderTime'), ('cone_radius',
    'GetConeRadius'), ('z_axis_label_text', 'GetZAxisLabelText'),
    ('normalized_tip_length', 'GetNormalizedTipLength'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('sphere_resolution', 'GetSphereResolution'),
    ('shaft_type', 'GetShaftType'), ('total_length', 'GetTotalLength'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('use_bounds',
    'GetUseBounds'), ('y_axis_label_text', 'GetYAxisLabelText'), ('scale',
    'GetScale'), ('cylinder_radius', 'GetCylinderRadius'),
    ('cone_resolution', 'GetConeResolution'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('sphere_radius', 'GetSphereRadius'),
    ('normalized_shaft_length', 'GetNormalizedShaftLength'),
    ('cylinder_resolution', 'GetCylinderResolution'), ('axis_labels',
    'GetAxisLabels'), ('normalized_label_position',
    'GetNormalizedLabelPosition'), ('orientation', 'GetOrientation'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('tip_type', 'GetTipType'))
    
    _full_traitnames_list_ = \
    (['axis_labels', 'debug', 'dragable', 'global_warning_display',
    'pickable', 'use_bounds', 'visibility', 'shaft_type', 'tip_type',
    'allocated_render_time', 'cone_radius', 'cone_resolution',
    'cylinder_radius', 'cylinder_resolution', 'estimated_render_time',
    'normalized_label_position', 'normalized_shaft_length',
    'normalized_tip_length', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale', 'sphere_radius',
    'sphere_resolution', 'total_length', 'x_axis_label_text',
    'y_axis_label_text', 'z_axis_label_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxesActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['axis_labels', 'use_bounds', 'visibility'],
            ['shaft_type', 'tip_type'], ['allocated_render_time', 'cone_radius',
            'cone_resolution', 'cylinder_radius', 'cylinder_resolution',
            'estimated_render_time', 'normalized_label_position',
            'normalized_shaft_length', 'normalized_tip_length', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale',
            'sphere_radius', 'sphere_resolution', 'total_length',
            'x_axis_label_text', 'y_axis_label_text', 'z_axis_label_text']),
            title='Edit AxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

