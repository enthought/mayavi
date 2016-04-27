# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from mayavi.core.common import get_output
from common import TestCase, get_example_data


class TestSetActiveAttribute(TestCase):
    def check(self):
        """Check if the visualization is OK.  Note that this is not an
        image based check, which is very convenient.
        """
        e = self.script.engine
        scene = e.current_scene
        src = scene.children[0]
        assert src.point_scalars_name == 'u'
        c = src.children[1]
        sc = get_output(c.outputs[0]).point_data.scalars
        assert sc.name == 'u'
        # It is an iso-contour!
        assert sc.range[0] == sc.range[1]
        aa = c.children[0].children[0]
        assert aa.point_scalars_name == 't'
        sc = get_output(aa.outputs[0]).point_data.scalars
        assert sc.name == 't'
        assert abs(sc.range[0] - 308) < 1.0
        assert abs(sc.range[1] - 631) < 1.0
        s = aa.children[0].children[0]

    def test(self):
        self.main()

    def do(self):
        """Test for the SetActiveAttribute filter.
        """
        from mayavi.sources.api import VTKXMLFileReader
        from mayavi.filters.contour import Contour
        from mayavi.filters.api import PolyDataNormals
        from mayavi.filters.set_active_attribute import SetActiveAttribute
        from mayavi.modules.api import Surface, Outline

        mayavi = script = self.script

        scene = self.new_scene()
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        mayavi.add_source(r)
        r.point_scalars_name = 'u'
        o = Outline()
        mayavi.add_module(o)
        c = Contour()
        mayavi.add_filter(c)
        n = PolyDataNormals()
        mayavi.add_filter(n)
        aa = SetActiveAttribute()
        mayavi.add_filter(aa)
        aa.point_scalars_name = 't'
        s = Surface()
        mayavi.add_module(s)

        scene.scene.isometric_view()
        # Check if things are OK.
        self.check()

        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        mayavi.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = mayavi.engine
        engine.close_scene(s)

        # Load visualization
        mayavi.load_visualization(f)
        s = engine.current_scene

        # Now do the check.
        s.scene.isometric_view()
        self.check()

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now do the check.
        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        # Now do the check.
        s.scene.isometric_view()
        self.check()

        # If we have come this far, we are golden!

if __name__ == '__main__':
    t = TestSetActiveAttribute()
    t.test()
