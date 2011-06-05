""" This module collects utility code that does not import any
significant envisage/mayavi code but is useful for scripts that use
mayavi.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import sys
from os.path import join, abspath, dirname, isdir

def get_data_dir( example_filename ):
    """ Get the data directory while running an example script.

        Parameters:
        -----------
        example_filename: Path
            absolute path of the example script

    """

    if 'mayavi2' in sys.argv[0]:
        if isdir('data'):
            return 'data'
        filename = sys.argv[-1]
        dir_name = join(dirname(abspath(filename)), 'data')
        if isdir(dir_name):
            return dir_name

        raise Exception('Run example from the example directory')

    else:
        return join(dirname(example_filename), 'data')


