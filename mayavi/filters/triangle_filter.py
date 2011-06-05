# Author: Robert Kern <robert.kern@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `TriangleFilter` class.
######################################################################
class TriangleFilter(FilterBase):

    """ Converts input polygons and triangle strips to triangles using
    the tvtk.TriangleFilter class.  This is useful when you have a
    downstream filter that only processes triangles."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.TriangleFilter, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data',
                                         'unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])

