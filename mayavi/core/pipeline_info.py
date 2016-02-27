"""
 Defines the class that describes the information on the inputs and
 outputs of an object in the pipeline.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2016, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import HasTraits, Enum, List

# The list of datasets supported.
DataSet = Enum('none', 'any', 'image_data', 'rectilinear_grid',
               'poly_data', 'structured_grid', 'unstructured_grid')

# Attribute type.
AttributeType = Enum('any', 'cell', 'point', 'none')

# Attribute.
Attribute = Enum('any', 'none', 'scalars', 'vectors', 'tensors')


################################################################################
# Utility functions.
################################################################################
def get_tvtk_dataset_name(dataset):
    """Given a TVTK dataset `dataset` return the string dataset type of
    the dataset.
    """
    result = 'none'
    if hasattr(dataset, 'is_a'):
        if not dataset.is_a('vtkDataSet') and hasattr(dataset, 'output'):
            # FIXME: Use pipeline information to do this correctly.
            dataset = dataset.output
        if dataset.is_a('vtkStructuredPoints') or \
           dataset.is_a('vtkImageData'):
               result = 'image_data'
        elif dataset.is_a('vtkRectilinearGrid'):
            result = 'rectilinear_grid'
        elif dataset.is_a('vtkPolyData'):
            result = 'poly_data'
        elif dataset.is_a('vtkStructuredGrid'):
            result = 'structured_grid'
        elif dataset.is_a('vtkUnstructuredGrid'):
            result = 'unstructured_grid'
        else:
            result = 'none'
    else:
        result = 'none'
    return result


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
