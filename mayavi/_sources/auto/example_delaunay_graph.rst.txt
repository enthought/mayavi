

.. _example_delaunay_graph:

Delaunay graph example
--------------------------------------------


An example illustrating graph manipulation and display with Mayavi
and NetworkX.

This example shows how to use Mayavi in a purely algorithmic way, to
compute a Delaunay from data points, extract it and pass it to networkx.
It also shows how to plot a graph using quiver.

Starting from points positioned regularly on a sphere, we first use VTK
to create the Delaunay graph, and also to plot it. We then create a
matching NetworkX graph, calling it's minimum spanning tree function. We
display it using Mayavi.

The visualization clearly shows that the minimum spanning tree of the
points, considering all possible connections, is included in the Delaunay
graph.

_____

The function `compute_delaunay_edges` uses VTK to retrieve the Delaunay
graph of a set of points. First a structure of unconnected points is
created using `mlab.points3d`. The Delaunay filter applied to it builds
an unstructured grid (see :ref:`data-structures-used-by-mayavi`). We
apply an ExtractEdges filter to it, which returns a structure of points
connected by edges: the :ref:`PolyData structure <poly_data>`. The
dataset structure can be retrieved as the first item of the `outputs`
list of the ExtractEdges filter object, returned by the
`mlab.pipeline.extract_edges` factory function. Once we have this object,
we extract the points and edge list from it. This graph-plotting
technique differs from the technique used in the examples
:ref:`example_protein` and :ref:`example_flight_graph` where points are
created and connected by lines. Unlike these techniques, it enables
storing scalar data on each line.

_____

To visualize the graph (function `graph_plot`), we build a list of
vectors giving the edges, and use `mlab.quiver3d` to display them. To
display an unoriented graph, it is best to use the `2ddash` mode of
`quiver3d`.



**Python source code:** :download:`delaunay_graph.py`

.. literalinclude:: delaunay_graph.py
    :lines: 43-


    