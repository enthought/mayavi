import os
import unittest
from unittest.mock import MagicMock, Mock
import tempfile
import shutil

from mayavi.core.null_engine import NullEngine
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from mayavi.modules.outline import Outline
from mayavi.tests.common import get_example_data
from tvtk.pyface.movie_maker import MovieMaker
from tvtk.pyface.tvtk_scene import TVTKScene


def make_mock_scene():
    """Mocks a scene suitable for testing the movie generation.
    """
    s = Mock(spec=TVTKScene)
    s.foreground = (1,0,0)
    s.off_screen_rendering = True
    mm = MagicMock(spec=MovieMaker)
    s.movie_maker = mm
    return s


class TestFileDataSourceTimestep(unittest.TestCase):
    def setUp(self):

        self.root = tempfile.mkdtemp()
        abc1 = os.path.join(self.root, 'abc_1.vti')
        abc2 = os.path.join(self.root, 'abc_2.vti')
        def1 = os.path.join(self.root, 'def_1.vti')
        def2 = os.path.join(self.root, 'def_2.vti')
        xyz1 = os.path.join(self.root, 'xyz_1.vti')
        cube = get_example_data('cube.vti')
        self.abc1, self.abc2 = abc1, abc2
        self.def1, self.def2 = def1, def2
        self.xyz1 = xyz1
        self.cube = cube
        for i in (abc1, abc2, def1, def2, xyz1):
            shutil.copy(cube, i)

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.engine = e

    def tearDown(self):
        self.engine.stop()
        shutil.rmtree(self.root)

    def test_sync_timesteps_steps_relevant_readers(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        e.add_source(r)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        r2 = VTKXMLFileReader()
        r2.initialize(self.def1)
        e.add_source(r2)

        r3 = VTKXMLFileReader()
        r3.initialize(self.xyz1)
        e.add_source(r3)

        # When
        r.sync_timestep = True
        r.timestep = 1

        # Then
        self.assertEqual(r.timestep, r2.timestep)
        self.assertNotEqual(r.timestep, r3.timestep)
        r.timestep = 0
        self.assertEqual(r.timestep, r2.timestep)

    def test_play_updates_timestep(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        r.timestep = 0
        e.add_source(r)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        r2 = VTKXMLFileReader()
        r2.initialize(self.def1)
        e.add_source(r2)

        # When
        r.play = True

        # Then
        self.assertEqual(r.timestep, 1)
        self.assertEqual(r2.timestep, 0)

    def test_loop_loops_timesteps(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        r.timestep = 0
        e.add_source(r)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        values = []
        def callback(new):
            values.append(new)
            # Shut off so only one loop is done.
            if new == 0:
                r.loop = False
        r.on_trait_change(callback, 'timestep')

        # When
        r.loop = True
        r.play = True

        # Then
        expected = [1, 0, 1]
        self.assertEqual(values, expected)
        self.assertEqual(r.timestep, 1)
        self.assertEqual(r.loop, False)

    def test_play_calls_movie_maker_correctly(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        r.timestep = 0
        e.add_source(r)
        # Mock
        s = make_mock_scene()
        r.scene = s
        mm = s.movie_maker

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        # When
        r.play = True

        # Then
        mm.animation_start.assert_called_once_with()
        self.assertEqual(mm.animation_step.call_count, 1)
        mm.animation_stop.assert_called_once_with()

    def test_update_files_updates_file_list(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        r.timestep = 0
        e.add_source(r)

        self.assertEqual(r._max_timestep, 1)
        self.assertEqual(len(r.file_list), 2)

        # When
        shutil.copy(self.abc1, os.path.join(self.root, 'abc_3.vti'))
        r.update_files = True

        # Then
        self.assertEqual(r._max_timestep, 2)
        self.assertEqual(len(r.file_list), 3)

    def test_update_files_updates_all_file_lists(self):
        # Given
        e = self.engine
        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(self.abc1)
        e.add_source(r)

        r2 = VTKXMLFileReader()
        r2.initialize(self.def1)
        e.add_source(r2)
        r.sync_timestep = True
        r.timestep = 0

        self.assertEqual(r._max_timestep, 1)
        self.assertEqual(len(r.file_list), 2)

        # When
        shutil.copy(self.abc1, os.path.join(self.root, 'abc_3.vti'))
        shutil.copy(self.def1, os.path.join(self.root, 'def_3.vti'))
        r.update_files = True

        # Then
        self.assertEqual(r._max_timestep, 2)
        self.assertEqual(len(r.file_list), 3)
        self.assertEqual(r2._max_timestep, 2)
        self.assertEqual(len(r2.file_list), 3)


if __name__ == '__main__':
    unittest.main()
