"""A contour grid plane module.  This module lets one take a slice of
input grid data and view contours of the data.  The module only works
for structured points, rectilinear grid and structured grid input.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool
from traitsui.api import View, Group, Item

# Local imports
from mayavi.core.module import Module
from mayavi.components.grid_plane import GridPlane
from mayavi.components.contour import Contour
from mayavi.components.actor import Actor
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ContourGridPlane` class.
######################################################################
class ContourGridPlane(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The grid plane component.
    grid_plane = Instance(GridPlane, allow_none=False, record=True)

    # Specifies if contouring is to be done or not.
    enable_contours = Bool(True, desc='if contours are generated')

    # The contour component that contours the data.
    contour = Instance(Contour, allow_none=False, record=True)

    # The actor component that represents the visualization.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['image_data',
                                        'structured_grid',
                                        'rectilinear_grid'],
                              attribute_types=['any'],
                              attributes=['any'])

    view = View([Group(Item(name='grid_plane', style='custom'),
                       show_labels=False),
                 Group(Item(name='enable_contours')),
                 Group(Item(name='contour', style='custom',
                            enabled_when='object.enable_contours'),
                       Item(name='actor', style='custom'),
                       show_labels=False)
                 ]
                )

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        # Create the components
        self.grid_plane = GridPlane()
        self.contour = Contour(auto_contours=True, number_of_contours=10)
        self.actor = Actor()

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        # Data is available, so set the input for the grid plane.
        self.grid_plane.inputs = [mm.source]

        # This makes sure that any changes made to enable_contours
        # when the module is not running are updated when it is
        # started.
        self._enable_contours_changed(self.enable_contours)
        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the components should do the rest if
        # they are connected.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _filled_contours_changed(self, value):
        """When filled contours are enabled, the mapper should use the
        the cell data, otherwise it should use the default scalar
        mode.
        """
        if value:
            self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _enable_contours_changed(self, value):
        """Turns on and off the contours."""
        if self.module_manager is None:
            return
        if value:
            self.actor.inputs = [self.contour]
            if self.contour.filled_contours:
                self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.actor.inputs = [self.grid_plane]
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _grid_plane_changed(self, old, new):
        cont = self.contour
        if cont is not None:
            cont.inputs = [new]
        self._change_components(old, new)

    def _contour_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self._filled_contours_changed,
                                'filled_contours',
                                remove=True)
        new.on_trait_change(self._filled_contours_changed,
                            'filled_contours')
        # Setup the contours input.
        gp = self.grid_plane
        if gp is not None:
            new.inputs = [gp]

        # Setup the actor.
        actor = self.actor
        if actor is not None:
            actor.inputs = [new]
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        if old is None:
            # First time this is set.
            new.property.trait_set(line_width=2.0)

        # Set the actors scene and input.
        new.scene = self.scene
        cont = self.contour
        if cont is not None:
            new.inputs = [cont]
        self._change_components(old, new)
