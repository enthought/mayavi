# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.core.registry import registry
from mayavi.sources.plot3d_reader import PLOT3DReader
from mayavi.core.metadata import SourceMetadata
from mayavi.core.pipeline_info import PipelineInfo

# Local Imports
from mayavi.tests.common import get_example_data

class DummyReader(PLOT3DReader):

    def print_info(self):
        """This is a Dummy Reader for Testing Purposes
        Its extended from PLOT3D Reader"""
        pass

    # Callable which always returns false
    @classmethod
    def check_read(cls, filename):
        """ Callable which alwasy returns False
        """
        return False


class TestRegistry(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase
        before any other test method is invoked"""
        e = NullEngine()
        #Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase
        after the test methods have been invoked"""
        self.e.stop()
        return

    def test_unique_reader(self):
        "Check if a file with a unique reader in Mayavi2 can be read"
        e = self.e
        reader = e.open(get_example_data('prism.neu'))
        self.assertNotEqual(reader, None)

    def test_unsupported_file(self):
        "Test if the mechanism to handle unsupported files works fine"
        reader = registry.get_file_reader('junk.abc')
        self.assertEqual(reader, None)

    def test_multipe_readers(self):
        "Test if reader conflict is resolved"
        # Testing two files with same extensions but have to be read
        # by different readers
        reader = registry.get_file_reader(get_example_data('tiny.xyz'))
        callable = reader.get_callable()
        self.assertEqual(callable.__name__, 'PLOT3DReader')

        reader = registry.get_file_reader(get_example_data('thio3xx.xyz'))
        callable = reader.get_callable()
        self.assertEqual(callable.__name__, 'PolyDataReader')

    def test_multiple_valid_readers(self):
        """Test if the fixture works fine if there are multiple readers
        capable of reading the file properly"""
        # Inserting a dummy reader into the registry also capable of
        # reading files with extension 'xyz'
        open_dummy = SourceMetadata(
                id            = "DummyFile",
                class_name    = "mayavi.tests.test_registry.DummyReader",
                menu_name     = "&PLOT3D file",
                tooltip       = "Open a PLOT3D data data",
                desc        = "Open a PLOT3D data data",
                help        = "Open a PLOT3D data data",
                extensions = ['xyz'],
                wildcard = 'PLOT3D files (*.xyz)|*.xyz',
                can_read_test = 'mayavi.tests.test_registry:DummyReader.check_read',
                output_info = PipelineInfo(datasets=['structured_grid'],
                    attribute_types=['any'],
                    attributes=['any'])
                )
        registry.sources.append(open_dummy)
        reader = registry.get_file_reader(get_example_data('tiny.xyz'))
        callable = reader.get_callable()
        self.assertEqual(callable.__name__, 'PLOT3DReader')

        # Removing existing readers for .xyz extensions to check if the Dummy
        # reader now reads it.
        remove = []
        for index, src in enumerate(registry.sources[:]):
            if 'xyz' in src.extensions and src.id != 'DummyFile':
                remove.append((index, src))
                registry.sources.remove(src)

        reader = registry.get_file_reader(get_example_data('tiny.xyz'))
        callable = reader.get_callable()
        self.assertEqual(callable.__name__, 'DummyReader')

        for index, src in remove:
            registry.sources.insert(index, src)
        registry.sources.remove(open_dummy)

    def test_no_valid_reader(self):
        """Test that if there is no reader which can read the file with
        assurity, the registry returns the last one of the readers
        which dont have a can_read_test and claim to read the file with
        the given extension"""
        open_dummy = SourceMetadata(
                id            = "DummyFile",
                class_name    = "mayavi.tests.test_registry.DummyReader",
                menu_name     = "&PLOT3D file",
                tooltip       = "Open a PLOT3D data data",
                desc        = "Open a PLOT3D data data",
                help        = "Open a PLOT3D data data",
                extensions = ['xyz'],
                wildcard = 'PLOT3D files (*.xyz)|*.xyz',
                can_read_test = 'mayavi.tests.test_registry:DummyReader.check_read',
                output_info = PipelineInfo(datasets=['structured_grid'],
                    attribute_types=['any'],
                    attributes=['any'])
                )
        registry.sources.append(open_dummy)

        # Remove the poly data reader.
        for index, src in enumerate(registry.sources[:]):
            if src.id == 'PolyDataFile':
                poly = src
                registry.sources.remove(src)
                break

        reader = registry.get_file_reader(get_example_data('tiny.xyz'))
        callable = reader.get_callable()
        self.assertEqual(callable.__name__, 'PLOT3DReader')

        # Add back the poly data reader.
        registry.sources.insert(index, poly)
        registry.sources.remove(open_dummy)

if __name__ == '__main__':
    unittest.main()
