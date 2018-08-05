"""Simple test for the ImageDataProbe filter.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

from pyface.api import GUI

# Local imports.
from common import TestCase, get_example_data


class TestLabels(TestCase):

    def check(self, saved=False):
        """Does the checking, if saved is True it does not change the
        properties at first to see how those behave and only tests the
        final unpickled state."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        src = scene.children[0]
        mm = src.children[0]
        l = mm.children[1]
        if not saved:
            np = l.visible_points.get_output_dataset().number_of_points
            assert np < 35 and np > 20
            l.visible_points.enabled = True
            l.mapper.label_mode = 'label_scalars'
            l.label_format = '%.1f'
            l.number_of_labels = 45
            l.property.color = (0, 0, 0)
            l.property.italic = False

        np = l.visible_points.get_output_dataset().number_of_points
        assert np < 60 and np > 25
        assert l.visible_points.enabled
        assert l.visible_points.get_output_dataset() == \
            l.visible_points.filter.filter.output
        assert l.property.color == (0, 0, 0)
        assert not l.property.italic
        assert l.mapper.label_mode == 'label_scalars'
        assert l.label_format == '%.1f'

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from mayavi.modules.api import ScalarCutPlane
        from mayavi.modules.labels import Labels
        from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()
        script = mayavi = self.script

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # Create the filters.
        cp = ScalarCutPlane()
        script.add_module(cp)
        l = Labels(object=cp)
        script.add_module(l)

        s.scene.isometric_view()
        GUI.process_events()
        self.check(saved=False)
        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2')  # We simulate a file.
        script.save_visualization(f)
        f.seek(0)

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene
        s.scene.isometric_view()

        # Seems to be needed for the test to pass. :(  Just flushes the
        # pipeline.
        s.children[0].pipeline_changed = True
        GUI.process_events()

        # Check.
        # Now do the check.
        self.check(saved=True)

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        GUI.process_events()

        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        GUI.process_events()

        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        GUI.process_events()
        # If we have come this far, we are golden!


if __name__ == "__main__":
    t = TestLabels()
    t.test()
