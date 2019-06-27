"""
This example shows how to read a stl file and flip it's normals.
"""

import sys
from tvtk.api import tvtk
from tvtk.common import configure_input
import numpy as np
from mayavi import mlab
import tempfile

cube_stl = """solid cube
    facet normal 0 0 1
        outer loop
        vertex 0 0 0
        vertex 0 1 0
        vertex 1 1 0
        endloop
    endfacet
    facet normal 0 0 1
        outer loop
        vertex 0 0 0
        vertex 1 1 0
        vertex 1 0 0
        endloop
    endfacet
    facet normal 1 0 0
        outer loop
        vertex 0 0 0
        vertex 0 0 1
        vertex 0 1 1
        endloop
    endfacet
    facet normal 1 0 0
        outer loop
        vertex 0 0 0
        vertex 0 1 1
        vertex 0 1 0
        endloop
    endfacet
    facet normal 0 1 0
        outer loop
        vertex 0 0 0
        vertex 1 0 0
        vertex 1 0 1
        endloop
    endfacet
    facet normal 0 1 0
        outer loop
        vertex 0 0 0
        vertex 1 0 1
        vertex 0 0 1
        endloop
    endfacet
    facet normal 0 0 1
        outer loop
        vertex 0 0 1
        vertex 1 0 1
        vertex 1 1 1
        endloop
    endfacet
    facet normal 0 0 -1
        outer loop
        vertex 0 0 1
        vertex 1 1 1
        vertex 0 1 1
        endloop
    endfacet
    facet normal -1 0 0
        outer loop
        vertex 1 0 0
        vertex 1 1 0
        vertex 1 1 1
        endloop
    endfacet
    facet normal -1 0 0
        outer loop
        vertex 1 0 0
        vertex 1 1 1
        vertex 1 0 1
        endloop
    endfacet
    facet normal 0 -1 0
        outer loop
        vertex 0 1 0
        vertex 0 1 1
        vertex 1 1 1
        endloop
    endfacet
    facet normal 0 -1 0
        outer loop
        vertex 0 1 0
        vertex 1 1 1
        vertex 1 1 0
        endloop
    endfacet
    endsolid cube"""


f = tempfile.NamedTemporaryFile(mode="w", delete=False)
f.write(cube_stl)
f.close()

def flip_normals(stl_fname):
    # reading the stl file and getting the triangle data
    reader = tvtk.STLReader()
    reader.file_name = stl_fname
    reader.update()

    x, y, z= [], [], []
    ordering = []
    polydata = reader.output
    n = len(polydata.polys.data)
    i = 0
    while(i < n):
        ordering.append([int(polydata.polys.data[i+1]),
                        int(polydata.polys.data[i+2]),
                        int(polydata.polys.data[i+3])])
        i = i + 4

    for i in range(len(polydata.points)):
        x.append(polydata.points[i][0])
        y.append(polydata.points[i][1])
        z.append(polydata.points[i][2])

    # getting normal data of the stl file
    normals = tvtk.PolyDataNormals()
    configure_input(normals, polydata)
    normals.compute_point_normals = 0
    normals.compute_cell_normals = 1
    normals.update()
    polydata_normals = normals.output
    m = len(polydata_normals.cell_data.normals)
    u, v, w = [], [], []
    for i in range(m):
        u.append(int(polydata_normals.cell_data.normals[i][0]))
        v.append(int(polydata_normals.cell_data.normals[i][1]))
        w.append(int(polydata_normals.cell_data.normals[i][2]))
    fig = mlab.figure(bgcolor=(0, 0, 0))

    # renders the given stl file
    triangles = mlab.triangular_mesh(x, y, z, ordering, figure=fig, opacity=0.6)

    # coordinates of centroids of the trianlges
    centroids_x, centroids_y, centroids_z = [], [], []
    for i in range(np.shape(ordering)[0]):
        centroid = (np.array(polydata.points[ordering[i][0]]) +
                    np.array(polydata.points[ordering[i][1]]) +
                    np.array(polydata.points[ordering[i][2]])) / 3

        centroids_x.append(centroid[0])
        centroids_y.append(centroid[1])
        centroids_z.append(centroid[2])

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

    ###############################################################################

    # refer to examples/mayavi/data_interaction/select_red_balls.py for detailed
    # information on using the callback
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
                normals.mlab_source.reset(u=u, v=v, w=w)
                outline.bounds = (x-outline_size, x+outline_size,
                                y-outline_size, y+outline_size,
                                z-outline_size, z+outline_size)

    picker = fig.on_mouse_pick(picker_callback)
    picker.tolerance = 0.01
    mlab.title("Click on centroid to invert normal", color=(1, 1, 1), figure=fig)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        stl_fname = f.name
    else:
        stl_fname = sys.argv[1]
    flip_normals(stl_fname)
