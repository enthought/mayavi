# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest
import numpy
from mayavi.core.null_engine import NullEngine
from mayavi.modules.outline import Outline

class DataReaderTestBase(unittest.TestCase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        raise NotImplementedError()

    def setup_viz(self):
        """Setup the visualization."""
        # Create an outline for the data.
        o = Outline()
        self.e.add_module(o)

    def setUp(self):

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        self.e = e
        s = e.new_scene()
        self.scene = e.current_scene

        self.setup_reader()
        self.setup_viz()
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self, scene, bounds, error = 1.01e-02):
        """Do the actual testing."""

        src = scene.children[0]
        ot = src.children[0].children[0]
        ot.render()  # Flush the pipeline.

        # Check the outline bounds
        got = ot.get_output_dataset().bounds
        msg = "Got: %s; expected: %s"%(got, bounds)
        self.assertEqual(numpy.allclose(got, bounds, atol=error), True, msg)

    def check_saving(self, engine, scene, bounds, error = 1.01e-02):

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        engine.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine.close_scene(scene)

        # Load visualization
        engine.load_visualization(f)
        self.scene = engine.current_scene
        self.check(scene,bounds,error)

    def check_deepcopying(self, scene, bounds, error = 1.01e-02):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################

        # Test if the MayaVi2 visualization can be deep-copied.

        # Pop the source object.
        source = scene.children.pop()
        # Add it back to see if that works without error.
        scene.children.append(source)
        self.check(scene, bounds, error)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        scene.children[0] = source1
        self.check(scene, bounds, error)
