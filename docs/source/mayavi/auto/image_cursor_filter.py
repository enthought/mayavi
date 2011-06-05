"""
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
"""

# Authors: Emmanuelle Gouillart <emmanuelle.gouillart@normalesup.org>
# and Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.


from mayavi import mlab
import numpy as np

# Define Gaussian data field
x, y, z = np.ogrid[0:1:40j, 0:1:40j, 0:1:40j]
sig = 0.5
center = 0.5
g = np.exp(-((x-center)**2 + (y-center)**2 + (z-center)**2)/(2*sig**2))

################################################################################

mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))

# Define the cursor
s = mlab.pipeline.scalar_field(g)
cursor = mlab.pipeline.user_defined(s, filter='ImageCursor3D')

# The TVTK filter used by Mayavi is accessible as the '.filter'
# attribute of the Mayavi filtered returned by user_defined.
# We can set the graphical properties of the cross via attributes of
# cursor.filter, and not of cursor itself. Here cursor is a Mayavi filter,
# that is an object that inserts in the Mayavi pipeline, whereas
# cursor.filter is the TVTK filter that actually does the work.

# Put the cursor at the center of the field volume (default is (0, 0, 0))
cursor.filter.cursor_position = np.array([20, 20, 20])
# Define the value of the cursor (default is 255) so that there is
# enough contrast between the cursor and the data values in the neighbourhood
# of the cursor. The cursor value is within the data value range so that
# the contrast of the data is not altered.
cursor.filter.cursor_value = 0
# Define the radius of the cross (the extent of the cross is 2xcursor_radius)
cursor.filter.cursor_radius = 10


# Display data and cursor using an image_plane_widget that intersects the
# cursor.
ipw = mlab.pipeline.image_plane_widget(cursor, plane_orientation='x_axes',
            slice_index=20)

# View
mlab.colorbar()
mlab.view(15, 70, 100, [20, 20, 20])
mlab.show()
