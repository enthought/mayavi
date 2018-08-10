import unittest

import vtk
from tvtk.api import tvtk

from mayavi.sources.vtk_object_source import VTKObjectSource
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi import mlab

from .test_mlab_integration import TestMlabNullEngine


class TestVTKObjectSource(TestMlabNullEngine):
    def test_simple_vtk_object_source(self):
        # Given
        cs = tvtk.ConeSource()
        ef = tvtk.ElevationFilter(input_connection=cs.output_port)
        engine = self.e

        # When
        src = VTKObjectSource(object=ef)
        engine.add_source(src)

        # Then
        self.assertEqual(src.outputs[0], ef)
        self.assertEqual(src.browser.root_object, [ef])
        self.assertEqual(src.output_info.datasets, ['poly_data'])
        self.assertEqual(src.name, 'VTK (ElevationFilter)')

        # When
        src.object = cs

        # Then
        self.assertEqual(src.outputs[0], cs)
        self.assertEqual(src.browser.root_object, [cs])
        self.assertEqual(src.output_info.datasets, ['poly_data'])
        self.assertEqual(src.name, 'VTK (ConeSource)')

    def test_data_changed_is_fired_when_object_is_modified(self):
        # Given
        cs = tvtk.ConeSource()

        # When
        src = mlab.pipeline.add_dataset(cs)

        # Then
        self.assertTrue(isinstance(src, VTKObjectSource))

        # When
        self.count = 0

        def callback():
            self.count += 1

        src.on_trait_change(callback, 'data_changed')
        cs.height = 2.0

        # Then
        self.assertTrue(self.count > 0)

    def test_add_dataset_uses_vtk_data_source_for_datasets(self):
        # Given
        pd = tvtk.PolyData()

        # When
        src = mlab.pipeline.add_dataset(pd)

        # Then
        self.assertTrue(isinstance(src, VTKDataSource))

    def test_vtk_object_source_works_with_any_vtk_object(self):
        # Given
        a = tvtk.Actor()

        # When/Then
        src = VTKObjectSource(object=a, actors=[a])

        # Then
        self.assertEqual(src.object, a)
        self.assertEqual(src.output_info.datasets, ['none'])

    def test_add_dataset_uses_vtk_object_source_for_objects(self):
        # Given
        a = tvtk.Actor()

        # When
        src = mlab.pipeline.add_dataset(a)

        # Then
        self.assertTrue(isinstance(src, VTKObjectSource))

        # Given
        a = vtk.vtkActor()

        # When
        src = mlab.pipeline.add_dataset(a)

        # Then
        self.assertTrue(isinstance(src, VTKObjectSource))


if __name__ == '__main__':
    unittest.main()
