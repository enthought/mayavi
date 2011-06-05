# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Local imports.
from mayavi.components.cutter import Cutter
from mayavi.components.implicit_plane import ImplicitPlane
from mayavi.filters.collection import Collection
from mayavi.core.pipeline_info import PipelineInfo

################################################################################
# `CutPlane` class.
################################################################################
class CutPlane(Collection):
    """
    This class represents a cut plane that can be used to slice through
    any dataset.  It also provides a 3D widget interface to position and
    move the slice interactively.
    """
    # The version of this class.  Used for persistence.
    __version__ = 0

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def setup_pipeline(self):
        """Creates the pipeline."""
        ip = ImplicitPlane()
        cut = Cutter(cut_function=ip.plane)
        self.filters = [ip, cut]

