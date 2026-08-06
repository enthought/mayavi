"""
This example shows to embed a Mayavi view in a wx frame.

The trick is to create a `HasTraits` object, as in the
mlab_traits_ui.py, mayavi_traits_ui.py, or the modifying_mlab_source.py
examples (:ref:`example_mlab_traits_ui`, :ref:`example_mayavi_traits_ui`,
:ref:`example_mlab_interactive_dialog`).

Calling the `edit_traits` method returns a `ui` object whose
`control` attribute is the wx widget. It can thus be embedded in a
standard wx application.

In this example, the wx part is very simple. See
:ref:`example_wx_mayavi_embed_in_notebook` for an example of more complex
embedding of Mayavi scenes in Wx applications.
"""

# The toolkit is a per-process choice, and pyface prefers Qt when both are
# installed, so a wx application has to claim it before anything reads it.
from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'wx'

from numpy import ogrid, sin

from traits.api import HasTraits, Instance
from traitsui.api import View, Item

from mayavi.sources.api import ArraySource
from mayavi.modules.api import IsoSurface

from mayavi.core.ui.api import SceneEditor, MlabSceneModel


class MayaviView(HasTraits):

    scene = Instance(MlabSceneModel, ())

    # The layout of the panel created by Traits
    view = View(Item('scene', editor=SceneEditor(), resizable=True,
                    show_label=False),
                    resizable=True)

    def __init__(self):
        HasTraits.__init__(self)
        # Create some data, and plot it using the embedded scene's engine
        x, y, z = ogrid[-10:10:100j, -10:10:100j, -10:10:100j]
        scalars = sin(x*y*z)/(x*y*z)
        src = ArraySource(scalar_data=scalars)
        self.scene.engine.add_source(src)
        src.add_module(IsoSurface())

#-----------------------------------------------------------------------------
# Wx Code
import wx


def pop_event_handlers(window):
    """ Undo the event handlers TraitsUI pushed onto a window tree.
    """
    while window.GetEventHandler() is not window:
        window.PopEventHandler(True)
    for child in window.GetChildren():
        pop_event_handlers(child)


class MainWindow(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Mayavi in Wx')
        self.mayavi_view = MayaviView()
        # Use traits to create a panel, and use it as the content of this
        # wx frame.
        self.control = self.mayavi_view.edit_traits(
                        parent=self,
                        kind='subpanel').control
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)

    def on_close(self, event):
        # TraitsUI pushes wx event handlers onto the panel and its children and
        # pops them only in ui.dispose(), which wx never gets to call on a
        # frame that is simply closed; wx asserts on destroying a window that
        # still has one.  Popping them by hand is enough -- disposing here
        # instead schedules a second Destroy through wx.CallAfter and crashes.
        pop_event_handlers(self.control)
        event.Skip()

app = wx.App(False)
frame = MainWindow(None, wx.ID_ANY)
app.MainLoop()

