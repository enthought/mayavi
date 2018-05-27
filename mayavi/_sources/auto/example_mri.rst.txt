

.. _example_mri:

Mri example
--------------------------------------------------------------------


Viewing MRI data with cut plane and iso surface.

This example downloads an MRI scan, turns it into a 3D numpy array and
visualizes it.

First we extract some internal structures of the brain by defining a
volume of interest around them, and using iso surfaces.

Then we display two cut planes to show the raw MRI data itself.

Finally we display the outer surface, but we restrict it to volume of
interest to leave a cut for the cut planes.

For an example of feature extraction from MRI data using Mayavi and vtk,
see :ref:`example_tvtk_segmentation`.


.. image:: ../generated_images/example_mri.jpg
    :align: center



**Python source code:** :download:`mri.py`

.. literalinclude:: mri.py
    :lines: 18-


    