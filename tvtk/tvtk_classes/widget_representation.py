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

from tvtk.tvtk_classes.prop import Prop


class WidgetRepresentation(Prop):
    """
    WidgetRepresentation - abstract class defines interface between
    the widget and widget representation classes
    
    Superclass: Prop
    
    This class is used to define the API for, and partially implement, a
    representation for different types of widgets. Note that the widget
    representation (i.e., subclasses of WidgetRepresentation) are a
    type of Prop; meaning that they can be associated with a
    Renderer end embedded in a scene like any other Actor. However,
    WidgetRepresentation also defines an API that enables it to be
    paired with a subclass AbstractWidget, meaning that it can be
    driven by a widget, serving to represent the widget as the widget
    responds to registered events.
    
    The API defined here should be regarded as a guideline for
    implementing widgets and widget representations. Widget behavior is
    complex, as is the way the representation responds to the registered
    widget events, so the API may vary from widget to widget to reflect
    this complexity.
    
    Caveats:
    
    The separation of the widget event handling and representation
    enables users and developers to create new appearances for the
    widget. It also facilitates parallel processing, where the client
    application handles events, and remote representations of the widget
    are slaves to the client (and do not handle events).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWidgetRepresentation, obj, update, **traits)
    
    need_to_render = tvtk_base.false_bool_trait(help=\
        """
        Some subclasses use this data member to keep track of whether to
        render or not (i.e., to minimize the total number of renders).
        """
    )
    def _need_to_render_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNeedToRender,
                        self.need_to_render_)

    place_factor = traits.Trait(1.0, traits.Range(0.01, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get a factor representing the scaling of the widget upon
        placement (via the place_widget() method). Normally the widget is
        placed so that it just fits within the bounding box defined in
        place_widget(bounds). The place_factor will make the widget larger
        (_place_factor > 1) or smaller (_place_factor < 1). By default,
        place_factor is set to 0.5.
        """
    )
    def _place_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlaceFactor,
                        self.place_factor)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Subclasses of WidgetRepresentation must implement these
        methods. This is considered the minimum API for a widget
        representation.
        
        set_renderer() - the renderer in which the widget is to appear
        must be set. build_representation() - update the geometry of the
        widget based on its
                                current state.  WARNING: The renderer is
        NOT reference counted by the representation, in order to avoid
        reference loops.  Be sure that the representation lifetime does
        not extend beyond the renderer lifetime.
        """
    )

    handle_size = traits.Trait(0.01, traits.Range(0.001, 1000.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the size of the handles that
        appear as part of the widget (if any). These handles (like
        spheres, etc.)  are used to manipulate the widget. The handle_size
        data member allows you to change the relative size of the
        handles. Note that while the handle size is typically expressed
        in pixels, some subclasses may use a relative size with respect
        to the viewport. (As a corollary, the value of this ivar is often
        set by subclasses of this class during instance instantiation.)
        """
    )
    def _handle_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSize,
                        self.handle_size)

    def _get_interaction_state(self):
        return self._vtk_obj.GetInteractionState()
    interaction_state = traits.Property(_get_interaction_state, help=\
        """
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their own depending on the specifics of the
        widget.
        """
    )

    def _get_need_to_render_max_value(self):
        return self._vtk_obj.GetNeedToRenderMaxValue()
    need_to_render_max_value = traits.Property(_get_need_to_render_max_value, help=\
        """
        Some subclasses use this data member to keep track of whether to
        render or not (i.e., to minimize the total number of renders).
        """
    )

    def _get_need_to_render_min_value(self):
        return self._vtk_obj.GetNeedToRenderMinValue()
    need_to_render_min_value = traits.Property(_get_need_to_render_min_value, help=\
        """
        Some subclasses use this data member to keep track of whether to
        render or not (i.e., to minimize the total number of renders).
        """
    )

    def build_representation(self):
        """
        V.build_representation()
        C++: virtual void BuildRepresentation()
        Subclasses of WidgetRepresentation must implement these
        methods. This is considered the minimum API for a widget
        representation.
        
        set_renderer() - the renderer in which the widget is to appear
        must be set. build_representation() - update the geometry of the
        widget based on its
                                current state.  WARNING: The renderer is
        NOT reference counted by the representation, in order to avoid
        reference loops.  Be sure that the representation lifetime does
        not extend beyond the renderer lifetime.
        """
        ret = self._vtk_obj.BuildRepresentation()
        return ret
        

    def compute_interaction_state(self, *args):
        """
        V.compute_interaction_state(int, int, int) -> int
        C++: virtual int ComputeInteractionState(int X, int Y,
            int modify=0)
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their o ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.ComputeInteractionState, *args)
        return ret

    def end_widget_interaction(self, *args):
        """
        V.end_widget_interaction([float, float])
        C++: virtual void EndWidgetInteraction(double newEventPos[2])
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their own depending on the s ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.EndWidgetInteraction, *args)
        return ret

    def highlight(self, *args):
        """
        V.highlight(int)
        C++: virtual void Highlight(int highlightOn)
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their own depending on the specifics of the
        widget.
        """
        ret = self._wrap_call(self._vtk_obj.Highlight, *args)
        return ret

    def start_widget_interaction(self, *args):
        """
        V.start_widget_interaction([float, float])
        C++: virtual void StartWidgetInteraction(double eventPos[2])
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their own depending on the  ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.StartWidgetInteraction, *args)
        return ret

    def widget_interaction(self, *args):
        """
        V.widget_interaction([float, float])
        C++: virtual void WidgetInteraction(double newEventPos[2])
        The following is a suggested API for widget representations.
        These methods define the communication between the widget and its
        representation. These methods are only suggestions because
        widgets take on so many different forms that a universal API is
        not deemed practical. However, these methods should be
        implemented when possible to insure that the VTK widget hierarchy
        remains self-consistent.
        
        place_widget() - given a bounding box
        (xmin,xmax,ymin,ymax,zmin,zmax), place
                        the widget inside of it. The current orientation
        of the widget
                        is preserved, only scaling and translation is
        performed. start_widget_interaction() - generally corresponds to a
        initial event (e.g.,
                                   mouse down) that starts the
        interaction process
                                   with the widget. widget_interaction() -
        invoked when an event causes the widget to change
                              appearance. end_widget_interaction() -
        generally corresponds to a final event (e.g., mouse up)
                                 and completes the interaction sequence.
        compute_interaction_state() - given (X,Y) display coordinates in a
        renderer, with a
                                    possible flag that modifies the
        computation,
                                    what is the state of the widget?
        get_interaction_state() - return the current state of the widget.
        Note that the
                                value of "0" typically refers to
        "outside". The
                                interaction state is strictly a function
        of the
                                representation, and the widget/represent
        must agree
                                on what they mean. Highlight() - turn on
        or off any highlights associated with the widget.
                      Highlights are generally turned on when the widget
        is selected.  Note that subclasses may ignore some of these
        methods and implement their own depending on the specifi ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.WidgetInteraction, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('reference_count', 'GetReferenceCount'),
    ('need_to_render', 'GetNeedToRender'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WidgetRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier']),
            title='Edit WidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

