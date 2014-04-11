"""Common code used by different components.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from tvtk.api import tvtk

# Local imports.
from tvtk.common import configure_input_data
from mayavi.core.component import Component
from mayavi.core.common import error


def get_module_source(obj):
    """Given an object (either a component or a module), return the
    ModuleManager managing the module that contains this component.
    """
    o = obj
    while isinstance(o, Component):
        o = o.inputs[0]
    return o


def convert_to_poly_data(data):
    """Given a VTK dataset object, this returns the data as PolyData.
    This is primarily used to convert the data suitably for filters
    that only work for PolyData.
    """
    if data.is_a('vtkPolyData'):
        return data

    conv = {'vtkStructuredPoints': tvtk.ImageDataGeometryFilter,
            'vtkImageData': tvtk.ImageDataGeometryFilter,
            'vtkRectilinearGrid': tvtk.RectilinearGridGeometryFilter,
            'vtkStructuredGrid': tvtk.StructuredGridGeometryFilter,
            'vtkUnstructuredGrid':tvtk.GeometryFilter}

    fil = None
    for name, fil_class in conv.items():
        if data.is_a(name):
            fil = fil_class()
            break

    if fil is not None:
        configure_input_data(fil, data)
        fil.update()
        return fil.output
    else:
        error('Given object is not a VTK dataset: %s'%data.__class__.__name__)

