"""Test for the PLOT3D reader and its multiblock capabilities.  This
also tests the SelectOutput filter.
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


class TestPLOT3DReader(TestCase):
    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.plot3d_reader import PLOT3DReader
        from mayavi.filters.select_output import SelectOutput
        from mayavi.modules.outline import Outline

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read the multi-block plot3d file.
        r = PLOT3DReader()
        r.reader.trait_set(has_byte_count=True, multi_grid=True,
                     byte_order='little_endian')
        r.initialize(get_example_data('tiny.xyz'),
                     get_example_data('tiny.q'),
                     configure=False)

        script.add_source(r)

        # Add the filter.
        f = SelectOutput()
        script.add_filter(f)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Check the bounds of the outline.
        assert o.outline_filter.output.bounds == (1.0, 2.0, 1.0, 2.0, 1.0, 2.0)

        # Copy the reader to see if it does not pop up the UI.
        r1 = copy.deepcopy(r)
        script.add_source(r1)
        s.render()

        o1 = r1.children[0].children[0].children[0]
        assert o1.outline_filter.output.bounds == (1.0, 2.0, 1.0, 2.0, 1.0, 2.0)
        r1.children[0].output_index = 1
        assert o1.outline_filter.output.bounds == (2.0, 3.0, 1.0, 2.0, 1.0, 2.0)

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

        o = s.children[0].children[0].children[0].children[0]
        o1 = s.children[1].children[0].children[0].children[0]

        assert o.outline_filter.output.bounds == (1.0, 2.0, 1.0, 2.0, 1.0, 2.0)
        assert o1.outline_filter.output.bounds == (2.0, 3.0, 1.0, 2.0, 1.0, 2.0)

        # If we have come this far, we are golden!
        return


if __name__ == "__main__":
    t = TestPLOT3DReader()
    t.test()


