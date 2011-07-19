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


class ButtonSource(PolyDataAlgorithm):
    """
    ButtonSource - abstract class for creating various button types
    
    Superclass: PolyDataAlgorithm
    
    ButtonSource is an abstract class that defines an API for creating
    "button-like" objects in VTK. A button is a geometry with a
    rectangular region that can be textured. The button is divided into
    two regions: the texture region and the shoulder region. The points
    in both regions are assigned texture coordinates. The texture region
    has texture coordinates consistent with the image to be placed on it.
     All points in the shoulder regions are assigned a texture coordinate
    specified by the user.  In this way the shoulder region can be
    colored by the texture.
    
    Creating a ButtonSource requires specifying its center point.
    (Subclasses have other attributes that must be set to control the
    shape of the button.) You must also specify how to control the shape
    of the texture region; i.e., wheter to size the texture region
    proportional to the texture dimensions or whether to size the texture
    region proportional to the button. Also, buttons can be created
    single sided are mirrored to create two-sided buttons.
    
    Caveats:
    
    The button is defined in the x-y plane. Use
    TransformPolyDataFilter or Glyph3D to orient the button in a
    different direction.
    
    See Also:
    
    EllipticalButtonSource RectangularButtonSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkButtonSource, obj, update, **traits)
    
    two_sided = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether the button is single or double sided. A double
        sided button can be viewed from two sides...it looks sort of like
        a "pill." A single-sided button is meant to viewed from a single
        side; it looks like a "clam-shell."
        """
    )
    def _two_sided_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoSided,
                        self.two_sided_)

    texture_style = traits.Trait('proportional',
    tvtk_base.TraitRevPrefixMap({'proportional': 1, 'fit_image': 0}), help=\
        """
        Set/Get the style of the texture region: whether to size it
        according to the x-y dimensions of the texture, or whether to
        make the texture region proportional to the width/height of the
        button.
        """
    )
    def _texture_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureStyle,
                        self.texture_style_)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    shoulder_texture_coordinate = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _shoulder_texture_coordinate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShoulderTextureCoordinate,
                        self.shoulder_texture_coordinate)

    texture_dimensions = traits.Array(shape=(2,), value=(100, 100), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _texture_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureDimensions,
                        self.texture_dimensions)

    _updateable_traits_ = \
    (('texture_style', 'GetTextureStyle'), ('center', 'GetCenter'),
    ('shoulder_texture_coordinate', 'GetShoulderTextureCoordinate'),
    ('debug', 'GetDebug'), ('progress_text', 'GetProgressText'),
    ('texture_dimensions', 'GetTextureDimensions'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('two_sided', 'GetTwoSided'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'two_sided', 'texture_style', 'center',
    'progress_text', 'shoulder_texture_coordinate', 'texture_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ButtonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['two_sided'], ['texture_style'], ['center',
            'shoulder_texture_coordinate', 'texture_dimensions']),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

