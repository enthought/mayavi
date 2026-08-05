"""Tests for the CustomGridPlane module and its component."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import unittest

from mayavi import mlab
from mayavi.components.custom_grid_plane import CustomGridPlane
from .common import get_example_data
from .test_engine_manager import patch_backend
from .test_filters import patch_pyface, save_and_reload


class TestCustomGridPlane(unittest.TestCase):
    def grid_plane(self, filename):
        src = mlab.pipeline.open(get_example_data(filename))
        return mlab.pipeline.custom_grid_plane(src).grid_plane

    @patch_pyface()
    @patch_backend('test')
    def test_structured_grid(self):
        # regression test: this read plane.input.whole_extent, which data
        # objects have not had since VTK 6, so every input raised here
        plane = self.grid_plane('SampleStructGrid.vtk')
        self.assertEqual(plane.plane.class_name,
                         'vtkStructuredGridGeometryFilter')
        self.assertEqual((plane._x_low, plane._x_high), (0, 19))
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_image_data(self):
        plane = self.grid_plane('cube.vti')
        self.assertEqual(plane.plane.class_name, 'vtkImageDataGeometryFilter')
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_rectilinear_grid(self):
        plane = self.grid_plane('RectGrid2.vtk')
        self.assertEqual(plane.plane.class_name,
                         'vtkRectilinearGridGeometryFilter')
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_unsupported_dataset(self):
        # driven directly rather than through mlab.pipeline: whether the
        # TypeError reaches the caller or is swallowed by the pipeline depends
        # on the traits exception handler, which other test modules push
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        component = CustomGridPlane()
        component.trait_setq(inputs=[src])
        with self.assertRaises(TypeError):
            component.update_pipeline()
        self.assertIsNone(component.plane)
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_extents_follow_each_other(self):
        plane = self.grid_plane('SampleStructGrid.vtk')
        plane.x_max = 5
        plane.x_min = 8
        # dragging the minimum past the maximum carries the maximum with it
        self.assertEqual(plane.x_max, 8)
        plane.y_min = 4
        plane.y_max = 2
        self.assertEqual(plane.y_min, 2)
        plane.z_min = plane.z_max = 1
        self.assertEqual(tuple(plane.plane.extent),
                         (8, 8, 2, 2, 1, 1))
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_survives_a_save(self):
        plane = self.grid_plane('SampleStructGrid.vtk')
        plane.x_min = plane.x_max = 3

        scene = save_and_reload(mlab.get_engine())
        module = scene.children[0].children[0].children[0]
        self.assertEqual(module.__class__.__name__, 'CustomGridPlane')
        self.assertEqual(module.grid_plane.x_min, 3)
        mlab.clf()


if __name__ == "__main__":
    unittest.main()
