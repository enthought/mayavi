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

from tvtk.tvtk_classes.render_view_base import RenderViewBase


class RenderView(RenderViewBase):
    """
    RenderView - A view containing a renderer.
    
    Superclass: RenderViewBase
    
    RenderView is a view which contains a Renderer.  You may add
    Actors directly to the renderer, or add certain
    DataRepresentation subclasses to the renderer.  The render view
    supports drag selection with the mouse to select cells.
    
    This class is also the parent class for any more specialized view
    which uses a renderer.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderView, obj, update, **traits)
    
    display_hover_text = tvtk_base.false_bool_trait(help=\
        """
        Whether the view should display hover text.
        """
    )
    def _display_hover_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayHoverText,
                        self.display_hover_text_)

    render_on_mouse_move = tvtk_base.false_bool_trait(help=\
        """
        Whether to render on every mouse move.
        """
    )
    def _render_on_mouse_move_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderOnMouseMove,
                        self.render_on_mouse_move_)

    label_placement_mode = traits.Trait('no_overlap',
    tvtk_base.TraitRevPrefixMap({'all': 1, 'no_overlap': 0}), help=\
        """
        Label placement mode. NO_OVERLAP uses LabelPlacementMapper,
        which has a faster startup time and works with 2d or 3d labels.
        ALL displays all labels (Warning: This may cause incredibly slow
        render times on datasets with more than a few hundred labels).
        """
    )
    def _label_placement_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelPlacementMode,
                        self.label_placement_mode_)

    selection_mode = traits.Trait('surface',
    tvtk_base.TraitRevPrefixMap({'frustum': 1, 'surface': 0}), help=\
        """
        Sets the selection mode for the render view. SURFACE selection
        uses HardwareSelector to perform a selection of visible cells.
        FRUSTUM selection just creates a view frustum selection, which
        will select everything in the frustum.
        """
    )
    def _selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMode,
                        self.selection_mode_)

    label_render_mode = traits.Trait('qt',
    tvtk_base.TraitRevPrefixMap({'freetype': 0, 'qt': 0}), help=\
        """
        Label render mode. FREETYPE uses the freetype label rendering. QT
        uses more advanced Qt-based label rendering.
        """
    )
    def _label_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelRenderMode,
                        self.label_render_mode_)

    interaction_mode = traits.Trait('3d',
    tvtk_base.TraitRevPrefixMap({'2d': 0, '3d': 1}), help=\
        """
        
        """
    )
    def _interaction_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionMode,
                        self.interaction_mode_)

    icon_size = traits.Array(shape=(2,), value=(16, 16), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _icon_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconSize,
                        self.icon_size)

    def _get_icon_texture(self):
        return wrap_vtk(self._vtk_obj.GetIconTexture())
    def _set_icon_texture(self, arg):
        old_val = self._get_icon_texture()
        self._wrap_call(self._vtk_obj.SetIconTexture,
                        deref_vtk(arg))
        self.trait_property_changed('icon_texture', old_val, arg)
    icon_texture = traits.Property(_get_icon_texture, _set_icon_texture, help=\
        """
        Set the icon sheet to use for rendering icons.
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set the view's transform. All RenderedRepresentations added to
        this view should use this transform.
        """
    )

    def get_display_size(self, *args):
        """
        V.get_display_size(int, int)
        C++: void GetDisplaySize(int &dsx, int &dsy)
        Set the display size of the icon (which may be different from the
        icon size). By default, if this value is not set, the the
        icon_size is used.
        """
        ret = self._wrap_call(self._vtk_obj.GetDisplaySize, *args)
        return ret

    def set_display_size(self, *args):
        """
        V.set_display_size(int, int)
        C++: void SetDisplaySize(int, int)
        V.set_display_size((int, int))
        C++: void SetDisplaySize(int a[2])"""
        ret = self._wrap_call(self._vtk_obj.SetDisplaySize, *args)
        return ret

    def _get_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetInteractorStyle())
    def _set_interactor_style(self, arg):
        old_val = self._get_interactor_style()
        self._wrap_call(self._vtk_obj.SetInteractorStyle,
                        deref_vtk(arg))
        self.trait_property_changed('interactor_style', old_val, arg)
    interactor_style = traits.Property(_get_interactor_style, _set_interactor_style, help=\
        """
        Get the interactor style associated with the render view.
        """
    )

    def add_labels(self, *args):
        """
        V.add_labels(AlgorithmOutput)
        C++: virtual void AddLabels(AlgorithmOutput *conn)
        Add labels from an input connection with an associated text
        property. The output must be a LabelHierarchy (normally the
        output of PointSetToLabelHierarchy).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLabels, *my_args)
        return ret

    def remove_labels(self, *args):
        """
        V.remove_labels(AlgorithmOutput)
        C++: virtual void RemoveLabels(AlgorithmOutput *conn)
        Remove labels from an input connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveLabels, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('display_hover_text',
    'GetDisplayHoverText'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interaction_mode',
    'GetInteractionMode'), ('icon_size', 'GetIconSize'), ('debug',
    'GetDebug'), ('selection_mode', 'GetSelectionMode'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'display_hover_text', 'global_warning_display',
    'render_on_mouse_move', 'interaction_mode', 'label_placement_mode',
    'label_render_mode', 'selection_mode', 'icon_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['display_hover_text', 'render_on_mouse_move'],
            ['interaction_mode', 'label_placement_mode', 'label_render_mode',
            'selection_mode'], ['icon_size']),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

