#!/usr/bin/env python
"""A simple example of how you can use Mayavi without using Envisage
or the Mayavi Envisage application and do off screen rendering.

On Linux/Mac, with VTK < 5.2, you should see a small black window popup
and disappear, see the section :ref:`offscreen_rendering` to avoid this.
On Win32 you will not see any windows popping up at all. In the end you
should have an offscreen.png image in the same directory with the
rendered visualization.

It can be run as::

    $ python offscreen.py
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from os.path import join, abspath, dirname

# The offscreen Engine.
from mayavi.api import OffScreenEngine

# Usual MayaVi imports
from mayavi.scripts.util import get_data_dir
from mayavi.sources.api import VTKXMLFileReader
from mayavi.modules.api import Outline, ScalarCutPlane, Streamline


def main():
    # Create the MayaVi offscreen engine and start it.
    e = OffScreenEngine()
    # Starting the engine registers the engine with the registry and
    # notifies others that the engine is ready.
    e.start()

    # Create a new scene.
    win = e.new_scene()

    # Now setup a normal MayaVi pipeline.
    src = VTKXMLFileReader()
    src.initialize(join(get_data_dir(dirname(abspath(__file__))),
                        'fire_ug.vtu'))
    e.add_source(src)
    e.add_module(Outline())
    e.add_module(ScalarCutPlane())
    e.add_module(Streamline())
    win.scene.isometric_view()
    # Change the size argument to anything you want.
    win.scene.save('offscreen.png', size=(800, 800))


if __name__ == '__main__':
    main()
