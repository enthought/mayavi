"""
Testing the MlabSceneModel
"""
import unittest

import numpy as np

from traits.api import HasTraits, Instance
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi import mlab

from mayavi.tests.test_mlab_integration import TestMlabNullEngine

###############################################################################
# class `TestMlabSceneModel`
###############################################################################
class TestMlabSceneModel(TestMlabNullEngine):
    """ Testing the MlabSceneModel, in particular the magic
        mlab attribute.
    """

    def test_several_scene_models(self):
        """ Check that plotting to scene attributes using their
            mlab attribute does create objects as children, and does not
            unset the current scene
        """
        class TestObject(HasTraits):
            scene1 = Instance(MlabSceneModel, ())
            scene2 = Instance(MlabSceneModel, ())

        test_object = TestObject()
        x, y, z = np.random.random((3, 10))
        plt = mlab.plot3d(x, y, z,
                    figure=test_object.scene1.mayavi_scene)
        pts = mlab.points3d(x, y, z,
                    figure=test_object.scene2.mayavi_scene)

        # Check that each figure got the module it should have
        self.assertEqual(plt.scene, test_object.scene1)
        self.assertEqual(pts.scene, test_object.scene2)

if __name__ == '__main__':
    unittest.main()
