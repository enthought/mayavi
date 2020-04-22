

.. _example_pick_on_surface:

Pick on surface example
--------------------------------------------

 Example showing how to pick data on a surface, going all the way back
to the index in the numpy arrays.

In this example, two views of the same data are shown. One with the data
on a sphere, the other with the data flat.

We use the 'on_mouse_pick' method of the scene to register a callback on
clicking on the sphere. The callback is called with a picker object as
and an argument. We use the point_id of the point that has been picked,
and go back to the 2D index on the data matrix to find its position.


**Python source code:** :download:`pick_on_surface.py`

.. literalinclude:: pick_on_surface.py
    :lines: 12-


    