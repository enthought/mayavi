#!/usr/bin/env mayavi2
"""This script demonstrates how one can script Mayavi's core API to display
streamlines and an iso surface.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join, abspath, dirname

# Enthought library imports
from mayavi.scripts import mayavi2
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from mayavi.sources.vrml_importer import VRMLImporter
from mayavi.modules.outline import Outline
from mayavi.modules.streamline import Streamline
from mayavi.modules.iso_surface import IsoSurface

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

@mayavi2.standalone
def main():
    mayavi.new_scene()

    data_dir = mayavi2.get_data_dir(dirname(abspath(__file__)))
    vrml_fname = join(data_dir, 'room_vis.wrl')
    r = show_vrml(vrml_fname)

    fname = join(data_dir, 'fire_ug.vtu')
    r = setup_data(fname)
    streamline()


if __name__ == '__main__':
    main()
