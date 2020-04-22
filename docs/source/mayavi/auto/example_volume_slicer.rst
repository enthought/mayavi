

.. _example_volume_slicer:

Volume slicer example
--------------------------------------------


Example of an elaborate dialog showing a multiple views on the same data, with
3 cuts synchronized.

This example shows how to have multiple views on the same data, how to
embedded multiple scenes in a dialog, and the caveat in populating them
with data, as well as how to add some interaction logic on an
ImagePlaneWidget.

The order in which things happen in this example is important, and it is
easy to get it wrong. First of all, many properties of the visualization
objects cannot be changed if there is not a scene created to view them.
This is why we put a lot of the visualization logic in the callback of
scene.activated, which is called after creation of the scene.
Second, default values created via the '_xxx_default' callback are created
lazily, that is, when the attributes are accessed. As the establishment
of the VTK pipeline can depend on the order in which it is built, we
trigger these access by explicitly calling the attributes.
In particular, properties like scene background color, or interaction
properties cannot be set before the scene is activated.

The same data is exposed in the different scenes by sharing the VTK
dataset between different Mayavi data sources. See
the :ref:`sharing_data_between_scenes` tip for more details.

In this example, the interaction with the scene and the various elements
on it is strongly simplified by turning off interaction, and choosing
specific scene interactor styles. Indeed, non-technical users can be
confused with too rich interaction.


**Python source code:** :download:`volume_slicer.py`

.. literalinclude:: volume_slicer.py
    :lines: 31-


    