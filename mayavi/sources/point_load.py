"""A source object that computes stress tensors on a volume.
     The tensors are computed from the application of a point load on a
     semi-infinite domain.
"""
# Authors: KK Rai (kk.rai [at] iitb.ac.in)
#          R. Ambareesha (ambareesha [at] iitb.ac.in)
#          Prabhu Ramachandran (prabhu [at] aero.iitb.ac.in)

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `PointLoad` class.
######################################################################
class PointLoad(Source):
    # The version of this class.  Used for persistence.
    __version__ = 0

    point_load = Instance(tvtk.PointLoad, args=(), allow_none=False,
                          record=True)

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])

    # Create the UI for the traits.
    view = View(Group(Item(name='point_load',
                           style='custom',
                           resizable=True),
                      label='PointLoad',
                      show_labels=False),
                resizable=True)

    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        # Call parent class' init.
        super(PointLoad, self).__init__(**traits)

        # Call render everytime source traits change.
        self.point_load.on_trait_change(self.render)

        # Setup the outputs.
        self.outputs = [self.point_load]

    def has_output_port(self):
        """ Return True as the point load has output port."""
        return True

    def get_output_object(self):
        """ Return the point load output port."""
        return self.point_load.output_port
