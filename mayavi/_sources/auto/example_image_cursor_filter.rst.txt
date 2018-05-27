

.. _example_image_cursor_filter:

Image cursor filter example
--------------------------------------------


Excample using the UserDefined filter to paint a cross-shaped cursor on data,
in order to point out a special position.

We use the UserDefined filter `ImageCursor3D` to create the cursor. A Gaussian
data field is painted with the cursor, and then visualized using the
ImagePlaneWIdget module.

ImageCursor3D is one example among many of the use of the UserDefined, which
allows to use TVTK filters that are not. See :ref:`using_userdefined_filter`
for more details. Also, other examples using the UserDefined filter are
provided in :ref:`example_mri` and :ref:`example_tvtk_segmentation`.

Selecting the UserDefined filter in the Mayavi pipeline is a convenient
way to look for additional filters. This pops up a dialog called `TVTK
class chooser`, with a `Search` field that allows to search for desired
actions or properties. For example, searching for `cursor` returns
several filters, among which Cursor3D and ImageCursor3D. As a rule of
thumb, the name of TVTK filters acting on TVTK ImageData dataset starts
with `Image` (ImageData is the type of VTK data set created by e.g.
mlab.pipeline.scalar_field. See :ref:`data-structures-used-by-mayavi` for
more details about VTK datasets). In the dialog used to interactively
add the UserDefined filet, we can therefore select `ImageCursor3D`.
The documentation of the filter is displayed when selecting its name
within the `Class name` field of the dialog.


**Python source code:** :download:`image_cursor_filter.py`

.. literalinclude:: image_cursor_filter.py
    :lines: 27-


    