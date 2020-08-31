

.. _example_custom_colormap:

Custom colormap example
--------------------------------------------------------------------


An example showing how a custom colormap (or look up table) can be used
for a given object.

Although the end user specifies colormaps by giving the name of a set of
predefined colormaps, Mayavi (and VTK) deal with color internally using
'Look Up Tables' (LUT): a table that associate a scalar value to a
color defined by its RGBA components.

In this example, we show how the LUT of an object can be retrieved and
modified. Specifically, we start by giving a surf object the 'cool'
colormap, but we modify add to add a transparency effect.

Notice in the resulting image how the surface becomes more transparent
for its lower points.

Note that if you want to use a different number of colors, you can
change the 'number_of_colors' attribute of the lut object and assign a
new array of the right shape to its 'table' attribute.


.. image:: ../generated_images/example_custom_colormap.jpg
    :align: center



**Python source code:** :download:`custom_colormap.py`

.. literalinclude:: custom_colormap.py
    :lines: 21-


    