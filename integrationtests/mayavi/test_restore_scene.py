"""Simple test for the Optional and Collection filters.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
from numpy import array

from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.modules.api import Surface
from mayavi.tools.camera import view
from apptools.persistence.state_pickler import get_state

# Local imports.
from common import TestCase, get_example_data


class TestRestoreScene(TestCase):

    def test(self):
        self.main()

    def do(self):
        script = self.script

        ############################################################
        # Create a new scene and set up the visualization.
        scene = self.new_scene()

        # Read a VTK (old style) data file.
        source = VTKFileReader()
        source.initialize(get_example_data('heart.vtk'))
        script.add_source(source)

        script.add_module(Surface())

        # In order to test the restoration of visualization properly
        # we should modify the camera
        view(130., 44., 65., [14., 14., 14.])
        
        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # This is the old camera state
        old_camera_state = get_state(scene.scene.camera)

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(scene)

        # Load visualization
        script.load_visualization(f)
        scene = engine.current_scene

        # Now do the check.
        new_camera_state = get_state(scene.scene.camera)

        for attr, new_value in new_camera_state.items():
            if attr.startswith("_"):
                continue
            new_value = array(new_value)
            old_value = array(old_camera_state[attr])
            assert (new_value == old_value).all()
            


if __name__ == "__main__":
    t = TestRestoreScene()
    t.test()

