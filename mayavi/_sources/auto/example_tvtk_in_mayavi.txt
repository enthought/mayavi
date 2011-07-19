

.. _example_tvtk_in_mayavi:

Tvtk in mayavi example
--------------------------------------------------------------------


An example of pure TVTK programming to build TVTK objects, which are then
added to a Mayavi scene.

This example show how pure TVTK objects can be added to a Mayavi scene.

This programming style does not allow to benefit from the data-management
facilities of Mayavi (the pipeline, the data-oriented mlab functions),
but it allows to easily reuse VTK code together with Mayavi or mlab code.

If you want to use arbritrary VTK filters with Mayavi, it is best to use
the UserDefined Mayavi filter, which enables the user to insert any VTK
filter in the Mayavi pipeline. See, for instance, the :ref:`example_mri`
for example of the UserDefined filter. For a full-blown example of a
complex VTK pipeline built with Mayavi, see
:ref:`example_tvtk_segmentation`.


.. image:: ../generated_images/example_tvtk_in_mayavi.jpg
    :align: center



**Python source code:** :download:`tvtk_in_mayavi.py`

.. literalinclude:: tvtk_in_mayavi.py
    :lines: 18-


    