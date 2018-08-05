# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk
from vtk.numpy_interface import dataset_adapter as dsa

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `MaskPoints` class.
######################################################################
class MaskPoints(FilterBase):

    """Selectively passes the input points downstream.  This can be
    used to subsample the input points.  Note that this does not pass
    geometry data, this means all grid information is lost.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.MaskPoints, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def update_pipeline(self):
        # FIXME: This is needed, for with VTK-5.10 (for sure), the filter
        # allocates memory for maximum_number_of_points which is impossibly
        # large,  so we set it to the number of points in the input
        # for safety.
        self.filter.maximum_number_of_points = \
            self._find_number_of_points_in_input()
        super(MaskPoints, self).update_pipeline()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _find_number_of_points_in_input(self):
        inp = self.inputs[0].get_output_dataset()
        o = dsa.WrapDataObject(tvtk.to_vtk(inp))
        return o.GetNumberOfPoints()
