import unittest
from io import BytesIO
from os.path import abspath
from unittest.mock import patch

from mayavi import mlab
from .common import get_example_data
from .test_engine_manager import patch_backend


def patch_pyface():
    return patch("mayavi.core.common.pyface", None)


def save_and_reload(engine):
    """Round-trip the current scene through a .mv2, as the GUI would."""
    saved = BytesIO()
    saved.name = abspath('test.mv2')  # save_visualization keys off the name
    engine.save_visualization(saved)
    saved.seek(0)
    engine.close_scene(engine.current_scene)
    engine.load_visualization(saved)
    return engine.current_scene


class TestFilters(unittest.TestCase):
    @patch_pyface()
    @patch_backend('test')
    def test_cell_to_point_data(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        cd = mlab.pipeline.cell_derivatives(src)
        cd.filter.vector_mode = 'compute_vorticity'
        c2p = mlab.pipeline.cell_to_point_data(cd)
        st = mlab.pipeline.streamline(c2p)
        st.update_pipeline()
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_transform_data(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        tf = mlab.pipeline.transform_data(src)
        mlab.pipeline.surface(tf)
        self.assertEqual(tf.outputs[0].class_name, 'vtkTransformFilter')
        self.assertIs(tf.transform, tf.filter.transform)

        tf.transform.translate(1.0, 2.0, 3.0)
        tf.widget.set_transform(tf.transform)
        tf._on_interaction_event(tf.widget, 'InteractionEvent')
        self.assertEqual(tuple(tf.filter.transform.position), (1.0, 2.0, 3.0))

        tf._reset_fired()
        self.assertEqual(tuple(tf.filter.transform.position), (0.0, 0.0, 0.0))
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_transform_data_survives_a_save(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        tf = mlab.pipeline.transform_data(src)
        tf.transform.translate(1.0, 2.0, 3.0)
        tf.widget.set_transform(tf.transform)

        scene = save_and_reload(mlab.get_engine())
        restored = scene.children[0].children[0]
        self.assertEqual(restored.__class__.__name__, 'TransformData')
        self.assertEqual(tuple(restored.transform.position), (1.0, 2.0, 3.0))
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_transform_data_rejects_image_data(self):
        src = mlab.pipeline.open(get_example_data('cube.vti'))
        with self.assertLogs('mayavi', level='ERROR') as logged:
            tf = mlab.pipeline.transform_data(src)
        self.assertIn('not supported', '\n'.join(logged.output))
        self.assertEqual(tf.outputs, [])
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_data_set_clipper(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        clipper = mlab.pipeline.data_set_clipper(src)
        mlab.pipeline.surface(clipper)
        self.assertEqual(clipper.widget.widget_mode, 'Box')
        self.assertEqual(clipper.widget.widget.class_name, 'vtkBoxWidget')

        # each mode swaps in both a widget and the implicit function the
        # clipping filter is driven by
        for mode, widget, function in [
                ('Sphere', 'vtkSphereWidget', 'vtkSphere'),
                ('Plane', 'vtkPlaneWidget', 'vtkPlane'),
                ('ImplicitPlane', 'vtkImplicitPlaneWidget', 'vtkPlane'),
                ('Box', 'vtkBoxWidget', 'vtkPlanes')]:
            with self.subTest(mode):
                clipper.widget.widget_mode = mode
                self.assertEqual(clipper.widget.widget.class_name, widget)
                self.assertEqual(clipper.widget.implicit_function.class_name,
                                 function)
                self.assertIs(clipper.filter.clip_function,
                              clipper.widget.implicit_function)

        clipper.widget.update_implicit_function()
        clipper._reset_button_fired()
        self.assertEqual(clipper.outputs[0].class_name, 'vtkClipDataSet')
        mlab.clf()

    @patch_pyface()
    @patch_backend('test')
    def test_data_set_clipper_update_mode(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        clipper = mlab.pipeline.data_set_clipper(src)
        self.assertEqual(clipper.update_mode, 'semi-interactive')
        clipper.update_mode = 'interactive'
        self.assertEqual(clipper.widget.update_mode, 'interactive')
        clipper.widget._on_interaction_event(clipper.widget.widget,
                                             'InteractionEvent')
        mlab.clf()
