"""Simple tests for the color transfer function utilities in tvtk."""

import unittest

from tvtk.util.ctf import (load_ctfs, save_ctfs, \
        rescale_ctfs, ColorTransferFunction, PiecewiseFunction)
from tvtk.api import tvtk


def make_volume_prop(mins=255, maxs=355):
    """Make a volume property for the testing."""
    table = tvtk.VolumeProperty()
    ctf = ColorTransferFunction()
    ds = (maxs-mins)/4.0
    try:
        ctf.range = (mins, maxs)
    except Exception:
        # VTK versions < 5.2 don't seem to need this.
        pass
    ctf.add_rgb_point(mins,      0.00, 0.0, 1.00)
    ctf.add_rgb_point(mins+ds,   0.25, 0.5, 0.75)
    ctf.add_rgb_point(mins+2*ds, 0.50, 1.0, 0.50)
    ctf.add_rgb_point(mins+3*ds, 0.75, 0.5, 0.25)
    ctf.add_rgb_point(maxs,      1.00, 0.0, 0.00)
    otf = PiecewiseFunction()
    otf.add_point(mins, 0.0)
    otf.add_point(maxs, 0.2)
    table.set_color(ctf)
    table.set_scalar_opacity(otf)
    return table, ctf, otf


################################################################################
# `TestCTFUtil` class.
################################################################################
class TestCTFUtil(unittest.TestCase):
    def setUp(self):
        """Called before every test is run."""
        vp, ctf, otf = make_volume_prop()
        self.vp = vp
        self.ctf = ctf
        self.otf = otf

    def tearDown(self):
        """Called after the test is run."""
        return

    def test_save_load_ctf(self):
        """Test saving and loading of a CTF."""
        # Create a default ctf, save it.
        data = save_ctfs(self.vp)
        # load it into another volume property,
        mvp = tvtk.VolumeProperty()
        ctf = load_ctfs(data, mvp)
        # get the data from the new one
        mdata = save_ctfs(mvp)
        # check that both the data are identical.
        self.assertEqual(mdata, data)

    def test_rescale_ctf(self):
        """Test rescaling a CTF."""
        # Expected data.
        evp, ectf, eotf = make_volume_prop(0.0, 1.0)
        edata = save_ctfs(evp)
        # Rescaled data.
        ctf, otf = rescale_ctfs(self.vp, (0.0, 1.0))
        data = save_ctfs(self.vp)
        # check that both the data are identical.
        self.assertEqual(edata, data)


if __name__ == '__main__':
    unittest.main()

