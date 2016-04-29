"""Tests for the tools.camera
"""
import sys
import unittest
from contextlib import contextmanager

from numpy import array
from mayavi import mlab
from mayavi.sources.builtin_image import BuiltinImage

from mayavi.tools import camera as camera_tools

from common import TestCase


@contextmanager
def check_attrs_change(test_case, obj, attrs):
    old_attrs = {attr: array(getattr(obj, attr))
                 for attr in attrs}

    try:
        yield
    finally:
        unchanged = []

        for attr, old_value in old_attrs.items():
            new_value = array(getattr(obj, attr))

            if all(new_value == old_value):
                unchanged.append(attr)

        if unchanged:
            msg = "Expect {} to change.  They stayed the same."
            test_case.fail(msg.format(", ".join(unchanged)))


@contextmanager
def check_attrs_do_not_change(test_case, obj, attrs):
    old_attrs = {attr: array(getattr(obj, attr))
                 for attr in attrs}

    try:
        yield
    finally:
        changed = []

        for attr, old_value in old_attrs.items():
            new_value = array(getattr(obj, attr))

            if any((new_value - old_value) > 1.e-5):
                changed.append((attr, old_value, new_value))

        msg = ("'{0}' changed: \n"
               "old value: {1}  New value: {2}")

        if changed:
            all_messages = "\n".join([msg.format(attr, old, new)
                                      for attr, old, new in changed])
            test_case.fail(all_messages)


class TestCameraUnitTest(unittest.TestCase):

    def setUp(self, figure=None):
        self.engine = mlab.get_engine()
        fig = mlab.figure()
        mlab.pipeline.surface(BuiltinImage(), figure=fig)
        self.camera = self.engine.current_scene.scene.camera

    def tearDown(self):
        mlab.close(all=True)

    def test_move_with_forward(self):
        camera = self.engine.current_scene.scene.camera

        with check_attrs_change(self, camera,
                                ("focal_point", "position", "clipping_range")):
            camera_tools.move(forward=20.)

    def test_camera_move_with_right(self):
        camera = self.engine.current_scene.scene.camera

        with check_attrs_change(self, camera, ("focal_point", "position")), \
                check_attrs_do_not_change(self, camera, ("clipping_range",)):
            camera_tools.move(right=20.)

    def test_camera_move_with_up(self):
        camera = self.engine.current_scene.scene.camera

        with check_attrs_change(self, camera,
                                ("focal_point", "position", "clipping_range")):
            camera_tools.move(up=20.)


class TestCamera(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCameraUnitTest)

        result = unittest.TextTestRunner().run(suite)

        if result.errors or result.failures:
            sys.exit(1)


if __name__ == "__main__":
    t = TestCamera()
    t.test()
