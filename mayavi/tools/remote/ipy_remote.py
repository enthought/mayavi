import base64
from IPython.display import display
from ipywidgets import Image
from ipyevents import Event

from .bridge import LocalBridge
from .remote_scene import SceneManager
from .remote_widget import RemoteWidget
from ..figure import gcf

decode_func = getattr(base64, 'decodebytes', getattr(base64, 'decodestring'))


def base64_to_bytes(str_or_bytes):
    data = str_or_bytes.encode('ascii')
    return decode_func(data)


class IPyRemoteWidget(RemoteWidget):
    def __init__(self, scene_proxy, bridge, *args, **kw):
        super(IPyRemoteWidget, self).__init__(scene_proxy, bridge, *args, **kw)
        self.image = Image(format='PNG')
        self.event = Event(
            source=self.image,
            watched_events=[
                'dragstart', 'mouseenter', 'mouseleave',
                'mousedown', 'mouseup', 'mousemove', 'wheel',
                'keyup', 'keydown'
            ],
            prevent_default_action=True
        )
        self.event.on_dom_event(self.handle_ipyevent)
        self._update_image()

    def _ipython_display_(self):
        display(self.image)

    # ###### Public protocol ##############

    def show(self):
        pass

    def show_image(self, data, format='PNG'):
        self.image.format = format
        self.image.value = data

    # ##### VTK Event handling ##########
    def on_render(self, data):
        self.show_image(base64_to_bytes(data['data']),
                        format=data.get('format', 'PNG'))

    def on_cursor_changed(self, data):
        # self.setCursor(cursor)
        pass

    def handle_ipyevent(self, event):
        type = event['type']
        shift = event.get('shiftKey', False)
        ctrl = event.get('ctrlKey', False)
        btn_map = {0: 'left', 1: 'right', 2: 'middle'}
        if type == 'mouseenter':
            self.on_enter(ctrl, shift)
        elif type == 'mouseleave':
            self.on_leave(ctrl, shift)
        elif type == 'mouseleave':
            self.on_leave(ctrl, shift)
        elif type == 'mousedown':
            repeat = 0
            button = btn_map.get(event.get('button'), 'none')
            x, y = event.get('relativeX'), event.get('relativeY')
            self.on_mouse_press(ctrl, shift, x, y, button, repeat)
        elif type == 'mouseup':
            x, y = event.get('relativeX'), event.get('relativeY')
            self.on_mouse_release(ctrl, shift, x, y)
        elif type == 'mousemove':
            button = btn_map.get(event.get('button'), 'none')
            x, y = event.get('relativeX'), event.get('relativeY')
            self.on_mouse_move(ctrl, shift, button, x, y)
        elif type == 'wheel':
            dx = event.get('deltaX')
            dy = event.get('deltaY')
            dz = event.get('deltaZ')
            delta = dx + dy + dz
            self.on_wheel(delta)
        elif type == 'keydown':
            key = event.get('key')
            # Need to map the special keys correctly.
            key_sym = key
            self.on_key_press(ctrl, shift, key, key_sym)
        elif type == 'keyup':
            key = event.get('key')
            # Need to map the special keys correctly.
            key_sym = key
            self.on_key_release(ctrl, shift, key)


class WidgetManager(object):
    def __init__(self):
        self.sm = SceneManager()
        # FIXME: we need a way to set the SceneManager.call_later.
        # not sure what sort of event loop we can rely on with IPython.
        self.bridge = LocalBridge(self.sm)
        self.bridge.run()
        self.widgets = {}

    def scene_to_ipy(self, scene):
        figure = gcf()
        sm = self.sm
        sid = sm.figure_to_id.get(figure)
        if sid is None:
            sid = sm.register_figure(figure)
        if sid in self.widgets:
            return self.widgets[sid]
        else:
            scene = sm.scenes[sid]
            w = IPyRemoteWidget(scene, self.bridge)
            self.widgets[sid] = w
            return w
