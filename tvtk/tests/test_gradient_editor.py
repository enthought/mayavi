"""Tests for the toolkit-independent half of tvtk.util.gradient_editor."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import os
import shutil
import tempfile
import unittest

from tvtk.api import tvtk
from tvtk.util.gradient_editor import (
    Color, ColorControlPoint, GradientTable, hsva_to_rgba, rgba_to_hsva,
)

# one per branch of the conversions: each channel in turn as the maximum,
# both orderings of the other two, plus grey (max == min) and black (v == 0)
COLORS = [
    (1.0, 0.0, 0.0), (1.0, 0.7, 0.0), (0.7, 1.0, 0.0), (0.0, 1.0, 0.3),
    (0.0, 0.6, 1.0), (0.4, 0.0, 1.0), (1.0, 0.0, 0.8), (0.5, 0.5, 0.5),
    (0.0, 0.0, 0.0), (1.0, 1.0, 1.0),
]


class TestColorConversion(unittest.TestCase):
    def test_roundtrip(self):
        for r, g, b in COLORS:
            with self.subTest(rgb=(r, g, b)):
                h, s, v, a = rgba_to_hsva(r, g, b, 0.25)
                for value in (h, s, v):
                    self.assertGreaterEqual(value, 0.0)
                    self.assertLess(value, 1.0 + 1e-10)
                back = hsva_to_rgba(h, s, v, a)
                for expect, got in zip((r, g, b, 0.25), back):
                    self.assertAlmostEqual(expect, got, places=6)

    def test_hue_is_undefined_for_grey(self):
        self.assertEqual(rgba_to_hsva(0.5, 0.5, 0.5, 1.0)[1], 0.0)


class TestColor(unittest.TestCase):
    def test_rgb(self):
        color = Color()
        color.set_rgb(0.0, 1.0, 0.0)
        self.assertEqual(color.get_rgb255(), (0, 255, 0))
        self.assertEqual(color.get_rgba()[3], 1.0)

    def test_hsva(self):
        color = Color()
        color.set_hsva(0.5, 1.0, 1.0, 0.5)
        self.assertEqual(color.get_hsva(), (0.5, 1.0, 1.0, 0.5))

    def test_lerp(self):
        black, white, mid = Color(), Color(), Color()
        black.set_rgba(0.0, 0.0, 0.0, 0.0)
        white.set_rgba(1.0, 1.0, 1.0, 1.0)
        mid.set_lerp(0.5, black, white)
        self.assertAlmostEqual(mid.get_hsva()[2], 0.5)
        self.assertAlmostEqual(mid.get_hsva()[3], 0.5)


class TestColorControlPoint(unittest.TestCase):
    def test_position_is_clamped(self):
        point = ColorControlPoint(active_channels="hsv")
        point.set_pos(1.5)
        self.assertEqual(point.pos, 1.0)
        point.set_pos(-0.5)
        self.assertEqual(point.pos, 0.0)

    def test_alpha_only_channel_stays_alone(self):
        self.assertEqual(ColorControlPoint("a").active_channels, "a")

    def test_activate_channels_does_not_duplicate(self):
        point = ColorControlPoint(active_channels="hsv")
        point.activate_channels("hsva")
        self.assertEqual(sorted(set(point.active_channels)),
                         sorted(point.active_channels))


class TestGradientTable(unittest.TestCase):
    def setUp(self):
        self.table = GradientTable(256)

    def test_default_gradient_runs_black_to_white(self):
        self.assertEqual(self.table.get_color(0.0)[:3], (0.0, 0.0, 0.0))
        self.assertEqual(self.table.get_color(1.0)[:3], (1.0, 1.0, 1.0))

    def test_control_points_stay_sorted(self):
        point = ColorControlPoint(active_channels="hsv")
        point.set_pos(0.2)
        self.table.insert_control_point(point)
        positions = [p.pos for p in self.table.control_points]
        self.assertEqual(positions, sorted(positions))

    def test_get_pos_color(self):
        color = self.table.get_pos_color(1.0)
        self.assertAlmostEqual(color.get_rgba()[2], 1.0)
        self.assertEqual(self.table.get_pos_rgba_color_lerped(0.0),
                         self.table.get_color(0.0))

    def test_store_to_vtk_lookup_table(self):
        lut = tvtk.LookupTable()
        self.table.store_to_vtk_lookup_table(lut, num_entries=32)
        self.assertEqual(lut.number_of_table_values, 32)
        self.assertEqual(tuple(lut.get_table_value(31))[:3], (1.0, 1.0, 1.0))

    def test_volume_prop_roundtrip(self):
        prop = tvtk.VolumeProperty()
        self.table.store_to_vtk_volume_prop(prop, (0.0, 100.0))
        loaded = GradientTable(256)
        loaded.load_from_vtk_volume_prop(prop)
        self.assertEqual(len(loaded.control_points),
                         len(self.table.control_points))
        for before, after in zip(self.table.control_points,
                                 loaded.control_points):
            self.assertAlmostEqual(before.pos, after.pos, places=5)


class TestGradientTableFiles(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp_dir)
        self.table = GradientTable(256)

    def test_save_load_roundtrip(self):
        stem = os.path.join(self.tmp_dir, 'gradient')
        self.table.save(stem)
        self.assertTrue(os.path.exists(stem + '.grad'))
        self.assertTrue(os.path.exists(stem + '.lut'))

        loaded = GradientTable(256)
        loaded.load(stem + '.grad')
        self.assertEqual(len(loaded.control_points),
                         len(self.table.control_points))
        for before, after in zip(self.table.control_points,
                                 loaded.control_points):
            self.assertAlmostEqual(before.pos, after.pos)
            self.assertEqual(before.fixed, after.fixed)
            self.assertEqual(before.active_channels, after.active_channels)
            for expect, got in zip(before.color.get_hsva(),
                                   after.color.get_hsva()):
                self.assertAlmostEqual(expect, got, places=5)

    def test_save_strips_its_own_extensions(self):
        stem = os.path.join(self.tmp_dir, 'gradient')
        self.table.save(stem + '.grad')
        self.assertTrue(os.path.exists(stem + '.grad'))
        self.assertFalse(os.path.exists(stem + '.grad.grad'))

    def test_load_rejects_a_short_line(self):
        path = os.path.join(self.tmp_dir, 'broken.grad')
        with open(path, 'w') as fh:
            fh.write("V 2.0 Color Gradient File\nScalingFunction: \n"
                     "ScalingParameter: 0.5\nControlPoints:\n0.0 True hsva\n")
        with self.assertRaises(ValueError):
            self.table.load(path)
