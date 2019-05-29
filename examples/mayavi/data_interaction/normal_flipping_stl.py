"""
This example shows how to read a stl file and flip it's normals.

The example stl file can be downloaded from
https://cults3d.com/en/3d-model/various/pyramide-carree

"""

import vtk
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy
from mayavi import mlab

# reading the stl file and getting the triangle data
reader = vtk.vtkSTLReader()
reader.SetFileName("pyramide4.stl")
reader.Update()
my_mesh_vectors = []
polydata = reader.GetOutput()
for i in range(polydata.GetNumberOfCells()):
        pts = polydata.GetCell(i).GetPoints()
        np_pts = np.array([pts.GetPoint(i)
                           for i in range(pts.GetNumberOfPoints())])
        my_mesh_vectors.append(np_pts)

# getting normal data of the stl file
normals = vtk.vtkPPolyDataNormals()
normals.SetInputConnection(reader.GetOutputPort())
normals.ComputeCellNormalsOn()
normals.ComputePointNormalsOff()
normals.ConsistencyOn()
normals.AutoOrientNormalsOn()
normals.Update()
cellNormals = vtk_to_numpy(normals.GetOutput().GetCellData().GetNormals())
my_mesh_normals = cellNormals

fig = mlab.figure(bgcolor=(0, 0, 0))
x, y, z, ordering, points = [], [], [], [], []  # cooridnates of points and
# connectivity information
for i in range(len(my_mesh_vectors)):
    order1, order2, order3 = -1, -1, -1
    for m in range(np.shape(my_mesh_vectors[i])[0]):
        point = [my_mesh_vectors[i][m][0],
                 my_mesh_vectors[i][m][1],
                 my_mesh_vectors[i][m][2]]
        if point in points:
            pass
        else:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])
        if point in points:
            if(m == 0):
                order1 = points.index(point)
            if(m == 1):
                order2 = points.index(point)
            if(m == 2):
                order3 = points.index(point)
        else:
            if(m == 0):
                order1 = len(points)
                points.append(point)
            if(m == 1):
                order2 = len(points)
                points.append(point)
            if(m == 2):
                order3 = len(points)
                points.append(point)
    ordering.append([order1, order2, order3])

# creates the given stl file
triangles = mlab.triangular_mesh(x, y, z, ordering, figure=fig, opacity=0.6)
# coordinates of centroids of the trianlges
centroids_x, centroids_y, centroids_z = [], [], []
for i in range(np.shape(my_mesh_vectors)[0]):
    centroid = (my_mesh_vectors[i][0] +
                my_mesh_vectors[i][1] +
                my_mesh_vectors[i][2]) / 3
    centroids_x.append(centroid[0])
    centroids_y.append(centroid[1])
    centroids_z.append(centroid[2])

u, v, w = [], [], []  # normals to the triangles
for i in range(np.shape(my_mesh_vectors)[0]):
    u.append(my_mesh_normals[i][0])
    v.append(my_mesh_normals[i][1])
    w.append(my_mesh_normals[i][2])

outline = mlab.outline(line_width=3)
outline.outline_mode = "cornered"
outline_size = 0.007
outline.bounds = (centroids_x[0]-outline_size, centroids_x[0]+outline_size,
                  centroids_y[0]-outline_size, centroids_y[0]+outline_size,
                  centroids_z[0]-outline_size, centroids_z[0]+outline_size)

# creates normals at centroids
normals = mlab.quiver3d(centroids_x, centroids_y, centroids_z,
                        u, v, w, figure=fig)
centroids = mlab.points3d(centroids_x, centroids_y, centroids_z,
                          color=(0.2, 0.6, 0.1), resolution=10)

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
