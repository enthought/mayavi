"""Module documentation goes here."""

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.components.actor import Actor


######################################################################
# `MyModule` class.
######################################################################
class MyModule(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actor component that represents the visualization.
    actor = Instance(Actor)

    ########################################
    # View related code.


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
        # Create the components and set them up.

        # Setup the actor suitably for this module.

        # Setup the components, actors and widgets. (sample code)
        #self.components.extend([your_components, ...])
        #self.actors.append(your_actor)
        # Note that self.actor.actor need not be added.
        #self.widgets.append(your_widget)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        # Data is available, so set the input for the grid plane.
        # Do your stuff here!

        # Now flush the pipeline
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
