#!/usr/bin/mayavi2
"""This example shows how you can produce contours on an IsoSurface.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# The following *optional* two lines allow a user to call this script
# as either `python script.py` or `mayavi2 script.py`.  These two
# lines must be placed before any other mayavi imports.
from enthought.mayavi.scripts import mayavi2
mayavi2.standalone(globals())

# Standard library imports
from os.path import join, abspath

# Mayavi imports.
from enthought.mayavi.sources.api import VTKXMLFileReader
from enthought.mayavi.filters.contour import Contour
from enthought.mayavi.filters.api import PolyDataNormals
from enthought.mayavi.filters.set_active_attribute import SetActiveAttribute
from enthought.mayavi.modules.api import Surface, Outline

def main():
    mayavi.new_scene()

    # Read the example data: fire_ug.vtu.
    r = VTKXMLFileReader()
    filename = join(mayavi2.get_data_dir(abspath(__file__)),
                    'fire_ug.vtu')
    r.initialize(filename)
    mayavi.add_source(r)
    # Set the active point scalars to 'u'.
    r.point_scalars_name = 'u'

    # Simple outline for the data.
    o = Outline()
    mayavi.add_module(o)

    # Branch the pipeline with a contour -- the outline above is
    # directly attached to the source whereas the contour below is a
    # filter and will branch the flow of data.   An isosurface in the
    # 'u' data attribute is generated and normals generated for it.

    c = Contour()
    mayavi.add_filter(c)
    n = PolyDataNormals()
    mayavi.add_filter(n)

    # Now we want to show the temperature 't' on the surface of the 'u'
    # iso-contour.  This is easily done by using the SetActiveAttribute
    # filter below.

    aa = SetActiveAttribute()
    mayavi.add_filter(aa)
    aa.point_scalars_name = 't'

    # Now view the iso-contours of 't' with a Surface filter.
    s = Surface(enable_contours=True)
    mayavi.add_module(s)


if __name__ == "__main__":
    main()

