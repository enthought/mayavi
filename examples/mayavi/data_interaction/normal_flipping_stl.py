"""
This example shows how to read a stl file and flip it's normals.
"""

import sys
from tvtk.api import tvtk
from tvtk.common import configure_input
import numpy as np
from mayavi import mlab


def flip_normals(stl_fname):
    # reading the stl file and getting the triangle data
    reader = tvtk.STLReader()
    reader.file_name = stl_fname
    reader.update()

    ordering = []
    polydata = reader.output
    points = polydata.points.to_array()
    x, y, z = points.T

    data = polydata.polys.to_array()
    data.shape = data.size//4,4
    ordering = np.delete(data, 0, 1)

    # getting normal data of the stl file
    normals = tvtk.PolyDataNormals()
    configure_input(normals, polydata)
    normals.compute_point_normals = 0
    normals.compute_cell_normals = 1
    normals.update()
    polydata_normals = normals.output

    u, v, w = polydata_normals.cell_data.normals.to_array().T
    fig = mlab.figure(bgcolor=(0, 0, 0))

    # renders the given stl file
    triangles = mlab.triangular_mesh(
        x, y, z, ordering, figure=fig, opacity=0.6
            )

    # coordinates of centroids of the trianlges
    centroids = np.sum(points[ordering], axis =1)/3
    centroids_x, centroids_y, centroids_z = centroids.T

    # renders normals at centroids
    normals = mlab.quiver3d(centroids_x, centroids_y, centroids_z,
                            u, v, w, figure=fig)
    centroids = mlab.points3d(centroids_x, centroids_y, centroids_z,
                              color=(0.2, 0.6, 0.1), resolution=15)

    outline = mlab.outline(line_width=3)
    outline.outline_mode = "cornered"
    outline_size= centroids.glyph.glyph_source.glyph_source.radius * 0.3
    outline.bounds = (centroids_x[0]-outline_size, centroids_x[0]+outline_size,
                      centroids_y[0]-outline_size, centroids_y[0]+outline_size,
                      centroids_z[0]-outline_size, centroids_z[0]+outline_size)

    ###########################################################################

    # refer to examples/mayavi/data_interaction/select_red_balls.py for
    # detailed information on using the callback
    glyph_normals = centroids.glyph.glyph_source.glyph_source.output.points.\
        to_array()


    def picker_callback(picker):
        if picker.actor in centroids.actor.actors:
            centroid_id = picker.point_id//glyph_normals.shape[0]
            if centroid_id != -1:
                x, y, z = centroids_x[centroid_id], centroids_y[centroid_id], \
                    centroids_z[centroid_id]
                u[centroid_id], v[centroid_id], w[centroid_id] = \
                    -1*u[centroid_id], -1*v[centroid_id], -1*w[centroid_id]
                normals.mlab_source.set(u=u, v=v, w=w)
                outline.bounds = (x-outline_size, x+outline_size,
                                  y-outline_size, y+outline_size,
                                  z-outline_size, z+outline_size)

    picker = fig.on_mouse_pick(picker_callback)
    picker.tolerance = 0.01
    mlab.title("Click on centroid to invert normal", color=(1, 1, 1), figure=fig)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        stl_fname = "../data/cube.stl"
    else:
        stl_fname = sys.argv[1]
    flip_normals(stl_fname)
    mlab.show()
