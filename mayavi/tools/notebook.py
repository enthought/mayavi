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


def _ipython_display_(self):
    '''Method attached to Mayavi objects.

    Note that here `self` is the Mayavi object that is going to be
    visualized. This method is used by IPython to display objects on a
    notebook, see here:
    https://ipython.readthedocs.io/en/stable/config/integrating.html#custom-methods

    '''
    return _backend.display(self)


def init(backend='ipy', width=None, height=None, local=True):
    """Initialize a suitable backend for Jupyter notebooks.

    **Parameters**

    backend :str: one of ('itk', 'ipy', 'x3d', 'png')
    width :int: suggested default width of the element
    height :int: suggested default height of the element
    local :bool: Use local copy of x3dom.js instead of online version.
    """
    from mayavi.core.base import Base
    from tvtk.pyface.tvtk_scene import TVTKScene
    global _backend, _registry

    backends = _registry.keys()
    error_msg = "Backend must be one of %r, got %s" % (backends, backend)
    assert backend in backends, error_msg
    from mayavi import mlab
    mlab.options.offscreen = True
    _backend = _registry[backend](width, height, local)
    Base._ipython_display_ = _ipython_display_
    TVTKScene._ipython_display_ = _ipython_display_
    print("Notebook initialized with %s backend." % backend)


class JupyterBackend(object):

    def __init__(self, width=None, height=None, local=True):
        self._width = width
        self._height = height
        self._local = local

    def display(self, obj):
        '''Override to display with this backend.

        ``obj`` is a Mayavi object that is going to be visualized.

        '''
        raise NotImplementedError()


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
        # Can also be removed when the PR below is merged and released.
        from itkwidgets import widget_viewer
        if hasattr(widget_viewer, 'have_mayavi'):
            widget_viewer.have_mayavi = False

    def _update_pipeline(self, actors):
        for a in actors:
            m = a.GetMapper()
            if m:
                m.Update()

    def display(self, obj):
        from IPython.display import display as idisplay
        scene = get_scene(obj)
        if scene is not None:
            actors = get_all_actors(scene)
            self._update_pipeline(actors)
            # Works around bug in released itkwidgets-0.32.1.
            # Can remove when this PR is merged and in a release:
            # https://github.com/InsightSoftwareConsortium/itkwidgets/pull/438
            kw = dict(
                actors=actors, geometries=[], geometry_colors=[],
                geometry_opacities=[], point_sets=[], point_set_colors=[],
                point_set_opacities=[]
            )
            return idisplay(self._view(**kw))
        else:
            return obj


class IPyBackend(JupyterBackend):
    _widget_manager = None

    def __init__(self, width=None, height=None, local=True):
        super().__init__(width, height, local)

        if self.__class__._widget_manager is None:
            # This is a singleton, no need to create multiple of these.
            from mayavi.tools.remote.ipy_remote import WidgetManager
            self.__class__._widget_manager = WidgetManager()

    def display(self, obj):
        from IPython.display import display as idisplay

        if hasattr(obj, 'render_window'):
            scene = obj
        elif hasattr(obj, 'scene'):
            scene = obj.scene

        return idisplay(self._widget_manager.scene_to_ipy(scene))


class PNGBackend(JupyterBackend):

    def display(self, obj):
        from IPython.display import HTML
        from IPython.display import display as idisplay

        if hasattr(obj, 'render_window'):
            scene = obj
        elif hasattr(obj, 'scene'):
            scene = obj.scene

        return idisplay(HTML(self.scene_to_png(scene)))

    def scene_to_png(self, scene):
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


class X3DBackend(JupyterBackend):

    def display(self, obj):
        from IPython.display import HTML
        from IPython.display import display as idisplay
        if hasattr(obj, 'render_window'):
            scene = obj
        elif hasattr(obj, 'scene'):
            scene = obj.scene

        return idisplay(HTML(self.scene_to_x3d(scene)))

    def _fix_x3d_header(self, x3d):
        id = 'scene_%d' % next(_counter)
        rep = '<X3D profile="Immersive" version="3.0" id="%s" ' % id
        if self._width is not None:
            rep += 'width="%dpx" ' % self._width
        if self._height is not None:
            rep += 'height="%dpx" ' % self._height
        rep += '>'
        if isinstance(x3d, bytes):
            x3d = x3d.decode("utf-8", "ignore")
        x3d = x3d.replace(
            '<X3D profile="Immersive" version="3.0">',
            rep
        )
        return x3d

    def scene_to_x3d(self, scene):
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
        if self._local:
            url_base = "nbextensions/mayavi/x3d"
        else:
            url_base = "https://www.x3dom.org/download/1.7.2"
        x3d_elem = self._fix_x3d_header(ex.output_string)
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


register_backend('itk', ITKBackend)
register_backend('ipy', IPyBackend)
register_backend('x3d', X3DBackend)
register_backend('png', PNGBackend)
