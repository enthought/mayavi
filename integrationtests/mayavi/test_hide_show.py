"""Test for the hide-show feature.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestHideShow(TestCase):

    def check(self, saved=False):
        """Does the checking, if saved is True it does not change the
        properties at first to see how those behave and only tests the
        final unpickled state."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        wrl = scene.children[0]
        src = scene.children[1]
        mm = src.children[0]
        scp = mm.children[0]
        iso = mm.children[1]
        if not saved:
            assert scp.actor.actor.visibility == True
            assert scp.implicit_plane.widget.enabled == True
            for a in wrl.actors:
                assert a.visibility == True

            assert iso.actor.actor.visibility == True

            # Check if widget state is remembered.
            scp.implicit_plane.widget.enabled = False
            scp.visible = False
            assert scp.actor.actor.visibility == False
            assert scp.implicit_plane.widget.enabled == False
            assert scp.name == 'ScalarCutPlane [Hidden]'
            # Reenable it and check widget state.
            scp.visible = True
            assert scp.actor.actor.visibility == True
            assert scp.implicit_plane.widget.enabled == False

            # Reset the visible state.
            wrl.visible = False
            scp.visible = False
            iso.visible = False

        # Check final state.
        for a in wrl.actors:
            assert a.visibility == False
        assert wrl.name.find('[Hidden]') > -1

        assert scp.actor.actor.visibility == False
        assert scp.implicit_plane.widget.enabled == False
        assert scp.name == 'ScalarCutPlane [Hidden]'
        assert iso.name == 'IsoSurface [Hidden]'
        assert iso.actor.actor.visibility == False


    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from mayavi.sources.api import VTKXMLFileReader,\
                VRMLImporter
        from mayavi.modules.api import ScalarCutPlane,\
                IsoSurface

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()
        script = mayavi = self.script

        # Read a VRML file.
        w = VRMLImporter()
        w.initialize(get_example_data('room_vis.wrl'))
        script.add_source(w)

        # Read a VTK data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # Create the modules.
        scp = ScalarCutPlane()
        script.add_module(scp)

        iso = IsoSurface()
        script.add_module(iso)

        # Check.
        self.check(saved=False)

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
        s.scene.isometric_view()

        # Now do the check.
        self.check(saved=True)

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        sources = s.children
        s.children = []
        # Add it back to see if that works without error.
        s.children.extend(sources)
        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        sources1 = copy.deepcopy(sources)
        s.children[:] = sources1
        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        # If we have come this far, we are golden!

if __name__ == "__main__":
    t = TestHideShow()
    t.test()

