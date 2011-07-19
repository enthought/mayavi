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

from tvtk.tvtk_classes.object import Object


class LabelRenderStrategy(Object):
    """
    LabelRenderStrategy - Superclass for label rendering
    implementations.
    
    Superclass: Object
    
    These methods should only be called within a mapper.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelRenderStrategy, obj, update, **traits)
    
    def _get_default_text_property(self):
        return wrap_vtk(self._vtk_obj.GetDefaultTextProperty())
    def _set_default_text_property(self, arg):
        old_val = self._get_default_text_property()
        self._wrap_call(self._vtk_obj.SetDefaultTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('default_text_property', old_val, arg)
    default_text_property = traits.Property(_get_default_text_property, _set_default_text_property, help=\
        """
        Set the default text property for the strategy.
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Set the renderer associated with this strategy.
        """
    )

    def compute_label_bounds(self, *args):
        """
        V.compute_label_bounds(TextProperty, string, [float, float,
            float, float])
        C++: virtual void ComputeLabelBounds(TextProperty *tprop,
            StdString label, double bds[4])
        V.compute_label_bounds(TextProperty, unicode, [float, float,
            float, float])
        C++: virtual void ComputeLabelBounds(TextProperty *tprop,
            UnicodeString label, double bds[4])
        Compute the bounds of a label. Must be performed after the
        renderer is set. Only the unicode string version must be
        implemented in subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeLabelBounds, *my_args)
        return ret

    def end_frame(self):
        """
        V.end_frame()
        C++: virtual void EndFrame()
        End a rendering frame.
        """
        ret = self._vtk_obj.EndFrame()
        return ret
        

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Release any graphics resources that are being consumed by this
        strategy. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def render_label(self, *args):
        """
        V.render_label([int, int], TextProperty, string)
        C++: virtual void RenderLabel(int x[2], TextProperty *tprop,
            StdString label)
        V.render_label([int, int], TextProperty, string, int)
        C++: virtual void RenderLabel(int x[2], TextProperty *tprop,
            StdString label, int maxWidth)
        V.render_label([int, int], TextProperty, unicode)
        C++: virtual void RenderLabel(int x[2], TextProperty *tprop,
            UnicodeString label)
        V.render_label([int, int], TextProperty, unicode, int)
        C++: virtual void RenderLabel(int x[2], TextProperty *tprop,
            UnicodeString label, int maxWidth)
        Render a label at a location in display coordinates. Must be
        performed between start_frame() and end_frame() calls. Only the
        unicode string version must be implemented in subclasses. The
        optional final parameter max_width specifies a maximum width for
        the label. Longer labels can be shorted with an ellipsis (...).
        Only renderer strategies that return true from
        supports_bounded_size must implement this version of th method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderLabel, *my_args)
        return ret

    def start_frame(self):
        """
        V.start_frame()
        C++: virtual void StartFrame()
        Start a rendering frame. Renderer must be set.
        """
        ret = self._vtk_obj.StartFrame()
        return ret
        

    def supports_bounded_size(self):
        """
        V.supports_bounded_size() -> bool
        C++: virtual bool SupportsBoundedSize()
        Whether the text rendering strategy supports bounded size. The
        superclass returns true. Subclasses should override this to
        return the appropriate value. Subclasses that return true from
        this method should implement the version of render_label() that
        takes a maximum size (see render_label()).
        """
        ret = self._vtk_obj.SupportsBoundedSize()
        return ret
        

    def supports_rotation(self):
        """
        V.supports_rotation() -> bool
        C++: virtual bool SupportsRotation()
        Whether the text rendering strategy supports rotation. The
        superclass returns true. Subclasses should override this to
        return the appropriate value.
        """
        ret = self._vtk_obj.SupportsRotation()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelRenderStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelRenderStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit LabelRenderStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelRenderStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

