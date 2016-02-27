"""Simple test for the Optional and Collection filters.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestOptionalCollection(TestCase):

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.filters.contour import Contour
        from mayavi.filters.optional import Optional
        from mayavi.filters.collection import Collection
        from mayavi.filters.api import PolyDataNormals
        from mayavi.modules.api import Surface

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
        script.add_filter(coll)
        s = Surface()
        script.add_module(s)

        ########################################
        # do the testing.
        def check(coll):
            """Check if test status is OK given the collection."""
            c, o = coll.filters
            c = c.filter
            n = o.filter
            assert coll.get_output_dataset().point_data.scalars.range == (127.5, 127.5)
            # Adding a contour should create the appropriate output in
            # the collection.
            c.contours.append(200)
            assert coll.get_output_dataset().point_data.scalars.range == (127.5, 200.0)
            # the collection's output should be that of the normals.
            assert coll.get_output_dataset() is n.get_output_dataset()
            # disable the optional filter and check.
            o.enabled = False
            assert 'disabled' in o.name
            assert coll.get_output_dataset() is c.get_output_dataset()
            # Set back everything to original state.
            c.contours.pop()
            o.enabled = True
            assert coll.get_output_dataset().point_data.scalars.range == (127.5, 127.5)
            assert coll.get_output_dataset() is n.get_output_dataset()
            assert 'disabled' not in o.name

        check(coll)

        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene

        # Now do the check.
        coll = s.children[0].children[0]
        check(coll)

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now do the check.
        coll = s.children[0].children[0]
        check(coll)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        # Now do the check.
        coll = s.children[0].children[0]
        check(coll)

        # If we have come this far, we are golden!

if __name__ == "__main__":
    t = TestOptionalCollection()
    t.test()
