"""
Integration tests of mlab with the null engine.

This also tests some numerics with VTK.
"""

import os
import tempfile
import unittest

import mock

import numpy as np
from numpy.testing import assert_allclose
from traits.testing.unittest_tools import UnittestTools

from mayavi import mlab
from mayavi.core.engine import Engine
from tvtk.api import tvtk
from mayavi.tools.engine_manager import engine_manager
from mayavi.core.registry import registry
from mayavi.tests.common import get_example_data


class TestMlabNullEngine(unittest.TestCase):
    """ Stub mlab to isolate as well as possible from creation of a new
        figure.
    """

    def setUp(self):
        mlab.options.backend = 'test'
        e = mlab.get_engine()
        self.e = e

    def tearDown(self):
        # Check that the NullEngine is still the mlab engine
        current_engine = mlab.get_engine()
        engine_overridden = current_engine is not self.e
        engine_manager.current_engine = None
        self.e.stop()
        registry.unregister_engine(self.e)
        if engine_overridden:
            current_engine.stop()
            registry.unregister_engine(current_engine)
            raise AssertionError("The NullEngine has been overridden")


class TestMlabNullEngineMisc(TestMlabNullEngine):
    """ Misc tests for mlab with the null engine
    """
    def test_contour_filter(self):
        a = np.zeros((3, 3, 3))
        a[1, 1, 1] = 1

        src = mlab.pipeline.scalar_field(a)
        filter = mlab.pipeline.contour(src)

        x, y, z = filter.get_output_dataset().points.to_array().T

        # Check that the contour filter indeed did its work:
        np.testing.assert_almost_equal(x, [2.0,  2.0,  1.5,  2.5,  2.0,  2.0])
        np.testing.assert_almost_equal(y, [2.0,  1.5,  2.0,  2.0,  2.5,  2.0])
        np.testing.assert_almost_equal(z, [1.5,  2.0,  2.0,  2.0,  2.0,  2.5])

        # Check that the filter was not added to a live scene:
        if filter.scene is not None:
            raise AssertionError("The NullEngine seems not to work")

    def test_user_defined_filter(self):
        x, y, z = np.random.random((3, 100))
        src = mlab.pipeline.scalar_scatter(x, y, z)
        density = mlab.pipeline.user_defined(src, filter='GaussianSplatter')

        self.assertEqual(len(density.outputs), 1)
        self.assertTrue(
            isinstance(density.get_output_dataset(), tvtk.ImageData))

    def test_mlab_source(self):
        """ Check that the different objects created by mlab have an
            'mlab_source' attribute.
        """
        # Test for functions taking 3D scalar data
        pipelines = (
            (mlab.pipeline.scalar_scatter, ),
            (mlab.pipeline.scalar_field, ),
            (mlab.pipeline.scalar_field, mlab.pipeline.image_plane_widget),
            (mlab.contour3d, ),
            (mlab.volume_slice, ),
            (mlab.points3d, ), )
        data = np.random.random((3, 3, 3))
        for pipeline in pipelines:
            obj = pipeline[0](data)
            for factory in pipeline[1:]:
                obj = factory(obj)
            self.assertTrue(hasattr(obj, 'mlab_source'))
        # Test for functions taking x, y, z 2d arrays.
        x, y, z = np.random.random((3, 3, 3))
        pipelines = (
            (mlab.mesh, ),
            (mlab.surf, ),
            (mlab.quiver3d, ),
            (mlab.pipeline.vector_scatter, ),
            (mlab.pipeline.vector_scatter,
             mlab.pipeline.extract_vector_components),
            (mlab.pipeline.vector_scatter,
             mlab.pipeline.extract_vector_norm),
            (mlab.pipeline.array2d_source, ), )
        for pipeline in pipelines:
            obj = pipeline[0](x, y, z)
            for factory in pipeline[1:]:
                obj = factory(obj)
            self.assertTrue(hasattr(obj, 'mlab_source'))

    def test_figure(self):
        """ Various tests for mlab.figure().
        """
        # Test when specifying figure instances
        f1 = mlab.figure()
        e = mlab.get_engine()
        self.assertTrue(e.current_scene is f1)
        f2 = mlab.figure()
        self.assertTrue(e.current_scene is f2)
        mlab.figure(f1)
        self.assertTrue(e.current_scene is f1)

        # Test when specifying figure numbers
        f1 = mlab.figure(3)
        self.assertTrue(e.current_scene is f1)
        f2 = mlab.figure(4)
        self.assertTrue(e.current_scene is f2)
        mlab.figure(3)
        self.assertTrue(e.current_scene is f1)

        # Test when specifying figure names
        f1 = mlab.figure('Test 1')
        self.assertTrue(e.current_scene is f1)
        f2 = mlab.figure('Test 2')
        self.assertTrue(e.current_scene is f2)
        mlab.figure('Test 1')
        self.assertTrue(e.current_scene is f1)

    def test_close(self):
        """ Various tests for mlab.close().
        """
        f = mlab.figure()
        self.assertTrue(f.running)
        mlab.close(f)
        self.assertFalse(f.running)

        f = mlab.figure(314)
        self.assertTrue(f.running)
        mlab.close(314)
        self.assertFalse(f.running)

        f = mlab.figure('test_figure')
        self.assertTrue(f.running)
        mlab.close('test_figure')
        self.assertFalse(f.running)

        f = mlab.figure()
        self.assertTrue(f.running)
        mlab.close()
        self.assertFalse(f.running)

        figs = [mlab.figure() for i in range(5)]
        for f in figs:
            self.assertTrue(f.running)
        mlab.close(all=True)
        for f in figs:
            self.assertFalse(f.running)

    def test_triangular_mesh_reset(self):
        """ When reseting the triangular mesh (ie polydata), if we are
            not careful, we can create a segfault by passing triangules
            between points that do not exist.
        """
        # We need to run this as a full test of mlab, rather than only a
        # test of the source, as to get a segfault, we need a module
        # opened on the source.
        n = 100
        triangles = np.c_[
            np.arange(n-3), np.arange(n-3)+1, n-1-np.arange(n-3)]
        x, y, z = np.random.random((3, n))
        src = mlab.triangular_mesh(x, y, z, triangles)

        # Now grow the mesh
        n = 1000
        triangles = np.c_[
            np.arange(n-3), np.arange(n-3)+1, n-1-np.arange(n-3)]
        x, y, z = np.random.random((3, n))
        src.mlab_source.reset(x=x, y=y, z=z, triangles=triangles)

    def test_colorbar(self):
        """ Test that when an object with scalars hidden is created, it
            does not get a colorbar, unless no other is avalaible.
        """
        a = np.random.random((5, 5))
        s1 = mlab.surf(a, colormap='gist_earth')
        s2 = mlab.surf(a, color=(0, 0, 0))
        mlab.colorbar()
        self.assertEqual(
            s2.module_manager.scalar_lut_manager.show_scalar_bar,
            False)
        self.assertEqual(
            s1.module_manager.scalar_lut_manager.show_scalar_bar,
            True)

    def test_source_can_save_output_to_file(self):
        # Given
        x, y, z = np.random.random((3, 100))
        src = mlab.pipeline.scalar_scatter(x, y, z)

        # When
        tmpfname = tempfile.mktemp('.vtk')
        src.save_output(tmpfname)

        # Then
        self.assertTrue(os.path.exists(tmpfname))

        # Cleanup
        if os.path.exists(tmpfname):
            os.remove(tmpfname)

    def test_slice_unstructured_grid(self):
        v = tvtk.Version()
        if v.vtk_major_version < 6 and v.vtk_minor_version < 10:
            raise unittest.SkipTest('Broken on Travis with VTK-5.8?')
        # Given
        src = mlab.pipeline.open(get_example_data('uGridEx.vtk'))
        eg = mlab.pipeline.extract_unstructured_grid(src)
        eg.filter.trait_set(cell_clipping=True, cell_maximum=2)

        # When
        sug = mlab.pipeline.slice_unstructured_grid(eg)

        # Then
        assert_allclose(
            sug.actor.actor.bounds, (1.0, 2.0, 0.0, 1.0, 0.0, 1.0)
        )

    def test_set_active_attribute(self):
        # Given
        x, y = np.mgrid[0:10:100j, 0:10:100j]
        z = x**2 + y**2
        w = np.arctan(x/(y+0.1))

        # Create the data source
        src = mlab.pipeline.array2d_source(z)

        # add second array
        dataset = src.mlab_source.dataset
        scalar_range = dataset.point_data.scalars.range
        array_id = dataset.point_data.add_array(w.T.ravel())
        dataset.point_data.get_array(array_id).name = 'color'
        dataset.point_data.update()

        # select the array from a copy
        # When/Then
        f = mlab.pipeline.set_active_attribute(dataset,
                                               point_scalars='color')
        self.assertFalse(np.allclose(
            f.get_output_dataset().point_data.scalars.range, scalar_range
        ))


class TestMlabPipeline(TestMlabNullEngine):
    """ Test the pipeline functions.
        For vtk versions greater than 5.10, widgets need
        a render window interactor to be set, otherwise an error is raised.
        As such this test checks for the current VTK version and setups a real
        engine for vtk > 5.10 and null engine otherwise.
    """

    def setUp(self):
        ver = tvtk.Version()
        self.less_than_or_equal_to_vtk_5_10 = True
        if ver.vtk_major_version >= 5 and ver.vtk_minor_version > 10:
            self.less_than_or_equal_to_vtk_5_10 = False
        if self.less_than_or_equal_to_vtk_5_10:
            super(TestMlabPipeline, self).setUp()
        else:
            e = Engine()
            e.start()
            mlab.set_engine(e)

    def tearDown(self):
        if self.less_than_or_equal_to_vtk_5_10:
            super(TestMlabPipeline, self).tearDown()
        else:
            for engine in list(registry.engines.keys()):
                registry.unregister_engine(engine)

    def test_probe_data(self):
        """ Test probe_data
        """
        x, y, z = np.mgrid[0:1:10j, 0:1:10j, 0:1:10j]
        r = np.sqrt(x**2 + y**2 + z**2)
        iso = mlab.contour3d(x, y, z, r)
        x_, y_, z_ = np.random.random((3, 10, 4, 2))
        r_ = mlab.pipeline.probe_data(iso, x_, y_, z_)
        np.testing.assert_array_almost_equal(r_,
                                             np.sqrt(x_**2 + y_**2 + z_**2),
                                             decimal=1)
        flow = mlab.flow(x, y, z, x, y, z)
        u_, v_, w_ = mlab.pipeline.probe_data(flow, x_, y_, z_,
                                              type='vectors')
        np.testing.assert_array_almost_equal(u_, x_,
                                             decimal=2)
        np.testing.assert_array_almost_equal(v_, y_,
                                             decimal=2)
        np.testing.assert_array_almost_equal(w_, z_,
                                             decimal=3)


class TestMlabHelperFunctions(TestMlabNullEngine, UnittestTools):
    """ Test various behaviors of the mlab helper functions.
    """

    def test_barchart(self):
        s = np.random.random((10, 10))
        x, y = np.indices(s.shape)
        bar1 = mlab.barchart(x, y, s)
        bar2 = mlab.barchart(s)
        bar3 = mlab.barchart(s, auto_scale=False)

        # Check that auto scaling worked well in the different
        # configurations
        for bar in bar1, bar2, bar3:
            self.assertEqual(bar.glyph.glyph_source.glyph_source.y_length, 0.9)

    def test_imshow(self):
        s = np.random.random((10, 10))
        # This should work.
        mlab.imshow(s)

    def test_imshow_extent(self):
        mlab.imshow(np.random.rand(10, 20),
                    extent=[-1, 11, -1, 21, 0, 0])

    def test_imshow_colormap(self):
        # Check if the pipeline is refreshed when we change colormap.
        # See issue #262
        a = np.random.random_integers(0, 10, (100, 100))

        actor = mlab.imshow(a, colormap="cool")

        with self.assertTraitChanges(actor, 'pipeline_changed'):
            actor.module_manager.scalar_lut_manager.lut_mode = 'jet'

    def test_volume_slice(self):
        x, y, z = np.ogrid[-5:5:20j, -5:5:20j, -5:5:20j]
        scalars = x * x * 0.5 + y * y + z * z * 2.0
        ipw = mlab.volume_slice(scalars, plane_orientation='y_axes')
        self.assertEqual(ipw.ipw.plane_orientation, 'y_axes')


################################################################################
# class `TestMlabModules`
################################################################################
class TestMlabModules(TestMlabNullEngine):
    """ Test the mlab modules.
    """
    def test_volume(self):
        """ Test the mlab volume factory.
        """
        scalars = np.zeros((3, 3, 3))
        scalars[0] = 1
        src = mlab.pipeline.scalar_field(scalars)
        color = (1, 0.1, 0.314)
        vol = mlab.pipeline.volume(src, vmin=0.5, vmax=0.9, color=color)
        # Test the color feature
        for value in np.random.random(10):
            # get_color() will sometimes return .314 as .313999...9995, so we
            # use allclose() to match the tuples.
            np.allclose(vol._ctf.get_color(value), color)
        # Test the vmin and vmax features
        for value in 0.5*np.random.random(10):
            self.assertEqual(vol._otf.get_value(value), 0)
        for value in (0.9+0.1*np.random.random(10)):
            self.assertEqual(vol._otf.get_value(value), 0.2)
        # Test the rescaling of the colormap when using vmin and vmax
        # Rmq: we have to be careful: the range of the ctf can change
        vol1 = mlab.pipeline.volume(src)
        range1 = vol1._ctf.range[1] - vol1._ctf.range[0]
        vol2 = mlab.pipeline.volume(src, vmin=0.25, vmax=0.75)
        range2 = vol2._ctf.range[1] - vol2._ctf.range[0]
        for value in 0.5*np.random.random(10):
            np.testing.assert_array_almost_equal(
                        vol1._ctf.get_color(2*range1*value),
                        vol2._ctf.get_color(0.25+range2*value))
        # Test outside the special [0, 1] range
        src = mlab.pipeline.scalar_field(2*scalars)
        vol1 = mlab.pipeline.volume(src)
        range1 = vol1._ctf.range[1] - vol1._ctf.range[0]
        vol2 = mlab.pipeline.volume(src, vmin=0.5, vmax=1.5)
        range2 = vol2._ctf.range[1] - vol2._ctf.range[0]
        for value in np.random.random(10):
            np.testing.assert_array_almost_equal(
                        vol1._ctf.get_color(2*range1*value),
                        vol2._ctf.get_color(0.5+range2*value))

    def test_text(self):
        """ Test the text module.
        """
        data = np.random.random((3, 3, 3))
        mlab.pipeline.scalar_field(data)
        # Some smoke testing
        mlab.text(0.1, 0.9, 'foo')
        mlab.text(3, 3, 'foo', z=3)
        mlab.title('foo')
        # Check that specifying 2D positions larger than 1 raises an
        # error
        self.assertRaises(ValueError, mlab.text, 0, 1.5, 'test')

    def test_text3d(self):
        """ Test the text3d module.
        """
        data = np.random.random((3, 3, 3))
        mlab.pipeline.scalar_field(data)
        mlab.text3d(
            0, 0, 0, 'foo', opacity=0.5, scale=2,
            orient_to_camera=False, color=(0, 0, 0),
            orientation=(90, 0, 0))

    def test_contour_grid_plane(self):
        """Test the contour_grid_plane.
        """
        data = np.random.random((10, 10, 10))
        src = mlab.pipeline.scalar_field(data)
        mlab.pipeline.outline(src)
        mlab.pipeline.grid_plane(src)
        mlab.pipeline.contour_grid_plane(src)

    def test_barchart(self):
        """Test the barchart function."""

        s = np.abs(np.random.random((3, 3)))
        b = mlab.barchart(s)
        self.assertEqual(b.glyph.glyph.scale_mode,
                         'scale_by_vector_components')
        s += 1
        b.mlab_source.update()
        self.assertEqual(b.glyph.glyph.scale_mode,
                         'scale_by_vector_components')

    def test_axes(self):
        s = mlab.test_plot3d()
        a = mlab.axes(s)
        assert_allclose(
            a.axes.ranges, [-1.5, 1.5, -1.5, 1.5, -0.5, 0.5],
            rtol=0, atol=0.1
        )

################################################################################
# class `TestMlabAnimate`
################################################################################
class TestMlabAnimate(TestMlabNullEngine):

    def test_animate_sets_up_movie_maker(self):
        # Given
        @mlab.animate(ui=False)
        def anim():
            for i in range(5): yield

        self.e.new_scene()
        from mayavi.tests.test_file_timestep import make_mock_scene
        self.e.current_scene.scene = make_mock_scene()
        mm = self.e.current_scene.scene.movie_maker

        # When
        from mayavi.core.file_data_source import NoUITimer
        with mock.patch('mayavi.tools.animator.Timer', NoUITimer):
            a = anim()
            a.timer.Start()

        # Then
        mm.animation_start.assert_called_once_with()
        self.assertEqual(mm.animation_step.call_count, 4)
        mm.animation_stop.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
