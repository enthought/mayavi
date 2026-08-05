"""
This example show how to embedded Mayavi in a wx notebook.

This is a slightly more complex example than the `wx_embedding` example (
:ref:`example_wx_embedding`), and can be used to see how a large wx
application can use different Mayavi views.

In this example, we embed one single Mayavi scene in a Wx notebook, with
2 tabs, each one of them hosting a different view of the scene.
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

from mayavi.core.ui.api import MlabSceneModel, SceneEditor

#-------------------------------------------------------------------------------
class MayaviView(HasTraits):

    scene = Instance(MlabSceneModel, ())

    # The layout of the panel created by traits.
    view = View(Item('scene', editor=SceneEditor(),
                    resizable=True,
                    show_label=False),
                resizable=True)

    def __init__(self):
        HasTraits.__init__(self)
        x, y, z = ogrid[-10:10:100j, -10:10:100j, -10:10:100j]
        scalars = sin(x*y*z)/(x*y*z)
        src = ArraySource(scalar_data=scalars)
        self.scene.mayavi_scene.add_child(src)
        src.add_module(IsoSurface())


#-------------------------------------------------------------------------------
# Wx Code
import wx
import wx.aui


def pop_event_handlers(window):
    """ Undo the event handlers TraitsUI pushed onto a window tree.
    """
    while window.GetEventHandler() is not window:
        window.PopEventHandler(True)
    for child in window.GetChildren():
        pop_event_handlers(child)


class MainWindow(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Mayavi in a Wx notebook')
        self.notebook = wx.aui.AuiNotebook(self, id=-1,
                style=wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_CLOSE_ON_ALL_TABS
                        | wx.aui.AUI_NB_LEFT)

        self.mayavi_view = MayaviView()

        # The edit_traits method opens a first view of our 'MayaviView'
        # object.  A notebook page has to be a child of the notebook itself,
        # not of the frame -- unlike a Qt layout, wx containers do not adopt
        # what you put in them.
        self.control = self.mayavi_view.edit_traits(
                        parent=self.notebook,
                        kind='subpanel').control
        self.notebook.AddPage(page=self.control, caption='Display 1')

        self.mayavi_view2 = MayaviView()

        # The second call to edit_traits opens a second view
        self.control2 = self.mayavi_view2.edit_traits(
                        parent=self.notebook,
                        kind='subpanel').control
        self.notebook.AddPage(page=self.control2, caption='Display 2')

        sizer = wx.BoxSizer()
        sizer.Add(self.notebook,1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)

    def on_close(self, event):
        # TraitsUI pushes wx event handlers onto each panel and its children and
        # pops them only in ui.dispose(), which wx never gets to call on a frame
        # that is simply closed; wx asserts on destroying a window that still
        # has one.  Popping them by hand is enough -- disposing here instead
        # schedules a second Destroy through wx.CallAfter, and the notebook then
        # crashes walking pages that are already gone.
        # only the TraitsUI panels: the notebook pushes handlers of its own,
        # and popping those aborts the interpreter on close
        pop_event_handlers(self.control)
        pop_event_handlers(self.control2)
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, wx.ID_ANY)
    app.MainLoop()
