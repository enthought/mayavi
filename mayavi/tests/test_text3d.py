# Author: Gael Varoquaux <gael dot varoquaux at enthought dot com>
# Copyright (c) 2009-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest
from io import BytesIO
from os.path import abspath

import numpy as np

# Local imports.
from mayavi.core.null_engine import NullEngine
from tvtk.api import tvtk

# Enthought library imports
from mayavi.sources.array_source import ArraySource
from mayavi.modules.text3d import Text3D

class TestText3D(unittest.TestCase):


    def make_data(self):
        """Trivial data """
        return np.zeros((10,10,10))

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()
        self.e=e
        self.s=s

        ############################################################
        # Create a new scene and set up the visualization.

        d = ArraySource()
        sc = self.make_data()
        d.scalar_data = sc

        e.add_source(d)
        self.t = Text3D()
        e.add_module(self.t)

        self.scene = e.current_scene
        return


    def save_and_reload(self):
        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        self.e.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        self.e.close_scene(self.scene)

        # Load visualization
        self.e.load_visualization(f)
        self.scene = self.e.current_scene


    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return



    def test_text3d(self):
        "Test if the text3d has been properly instanciated"
        self.assertTrue(isinstance(self.t, Text3D))


    def test_follower(self):
        """ Test if changing 'orient_to_camera' switches between plain
            actor and follower """
        self.t.orient_to_camera = True
        self.assertTrue(isinstance(self.t.actor.actor, tvtk.Follower))
        self.t.orient_to_camera = False
        self.assertFalse(isinstance(self.t.actor.actor, tvtk.Follower))


    def test_persistence(self):
        # First test persistence without follower
        self.save_and_reload()
        self.t.orient_to_camera = False
        self.assertFalse(isinstance(self.t.actor.actor, tvtk.Follower))
        self.assertFalse(self.t.orient_to_camera)
        self.t.orient_to_camera = True
        self.assertTrue(isinstance(self.t.actor.actor, tvtk.Follower))
        self.save_and_reload()
        self.assertTrue(self.t.orient_to_camera)
        self.assertTrue(isinstance(self.t.actor.actor, tvtk.Follower))

if __name__ == '__main__':
    unittest.main()
