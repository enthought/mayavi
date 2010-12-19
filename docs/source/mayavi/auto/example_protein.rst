

.. _example_protein:

Protein example
--------------------------------------------------------------------


Visualize a protein graph structure downloaded from the protein database in
standard pdb format.

We parse the pdb file, but extract only a very small amount of
information: the type of atoms, their positions, and the links between them.

Most of the complexity of this example comes from the code turning the
PDB information into a list of 3D positions, with associated scalar
and connection information.

We assign a scalar value for the atoms to differenciate the different
types of atoms, but it does not correspond to the atomic mass. The size
and the color of the atom on the visualization is therefore not
chemicaly-significant.

The atoms are plotted using mlab.points3d, and connections between atoms
are added to the dataset, and visualized using a surface module.

The graph is created by adding connection information to points. For this, each
point is designated by its number (in the order of the array passed to
mlab.points3d), and the connection array, made of pairs of these numbers, is
constructed. There is some slightly tedious data manipulation to go from the
named-node graph representation as stored in the pdb file, to the index-based
connection pairs. A similar technique to plot the graph is done in the
:ref:`example_flight_graph`. Another example of graph plotting, showing a
different technique to plot the graph, can be seen on
:ref:`example_delaunay_graph`.

To visualize the local atomic density, we use a gaussian splatter filter
that builds a kernel density estimation of the continuous density field:
each point is convoluted by a Gaussian kernel, and the sum of these
Gaussians form the resulting density field. We visualize this field using
volume rendering.

Reference for the pdb file standard:
http://mmcif.pdb.org/dictionaries/pdb-correspondence/pdb2mmcif.html


.. image:: ../generated_images/example_protein.jpg
    :align: center



**Python source code:** :download:`protein.py`

.. literalinclude:: protein.py
    :lines: 39-


    