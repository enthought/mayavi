# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance

# Local imports.
from mayavi.components.contour import Contour as ContourComponent
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.filters.wrapper import Wrapper

################################################################################
# `Contour` class.
################################################################################
class Contour(Wrapper):
    """
    A contour filter that wraps around the Contour component to generate
    iso-surfaces on any input dataset.
    """
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The contour component this wraps.
    filter = Instance(ContourComponent, args=(), record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['point'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
