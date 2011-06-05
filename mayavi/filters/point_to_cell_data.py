# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.cell_to_point_data import CellToPointData
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `PointToCellData` class.
######################################################################
class PointToCellData(CellToPointData):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.PointDataToCellData,
                            args=(), kw={'pass_point_data':1},
                            allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['point'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['cell'],
                               attributes=['any'])

