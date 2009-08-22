"""
An example showing how to select points out of a cloud.

This example shows two tricks:

 1) How to select from a list of visualization objects

 2) How to find the point number, when selecting in a cloud of points
    represented by glyphs.

To handle mouse events, we register a set of callbacks that will call
the picker when the mouse button is pressed, but there is no movement.
The picker is called, and triggers the picker callback.

The trick to act only on specific visualization objects is to test that
the actors of the objects we are interested in are in the list of actors
selected by the picker.

Finally, we need to find the specific data point corresponding to the
glyph selected. For this we find out how many points each individual
glyph contains, and we look at the point id of vertex selected. Dividing
the later by the former gives us the corresponding data point
id.
"""

import numpy as np
from enthought.mayavi import mlab 

################################################################################
# Disable the rendering, to get bring up the figure quicker:
figure = mlab.gcf()
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

picker = figure.scene.picker

def picker_callback(vtk_picker, event):
    """ Picker callback: this get called when on pick events. 
    """
    # Here we are using a the module-level variable for the picker. We
    # could also retrieve it doing:
    # picker = tvtk.to_vtk(tvtk_picker)

    if picker.pointpicker.actor in red_glyphs.actor.actors:
        # Find which data point corresponds to the point picked:
        # we have to account for the fact that each data point is
        # represented by a glyph with several points 
        point_id = picker.pointpicker.point_id/glyph_points.shape[0]
        # If the no points have been selected, we have '-1'
        if not point_id == -1:
            # Retrieve the coordinnates coorresponding to that data
            # point
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # Move the outlint to the data point.
            outline.bounds = (x-0.1, x+0.1, 
                              y-0.1, y+0.1, 
                              z-0.1, z+0.1)


################################################################################
# Some logic to pick on click but no move
class MvtPicker(object):
    """ An event dispatcher to send pick event on mouse clicks without a
        movement.
    """
    mouse_mvt = False

    def __init__(self, figure, callback):
        self.picker = figure.scene.picker.pointpicker
        figure.scene.interactor.add_observer('LeftButtonPressEvent', 
                                        self.on_button_press)
        figure.scene.interactor.add_observer('MouseMoveEvent', 
                                        self.on_mouse_move)
        figure.scene.interactor.add_observer('LeftButtonReleaseEvent', 
                                        self.on_button_release)
        self.picker.pointpicker.add_observer("EndPickEvent", callback)

    def on_button_press(self, vtk_picker, event):
        self.mouse_mvt = False

    def on_mouse_move(self, vtk_picker, event):
        self.mouse_mvt = True

    def on_button_release(self, vtk_picker, event):
        if not self.mouse_mvt:
            x, y = obj.GetEventPosition()
            self.picker.pick((x, y, 0), figure.scene.renderer)
        self.mouse_mvt = False
        


################################################################################
mvt_picker = MvtPicker(figure, picker_callback)

# Decrease the tolerance, so that we can more easily select a precise
# point.
picker.pointpicker.tolerance = 0.01

mlab.show()
