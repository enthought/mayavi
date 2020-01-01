#!/usr/bin/env python
"""
This script demonstrates using the Mayavi core API to add a VectorCutPlane,
split the pipeline using a MaskPoints filter and then view the filtered data
with the Glyph module.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join, abspath, dirname

# Enthought library imports
from mayavi.scripts import mayavi2
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from mayavi.modules.outline import Outline
from mayavi.modules.glyph import Glyph
from mayavi.modules.vector_cut_plane import VectorCutPlane
from mayavi.filters.mask_points import MaskPoints

@mayavi2.standalone
def glyph():
    """The script itself.  We needn't have defined a function but
    having a function makes this more reusable.
    """
    # 'mayavi' is always defined on the interpreter.
    # Create a new VTK scene.
    mayavi.new_scene()

    # Read a VTK (old style) data file.
    r = VTKXMLFileReader()
    r.initialize(join(mayavi2.get_data_dir(dirname(abspath(__file__))),
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
    m.filter.trait_set(on_ratio=10, random_mode=True)
    mayavi.add_filter(m)

    g = Glyph()
    mayavi.add_module(g)
    # Note that this adds the module to the filtered output.
    g.glyph.scale_mode = 'scale_by_vector'
    # Use arrows to view the scalars.
    gs = g.glyph.glyph_source
    gs.glyph_source = gs.glyph_dict['arrow_source']


if __name__ == '__main__':
    glyph()
