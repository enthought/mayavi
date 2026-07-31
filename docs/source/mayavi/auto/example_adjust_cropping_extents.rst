

.. _example_adjust_cropping_extents:

Adjust cropping extents example
--------------------------------------------

A custom dialog to adjust the parameters of a GeometryFilter to crop
data points.

This example shows how to use a GeometryFilter to crop data points, but
also how to build a custom dialog to easily set interactively parameters
of a filter, or any other Mayavi object.

The GeometryFilter crops all data within a bounding box specified by
'extents'. In this example, we want to be able to tweak these extents
interactively. For this, we build a Traits object that has 'x_min',
'x_max', 'y_min', ... attributes. Traits enables us to represent this
object as a dialog box. We use a callback called when these attributes
are modified to propagate them to the filter. For more information
on creating GUIs with Traits:

    https://docs.enthought.com/traitsui

    https://docs.enthought.com/traits

    https://support.enthought.com/hc/en-us/articles/204469620-Introductory-materials-for-Traits-and-Traits-UI

.. image:: ../generated_images/example_adjust_cropping_extents.jpg
    :align: center



**Python source code:** :download:`adjust_cropping_extents.py`

.. literalinclude:: adjust_cropping_extents.py
    :lines: 24-


    