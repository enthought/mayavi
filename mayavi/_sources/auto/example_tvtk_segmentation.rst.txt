

.. _example_tvtk_segmentation:

Tvtk segmentation example
--------------------------------------------


Using VTK to assemble a pipeline for segmenting MRI images. This example
shows how to insert well-controled custom VTK filters in Mayavi.

This example downloads an MRI scan, turns it into a 3D numpy array,
applies a segmentation procedure made of VTK filters to extract the
gray-matter/white-matter boundary.

The segmentation algorithm used here is very naive and should, of course,
not be used as an example of segmentation.



**Python source code:** :download:`tvtk_segmentation.py`

.. literalinclude:: tvtk_segmentation.py
    :lines: 13-


    