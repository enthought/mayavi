#!/usr/bin/mayavi2
"""This example shows how you can produce contours on an IsoSurface.

WARNING:  If you turn on the visibility of the iso-surface this script
will very likely segfault!
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
from enthought.mayavi.sources.api import VTKXMLFileReader, VTKDataSource
from enthought.mayavi.modules.api import IsoSurface, Surface

def main():
    mayavi.new_scene()
    r = VTKXMLFileReader()
    filename = join(mayavi2.get_data_dir(abspath(__file__)),
                    'fire_ug.vtu')
    r.initialize(filename)
    mayavi.add_source(r)

    iso = IsoSurface()
    mayavi.add_module(iso)
    # Don't show the isosurface if not we run into problems.  Need to
    # figure out how to work around that.
    iso.actor.actor.visibility = False

    # Now get the data of the contours of the IsoSurface and use that as
    # a data source.
    data = iso.contour.outputs[0]
    s = VTKDataSource(data=data)
    mayavi.add_source(s)
    # Select the 'u' scalar to contour
    s.point_scalars_name = 'u'

    # Now view this surface.
    surf = Surface(enable_contours=True)
    mayavi.add_module(surf)


if __name__ == "__main__":
    main()

