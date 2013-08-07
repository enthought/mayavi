#from enthought.mayavi import mlab
import numpy as np
#from scipy.special import sph_harm

def fexp(x,p):
    """a different kind of exponentiation"""
    return (np.sign(x)*(np.abs(x)**p))

def tens_fld(A,B,C,P,Q):
    """this module plots superquadratic surfaces with the given parameters"""
   # mlab.figure(fgcolor=(1,1,1), bgcolor=(0,0,0))
    phi, theta = np.mgrid[0:np.pi:80j, 0:2*np.pi:80j]
    x       =A*(fexp(np.sin(phi),P)) *(fexp(np.cos(theta),Q))
    y       =B*(fexp(np.sin(phi),P)) *(fexp(np.sin(theta),Q))
    z       =C*(fexp(np.cos(phi),P))
    #s       = sph_harm(1, 1, theta, phi).real
    return x , y , z 
    #mlab.mesh(x, y, z, colormap='copper')

    #mlab.show()

from enthought.traits.api import HasTraits, Range, Instance, \
                    on_trait_change
from enthought.traits.ui.api import View, Item, HGroup
from enthought.tvtk.pyface.scene_editor import SceneEditor
from enthought.mayavi.tools.mlab_scene_model import \
                    MlabSceneModel
from enthought.mayavi.core.ui.mayavi_scene import MayaviScene


class Visualization(HasTraits):
    alpha = Range(0.0, 4.0,  1.0/4)
    beta  = Range(0.0, 4.0,  1.0/4)
    scene      = Instance(MlabSceneModel, ())

    def __init__(self):
        # Do not forget to call the parent's __init__
        HasTraits.__init__(self)
        x, y, z, = tens_fld(1,1,1,self.beta, self.alpha)
        self.plot = self.scene.mlab.mesh(x, y, z, colormap='copper', representation='surface')

    @on_trait_change('beta,alpha')
    def update_plot(self):
        x, y, z, = tens_fld(1,1,1,self.beta, self.alpha)
        self.plot.mlab_source.set(x=x, y=y, z=z)


    # the layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                    height=750, width=750, show_label=False),
                HGroup(
                        '_', 'beta', 'alpha',
                    ),
                )

visualization = Visualization()
visualization.configure_traits()


