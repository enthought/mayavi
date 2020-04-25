"""
 Defines the class that describes the information on the inputs and
 outputs of an object in the pipeline.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import HasTraits, Enum, List

from .utils import get_tvtk_dataset_name

# The list of datasets supported.
DataSet = Enum('none', 'any', 'image_data', 'rectilinear_grid',
               'poly_data', 'structured_grid', 'unstructured_grid')

# Attribute type.
AttributeType = Enum('any', 'cell', 'point', 'none')

# Attribute.
Attribute = Enum('any', 'none', 'scalars', 'vectors', 'tensors')


################################################################################
# `PipelineInfo` class.
################################################################################
class PipelineInfo(HasTraits):

    """
    This class represents the information that a particular input or
    output of an object should contain.
    """

    # The datasets supported by the object.
    datasets = List(DataSet)

    # The attribute types the object works on.
    attribute_types = List(AttributeType)

    # The attributes the object can use/produce.
    attributes = List(Attribute)
