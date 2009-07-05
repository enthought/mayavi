"""
Testing the MlabSceneModel
"""
import unittest

from enthought.traits.api import HasTraits, Instance
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel
from enthought.mayavi import mlab

from test_mlab_integration import TestMlabNullEngine

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

        f = mlab.figure()
        test_object = TestObject()
        plt = test_object.scene1.mlab.test_plot3d()
        pts = test_object.scene2.mlab.test_points3d()

        # Check that each figure got the module it should have
        self.assertEqual(plt.scene, test_object.scene1)
        self.assertEqual(pts.scene, test_object.scene2)
        # Check that the current figure was not upset by plotting to the
        # object
        self.assertEqual(mlab.gcf(), f)


if __name__ == '__main__':
    unittest.main()
