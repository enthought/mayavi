"""
This example shows how to use a callback to select a red ball amongst white
balls.

The example uses the figure method 'on_mouse_pick', added in Mayavi
3.4, to register a callback when the left mouse is pressed. The callback
is called with a picker, enabling to identify the object selected.
Specifically, actors are selected, each object is represented on the scene
via actors. The selected actors can be found in 'picker.actors'. In this
example, we have plotted red balls and white ball. We want to select the
red balls, and thus test if any actor in picker.actors corresponds to an
actor of red balls.

To identify which ball has been selected, we use the point id. However,
each ball is represented by several points. Thus we need to retrieve the
number of points per ball, and divide the point id by this number.

We use an outline to display which ball was selected by positioning it on
the corresponding ball.
"""

# Author: Gael Varoquaux <gael dot varoquaux at normalesup.org>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD style.

import numpy as np
from mayavi import mlab

################################################################################
# Disable the rendering, to get bring up the figure quicker:
figure = mlab.gcf()
mlab.clf()
figure.scene.disable_render = True

# Creates two set of points using mlab.points3d: red point and
# white points
x1, y1, z1 = np.random.random((3, 10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0),
                resolution=20)

x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9),
                resolution=20)

# Add an outline to show the selected point and center it on the first
# data point.
outline = mlab.outline(line_width=3)
outline.outline_mode = 'cornered'
outline.bounds = (x1[0]-0.1, x1[0]+0.1,
                  y1[0]-0.1, y1[0]+0.1,
                  z1[0]-0.1, z1[0]+0.1)

# Every object has been created, we can reenable the rendering.
figure.scene.disable_render = False
################################################################################


# Here, we grab the points describing the individual glyph, to figure
# out how many points are in an individual glyph.
glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()


def picker_callback(picker):
    """ Picker callback: this get called when on pick events.
    """
    if picker.actor in red_glyphs.actor.actors:
        # Find which data point corresponds to the point picked:
        # we have to account for the fact that each data point is
        # represented by a glyph with several points
        point_id = picker.point_id//glyph_points.shape[0]
        # If the no points have been selected, we have '-1'
        if point_id != -1:
            # Retrieve the coordinates coorresponding to that data
            # point
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # Move the outline to the data point.
            outline.bounds = (x-0.1, x+0.1,
                              y-0.1, y+0.1,
                              z-0.1, z+0.1)


picker = figure.on_mouse_pick(picker_callback)

# Decrease the tolerance, so that we can more easily select a precise
# point.
picker.tolerance = 0.01

mlab.title('Click on red balls')

mlab.show()
