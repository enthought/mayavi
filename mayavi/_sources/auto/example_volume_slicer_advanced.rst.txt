

.. _example_volume_slicer_advanced:

Volume slicer advanced example
--------------------------------------------


An efficient implementation of the triple-plane view showing 3 cut planes
on volumetric data, and side views showing each cut, with a cursor to
move the other cuts.

This is an example of complex callback interaction. It builds on the
:ref:`example_volume_slicer` but has more complex logic. You should try
to understand the :ref:`example_volume_slicer` first.

In this example, the VolumeSlicer object displays a position attribute
giving the position of the cut in data coordinates. Traits callbacks are
used to move the cut planes when this position attribute is modifed.

In the 3D window, the 3D cuts are displayed using ImagePlaneWidgets
cutting the 3D volumetric data. The data extracted by the
ImagePlaneWidgets for plotting is captured using the TVTK
ImagePlaneWidget's `_get_reslice_output` method. The resulting dataset is
plotted in each side view using another ImagePlaneWidget. As a result the
data is not copied (at the VTK level, there is only one pipeline), and
modifications of the data plotted on the planes in the 3D view (for
instance when these planes are moved) are propagated to the 2D side views
by the VTK pipeline.

A cursor is displayed in each side view using a glyph. The cursor
indicates the position of the cut.

In the side view, when the mouse button is pressed on the planes, it
creates a VTK `InteractionEvent`. When this happens, VTK calls an
callback (observer, it VTK terms), that we use to move the position of
the cut. The Traits callbacks do the rest for the updating.


**Python source code:** :download:`volume_slicer_advanced.py`

.. literalinclude:: volume_slicer_advanced.py
    :lines: 32-


    