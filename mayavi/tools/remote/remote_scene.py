import base64
from collections import namedtuple
import time

from traits.api import (Any, Bool, Dict, Enum, Event, HasTraits,
                        Instance, Int, List, Callable)
import vtk

from tvtk.api import tvtk
from ..figure import figure, gcf
from ..engine_manager import options
from tvtk.tvtk_base import global_disable_update

options.offscreen = True

EventInfo = namedtuple('EventInfo', ['id', 'name', 'event', 'data'])


if hasattr(vtk, 'vtkOSOpenGLRenderWindow'):
    # Needed for VTK's vtkglew to be able to load the OSMesa.so. See:
    # https://www.vtk.org/pipermail/vtk-developers/2017-November/035592.html
    import ctypes
    osm = ctypes.CDLL("libOSMesa.so", ctypes.RTLD_GLOBAL)


class ImageEncoder(HasTraits):
    scene = Any
    w2if = Instance(tvtk.WindowToImageFilter)
    writer = Instance(tvtk.ImageWriter)
    image_type = Enum('png', 'jpeg')
    quality = Int(60)
    compress = Bool(False)

    _png_writer = Instance(tvtk.ImageWriter)
    _jpg_writer = Instance(tvtk.ImageWriter)

    # ---- Public protocol -------
    def get_raw_image(self):
        '''Returns the raw bytes of the image.
        '''
        self.w2if.modified()
        w = self.writer
        w.update()
        w.write()
        return w.result.to_array().tostring()

    # ---- Private protocol -------
    def _w2if_default(self):
        w2if = tvtk.WindowToImageFilter()
        if self.scene is not None:
            w2if.input = self.scene.render_window
        return w2if

    def _writer_default(self):
        return self._get_writer(self.image_type)

    def _get_writer(self, image_type):
        if image_type == 'png':
            writer = self._png_writer
        else:
            writer = self._jpg_writer
        writer.set_input_connection(self.w2if.output_port)
        return writer

    def __png_writer_default(self):
        return tvtk.PNGWriter(write_to_memory=True)

    def __jpg_writer_default(self):
        return tvtk.JPEGWriter(quality=self.quality, write_to_memory=True)

    def _quality_changed(self, value):
        self._jpg_writer.quality = value

    def _image_type_changed(self, value):
        if self.writer is not None:
            self.writer.set_input_connection(None)
        self.writer = self._get_writer(value)

    def _scene_changed(self, value):
        self.w2if.input = value.render_window

    def _compress_changed(self, value):
        if value:
            self.image_type = 'jpeg'
        else:
            self.image_type = 'png'


class RemoteScene(HasTraits):

    #: Any events for clients to listen to. Only a subset of events are emitted
    # currently, the event is an `EventInfo` instance.
    event = Event

    #: Set a callback function with signature `f(secs, callable, *args, **kw)`.
    # The function should call the passed `callable` function with the given
    # args and kwargs after the specified time in seconds.
    call_later = Callable

    #: The image encoder which converts the scene to a suitable image.
    image_encoder = Instance(ImageEncoder)

    def __init__(self, figure=None, **traits):
        super(RemoteScene, self).__init__(**traits)
        if figure is None:
            figure = gcf()
        self.figure = figure
        self.scene = figure.scene
        self.trw = self.scene.render_window
        self.trwi = self.scene.interactor
        self.rwi = tvtk.to_vtk(self.trwi)
        self.rw = tvtk.to_vtk(self.trw)
        self.ren = tvtk.to_vtk(self.scene.renderer)
        self.id = id(self)
        self._last_image = ''
        self._last_render = 0
        self._time_to_render = 0
        self._time_for_image = 0
        self._render_size = 200*200
        self._pending_render = False
        self._doing_render = False
        self._timer_enabled = True
        self._setup_scene()

    # ## Public protocol ####
    def get_raw_image(self):
        # This flag is set to prevent render events from being generated
        # while generating the image (which does happen!).
        self._doing_render = True
        data = self.image_encoder.get_raw_image()
        self._doing_render = False
        return data

    def get_image(self):
        data = self.get_raw_image()
        return base64.encodebytes(data).decode('ascii')

    def call_rwi(self, method, *args):
        if method == 'SetSize':
            # This is an issue with the way TVTK is setup and how VTK resizes
            # an offscreen window. It basically releases all graphics resources
            # and this job is passed on to the various mappers. When the mapper
            # does this it emits a ModifiedEvent which is picked by TVTK to
            # fire a render. This call to render when the window is resizing
            # locks up VTK or entirely messes up the rendering. I've reported
            # this upstream but it turns out that disabling the auto updates in
            # TVTK maybe of general use so we have a convenient context manager
            # to do this called `global_disable_update` that shuts off the
            # automatic updates for ALL TVTK objects for a brief while. This
            # fixes the issue.
            with global_disable_update():
                self.trw.size = args
                self.trw.render()

        if 'PressEvent' in method:
            self.image_encoder.compress = True
        if 'ReleaseEvent' in method:
            self.image_encoder.compress = False

        getattr(self.rwi, method)(*args)

    # ## Private protocol ####

    def _send_pending_render(self):
        if self._pending_render:
            self._send_render_event()

    def _emit_event(self, obj, evt):
        self.event = EventInfo(self.id, obj.GetClassName(), evt, None)

    def _required_time_to_render(self):
        return (self._time_for_image + self._time_to_render +
                self._render_size/1e6)

    def _ok_to_send_render_event(self):
        required_time = self._required_time_to_render()
        return (time.time() - self._last_render) > required_time

    def _on_create_timer(self, obj, evt):
        self._timer_enabled = True
        self.call_later(0.05, self._on_timer_event)

    def _on_destroy_timer(self, obj, evt):
        self._timer_enabled = False

    def _on_timer_event(self):
        if self._timer_enabled:
            self.rwi.TimerEvent()

    @vtk.calldata_type(vtk.VTK_INT)
    def _on_cursor_changed_event(self, obj, evt, calldata):
        self.event = EventInfo(self.id, obj.GetClassName(), evt, calldata)

    def _on_render_event(self, obj, event):
        if self._doing_render:
            return

        if self._ok_to_send_render_event():
            self._send_render_event()
        else:
            if not self._pending_render and self.call_later:
                req_time = self._required_time_to_render()
                # print("Required time:", req_time)
                self.call_later(min(req_time, 0.25), self._send_pending_render)
            self._pending_render = True

    def _send_render_event(self):
        self._pending_render = False
        event = 'RenderEvent'
        start = time.time()
        img = self.get_image()
        self._render_size = len(img)
        # print(self._render_size)
        self._last_render = time.time()
        self._time_for_image = self._last_render - start
        self._time_to_render = self.ren.GetLastRenderTimeInSeconds()
        # print("Time to render:", self._time_to_render)
        if img != self._last_image:
            self._last_image = img
            format = self.image_encoder.image_type.upper()
            data = dict(data=img, type='image', format=format,
                        time=self._time_for_image,
                        render_time=self._time_to_render)
            self.event = EventInfo(
                self.id, self.rw.GetClassName(), event, data
            )

    def _setup_scene(self):
        self.trwi.interactor_style.set_current_style_to_trackball_camera()
        self.rwi.AddObserver('CreateTimerEvent', self._on_create_timer)
        self.rwi.AddObserver('DestroyTimerEvent', self._on_destroy_timer)
        rw = self.rw
        rw.AddObserver('RenderEvent', self._on_render_event)
        rw.AddObserver('CursorChangedEvent', self._on_cursor_changed_event)

    def _image_encoder_default(self):
        return ImageEncoder(scene=self.scene, quality=60)


class SceneManager(HasTraits):

    scenes = Dict

    figure_to_id = Dict

    clients = List

    #: Set a callback function with signature `f(secs, callable, *args, **kw)`.
    # The function should call the passed `callable` function with the given
    # args and kwargs after the specified time in seconds.
    call_later = Callable

    def add_client(self, client):
        '''All the client needs to do is to provide a method called
        `handle_event` which is given the event data from the scenes
        and route that to the appropriate recipient.

        The event data is basically an `EventInfo` instance.
        '''
        self.clients.append(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def register_figure(self, figure):
        '''Given an existing figure, set it up for remote visualization.
        '''
        remote = RemoteScene(figure=figure)
        r_id = id(remote)
        self.figure_to_id[figure] = r_id
        self.scenes[r_id] = remote
        self._setup_events(remote)
        if self.call_later:
            remote.call_later = self.call_later
        return r_id

    def figure(self, *args, **kw):
        '''Create a figure and manage it as a remote figure. Any args
        and kwargs are passed on to the `mlab.figure` function.

        '''
        f = figure(*args, **kw)
        return self.register_figure(f)

    def message(self, obj_id, method_name, *args, **kw):
        '''Call a method with given args but do not return any responses.

        This is meant to be used for passing messages to the scenes.
        '''
        self.call(obj_id, method_name, *args, **kw)

    def call(self, obj_id, method_name, *args, **kw):
        '''Call a method and also return the response of the method.

        Used for synchronous calls to the scenes.
        '''
        scene = self.scenes[obj_id]
        method = getattr(scene, method_name)
        return method(*args, **kw)

    # ## Private protocol ####

    def _setup_events(self, obj):
        obj.on_trait_change(self._forward_event, 'event')

    def _forward_event(self, event):
        # Override this to change the default if needed.
        for client in self.clients:
            client.handle_event(event)

    def _call_later_changed(self, f):
        for scene in self.scenes.values():
            scene.call_later = f
