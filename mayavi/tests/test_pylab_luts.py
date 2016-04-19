import sys
import unittest

from mock import patch


class TestPylabLuts(unittest.TestCase):

    @unittest.skipIf("mayavi.core.lut_manager" in sys.modules,
                     ("mayavi.core.lut_manager is already loaded in "
                      "another tests. If those tests pass, this test "
                      "is automatically fulfilled"))
    @patch("mayavi.core.lut.__file__", "wrong_path/for_lut.py")
    def test_fail_load_pylab_luts(self):
        """ Test if lut_manager can be loaded despite faulty pylab_luts.pkl
        """
        import mayavi.core.lut_manager
