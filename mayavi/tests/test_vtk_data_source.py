# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy
import unittest

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.modules.outline import Outline
from mayavi.modules.iso_surface import IsoSurface
from mayavi.modules.contour_grid_plane import ContourGridPlane
from mayavi.modules.scalar_cut_plane import ScalarCutPlane
from tvtk.api import tvtk

from mayavi.tests import datasets


class TestVTKDataSource(unittest.TestCase):

    def setUp(self):
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        # e = Engine()
        e.start()
        e.new_scene()
        self.e = e

        sgrid = datasets.generateStructuredGrid()
        src = VTKDataSource(data=sgrid)
        e.add_source(src)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp1 = ContourGridPlane()
        e.add_module(cgp1)
        # Set the position to the middle of the data.
        cgp1.grid_plane.position = 15

        # Another with filled contours normal to 'y' axis.
        cgp2 = ContourGridPlane()
        cgp2.contour.filled_contours = True
        # Set the axis and position to the middle of the data.
        cgp2.grid_plane.axis = 'y'
        cgp2.grid_plane.position = 15
        e.add_module(cgp2)

        # An isosurface module.
        iso = IsoSurface(compute_normals=True)
        e.add_module(iso)
        iso.contour.contours = [5]

        # An interactive scalar cut plane.
        cp = ScalarCutPlane()
        e.add_module(cp)
        ip = cp.implicit_plane
        ip.normal = 0, 0, 1
        ip.origin = 0.5, 0.5, 1.0
        # Since this is running offscreen this seems necessary.
        ip.widget.origin = 0.5, 0.5, 1.0
        ip.widget.enabled = False
        self.scene = e.current_scene
        self.cgp2 = cgp2
        self.iso = iso
        self.cp = cp

    def tearDown(self):
        self.e.stop()

    def check(self):
        scene = self.scene
        src = scene.children[0]
        mm = src.children[0]
        cgp1 = mm.children[1]
        self.assertEqual(cgp1.grid_plane.position, 15)

        cgp2 = mm.children[2]
        self.assertEqual(cgp2.contour.filled_contours, True)
        self.assertEqual(cgp2.grid_plane.axis, 'y')
        self.assertEqual(cgp2.grid_plane.position, 15)

        iso = mm.children[3]
        ctr = iso.contour.contours
        self.assertEqual(iso.compute_normals, True)
        self.assertEqual(ctr, [5.0])
        rng = iso.actor.mapper.input.point_data.scalars.range
        self.assertEqual(rng[0], 5.0)
        self.assertEqual(rng[1], 5.0)


        cp = mm.children[4]
        ip = cp.implicit_plane
        self.assertAlmostEqual(numpy.sum(ip.normal - (0, 0, 1)), 1e-16)
        self.assertAlmostEqual(numpy.sum(ip.origin - (0.5, 0.5, 1.0)), 0.0)
        self.assertEqual(ip.widget.enabled, False)

    def test_vtk_data_source(self):

        self.check()

        # from mayavi.tools.show import show
        # show()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2')  # We simulate a file.
        engine.save_visualization(f)
        f.seek(0)  # So we can read this saved data.

        # Remove existing scene.

        engine.close_scene(scene)

        # Load visualization
        engine.load_visualization(f)
        self.scene = engine.current_scene

        self.check()

    def test_deepcopied(self):
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        # Pop the source object.
        s = self.scene
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        cp = source.children[0].children[-1]
        cp.implicit_plane.widget.enabled = False

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        cp = source1.children[0].children[-1]
        cp.implicit_plane.widget.enabled = False
        self.check()

    def test_add_child(self):
        """Test if adding a source as a child works correctly."""
        src = self.e.scenes[0].children[0]
        new_src = VTKDataSource(data=tvtk.PolyData())
        src.add_child(new_src)


class TestVTKDataSourceAttributes(unittest.TestCase):
    def setUp(self):
        sgrid = tvtk.StructuredPoints(
            dimensions=(2, 2, 1), spacing=(1, 1, 1), origin=(0, 0, 0)
        )
        self.sgrid = sgrid

    def test_add_attribute_works_for_point_data(self):
        # Given
        sgrid = self.sgrid
        s1 = numpy.ones(4)
        sgrid.point_data.scalars = s1
        sgrid.point_data.scalars.name = 's1'
        src = VTKDataSource(data=sgrid)
        self.assertEqual(src.point_scalars_name, 's1')
        self.assertEqual(sorted(src._point_scalars_list), ['', 's1'])

        # When
        s2 = s1 + 1.0
        src.add_attribute(s2, 's2')
        v1 = numpy.ones((4, 3))
        src.add_attribute(v1, 'v1')
        t1 = numpy.ones((4, 9))
        src.add_attribute(t1, 't1')

        # Then
        self.assertEqual(src._point_scalars_list, ['', 's1', 's2'])
        self.assertTrue(
            numpy.allclose(src.data.point_data.get_array('s2').to_array(), s2)
        )
        self.assertEqual(src._point_vectors_list, ['', 'v1'])
        self.assertTrue(
            numpy.allclose(src.data.point_data.get_array('v1').to_array(), v1)
        )
        self.assertEqual(src._point_tensors_list, ['', 't1'])
        self.assertTrue(
            numpy.allclose(src.data.point_data.get_array('t1').to_array(), t1)
        )

    def test_add_attribute_works_for_cell_data(self):
        # Given
        sgrid = self.sgrid
        s1 = numpy.ones(4)
        sgrid.cell_data.scalars = s1
        sgrid.cell_data.scalars.name = 's1'
        src = VTKDataSource(data=sgrid)
        self.assertEqual(src.cell_scalars_name, 's1')
        self.assertEqual(sorted(src._cell_scalars_list), ['', 's1'])

        # When
        s2 = s1 + 1.0
        src.add_attribute(s2, 's2', category='cell')
        v1 = numpy.ones((4, 3))
        src.add_attribute(v1, 'v1', category='cell')
        t1 = numpy.ones((4, 9))
        src.add_attribute(t1, 't1', category='cell')

        # Then
        self.assertEqual(src._cell_scalars_list, ['', 's1', 's2'])
        self.assertTrue(
            numpy.allclose(src.data.cell_data.get_array('s2').to_array(), s2)
        )
        self.assertEqual(src._cell_vectors_list, ['', 'v1'])
        self.assertTrue(
            numpy.allclose(src.data.cell_data.get_array('v1').to_array(), v1)
        )
        self.assertEqual(src._cell_tensors_list, ['', 't1'])
        self.assertTrue(
            numpy.allclose(src.data.cell_data.get_array('t1').to_array(), t1)
        )

    def test_add_attribute_raises_errors(self):
        # Given
        sgrid = self.sgrid
        s1 = numpy.ones(4)
        sgrid.point_data.scalars = s1
        sgrid.point_data.scalars.name = 's1'
        src = VTKDataSource(data=sgrid)

        # When/Then
        data = numpy.ones((4, 3, 3))
        self.assertRaises(AssertionError, src.add_attribute, data, 's2')

        data = numpy.ones((4, 5))
        self.assertRaises(AssertionError, src.add_attribute, data, 's2')

    def test_remove_attribute(self):
        # Given
        sgrid = self.sgrid
        s1 = numpy.ones(4)
        sgrid.point_data.scalars = s1
        sgrid.point_data.scalars.name = 's1'
        src = VTKDataSource(data=sgrid)
        self.assertEqual(src.point_scalars_name, 's1')
        self.assertEqual(sorted(src._point_scalars_list), ['', 's1'])

        # When
        s2 = s1 + 1.0
        src.add_attribute(s2, 's2')

        # Then
        self.assertEqual(sorted(src._point_scalars_list), ['', 's1', 's2'])

        # When
        src.remove_attribute('s2')

        # Then
        self.assertEqual(sorted(src._point_scalars_list), ['', 's1'])
        self.assertEqual(src.data.point_data.get_array('s2'), None)

    def test_rename_attribute(self):
        # Given
        sgrid = self.sgrid
        s1 = numpy.ones(4)
        sgrid.point_data.scalars = s1
        sgrid.point_data.scalars.name = 's1'
        src = VTKDataSource(data=sgrid)
        self.assertEqual(src.point_scalars_name, 's1')
        self.assertEqual(sorted(src._point_scalars_list), ['', 's1'])

        # When
        src.rename_attribute('s1', 's2')

        # Then
        self.assertEqual(sorted(src._point_scalars_list), ['', 's2'])
        self.assertTrue(numpy.all(src.data.point_data.get_array('s2') == s1))
        self.assertEqual(src.data.point_data.get_array('s1'), None)


if __name__ == '__main__':
    unittest.main()
