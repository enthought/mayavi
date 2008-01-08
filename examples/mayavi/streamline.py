#!/usr/bin/env mayavi2
"""This script demonstrates how one can script MayaVi to display
streamlines and an iso surface.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# The following *optional* two lines allow a user to call this script
# as either `python script.py` or `mayavi2 script.py`.  These two
# lines must be placed before any other mayavi imports.
from enthought.mayavi.scripts import mayavi2
mayavi2.standalone(globals())

# Standard library imports
from os.path import join, dirname

# Enthought library imports
from enthought.mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from enthought.mayavi.sources.vrml_importer import VRMLImporter
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.modules.streamline import Streamline
from enthought.mayavi.modules.iso_surface import IsoSurface


def setup_data(fname):
    """Given a VTK XML file name `fname`, this creates a mayavi2
    reader for it and adds it to the pipeline.  It returns the reader
    created.
    """
    r = VTKXMLFileReader()
    r.initialize(fname)
    mayavi.add_source(r)
    return r

def show_vrml(fname):
    """Given a VRML file name it imports it into the scene.
    """
    r = VRMLImporter()
    r.initialize(fname)
    mayavi.add_source(r)
    return r

def streamline():
    """Sets up the mayavi pipeline for the visualization.
    """
    # Create an outline for the data.
    o = Outline()
    mayavi.add_module(o)

    s = Streamline(streamline_type='tube')
    mayavi.add_module(s)
    s.stream_tracer.integration_direction = 'both'
    s.seed.widget.center = 3.5, 0.625, 1.25
    s.module_manager.scalar_lut_manager.show_scalar_bar = True

    i = IsoSurface()
    mayavi.add_module(i)
    i.contour.contours[0] = 550
    i.actor.property.opacity = 0.5


if __name__ == '__main__':
    import enthought.mayavi
    mayavi.new_scene()
    vrml_fname = join('data', 'room_vis.wrl')
    r = show_vrml(vrml_fname)

    fname = join('data', 'fire_ug.vtu')
    r = setup_data(fname)
    streamline()
