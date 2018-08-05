"""A custom grid plane with a lot more flexibility than
GridPlane.  This also only works for non-unstructured/non-polygonal
datasets.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007,  Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports
from mayavi.components import custom_grid_plane
from mayavi.modules.contour_grid_plane import \
     ContourGridPlane, Contour, Actor


######################################################################
# `CustomGridPlane` class.
######################################################################
class CustomGridPlane(ContourGridPlane):

    grid_plane = Instance(custom_grid_plane.Component,
                          allow_none=False, record=True)

    # Overriding the ContourGridPlane's default view.
    view = View(Group(Item(name='grid_plane', style='custom'),
                      show_labels=False,
                      label='GridPlane'),
                Group(Group(Item(name='enable_contours')),
                      Group(Item(name='contour', style='custom',
                                 enabled_when='object.enable_contours'),
                            show_labels=False,
                            ),
                      label='Contour',
                      ),
                Group(Item(name='actor', style='custom'),
                      label='Actor',
                      show_labels=False)
                )

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        # Note that we don't call the parent class method here.  This
        # is intentional to avoid problems with the execution of the
        # VTK pipeline.

        # Create the components.
        self.grid_plane = custom_grid_plane.CustomGridPlane()
        self.contour = Contour(auto_contours=True, number_of_contours=10)
        self.actor = Actor()
        self.enable_contours = False
        self.actor.property.point_size = 2
