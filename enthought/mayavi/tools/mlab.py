"""
Refactoring of mlab. The problem with mlab is that adding keyword to the
functions constructing the modules and data object ends up in a lot of
code duplication. This is an attempt to provide an OOP way to build
mlab's function. This is work in progress and the class structure and
class API is meant to change. Suggestions welcomed.

This module provides the api and should be imported for interactive work.

Submodules
-----------

:tools: Contains all the functions to control the figure and the
    pipeline, as well as the colorbar. Thos sub module should not import
    symbols from any other.

:modules: Contains functional wrappers to mayabi modules. They all take
    one positional argument, the object to wich the module applies, and
    should have the same name as module in the visualize->modules menu,
    but all lower case, with not underscores. These functions should
    return the create module.

:sources: Contains functional wrappers to mayavi and tvtk sources to
    build data sources from a various number of arrays. These functions
    should not build anything other than one data source, and return it.

:helper_functions: Contains functions using both data_sources and modules
    to create a full visualization from arrays. These should not create
    axes, labels, etc... as the user may want to create only one set of
    axes for different visualizations. Each helper function should have
    at least one test function assiocated with it, use both for testing,
    and for illustrating its use.

:pipeline: convenience module to give a namespace for pipeline
    manipulation functions: TVTK sources and modules.

We are trying not to depend on scipy, but only on numpy. So far it has
worked out.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net> 
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

from camera import view, roll
from figure import figure, clf, gcf, savefig, draw
from enthought.mayavi.config.config import options 
from config import get_engine, show_engine

#from modules import isosurface, vectors, glyph, text, streamline
#from data_sources import scalarfield, scalarscatter, vectorscatter, \
#    vectorfield
from helper_functions import contour3d, test_contour3d, \
    quiver3d, test_quiver3d, test_quiver3d_2d_data, \
    points3d, test_points3d, test_molecule, \
    flow, test_flow, \
    imshow, test_imshow, \
    surf, test_surf, mesh, test_mesh, test_simple_surf, \
    test_mesh_sphere, test_fancy_mesh,\
    contour_surf, test_contour_surf, \
    plot3d, test_plot3d 
from decorations import colorbar, scalarbar, vectorbar, \
    outline, axes, xlabel, ylabel, zlabel, title

import pipeline

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

