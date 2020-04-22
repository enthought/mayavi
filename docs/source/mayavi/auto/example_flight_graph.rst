

.. _example_flight_graph:

Flight graph example
--------------------------------------------------------------------


An example showing a graph display between cities positioned on the
Earth surface.

This graph displays the longest flight routes operated by Boing
777. The two main interests of this example are that it shows how to
build a graph of arbitrary connectivity, and that it shows how to
position data on the surface of the Earth.

The graph is created by first building a scalar scatter dataset with the
mlab.points3d command, and adding line information to it. One of the
difficulties is that the lines are specified using the indexing number of
the points, so we must 'massage' our data when loading it. A similar
technique to plot the graph is done in the :ref:`example_protein`.
Another example of graph plotting, showing a different technique to plot
the graph, can be seen on :ref:`example_delaunay_graph`.

To simplify things we do not plot the connection on the surface of the
Earth, but as straight lines going through the Earth. As a result
must use transparency to show the connection.

Data source: http://www.777fleetpage.com/777fleetpage3.htm


.. image:: ../generated_images/example_flight_graph.jpg
    :align: center



**Python source code:** :download:`flight_graph.py`

.. literalinclude:: flight_graph.py
    :lines: 24-


    