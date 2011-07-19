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


class Cursor2D(PolyDataAlgorithm):
    """
    Cursor2D - generate a 2d cursor representation
    
    Superclass: PolyDataAlgorithm
    
    Cursor2D is a class that generates a 2d cursor representation. The
    cursor consists of two intersection axes lines that meet at the
    cursor focus. Several optional features are available as well. An
    optional 2d bounding box may be enabled. An inner radius, centered at
    the focal point, can be set that erases the intersecting lines (e.g.,
    it leaves a clear area under the focal point so you can see what you
    are selecting). And finally, an optional point can be enabled located
    at the focal point. All of these features can be turned on and off
    independently.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCursor2D, obj, update, **traits)
    
    wrap = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
        """
    )
    def _wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrap,
                        self.wrap_)

    axes = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe axes.
        """
    )
    def _axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxes,
                        self.axes_)

    translation_mode = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
    )
    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    outline = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe bounding box.
        """
    )
    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    point = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the point located at the cursor focus.
        """
    )
    def _point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint,
                        self.point_)

    model_bounds = traits.Array(shape=(6,), value=(-10.0, 10.0, -10.0, 10.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set / get the bounding box of the 2d cursor. This defines the
        outline of the cursor, and where the focal point should lie.
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    radius = traits.Trait(2.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Specify a radius for a circle. This erases the cursor lines
        around the focal point.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    focal_point = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of cursor focus. If translation mode is on,
        then the entire cursor (including bounding box, cursor, and
        shadows) is translated. Otherwise, the focal point will either be
        clamped to the bounding box, or wrapped, if Wrap is on. (Note:
        this behavior requires that the bounding box is set prior to the
        focal point.) Note that the method takes a 3d point but ignores
        the z-coordinate value.
        """
    )
    def _focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalPoint,
                        self.focal_point)

    def all_off(self):
        """
        V.all_off()
        C++: void AllOff()
        Turn every part of the cursor on or off.
        """
        ret = self._vtk_obj.AllOff()
        return ret
        

    def all_on(self):
        """
        V.all_on()
        C++: void AllOn()
        Turn every part of the cursor on or off.
        """
        ret = self._vtk_obj.AllOn()
        return ret
        

    _updateable_traits_ = \
    (('model_bounds', 'GetModelBounds'), ('outline', 'GetOutline'),
    ('point', 'GetPoint'), ('axes', 'GetAxes'), ('progress_text',
    'GetProgressText'), ('wrap', 'GetWrap'), ('focal_point',
    'GetFocalPoint'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('radius', 'GetRadius'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('translation_mode',
    'GetTranslationMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'axes', 'debug', 'global_warning_display',
    'outline', 'point', 'release_data_flag', 'translation_mode', 'wrap',
    'focal_point', 'model_bounds', 'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Cursor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Cursor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['axes', 'outline', 'point', 'translation_mode',
            'wrap'], [], ['focal_point', 'model_bounds', 'radius']),
            title='Edit Cursor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Cursor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

