"""
mlab: a simple scripting interface to Mayavi2 for 3D plotting.

Can be used inside Mayavi2 itself, in "ipython -wthread", or in any
application with the WxWidget mainloop running.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net> 
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

# Before anything else, check that we have a traits backend installed
from enthought.traits.ui.toolkit import toolkit
toolkit() # This forces the selection of a toolkit.
from enthought.etsconfig.api import ETSConfig
if ETSConfig.toolkit in ('null', ''):
    raise ImportError, '''Could not import backend for traits
________________________________________________________________________________
Make sure that you have either the TraitsBackendWx or the TraitsBackendQt
projects installed.'''

# Mayavi imports
from enthought.mayavi.tools.camera import view, roll
from enthought.mayavi.tools.figure import figure, clf, gcf, savefig, draw
from enthought.mayavi.tools.engine_manager import get_engine, show_pipeline, \
        options, set_engine
from enthought.mayavi.tools.show import show


def show_engine():
    """ This function is depreciated, please use show_pipeline.
    """
    import warnings
    warnings.warn('The show_engine function is depreciated, please use'
                    'show_pipeline', stacklevel=2)
    return show_pipeline()

from tools.helper_functions import contour3d, test_contour3d, \
    quiver3d, test_quiver3d, test_quiver3d_2d_data, \
    points3d, test_points3d, test_molecule, \
    flow, test_flow, \
    imshow, test_imshow, \
    surf, test_surf, mesh, test_mesh, test_simple_surf, \
    test_mesh_sphere, test_fancy_mesh,\
    contour_surf, test_contour_surf, \
    plot3d, test_plot3d 
from tools.decorations import colorbar, scalarbar, vectorbar, \
    outline, axes, xlabel, ylabel, zlabel, text, title, \
    orientationaxes

import tools.pipeline as pipeline

if __name__ == "__main__":
    import numpy

    n_mer, n_long = 6, 11
    pi = numpy.pi
    dphi = pi/1000.0 
    phi = numpy.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = numpy.cos(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    y = numpy.sin(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    z = numpy.sin(n_long*mu/n_mer)*0.5

    pl = plot3d(x, y, z, numpy.sin(mu), tube_radius=0.05, colormap='Spectral')

    colorbar(orientation='vertical')

    t = numpy.linspace(0, 4*numpy.pi, 100)
    cos = numpy.cos
    sin = numpy.sin

    x = sin(2*t)
    y = cos(t)
    z = sin(2*t)
    s = sin(t)

    pts = points3d(x, y, z, s, colormap="YlGnBu", scale_factor=0.1,
            extent=(-0.3,0.3, -0.3, 0.3, -0.2,0.2))

    axes(xlabel='X', ylabel='Y', zlabel='Z')
    outline(pl)

    title('Mayavi rocks', height=0.85)

