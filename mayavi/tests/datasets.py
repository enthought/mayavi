# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.

import numpy
from numpy import linspace, cos, sin, pi, empty, sqrt,array,arange,random

# Enthought library imports
from tvtk.api import tvtk


def generate_annulus(r=None, theta=None, z=None):
    """ Generate points for structured grid for a cylindrical annular
        volume.  This method is useful for generating a unstructured
        cylindrical mesh for VTK (and perhaps other tools).

        Parameters
        ----------
        r : array : The radial values of the grid points.
                    It defaults to linspace(1.0, 2.0, 11).

        theta : array : The angular values of the x axis for the grid
                        points. It defaults to linspace(0,2*pi,11).

        z: array : The values along the z axis of the grid points.
                   It defaults to linspace(0,0,1.0, 11).

        Return
        ------
        points : array
            Nx3 array of points that make up the volume of the annulus.
            They are organized in planes starting with the first value
            of z and with the inside "ring" of the plane as the first
            set of points.  The default point array will be 1331x3.
    """
    # Default values for the annular grid.
    if r is None: r = linspace(1.0,2.0, 11)
    if theta is None: theta = linspace(0,2*pi,11)
    if z is None: z = linspace(0.0,1.0, 11)

    # Find the x values and y values for each plane.
    x_plane = (cos(theta)*r[:,None]).ravel()
    y_plane = (sin(theta)*r[:,None]).ravel()

    # Allocate an array for all the points.  We'll have len(x_plane)
    # points on each plane, and we have a plane for each z value, so
    # we need len(x_plane)*len(z) points.
    points = empty([len(x_plane)*len(z),3])

    # Loop through the points for each plane and fill them with the
    # correct x,y,z values.
    start = 0
    for z_plane in z:
        end = start+len(x_plane)
        # slice out a plane of the output points and fill it
        # with the x,y, and z values for this plane.  The x,y
        # values are the same for every plane.  The z value
        # is set to the current z
        plane_points = points[start:end]
        plane_points[:,0] = x_plane
        plane_points[:,1] = y_plane
        plane_points[:,2] = z_plane
        start = end

    return points


def single_type_ug():
    """Simple example showing how to create an unstructured grid
    consisting of cells of a single type.
    """
    points = array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], # tets
                    [1,0,0], [2,0,0], [1,1,0], [1,0,1],
                    [2,0,0], [3,0,0], [2,1,0], [2,0,1],
                    ], 'f')
    tets = array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    tet_type = tvtk.Tetra().cell_type
    ug = tvtk.UnstructuredGrid(points=points)
    ug.set_cells(tet_type, tets)
    return ug

def mixed_type_ug():
    """A slightly more complex example of how to generate an
    unstructured grid with different cell types.  Returns a created
    unstructured grid.
    """
    points = array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], # tetra
                    [2,0,0], [3,0,0], [3,1,0], [2,1,0],
                    [2,0,1], [3,0,1], [3,1,1], [2,1,1], # Hex
                    ], 'f')
    # shift the points so we can show both.
    points[:,1] += 2.0
    # The cells
    cells = array([4, 0, 1, 2, 3, # tetra
                   8, 4, 5, 6, 7, 8, 9, 10, 11 # hex
                   ])
    # The offsets for the cells, i.e. the indices where the cells
    # start.
    offset = array([0, 5])
    tetra_type = tvtk.Tetra().cell_type # VTK_TETRA == 10
    hex_type = tvtk.Hexahedron().cell_type # VTK_HEXAHEDRON == 12
    cell_types = array([tetra_type, hex_type])
    # Create the array of cells unambiguously.
    cell_array = tvtk.CellArray()
    cell_array.set_cells(2, cells)
    # Now create the UG.
    ug = tvtk.UnstructuredGrid(points=points)
    # Now just set the cell types and reuse the ug locations and cells.
    ug.set_cells(cell_types, offset, cell_array)
    return ug

def generateStructuredGrid():
    """Generates Structured Grid"""
    dims = (32, 32, 12)
    sgrid = tvtk.StructuredGrid(dimensions=(dims[1], dims[0], dims[2]))
    r = linspace(1, 10, dims[0])
    theta = linspace(0, 2*numpy.pi, dims[1])
    z = linspace(0, 5, dims[2])
    pts = generate_annulus(r, theta, z)
    sgrid.points = pts
    s = sqrt(pts[:,0]**2 + pts[:,1]**2 + pts[:,2]**2)
    sgrid.point_data.scalars = numpy.ravel(s.copy())
    sgrid.point_data.scalars.name = 'scalars'

    return sgrid

def generateUnstructuredGrid_single():
    """Generates Untructured Grid"""
    ug = single_type_ug()
    temperature = arange(0, 120, 10, 'd')
    velocity = random.randn(12, 3)
    ug.point_data.scalars = temperature
    ug.point_data.scalars.name = 'temperature'
    # Some vectors.
    ug.point_data.vectors = velocity
    ug.point_data.vectors.name = 'velocity'
    return ug

def generateUnstructuredGrid_mixed():
    """Generates Untructured Grid"""
    ug = mixed_type_ug()
    temperature = arange(0, 120, 10, 'd')
    velocity = random.randn(12, 3)
    ug.point_data.scalars = temperature
    ug.point_data.scalars.name = 'temperature'
    # Some vectors.
    ug.point_data.vectors = velocity
    ug.point_data.vectors.name = 'velocity'
    return ug

