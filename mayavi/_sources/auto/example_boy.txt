

.. _example_boy:

Boy example
--------------------------------------------------------------------


A script to generate the Mayavi logo: a Boy surface.

The boy surface is a mathematical parametric surface, see
http://en.wikipedia.org/wiki/Boy%27s_surface . We display it by sampling
the two parameters of the surface on a grid and using the mlab's mesh
function: :func:`mayavi.mlab.mesh`.


.. image:: ../generated_images/example_boy.jpg
    :align: center



**Python source code:** :download:`boy.py`

.. literalinclude:: boy.py
    :lines: 9-


    