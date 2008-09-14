"""
This example show how to embedded Mayavi in a wx notebook. 

This is a slightly more complex example than the wx_embedding.py one, and
can be used to see how a large wx application can use different
Mayavi views.
"""

from numpy import ogrid, sin

from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item

from enthought.mayavi.sources.api import ArraySource
from enthought.mayavi.modules.api import IsoSurface

from enthought.tvtk.pyface.scene_editor import SceneEditor
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel

class MayaviView(HasTraits):

    scene = Instance(MlabSceneModel, ())
    
    view = View(Item('scene', editor=SceneEditor(), resizable=True,
                    show_label=False),
                    resizable=True)

    def __init__(self):
        HasTraits.__init__(self)
        x, y, z = ogrid[-10:10:100j, -10:10:100j, -10:10:100j]
        scalars = sin(x*y*z)/(x*y*z)
        src = ArraySource(scalar_data=scalars)
        self.scene.engine.add_source(src)
        src.add_module(IsoSurface())
#
# Wx Code
import wx

class MainWindow(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Mayavi in a Wx notebook')
        self.notebook = wx.aui.AuiNotebook(self, id=-1, 
                style=wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_CLOSE_ON_ALL_TABS
                        | wx.aui.AUI_NB_LEFT)

        self.mayavi_view = MayaviView()

        self.control = self.mayavi_view.edit_traits(
                        parent=self,
                        kind='subpanel').control
        self.notebook.AddPage(page=self.control, caption='Display 1')
        self.mayavi_view2 = MayaviView()

        self.control2 = self.mayavi_view2.edit_traits(
                        parent=self,
                        kind='subpanel').control
        self.notebook.AddPage(page=self.control2, caption='Display 2')

        sizer = wx.BoxSizer()
        sizer.Add(self.notebook,1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Show(True)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainWindow(None, wx.ID_ANY)
    app.MainLoop()
