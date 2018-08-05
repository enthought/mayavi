"""Common code used by different components.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2016, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from tvtk.api import tvtk

# Local imports.
from tvtk.common import configure_input
from mayavi.core.component import Component
from mayavi.core.common import error
from mayavi.core.utils import get_new_output


def get_module_source(obj):
    """Given an object (either a component or a module), return the
    ModuleManager managing the module that contains this component.
    """
    o = obj
    while isinstance(o, Component):
        o = o.inputs[0]
    return o


def convert_to_poly_data(obj):
    """Given a VTK dataset object, this returns the data as PolyData.
    This is primarily used to convert the data suitably for filters
    that only work for PolyData.
    """
    data = get_new_output(obj)

    if obj.is_a('vtkPolyData') or data.is_a('vtkPolyData'):
        return obj

    conv = {'vtkStructuredPoints': tvtk.ImageDataGeometryFilter,
            'vtkImageData': tvtk.ImageDataGeometryFilter,
            'vtkRectilinearGrid': tvtk.RectilinearGridGeometryFilter,
            'vtkStructuredGrid': tvtk.StructuredGridGeometryFilter,
            'vtkUnstructuredGrid': tvtk.GeometryFilter,
            'vtkCompositeDataSet': tvtk.CompositeDataGeometryFilter}

    fil = None
    for name, fil_class in conv.items():
        if data.is_a(name):
            fil = fil_class()
            break

    if fil is not None:
        configure_input(fil, obj)
        fil.update()
        return fil
    else:
        error('Given object is not a VTK dataset: %s' % data.__class__.__name__)
