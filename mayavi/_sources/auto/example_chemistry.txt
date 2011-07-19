

.. _example_chemistry:

Chemistry example
--------------------------------------------------------------------


In this example, we display the H2O molecule, and use volume rendering to
display the electron localization function.

The atoms and the bounds are displayed using mlab.points3d and
mlab.plot3d, with scalar information to control the color.

The electron localization function is displayed using volume rendering.
Good use of the `vmin` and `vmax` argument to
`mlab.pipeline.volume` is critical to achieve a good visualization: the
`vmin` threshold should placed high-enough for features to stand out.

The original is an electron localization function from Axel Kohlmeyer.


.. image:: ../generated_images/example_chemistry.jpg
    :align: center



**Python source code:** :download:`chemistry.py`

.. literalinclude:: chemistry.py
    :lines: 15-


    