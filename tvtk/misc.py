"""Some miscellaneous convenience functionality.
"""
# Author: Prabhu Ramachandran <prabhu_r [at] users.sf.net>
# Copyright (c) 2007,  Enthought, Inc.
# License: BSD Style.

from os.path import splitext

# We import from tvtk.py and not api.py to prevent circular imports.
from tvtk.tvtk_access import tvtk
from tvtk.common import configure_input_data

######################################################################
# Utility functions.
######################################################################
def write_data(dataset, fname, **kwargs):
    """Given a TVTK `dataset` this writes the `dataset` to a VTK XML
    file having file name `fname`.

    If the given file name has no extension, one is automatically picked
    based on the dataset and an XML file is written out.  If the
    filename has a '.vtk' extension an old style VTK file is written.
    If any other extension is specified, an XML file is written out with
    the given extension.

    Any additional keyword arguments are passed to the writer used.
    """

    err_msg = "Can only write tvtk.DataSet instances "\
              "'got %s instead"%(dataset.__class__.__name__)
    assert isinstance(dataset, tvtk.DataSet), err_msg

    # Mapping to determine appropriate extension and writer.
    d2r = {'vtkImageData': ('.vti', tvtk.StructuredPointsWriter),
           'vtkRectilinearGrid': ('.vtr', tvtk.RectilinearGridWriter),
           'vtkStructuredGrid': ('.vts', tvtk.StructuredGridWriter),
           'vtkPolyData': ('.vtp', tvtk.PolyDataWriter),
           'vtkUnstructuredGrid': ('.vtu', tvtk.UnstructuredGridWriter)
           }

    for type in d2r:
        if dataset.is_a(type):
            datatype = d2r[type]
            break

    ext = splitext(fname)[1]
    if ext == '.vtk':
        file_name = fname
        writer = datatype[1]
    elif len(ext) == 0:
        file_name = fname + datatype[0]
        writer = tvtk.XMLDataSetWriter
    else:
        file_name = fname
        writer = tvtk.XMLDataSetWriter

    w = writer(file_name=file_name, **kwargs)
    configure_input_data(w, dataset)
    w.write()
