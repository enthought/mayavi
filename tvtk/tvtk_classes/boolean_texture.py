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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class BooleanTexture(ImageAlgorithm):
    """
    BooleanTexture - generate 2d texture map based on combinations of
    inside, outside, and on region boundary
    
    Superclass: ImageAlgorithm
    
    BooleanTexture is a filter to generate a 2d texture map based on
    combinations of inside, outside, and on region boundary. The "region"
    is implicitly represented via 2d texture coordinates. These texture
    coordinates are normally generated using a filter like
    ImplicitTextureCoords, which generates the texture coordinates for
    any implicit function.
    
    BooleanTexture generates the map according to the s-t texture
    coordinates plus the notion of being in, on, or outside of a region.
    An in region is when the texture coordinate is between
    (0,0.5-thickness/2).  An out region is where the texture coordinate
    is (0.5+thickness/2). An on region is between
    (0.5-thickness/2,0.5+thickness/2). The combination in, on, and out
    for each of the s-t texture coordinates results in 16 possible
    combinations (see text). For each combination, a different value of
    intensity and transparency can be assigned. To assign maximum
    intensity and/or opacity use the value 255. A minimum value of 0
    results in a black region (for intensity) and a fully transparent
    region (for transparency).
    
    See Also:
    
    ImplicitTextureCoords ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBooleanTexture, obj, update, **traits)
    
    on_out = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _on_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnOut,
                        self.on_out)

    in_in = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _in_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInIn,
                        self.in_in)

    on_in = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _on_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnIn,
                        self.on_in)

    y_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        Set the Y texture map dimension.
        """
    )
    def _y_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYSize,
                        self.y_size)

    thickness = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the thickness of the "on" region.
        """
    )
    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

    out_out = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _out_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutOut,
                        self.out_out)

    x_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        Set the X texture map dimension.
        """
    )
    def _x_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXSize,
                        self.x_size)

    on_on = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _on_on_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnOn,
                        self.on_on)

    in_on = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _in_on_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInOn,
                        self.in_on)

    out_in = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _out_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutIn,
                        self.out_in)

    out_on = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _out_on_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutOn,
                        self.out_on)

    in_out = traits.Array(shape=(2,), value=(255, 255), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _in_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInOut,
                        self.in_out)

    _updateable_traits_ = \
    (('y_size', 'GetYSize'), ('out_on', 'GetOutOn'), ('on_out',
    'GetOnOut'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('in_on', 'GetInOn'), ('on_on', 'GetOnOn'), ('on_in', 'GetOnIn'),
    ('progress_text', 'GetProgressText'), ('out_in', 'GetOutIn'),
    ('out_out', 'GetOutOut'), ('thickness', 'GetThickness'), ('in_in',
    'GetInIn'), ('debug', 'GetDebug'), ('x_size', 'GetXSize'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('in_out', 'GetInOut'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'in_in', 'in_on', 'in_out', 'on_in', 'on_on',
    'on_out', 'out_in', 'out_on', 'out_out', 'progress_text', 'thickness',
    'x_size', 'y_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BooleanTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BooleanTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['in_in', 'in_on', 'in_out', 'on_in', 'on_on',
            'on_out', 'out_in', 'out_on', 'out_out', 'thickness', 'x_size',
            'y_size']),
            title='Edit BooleanTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BooleanTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

