"""
An object to register callbacks and dispatch event wiring mouse clicks
on a scene to picking.
"""

# ETS imports
from traits.api import HasTraits, Dict, Instance, \
        Enum, Int, Callable, on_trait_change, List, Tuple, WeakRef

from mayavi.core.scene import Scene
from tvtk.api import tvtk


################################################################################
# class `MousePickDispatcher`
################################################################################
class MousePickDispatcher(HasTraits):
    """ An event dispatcher to send pick event on mouse clicks.

        This objects wires VTK observers so that picking callbacks
        can be bound to mouse click without movement.

        The object deals with adding and removing the VTK-level
        callbacks.
    """

    # The scene events are wired to.
    scene = WeakRef(Scene)

    # The list of callbacks, with the picker type they should be using,
    # and the mouse button that triggers them.
    callbacks = List(Tuple(
                        Callable,
                        Enum('cell', 'point', 'world'),
                        Enum('Left', 'Middle', 'Right'),
                        ),
                    help="The list of callbacks, with the picker type they "
                         "should be using, and the mouse button that "
                         "triggers them. The callback is passed "
                         "as an argument the tvtk picker."
                    )

    #--------------------------------------------------------------------------
    # Private traits
    #--------------------------------------------------------------------------

    # Whether the mouse has moved after the button press
    _mouse_no_mvt = Int

    # The button that has been pressed
    _current_button = Enum('Left', 'Middle', 'Right')

    # The various picker that are used when the mouse is pressed
    _active_pickers = Dict

    # The VTK callback numbers corresponding to our callbacks
    _picker_callback_nbs = Dict(value_trait=Int)

    # The VTK callback numbers corresponding to mouse movement
    _mouse_mvt_callback_nb = Int

    # The VTK callback numbers corresponding to mouse press
    _mouse_press_callback_nbs = Dict

    # The VTK callback numbers corresponding to mouse release
    _mouse_release_callback_nbs = Dict

    #--------------------------------------------------------------------------
    # Callbacks management
    #--------------------------------------------------------------------------

    @on_trait_change('callbacks_items')
    def dispatch_callbacks_change(self, name, trait_list_event):
        for item in trait_list_event.added:
            self.callback_added(item)
        for item in trait_list_event.removed:
            self.callback_removed(item)


    def callback_added(self, item):
        """ Wire up the different VTK callbacks.
        """
        callback, type, button = item
        picker = getattr(self.scene.scene.picker, '%spicker' % type)
        self._active_pickers[type] = picker

        # Register the pick callback
        if not type in self._picker_callback_nbs:
            self._picker_callback_nbs[type] = \
                            picker.add_observer("EndPickEvent",
                                                self.on_pick)

        # Register the callbacks on the scene interactor
        move_event = "RenderEvent"
        if not self._mouse_mvt_callback_nb:
            self._mouse_mvt_callback_nb = \
                self.scene.scene.interactor.add_observer(move_event,
                                                self.on_mouse_move)
        if not button in self._mouse_press_callback_nbs:
            self._mouse_press_callback_nbs[button] = \
                self.scene.scene.interactor.add_observer(
                                    '%sButtonPressEvent' % button,
                                    self.on_button_press)
        release_event = "EndInteractionEvent"
        if not button in self._mouse_release_callback_nbs:
            self._mouse_release_callback_nbs[button] = \
                self.scene.scene.interactor.add_observer(
                                    release_event,
                                    self.on_button_release)


    def callback_removed(self, item):
        """ Clean up the unnecessary VTK callbacks.
        """
        callback, type, button = item

        # If the picker is no longer needed, clean up its observers.
        if not [t for c, t, b in self.callbacks if t == type]:
            picker = self._active_pickers[type]
            picker.remove_observer(self._picker_callback_nbs[type])
            del self._active_pickers[type]

        # If there are no longer callbacks on the button, clean up
        # the corresponding observers.
        if not [b for c, t, b in self.callbacks if b == button]:
            self.scene.scene.interactor.remove_observer(
                    self._mouse_press_callback_nbs[button])
            self.scene.scene.interactor.remove_observer(
                    self._mouse_release_callback_nbs[button])
        if len(self.callbacks) == 0 and self._mouse_mvt_callback_nb:
            self.scene.scene.interactor.remove_observer(
                            self._mouse_mvt_callback_nb)
            self._mouse_mvt_callback_nb = 0


    def clear_callbacks(self):
        while self.callbacks:
            self.callbacks.pop()

    #--------------------------------------------------------------------------
    # Mouse movement dispatch mechanism
    #--------------------------------------------------------------------------

    def on_button_press(self, vtk_picker, event):
        self._current_button = event[:-len('ButtonPressEvent')]
        self._mouse_no_mvt = 2


    def on_mouse_move(self, vtk_picker, event):
        if self._mouse_no_mvt:
            self._mouse_no_mvt -= 1


    def on_button_release(self, vtk_picker, event):
        """ If the mouse has not moved, pick with our pickers.
        """
        if self._mouse_no_mvt:
            x, y = vtk_picker.GetEventPosition()
            for picker in self._active_pickers.values():
                try:
                    picker.pick((x, y, 0), self.scene.scene.renderer)
                except TypeError:
                    picker.pick(x, y, 0, self.scene.scene.renderer)
        self._mouse_no_mvt = 0


    def on_pick(self, vtk_picker, event):
        """ Dispatch the pick to the callback associated with the
            corresponding mouse button.
        """
        picker = tvtk.to_tvtk(vtk_picker)
        for event_type, event_picker in self._active_pickers.items():
            if picker is event_picker:
                for callback, type, button in self.callbacks:
                    if ( type == event_type
                                    and button == self._current_button):
                        callback(picker)
                break

    #--------------------------------------------------------------------------
    # Private methods
    #--------------------------------------------------------------------------

    def __del__(self):
        self.clear_callbacks()
