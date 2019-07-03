"""Functionality to display Mayavi scenes inside Jupyter notebooks.
"""
from __future__ import print_function

import base64
from itertools import count

from tvtk.api import tvtk
from tvtk.common import configure_input


_backend = 'ipy'
_width = None
_height = None
_local = True
_widget_manager = None
_counter = count()


def init(backend='ipy', width=None, height=None, local=True):
    """Initialize a suitable backend for Jupyter notebooks.

    **Parameters**

    backend :str: one of ('png', 'x3d', 'ipy')
    width :int: suggested default width of the element
    height :int: suggested default height of the element
    local :bool: Use local copy of x3dom.js instead of online version.
    """
    global _backend, _width, _height, _local, _widget_manager
    backends = ('png', 'x3d', 'ipy')
    error_msg = "Backend must be one of %r, got %s" % (backends, backend)
    assert backend in backends, error_msg
    from mayavi import mlab
    mlab.options.offscreen = True
    _backend = backend
    _width, _height = width, height
    _local = local
    if backend == 'ipy':
        _setup_widget_manager()
    _monkey_patch_for_ipython()
    print("Notebook initialized with %s backend." % backend)


def _setup_widget_manager():
    global _widget_manager
    if _widget_manager is None:
        from mayavi.tools.remote.ipy_remote import WidgetManager
        _widget_manager = WidgetManager()


def _monkey_patch_for_ipython():
    from mayavi.core.base import Base
    from tvtk.pyface.tvtk_scene import TVTKScene
    Base._ipython_display_ = _ipython_display_
    TVTKScene._ipython_display_ = _ipython_display_


def _ipython_display_(self):
    """Method for displaying elements on the Jupyter notebook.
    """
    from IPython.display import HTML
    from IPython.display import display as idisplay

    if hasattr(self, 'render_window'):
        scene = self
    elif hasattr(self, 'scene'):
        scene = self.scene
    if _backend == 'png':
        return idisplay(HTML(scene_to_png(scene)))
    elif _backend == 'x3d':
        return idisplay(HTML(scene_to_x3d(scene)))
    elif _backend == 'ipy':
        return idisplay(scene_to_ipy(scene))


def _fix_x3d_header(x3d):
    id = 'scene_%d' % next(_counter)
    rep = '<X3D profile="Immersive" version="3.0" id="%s" ' % id
    if _width is not None:
        rep += 'width="%dpx" ' % _width
    if _height is not None:
        rep += 'height="%dpx" ' % _height
    rep += '>'
    if isinstance(x3d, bytes):
        x3d = x3d.decode("utf-8", "ignore") 
    x3d = x3d.replace(
        '<X3D profile="Immersive" version="3.0">',
        rep
    )
    return x3d


def scene_to_x3d(scene):
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
    if _local:
        url_base = "nbextensions/mayavi/x3d"
    else:
        url_base = "https://www.x3dom.org/download/1.7.2"
    x3d_elem = _fix_x3d_header(ex.output_string)
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


def scene_to_png(scene):
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


def scene_to_ipy(scene):
    return _widget_manager.scene_to_ipy(scene)


def display(obj, backend=None):
    """Display given object on Jupyter notebook using given backend.

    This is largely for testing.
    """
    global _backend
    backend = _backend if backend is None else backend
    if backend == 'ipy':
        _setup_widget_manager()
    orig_backend = _backend
    _backend = backend
    result = _ipython_display_(obj)
    _backend = orig_backend
    return result
