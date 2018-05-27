

.. _example_lorenz:

Lorenz example
--------------------------------------------------------------------


An example displaying the trajectories for the Lorenz system of
equations along with the z-nullcline.

The vector field of the Lorenz system flow is integrated to display
trajectories using mlab's flow function:
:func:`mayavi.mlab.flow`.

The z-nullcline is plotted by extracting the z component of the vector
field data source with the ExtractVectorComponent filter, and applying
an IsoSurface module on this scalar component.


.. image:: ../generated_images/example_lorenz.jpg
    :align: center



**Python source code:** :download:`lorenz.py`

.. literalinclude:: lorenz.py
    :lines: 13-


    