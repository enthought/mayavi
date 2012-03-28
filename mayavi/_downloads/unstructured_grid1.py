"""A MayaVi example of how to generate an unstructured grid dataset
using numpy arrays.  Also shown is a way to visualize this data with
mayavi2.  The script can be run like so:

  $ mayavi2 -x unstructured_grid.py

Alternatively, it can be run as:

  $ python unstructured_grid.py

Author: Prabhu Ramachandran <prabhu at aero dot iitb dot ac dot in>

Copyright (c) 2007, Enthought, Inc.
License: BSD style.
"""

from numpy import array, arange, random
from tvtk.api import tvtk
from mayavi.scripts import mayavi2

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

def save_xml(ug, file_name):
    """Shows how you can save the unstructured grid dataset to a VTK
    XML file."""
    w = tvtk.XMLUnstructuredGridWriter(input=ug, file_name=file_name)
    w.write()

# ----------------------------------------------------------------------
# Create the unstructured grids and assign scalars and vectors.
ug1 = single_type_ug()
ug2 = mixed_type_ug()
temperature = arange(0, 120, 10, 'd')
velocity = random.randn(12, 3)
for ug in ug1, ug2:
    ug.point_data.scalars = temperature
    ug.point_data.scalars.name = 'temperature'
    # Some vectors.
    ug.point_data.vectors = velocity
    ug.point_data.vectors.name = 'velocity'

# Uncomment this to save the file to a VTK XML file.
#save_xml(ug2, 'file.vtu')

# Now view the data.
@mayavi2.standalone
def view():
    from mayavi.sources.vtk_data_source import VTKDataSource
    from mayavi.modules.outline import Outline
    from mayavi.modules.surface import Surface
    from mayavi.modules.vectors import Vectors

    mayavi.new_scene()
    # The single type one
    src = VTKDataSource(data = ug1)
    mayavi.add_source(src)
    mayavi.add_module(Outline())
    mayavi.add_module(Surface())
    mayavi.add_module(Vectors())

    # Mixed types.
    src = VTKDataSource(data = ug2)
    mayavi.add_source(src)
    mayavi.add_module(Outline())
    mayavi.add_module(Surface())
    mayavi.add_module(Vectors())

if __name__ == '__main__':
    view()
