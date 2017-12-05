"""Displays different types of glyphs oriented and colored as per
vector data at the input points.  This is merely a convenience module
that is entirely based on the Glyph module.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Local imports
from mayavi.modules.glyph import Glyph

######################################################################
# `Vectors` class.
######################################################################
class Vectors(Glyph):

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        super(Vectors, self).setup_pipeline()
        self.glyph.trait_set(scale_mode='scale_by_vector',
                       color_mode='color_by_vector',
                       show_scale_mode=False)
        self.glyph.glyph_source.glyph_position='tail'
