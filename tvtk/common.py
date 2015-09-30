"""Common functions and classes.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2015, Enthought, Inc.
# License: BSD Style.

import os
import string
import sys
import re
import vtk

vtk_major_version = vtk.vtkVersion.GetVTKMajorVersion()
vtk_minor_version = vtk.vtkVersion.GetVTKMinorVersion()

######################################################################
# Utility functions.
######################################################################

def get_tvtk_name(vtk_name):
    """Converts a VTK class name to a TVTK class name.

    This function additionally converts any leading digits into a
    suitable string.

    For example:

      >>> get_tvtk_name('vtk3DSImporter')
      'ThreeDSImporter'
      >>> get_tvtk_name('vtkXMLDataReader')
      'XMLDataReader'

    """
    if vtk_name[:3] == 'vtk':
        name = vtk_name[3:]
        dig2name = {'1':'One', '2':'Two', '3':'Three', '4':'Four',
                    '5':'Five', '6': 'Six', '7':'Seven', '8':'Eight',
                    '9': 'Nine', '0':'Zero'}

        if name[0] in string.digits:
            return dig2name[name[0]] + name[1:]
        else:
            return name
    else:
        return vtk_name

def is_old_pipeline():
    return vtk_major_version < 6

def is_version_62_or_later():
    return vtk_major_version == 6 and vtk_minor_version > 1

def is_version_58():
    return vtk_major_version == 5 and vtk_minor_version == 8

def configure_connection(obj, inp):
    """ Configure topology for vtk pipeline obj."""
    if hasattr(inp, 'output_port'):
        obj.input_connection = inp.output_port
    elif inp.has_output_port():
        obj.input_connection = inp.get_output_object()
    else:
        configure_input(obj, inp.outputs[0])

def configure_input_data(obj, data):
    """ Configure the input data for vtk pipeline object obj."""
    if is_old_pipeline():
        obj.input = data
    else:
        obj.set_input_data(data)

def configure_port_input_data(obj, port, data):
    """ Configure the input data for vtk pipeline object obj at port."""
    if is_old_pipeline():
        obj.set_input(port, data)
    else:
        obj.set_input_data(port, data)

def configure_input(inp, op):
    """ Configure the inp using op."""
    if is_old_pipeline():
        if op.is_a('vtkDataSet'):
            inp.input = op
        else:
            inp.input = op.output
    else:
        if hasattr(op, 'output_port'):
            inp.input_connection = op.output_port
        elif op.is_a('vtkAlgorithmOutput'):
            inp.input_connection = op
        elif op.is_a('vtkDataSet'):
            inp.set_input_data(op)
        else:
            raise ValueError('Unknown input type for object %s'%op)

def configure_outputs(obj, tvtk_obj):
    if is_old_pipeline():
        obj.outputs = [tvtk_obj.output]
    else:
        if hasattr(tvtk_obj, 'output_port'):
            obj.outputs = [tvtk_obj.output_port]
        else:
            obj.outputs = [tvtk_obj]

def configure_source_data(obj, data):
    """ Configure the source data for vtk pipeline object obj."""
    if is_old_pipeline():
        obj.source = data
    else:
        if data.is_a('vtkAlgorithmOutput'):
            obj.set_source_connection(data)
        else:
            obj.set_source_data(data)

class _Camel2Enthought:
    """Simple functor class to convert names from CamelCase to
    Enthought compatible names.

    For example::
      >>> camel2enthought = _Camel2Enthought()
      >>> camel2enthought('XMLActor2DToSGML')
      'xml_actor2d_to_sgml'

    """

    def __init__(self):
        self.patn = re.compile(r'([A-Z0-9]+)([a-z0-9]*)')
        self.nd_patn = re.compile(r'(\D[123])_D')
    def __call__(self, name):
        ret = self.patn.sub(self._repl, name)
        ret = self.nd_patn.sub(r'\1d', ret)
        if ret[0] == '_':
            ret = ret[1:]
        return ret.lower()
    def _repl(self, m):
        g1 = m.group(1)
        g2 = m.group(2)
        if len(g1) > 1:
            if g2:
                return '_' + g1[:-1] + '_' + g1[-1] + g2
            else:
                return '_' + g1
        else:
            return '_' + g1 + g2

# Instantiate a converter.
camel2enthought = _Camel2Enthought()
