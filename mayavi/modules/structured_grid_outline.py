"""Draws a grid-conforming outline for structured grids.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007,  Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports.
from mayavi.components.actor import Actor
from mayavi.modules.outline import Outline


######################################################################
# `StructuredGridOutline` class.
######################################################################
class StructuredGridOutline(Outline):
    """Draws a grid-conforming outline for structured grids.
    """

    # The outline filter.
    outline_filter = Instance(tvtk.StructuredGridOutlineFilter,
                              allow_none = False, record=True)

    def setup_pipeline(self):
        self.outline_filter = tvtk.StructuredGridOutlineFilter()
        self.actor = Actor()

