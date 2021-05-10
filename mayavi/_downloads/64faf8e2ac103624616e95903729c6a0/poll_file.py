#!/usr/bin/env python
"""A simple script that polls a data file for changes and then updates
the mayavi pipeline automatically.

This script is to be run like so::

 $ mayavi2 -x poll_file.py

Or::

 $ python poll_file.py

The script currently defaults to using the example data in
examples/data/heart.vtk.  You can try editing that data file or change
this script to point to other data which you can edit.
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006-2020, Enthought Inc.
# License: BSD Style.

# Standard imports.
import os
from os.path import join, abspath, dirname

# Enthought library imports
from mayavi.scripts import mayavi2
from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.modules.outline import Outline
from mayavi.modules.contour_grid_plane import ContourGridPlane
from pyface.timer.api import Timer


######################################################################
# `Pollster` class.
class Pollster(object):
    """Given a file name and a mayavi2 data reader object, this class
    polls the file for any changes and automatically updates the
    mayavi pipeline.
    """
    def __init__(self, fname, data):
        """Initialize the object.

        Parameters:
        -----------
        fname -- filename to poll.
        data -- the MayaVi source object to update.
        """
        self.fname = fname
        self.data = data
        self.last_stat = os.stat(fname)

    def poll_file(self):
        # Check the file's time stamp.
        s = os.stat(self.fname)
        if s[-2] == self.last_stat[-2]:
            return
        else:
            self.last_stat = s
            self.update_pipeline()

    def update_pipeline(self):
        """Override this to do something else if needed.
        """
        print("file changed")
        # Force the reader to re-read the file.
        d = self.data
        d.reader.modified()
        d.update()
        # Propagate the changes in the pipeline.
        d.data_changed = True



def setup_data(fname):
    """Given a VTK file name `fname`, this creates a mayavi2 reader
    for it and adds it to the pipeline.  It returns the reader
    created.
    """
    # 'mayavi' is always defined on the interpreter.
    mayavi.new_scene()
    d = VTKFileReader()
    d.initialize(fname)
    mayavi.add_source(d)
    return d

def view_data():
    """Sets up the mayavi pipeline for the visualization.
    """
    # 'mayavi' is always defined on the interpreter.
    o = Outline()
    mayavi.add_module(o)

    c = ContourGridPlane()
    mayavi.add_module(c)
    c.grid_plane.position = 16
    c.module_manager.scalar_lut_manager.show_scalar_bar = True

@mayavi2.standalone
def main():
    # Change this to suit your needs.  Edit the file after running this
    # script and the pipeline should be updated automatically.

    fname = join(mayavi2.get_data_dir(abspath(dirname(__file__))),
                 'heart.vtk')

    data = setup_data(fname)
    view_data()

    # Poll the file.
    p = Pollster(fname, data)
    timer = Timer(1000, p.poll_file)
    # Keep a reference on the timer
    mayavi2.savedtimerbug = timer

    # To stop polling the file do:
    #timer.Stop()

if __name__ == '__main__':
    main()
