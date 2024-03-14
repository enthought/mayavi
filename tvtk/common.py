"""Common functions and classes.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

from contextlib import contextmanager
import string
import re
import vtk

vtk_major_version = vtk.vtkVersion.GetVTKMajorVersion()
vtk_minor_version = vtk.vtkVersion.GetVTKMinorVersion()


######################################################################
# Utility functions.
######################################################################
@contextmanager
def suppress_vtk_warnings():
    """A context manager to suppress VTK warnings.

    This is handy when trying to find something dynamically with VTK.

    **Example**

    with supress_vtk_warnings():
       x = tvtk.VolumeRayCastMapper()

    """
    try:
        obj = vtk.vtkObject()
        obj.GlobalWarningDisplayOff()
        yield
    finally:
        obj.GlobalWarningDisplayOn()


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
    name = vtk_name
    if name.startswith('vtk'):
        name = name[3:]
    return _sanitize_name(name)


def _sanitize_name(name):
    """Turn a VTK name (like a class or method def) into a valid Python var name."""
    dig2name = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
                '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
                '9': 'Nine', '0': 'Zero'}

    if name[0].isdigit():
        name = dig2name[name[0]] + name[1:]
    return name


def is_version_9():
    return vtk_major_version > 8


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
    obj.set_input_data(data)


def configure_port_input_data(obj, port, data):
    """ Configure the input data for vtk pipeline object obj at port."""
    obj.set_input_data(port, data)


def configure_input(inp, op):
    """ Configure the inp using op."""
    if hasattr(op, 'output_port'):
        if hasattr(inp, 'input_connection'):
            inp.input_connection = op.output_port
        elif hasattr(inp, 'set_input_connection'):
            inp.set_input_connection(op.output_port)
    elif op.is_a('vtkAlgorithmOutput'):
        inp.input_connection = op
    elif op.is_a('vtkDataSet'):
        inp.set_input_data(op)
    else:
        raise ValueError('Unknown input type for object %s' % op)


def configure_outputs(obj, tvtk_obj):
    if hasattr(tvtk_obj, 'output_port'):
        obj.outputs = [tvtk_obj.output_port]
    else:
        obj.outputs = [tvtk_obj]


def configure_source_data(obj, data):
    """ Configure the source data for vtk pipeline object obj."""
    if data.is_a('vtkAlgorithmOutput'):
        obj.set_source_connection(data)
    elif hasattr(data, 'output_port'):
        obj.set_source_connection(data.output_port)
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
