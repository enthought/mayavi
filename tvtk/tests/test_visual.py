import unittest

import numpy as np
from numpy.testing import assert_allclose

from tvtk.tools import visual

def get_bounds(pos, sz):
    pos = np.asarray(pos)
    sz = np.asarray(sz)
    diff = sz*0.5
    bounds = np.zeros(6, dtype=float)
    bounds[::2] = pos - diff
    bounds[1::2] = pos + diff
    return bounds

class DummyScene:
    def __init__(self):
        self.actors = []

    def add_actors(self, *args):
        self.actors.extend(args)

    def remove_actors(self, *args):
        for arg in args:
            self.actors.remove(arg)

    def render(self):
        pass

    def reset_zoom(self):
        pass


class DummyViewer:
    def __init__(self):
        self.scene = DummyScene()


class TestVisual(unittest.TestCase):
    def setUp(self):
        self.viewer = DummyViewer()
        visual.set_viewer(self.viewer)

    def tearDown(self):
        visual.set_viewer(None)

    def test_ring(self):
        # Given
        r = visual.ring()

        # Then
        assert_allclose(r.polydata.bounds, (0.0, 0.0, -0.5, 0.5, -0.5, 0.5))
        self.assertEqual(r.radius, 0.5)
        self.assertEqual(r.tube.radius, 0.01)

        # Given
        r = visual.ring(radius=1.0, pos=(1.0, 1.0, 1.0))

        # When/Then
        self.assertEqual(r.radius, 1.0)
        self.assertEqual(r.thickness, 0.01)
        self.assertEqual(r.tube.radius, 0.01)
        assert_allclose(r.pos, (1.0, 1.0, 1.0))
        assert_allclose(r.polydata.bounds, (1.0, 1.0, 0.0, 2.0, 0.0, 2.0))

        # When
        r.x = 10.0
        # Then
        assert_allclose(r.pos, (10.0, 1.0, 1.0))

        # When
        r = visual.ring(axis=(0., 1., 0.))
        # Then
        assert_allclose(r.polydata.bounds, (-0.5, 0.5, 0.0, 0.0, -0.5, 0.5),
                        atol=1e-8, rtol=0)
        self.assertEqual(r.radius, 0.5)
        self.assertEqual(r.tube.radius, 0.01)

        # When
        r.axis = 1,0,0
        assert_allclose(r.polydata.bounds, (0.0, 0.0, -0.5, 0.5, -0.5, 0.5))

    def test_cone(self):
        # Given
        c = visual.cone()

        # Then
        z = np.sqrt(3)/4
        assert_allclose(c.polydata.bounds,
                        (-0.5, 0.5, -0.5, 0.5, -z, z))
        self.assertEqual(c.radius, 0.5)
        self.assertEqual(c.height, 1.0)

        # When
        c = visual.cone(pos=(1.0, 1.0, 1.0))

        # Then
        z = np.sqrt(3)/4
        assert_allclose(c.polydata.bounds,
                        (0.5, 1.5, 0.5, 1.5, 1-z, 1+z))

        # When
        c = visual.cone(axis=(0, 1, 0), height=2.0)
        # Then
        z = np.sqrt(3)/4
        assert_allclose(c.polydata.bounds,
                        (-0.5, 0.5, -1, 1., -z, z))

    def test_sphere(self):
        # When
        s = visual.sphere()

        # Then

        # The discrete representation of the sphere makes the bounds a bit
        # smaller than one would expect.
        assert_allclose(s.polydata.bounds,
                        (-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), rtol=1e-2)
        self.assertEqual(s.radius, 0.5)

        # When
        s = visual.sphere(pos=(1.0, 1.0, 1.0))
        # Then
        assert_allclose(s.polydata.bounds,
                        (0.5, 1.5, 0.5, 1.5, 0.5, 1.5), rtol=1e-2)

        # When
        s = visual.sphere(x=1.0)
        # Then
        assert_allclose(s.polydata.bounds,
                        (0.5, 1.5, -0.5, 0.5, -0.5, 0.5), rtol=1e-2)

    def test_cylinder(self):
        # When
        c = visual.cylinder(radius=0.5, length=2, pos=(1., 1, 1))

        # Then
        assert_allclose(
            c.polydata.bounds, (1.0, 3.0, 0.5, 1.5, 0.5, 1.5), rtol=1e-2
         )

        # When
        c = visual.cylinder(radius=0.5, length=2, x=1.0)

        # Then
        assert_allclose(
            c.polydata.bounds, (1.0, 3.0, -0.5, 0.5, -0.5, 0.5), rtol=5e-2
         )

    def test_box(self):
        # When
        pos = np.array((1.0, 2.0, 3.0))
        sz = pos.copy()
        b = visual.box(size=tuple(sz), pos=pos)

        # Then
        bounds = get_bounds(pos, sz)
        assert_allclose(b.polydata.bounds, bounds)

        # Given
        b = visual.box()
        orig_bounds = (-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
        assert_allclose(b.polydata.bounds, orig_bounds)
        # When
        b.axis = 1,1,0
        # Then
        x = np.sqrt(2)
        bounds = get_bounds((0.,0,0), (x, x, 1.0))
        assert_allclose(b.polydata.bounds, bounds)

        # When
        b.axis = 1,0,0
        assert_allclose(b.polydata.bounds, orig_bounds)

    def test_arrow(self):
        # Given
        a = visual.arrow()
        # Then
        self.assertEqual(a.radius_cone, 0.08)
        self.assertEqual(a.radius_shaft, 0.03)
        self.assertEqual(a.length_cone, 0.35)
        bounds = get_bounds((0.5, 0.0, 0.0), (1.0, 0.16, 0.14))
        assert_allclose(a.polydata.bounds, bounds, atol=1e-3, rtol=0)

        # When
        a.axis = 0, 0, 1
        # Then
        bounds = get_bounds((0.0, 0.0, 0.5), (0.14, 0.16, 1.0))
        assert_allclose(a.polydata.bounds, bounds, atol=1e-3, rtol=0)

        # Given
        a = visual.arrow(pos=(1.0, 1.0, 1.0))
        # Then
        bounds = get_bounds((1.5, 1.0, 1.0), (1.0, 0.16, 0.14))
        assert_allclose(a.pos, (1., 1., 1.))
        assert_allclose(a.polydata.bounds, bounds, atol=1e-3, rtol=0)

    def test_ellipsoid(self):
        # When
        s = visual.ellipsoid(size=(1.0, 1.0, 1.0), pos=(1., 1., 1.))

        # Then

        # The discrete representation of the sphere makes the bounds a bit
        # smaller than one would expect.
        bounds = get_bounds((1., 1, 1), (1., 1, 1))
        assert_allclose(s.polydata.bounds, bounds, rtol=1e-2)
        self.assertEqual(s.radius, 0.5)

        # Given/When
        s = visual.ellipsoid(size=(1.0, 1.0, 0.5))

        # Then
        bounds = get_bounds((0., 0, 0), (1., 1.0, 0.5))
        assert_allclose(s.polydata.bounds, bounds, rtol=1e-2)
        self.assertEqual(s.length, 1.0)
        self.assertEqual(s.height, 1.0)
        self.assertEqual(s.width, 0.5)

        # Given/When
        s = visual.ellipsoid(length=1.0, height=1.0, width=0.5)

        # Then
        bounds = get_bounds((0., 0, 0), (1., 1.0, 0.5))
        assert_allclose(s.polydata.bounds, bounds, rtol=1e-2)
        assert_allclose(s.size, (1.0, 1.0, 0.5))
        self.assertEqual(s.length, 1.0)
        self.assertEqual(s.height, 1.0)
        self.assertEqual(s.width, 0.5)

    def test_curve(self):
        # Given/When
        c = visual.curve(points=[[0.,0.,0.],[1.,1.,1.]], pos=(1.,1.,1.))

        # Then
        bounds = get_bounds((1.5, 1.5, 1.5), (1.0, 1.0, 1.0))
        assert_allclose(c.polydata.bounds, bounds)

        # When
        c = visual.curve(points=[[0.,0,0],[1.,1,1]], axis=(0., 1, 0))
        # Then
        bounds = get_bounds((-0.5, 0.5, 0.5), (1.0, 1.0, 1.0))
        assert_allclose(c.polydata.bounds, bounds)

    def test_helix(self):
        # Given/When
        h = visual.helix(pos=(1., 1.,1.))

        # Then
        bounds = get_bounds((1.5, 1.0, 1.0), (1.0, 0.4, 0.4))
        assert_allclose(h.polydata.bounds, bounds, atol=3e-2, rtol=0)

        # Given/When
        h.axis = 0., 1., 0.
        # Then
        bounds = get_bounds((1.0, 1.5, 1.0), (0.4, 1.0, 0.4))
        assert_allclose(h.polydata.bounds, bounds, atol=3e-2, rtol=0)

        # Given/When
        h.axis = 1, 0, 0
        # Then
        bounds = get_bounds((1.5, 1.0, 1.0), (1.0, 0.4, 0.4))
        assert_allclose(h.polydata.bounds, bounds, atol=3e-2, rtol=0)

    def test_frame(self):
        # Given
        s = visual.sphere()
        a = visual.arrow()
        f = visual.frame(s, a)

        # Then
        axis = (1.0, 0, 0)
        assert_allclose(s.axis, axis, rtol=0, atol=1e-15)
        assert_allclose(a.axis, axis, rtol=0, atol=1e-15)
        assert_allclose(f.axis, axis, rtol=0, atol=1e-15)

        # When
        axis = (0, 1.0, 0.0)
        f.axis = axis

        # Then
        assert_allclose(s.axis, axis, rtol=0, atol=1e-15)
        assert_allclose(a.axis, axis, rtol=0, atol=1e-15)
        assert_allclose(f.axis, axis, rtol=0, atol=1e-15)

        # When
        pos = (1., 1.0, 1.0)
        f.pos = pos

        # Then
        assert_allclose(s.pos, pos, rtol=0, atol=1e-15)
        assert_allclose(a.pos, pos, rtol=0, atol=1e-15)
        assert_allclose(f.pos, pos, rtol=0, atol=1e-15)

if __name__ == '__main__':
    unittest.main()
