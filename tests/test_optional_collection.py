"""Simple test for the Optional and Collection filters.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from StringIO import StringIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestOptionalCollection(TestCase):

    def test(self):
        ############################################################
        # Imports.
        script = self.script
        from enthought.mayavi.sources.vtk_file_reader import VTKFileReader
        from enthought.mayavi.components.contour import Contour
        from enthought.mayavi.filters.optional import Optional
        from enthought.mayavi.filters.collection import Collection 
        from enthought.mayavi.filters.api import PolyDataNormals
        from enthought.mayavi.modules.api import Surface

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(get_example_data('heart.vtk'))
        script.add_source(r)

        c = Contour() 
        # `name` is used for the notebook tabs.
        n = PolyDataNormals(name='Normals') 
        o = Optional(filter=n, label_text='Compute normals')
        coll = Collection(filters=[c, o], name='IsoSurface')
        mayavi.add_filter(coll)
        s = Surface()
        mayavi.add_module(s)

        ########################################
        # do the testing.
        def check():
            """Check if test status is OK."""
            assert coll.outputs[0].point_data.scalars.range == (127.5, 127.5)
            # Adding a contour should create the appropriate output in
            # the collection.
            c.contours.append(200)
            assert coll.outputs[0].point_data.scalars.range == (127.5, 200.0)
            # the collection's output should be that of the normals.
            assert coll.outputs[0] is n.outputs[0]
            # disable the optional filter and check.
            o.enabled = False
            assert 'disabled' in o.name
            assert coll.outputs[0] is c.outputs[0]
            # Set back everything to original state.
            c.contours.pop()
            o.enabled = True
            assert coll.outputs[0].point_data.scalars.range == (127.5, 127.5)
            assert coll.outputs[0] is n.outputs[0]
            assert 'disabled' not in o.name

        check()

        # FIXME:  The Collection and Optional filters cannot be
        # persisted due to the broken nature of our persistence
        # framework.  This should work when we use the new pickle
        # approach.


if __name__ == "__main__":
    t = TestOptionalCollection()
    t.main()

