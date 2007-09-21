"""Some miscellaneous convenience functionality.
"""
# Author: Prabhu Ramachandran <prabhu_r [at] users.sf.net>
# Copyright (c) 2007,  Enthought, Inc.
# License: BSD Style.

# We import from tvtk.py and not api.py to prevent circular imports.
from enthought.tvtk.tvtk import tvtk

######################################################################
# Utility functions.
######################################################################
def write_data(dataset, fname):
    """Given a TVTK `dataset` this writes the `dataset` to a VTK XML
    file having file name `fname`.
    """
    err_msg = "Can only write tvtk.DataSet instances "\
              "'got %s instead"%(dataset.__class__.__name__)
    assert isinstance(dataset, tvtk.DataSet), err_msg

    w = tvtk.XMLDataSetWriter(file_name=fname, input=dataset)
    w.write()
    
