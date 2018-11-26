import imghdr


class RemoteWidget(object):
    """An abstract remote widget which talks to the bridge but has no toolkit
    specific code.

    This is similar to the QVTKRenderWindowInteractor but instead of actually
    setting things on a local render window interactor, passes them off to a
    remote server to do the job and simply renders a PNG sent by the remote
    server.
    """
    def __init__(self, scene_proxy, bridge, **kw):
        super(RemoteWidget, self).__init__(**kw)
        self.scene_proxy = scene_proxy
        self.bridge = bridge
        bridge.add_widget(scene_proxy.id, self)

        self._ActiveButton = 'none'

        # private attributes
        self._saveX = 0
        self._saveY = 0
        self._saveModifiers = False, False
        self._saveButtons = 'none'
        self._wheelDelta = 0
        self._is_resizing = False
        self._move_count = 0

        # Note that since this is just a raw image sent by the server we do
        # not need to worry about the pixel ratio for this case unlike
        # the QRenderWindowInteractor.

    # ###### Public protocol ##############

    def handle_vtk_event(self, obj_name, vtk_event, data):
        if vtk_event == 'RenderEvent':
            if not self._is_resizing:
                self.on_render(data)
        elif vtk_event == 'CursorChangedEvent':
            self.on_cursor_changed(data)

    def send(self, method, *args):
        self.scene_proxy.call_rwi(*((method, ) + args))

    def show_image(self, data, format='PNG'):
        pass

    # #### Private protocol ############

    def _update_image(self):
        data = self.scene_proxy.get_raw_image()
        format = imghdr.what('', h=data)
        self.show_image(data, format=format.upper())

    # ##### VTK Event handling ##########
    def on_render(self, data):
        pass

    def on_cursor_changed(self, data):
        pass

    # ##### Toolkit event handling ##########

    def on_resize(self, w, h):
        if not self._is_resizing:
            self.send('SetSize', w, h)
            self.send('ConfigureEvent')
            self._update_image()

    def on_close(self):
        self.bridge.remove_widget(self.scene_proxy.id, self)

    def on_enter(self, ctrl, shift):
        self.send('SetEventInformationFlipY', self._saveX, self._saveY,
                  ctrl, shift, chr(0), 0, None)
        self.send('EnterEvent')

    def on_leave(self, ctrl, shift):
        self.send('SetEventInformationFlipY', self._saveX, self._saveY,
                  ctrl, shift, chr(0), 0, None)
        self.send('LeaveEvent')

    def on_mouse_press(self, ctrl, shift, x, y, button, repeat=0):
        '''
        ctrl, shift are bools indicating if the modifiers are pressed.
        x, y are screen relative coordinates.
        button is one of 'left', 'right', 'middle' or 'none'
        repeate is for repeat clicks (double click)
        '''
        self.send('SetEventInformationFlipY', x, y,
                  ctrl, shift, chr(0), repeat, None)

        self._ActiveButton = 'left'

        if button == 'left':
            self.send('LeftButtonPressEvent')
        elif button == 'right':
            self.send('RightButtonPressEvent')
        elif button == 'middle':
            self.send('MiddleButtonPressEvent')

    def on_mouse_release(self, ctrl, shift, x, y):
        self.send('SetEventInformationFlipY', x, y,
                  ctrl, shift, chr(0), 0, None)
        button = self._ActiveButton
        if button == 'left':
            self.send('LeftButtonReleaseEvent')
        elif button == 'right':
            self.send('RightButtonReleaseEvent')
        elif button == 'middle':
            self.send('MiddleButtonReleaseEvent')

    def on_mouse_move(self, ctrl, shift, button, x, y):
        self._move_count += 1

        if self._move_count % 3 == 0:
            self._saveModifiers = ctrl, shift
            self._saveButtons = button
            self._saveX = x
            self._saveY = y

            self.send('SetEventInformationFlipY', x, y,
                      ctrl, shift, chr(0), 0, None)
            self.send('MouseMoveEvent')
            self._move_count = 0

    def on_key_press(self, ctrl, shift, key, key_sym):
        """ React to key pressed event.

        """
        self.send('SetEventInformationFlipY', self._saveX, self._saveY,
                  ctrl, shift, key, 0, key_sym)
        self.send('KeyPressEvent')
        self.send('CharEvent')

    def on_key_release(self, ctrl, shift, key):
        self.send('SetEventInformationFlipY', self._saveX, self._saveY,
                  ctrl, shift, key, 0, None)
        self.send('KeyReleaseEvent')

    def on_wheel(self, delta):
        self._wheelDelta += delta

        if self._wheelDelta >= 60:
            self.send('MouseWheelForwardEvent')
            self._wheelDelta = 0
        elif self._wheelDelta <= -60:
            self.send('MouseWheelBackwardEvent')
            self._wheelDelta = 0
