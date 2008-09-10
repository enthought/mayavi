# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.filter_base import FilterBase
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ExtractTensorComponents` class.
######################################################################
class ExtractTensorComponents(FilterBase):
    """Wraps the TVTK ExtractTensorComponents filter to extract components from
    a tensor field.    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.ExtractTensorComponents, args=(),
                      kw={'pass_tensors_to_output':True,
                          'scalar_mode': 'effective_stress',
                          'extract_scalars': True},
                      allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

