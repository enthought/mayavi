# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy as np
import unittest

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.filters.contour import Contour
from mayavi.filters.optional import Optional
from mayavi.filters.collection import Collection
from mayavi.filters.api import PolyDataNormals
from mayavi.modules.api import Surface
from mayavi.sources.vtk_data_source import VTKDataSource

from mayavi.tests import datasets

class TestOptionalCollection(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e

        sgrid=datasets.generateStructuredGrid()
        src = VTKDataSource(data = sgrid)
        e.add_source(src)

        c = Contour()
        # `name` is used for the notebook tabs.
        n = PolyDataNormals(name='Normals')
        o = Optional(filter=n, label_text='Compute normals')
        coll = Collection(filters=[c, o], name='IsoSurface')
        e.add_filter(coll)
        s = Surface()
        e.add_module(s)
        self.coll = coll
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self,coll):
        """Do the actual testing."""
        scene = self.scene
        """Check if test status is OK given the collection."""
        c, o = coll.filters
        c = c.filter
        n = o.filter

        r = coll.get_output_dataset().point_data.scalars.range

        self.assertEqual(np.allclose(r, (6.09,6.09), atol=1.01e-03), True)
        # Adding a contour should create the appropriate output in
        # the collection.
        c.contours.append(10)
        self.assertEqual(np.allclose(r, [6.09,6.09], atol=1.01e-03), True)
        # the collection's output should be that of the normals.
        self.assertEqual(coll.outputs[0] is n.outputs[0],True)
        # disable the optional filter and check.
        o.enabled = False
        self.assertEqual('disabled' in o.name,True)
        self.assertEqual(coll.outputs[0] is c.outputs[0],True)
        # Set back everything to original state.
        c.contours.pop()
        o.enabled = True
        self.assertEqual(np.allclose(r, (6.09,6.09), atol=1.01e-03), True)
        self.assertEqual(coll.outputs[0] is n.outputs[0], True)
        self.assertEqual('disabled' not in o.name, True)

    def test_optional_collection(self):
        "Test if the test fixture works"
        #Now test.
        coll = self.coll
        self.check(coll)

        #from mayavi.tools.show import show
        #show()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene

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
        coll = self.scene.children[0].children[0]

        self.check(coll)


    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        # Pop the source object.
        s =  self.scene
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        coll = s.children[0].children[0]

        self.check(coll)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        coll = s.children[0].children[0]
        self.check(coll)
        #from mayavi.tools.show import show
        #show()



if __name__ == '__main__':
    unittest.main()
