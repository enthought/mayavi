""" Tests for the garbage collection of objects in tvtk package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015-2021, Enthought, Inc.
# License: BSD Style.

import sys
import unittest
from traits.etsconfig.api import ETSConfig

from packaging.version import Version

from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.pyface.api import DecoratedScene, Scene
from tvtk.pyface.scene_model import SceneModel
from tvtk.tests.common import TestGarbageCollection

# This should be okay to do once the tvtk.pyface.api.DecoratedScene is imported
bad_pyqt5 = False
if ETSConfig.toolkit in ('qt4', 'qt'):
    import pyface
    from pyface.qt import api_name
    if api_name in ('pyqt', 'pyqt5') and \
            Version(pyface.__version__) < Version('7.5.0.dev0'):
        bad_pyqt5 = True

def skip_pyside6():
    from pyface.qt import qt_api
    if qt_api == 'pyside6':
        raise unittest.SkipTest('Test fails with PySide6.')


class TestTVTKGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """

    @unittest.skipIf(
        sys.platform.startswith('win') or ETSConfig.toolkit == 'null',
        'CI with windows fails due to lack of OpenGL, or toolkit is null, '
        f'got toolkit={ETSConfig.toolkit}'
    )
    def test_tvtk_scene(self):
        """ Tests if TVTK scene can be garbage collected."""
        def create_fn():
            return TVTKScene()

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)

    @unittest.skipIf(ETSConfig.toolkit in ('wx', 'null'),
                     'Test segfaults using WX (issue #216) and fails on null, '
                     f'got toolkit={ETSConfig.toolkit}')
    def test_scene(self):
        """ Tests if Scene can be garbage collected."""
        def create_fn():
            return Scene()

        def close_fn(o):
            o.close()

        self.check_object_garbage_collected(create_fn, close_fn)

    @unittest.skipIf(ETSConfig.toolkit in ('wx', 'null'),
                     'Test segfaults using WX (issue #216) and fails on null, '
                     f'got toolkit={ETSConfig.toolkit}')
    @unittest.skipIf(bad_pyqt5, 'Test segfaults using PyQt5 with older PyFace')
    def test_decorated_scene(self):
        """ Tests if Decorated Scene can be garbage collected."""
        skip_pyside6()

        def create_fn():
            return DecoratedScene(parent=None)

        def close_fn(o):
            o.close()

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_scene_model(self):
        """ Tests if SceneModel can be garbage collected."""
        def create_fn():
            return SceneModel()

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)
