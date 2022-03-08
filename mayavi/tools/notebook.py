"""Functionality to display Mayavi scenes inside Jupyter notebooks.
"""
import base64
from itertools import count

from tvtk.api import tvtk
from tvtk.common import configure_input

from mayavi.core.scene import Scene


_registry = dict()
_backend = None
_counter = count()


def register_backend(name, klass):
    global _registry
    _registry[name] = klass


def init(backend='ipy', width=None, height=None, local=True):
    """Initialize a suitable backend for Jupyter notebooks.

    **Parameters**

    backend :str: one of ('itk', 'ipy', 'x3d', 'png')
    width :int: suggested default width of the element
    height :int: suggested default height of the element
    local :bool: Use local copy of x3dom.js instead of online version.
    """
    global _backend, _registry
    backends = _registry.keys()
    error_msg = "Backend must be one of %r, got %s" % (backends, backend)
    assert backend in backends, error_msg
    from mayavi import mlab
    mlab.options.offscreen = True
    _backend = _registry[backend](width, height, local)
    print("Notebook initialized with %s backend." % backend)


class JupyterBackend(object):
    _width = None
    _height = None
    _local = True

    def __init__(self, width=None, height=None, local=True):
        self._width = width
        self._height = height
        self._local = local
        self._monkey_patch_for_ipython()

    def _monkey_patch_for_ipython(self):
        from mayavi.core.base import Base
        from tvtk.pyface.tvtk_scene import TVTKScene
        Base._ipython_display_ = self.__class__._ipython_display_
        TVTKScene._ipython_display_ = self.__class__._ipython_display_

    def _ipython_display_(self):
        '''Override to display with this backend.

        Note that here `self` is not an instance of JupyterBackend but of the
        Mayavi object that is going to be visualized.

        '''
        pass


def get_scene(obj):
    '''Walks up the object to get to the Scene.
    '''
    while obj is not None:
        if isinstance(obj, Scene):
            return obj
        else:
            obj = obj.parent
    return None


def get_all_actors(obj):
    '''Walks down a given object and finds all the actors.'''

    def _get_actors(x):
        return [tvtk.to_vtk(i) for i in x]

    actors = []
    if hasattr(obj, 'actors'):
        actors.extend(_get_actors(obj.actors))
    if hasattr(obj, 'actor'):
        actors.extend(_get_actors(obj.actor.actors))
    if hasattr(obj, 'children'):
        for x in obj.children:
            actors.extend(get_all_actors(x))
    return actors


class ITKBackend(JupyterBackend):
    _view = None

    def __init__(self, width=None, height=None, local=True):
        super().__init__(width, height, local)
        from mayavi import mlab
        mlab.options.backend = 'test'

        if self.__class__._view is None:
            try:
                from itkwidgets import view
                self.__class__._view = view
                self._workaround_itkwidgets_bug()
            except ImportError:
                print("The itk backend requires itkwidgets to be installed.")

    def _workaround_itkwidgets_bug(self):
        from itkwidgets import widget_viewer
        if hasattr(widget_viewer, 'have_mayavi'):
            widget_viewer.have_mayavi = False

    @classmethod
    def display(klass, obj):
        from IPython.display import display as idisplay
        scene = get_scene(obj)
        if scene is not None:
            actors = get_all_actors(scene)
            return idisplay(klass._view(actors=actors))
        else:
            return obj

    def _ipython_display_(self):
        return ITKBackend.display(self)


class IPyBackend(JupyterBackend):
    _widget_manager = None

    def __init__(self, width=None, height=None, local=True):
        super().__init__(width, height, local)

        if self.__class__._widget_manager is None:
            # This is a singleton, no need to create multiple of these.
            from mayavi.tools.remote.ipy_remote import WidgetManager
            self.__class__._widget_manager = WidgetManager()

    @classmethod
    def display(klass, scene):
        return klass._widget_manager.scene_to_ipy(scene)

    def _ipython_display_(self):
        from IPython.display import display as idisplay
        if hasattr(self, 'render_window'):
            scene = self
        elif hasattr(self, 'scene'):
            scene = self.scene
        return idisplay(IPyBackend.display(scene))


class PNGBackend(JupyterBackend):

    @classmethod
    def display(klass, scene):
        from IPython.display import HTML
        from IPython.display import display as idisplay

        return idisplay(HTML(klass.scene_to_png(scene)))

    @classmethod
    def scene_to_png(klass, scene):
        w2if = tvtk.WindowToImageFilter()
        w2if.input = scene.render_window
        ex = tvtk.PNGWriter()
        ex.write_to_memory = True
        configure_input(ex, w2if)
        ex.update()
        ex.write()
        data = base64.b64encode(ex.result.to_array()).decode('ascii')
        html = '<img src="data:image/png;base64,%s" alt="PNG image"></img>'
        return html % data

    def _ipython_display_(self):
        if hasattr(self, 'render_window'):
            scene = self
        elif hasattr(self, 'scene'):
            scene = self.scene
        return PNGBackend.display(scene)


class X3DBackend(JupyterBackend):

    @classmethod
    def display(klass, scene):
        from IPython.display import HTML
        from IPython.display import display as idisplay

        return idisplay(HTML(klass.scene_to_x3d(scene)))

    @classmethod
    def _fix_x3d_header(klass, x3d):
        id = 'scene_%d' % next(_counter)
        rep = '<X3D profile="Immersive" version="3.0" id="%s" ' % id
        if klass._width is not None:
            rep += 'width="%dpx" ' % klass._width
        if klass._height is not None:
            rep += 'height="%dpx" ' % klass._height
        rep += '>'
        if isinstance(x3d, bytes):
            x3d = x3d.decode("utf-8", "ignore")
        x3d = x3d.replace(
            '<X3D profile="Immersive" version="3.0">',
            rep
        )
        return x3d

    @classmethod
    def scene_to_x3d(klass, scene):
        ex = tvtk.X3DExporter()
        ex.input = scene.render_window
        lm = scene.light_manager.light_mode
        # The default raymond mode is too bright so switch back to vtk mode.
        scene.light_manager.light_mode = 'vtk'
        ex.write_to_output_string = True
        ex.update()
        ex.write()
        # Switch back
        scene.light_manager.light_mode = lm
        if klass._local:
            url_base = "nbextensions/mayavi/x3d"
        else:
            url_base = "https://www.x3dom.org/download/1.7.2"
        x3d_elem = klass._fix_x3d_header(ex.output_string)
        html = '''
        %s
        <script type="text/javascript">
        require(["%s/x3dom"], function(x3dom) {
            var x3dom_css = document.getElementById("x3dom-css");
            if (x3dom_css === null) {
                var l = document.createElement("link");
                l.setAttribute("rel", "stylesheet");
                l.setAttribute("type", "text/css");
                l.setAttribute("href", require.toUrl("%s/x3dom.css"));
                l.setAttribute("id", "x3dom-css");
                $("head").append(l);
            }
            if (typeof x3dom != 'undefined') {
                x3dom.reload();
            }
            else if (typeof window.x3dom != 'undefined') {
                window.x3dom.reload();
            }
        })
        </script>
        ''' % (x3d_elem, url_base, url_base)
        return html

    def _ipython_display_(self):
        if hasattr(self, 'render_window'):
            scene = self
        elif hasattr(self, 'scene'):
            scene = self.scene
        return X3DBackend.display(scene)


register_backend('itk', ITKBackend)
register_backend('ipy', IPyBackend)
register_backend('x3d', X3DBackend)
register_backend('png', PNGBackend)
