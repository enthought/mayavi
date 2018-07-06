"""
mlab: a simple scripting interface to Mayavi2 for 3D plotting.

Can be used inside Mayavi2 itself, in "ipython --gui=qt", or in any
application with a compatible UI (Qt or wxPython).
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
#         Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2007-2018, Enthought, Inc.
# License: BSD Style.


# Mayavi imports
from mayavi.core.common import process_ui_events
from mayavi.tools.camera import view, roll, yaw, pitch, move
from mayavi.tools.figure import figure, clf, gcf, savefig, \
    draw, sync_camera, close, screenshot
from mayavi.tools.engine_manager import get_engine, show_pipeline, \
        options, set_engine
from mayavi.tools.show import show
from mayavi.tools.animator import animate


def show_engine():
    """This function is deprecated, please use show_pipeline.
    """
    import warnings
    warnings.warn('The show_engine function is deprecated, please use'
                  'show_pipeline', stacklevel=2)
    return show_pipeline()


from .tools.helper_functions import contour3d, test_contour3d, \
    quiver3d, test_quiver3d, test_quiver3d_2d_data, \
    points3d, test_points3d, test_molecule, \
    volume_slice, test_volume_slice, \
    flow, test_flow, \
    imshow, test_imshow, \
    surf, test_surf, mesh, test_mesh, test_simple_surf, \
    test_mesh_sphere, test_fancy_mesh,\
    contour_surf, test_contour_surf, \
    plot3d, test_plot3d, \
    test_plot3d_anim, test_points3d_anim, test_contour3d_anim,\
    test_simple_surf_anim, test_flow_anim, test_mesh_sphere_anim, \
    test_volume_slice_anim, \
    triangular_mesh, test_triangular_mesh, barchart, \
    test_barchart, test_mesh_mask_custom_colors


from .tools.decorations import colorbar, scalarbar, vectorbar, \
    outline, axes, xlabel, ylabel, zlabel, text, title, \
    orientation_axes, text3d

from .tools import pipeline

from .tools.tools import start_recording, stop_recording

from .tools.notebook import init as init_notebook

if __name__ == "__main__":
    import numpy as np

    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2*np.pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = np.cos(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
    y = np.sin(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
    z = np.sin(n_long*mu/n_mer)*0.5

    pl = plot3d(x, y, z, np.sin(mu), tube_radius=0.05, colormap='Spectral')

    colorbar(orientation='vertical')

    t = np.linspace(0, 4*np.pi, 100)
    x = np.sin(2*t)
    y = np.cos(t)
    z = np.sin(2*t)
    s = np.sin(t)

    pts = points3d(x, y, z, s, colormap="YlGnBu", scale_factor=0.1,
                   extent=(-0.3, 0.3, -0.3, 0.3, -0.2, 0.2))

    axes(xlabel='X', ylabel='Y', zlabel='Z')
    outline(pl)

    title('Mayavi rocks', height=0.85)
