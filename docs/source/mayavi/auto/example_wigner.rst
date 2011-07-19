

.. _example_wigner:

Wigner example
--------------------------------------------------------------------


An example in which 3 functions of x and y  are displayed with a surf plot,
while the z scaling is kept constant, to allow comparison between them.

The important aspect of this example is that the 3 functions should not
be displayed on top of each other, but side by side. For this we use the
extent keyword argument.

In addition, the relative scale between the different plots is important.
This is why we also use the `warp_scale` keyword argument, to have the same
scale on all plots.

Finally, we have to adjust the data bounds: as we want the "horizon" of
the wigner function in the middle of our extents, we put this to zero.

We add a set of axes and outlines to the plot. We have to play we extents
and ranges in order to make them fit with the data.


.. image:: ../generated_images/example_wigner.jpg
    :align: center



**Python source code:** :download:`wigner.py`

.. literalinclude:: wigner.py
    :lines: 19-


    