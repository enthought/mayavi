import unittest

from mock import patch


class TestPylabLuts(unittest.TestCase):

    @patch("mayavi.core.lut.__file__",
           "wrong_path/for_lut.py")
    def test_fail_load_pylab_luts(self):
        """ Test if lut_manager can be loaded despite faulty pylab_luts.pkl
        """
        from mayavi.core.lut_manager import pylab_luts
        self.assertEqual(pylab_luts, {})
