#!/usr/bin/env mayavi2

"""This script demonstrates the use of a VectorCutPlane, splitting the
pipeline using a MaskPoints filter and then viewing the filtered data
with the Glyph module.
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
from os.path import join, abspath

# Enthought library imports
import enthought.mayavi
from enthought.mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.modules.glyph import Glyph
from enthought.mayavi.modules.vector_cut_plane import VectorCutPlane
from enthought.mayavi.modules.vectors import Vectors
from enthought.mayavi.filters.mask_points import MaskPoints


def glyph():
    """The script itself.  We needn't have defined a function but
    having a function makes this more reusable.
    """
    # 'mayavi' is always defined on the interpreter.
    # Create a new VTK scene.
    mayavi.new_scene()

    # Read a VTK (old style) data file.
    r = VTKXMLFileReader()
    r.initialize(join(mayavi2.get_data_dir(abspath(__file__)),
                      'fire_ug.vtu'))
    mayavi.add_source(r)

    # Create an outline and a vector cut plane.
    mayavi.add_module(Outline())

    v = VectorCutPlane()
    mayavi.add_module(v)
    v.glyph.color_mode = 'color_by_scalar'

    # Now mask the points and show glyphs (we could also use
    # Vectors but glyphs are a bit more generic)
    m = MaskPoints()
    m.filter.set(on_ratio=10, random_mode=True)
    mayavi.add_filter(m)

    g = Glyph()
    mayavi.add_module(g)
    # Note that this adds the module to the filtered output.
    g.glyph.scale_mode = 'scale_by_vector'
    # Use arrows to view the scalars.
    gs = g.glyph.glyph_source
    gs.glyph_source = gs.glyph_list[1]


if __name__ == '__main__':
    glyph()
