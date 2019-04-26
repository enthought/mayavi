# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought Inc.
# License: BSD Style.

import unittest
from pkg_resources import resource_filename

from traits.api import Str, Int, Bool
from apptools.preferences.api import set_default_preferences
from apptools.preferences.api import Preferences, PreferencesHelper
from mayavi.tools.preferences_mirror import PreferencesMirror


class _TestPreference(PreferencesHelper):
    """A simple test preference helper."""
    preferences_path = "test"

    bg = Str
    width = Int
    show = Bool


class ClassNameTest(unittest.TestCase):
    def setUp(self):
        """Called before each test is run"""
        self.preferences = set_default_preferences(Preferences())
        # The filename of the example preferences file.
        pref_file = resource_filename('mayavi.tests',
                                      'test_preference.ini')
        self.preferences.load(pref_file)
        self.pref = _TestPreference()
        self.mirror = PreferencesMirror()
        self.mirror.preferences = self.pref

    def test_mirroring(self):
        """Are the traits properly mirrored?"""
        pref = self.pref
        mirror = self.mirror
        self.assertEqual(pref.bg, mirror.bg)
        self.assertEqual(pref.width, mirror.width)
        self.assertEqual(pref.show, mirror.show)

    def test_sync(self):
        """Does the mirror listen for changes on original preference."""
        pref = self.pref
        mirror = self.mirror
        # Save original state.
        saved = pref.trait_get()
        pref.trait_set(bg = 'white', width=20, show=True)
        self.assertEqual(pref.bg, mirror.bg)
        self.assertEqual(pref.width, mirror.width)
        self.assertEqual(pref.show, mirror.show)
        # Reset preferences back to defaults.
        pref.trait_set(saved)

    def test_no_reverse_sync(self):
        """mirror must not sync changes back to the original preferences."""
        pref = self.pref
        mirror = self.mirror
        saved = pref.trait_get()
        mirror.trait_set(bg = 'white', width=20, show=True)
        self.assertNotEqual(pref.bg, mirror.bg)
        self.assertNotEqual(pref.width, mirror.width)
        self.assertNotEqual(pref.show, mirror.show)
        self.assertEqual(pref.bg, saved['bg'])
        self.assertEqual(pref.width, saved['width'])
        self.assertEqual(pref.show, saved['show'])

    def test_save(self):
        """Are Mirror's preferences saved correctly"""
        pref = self.pref
        mirror = self.mirror
        saved = pref.trait_get()
        mirror.trait_set(bg = 'white', width=20, show=True)
        mirror.save()
        self.assertEqual(pref.bg, mirror.bg)
        self.assertEqual(pref.width, mirror.width)
        self.assertEqual(pref.show, mirror.show)
        # Reset preferences back to defaults.
        pref.trait_set(saved)

if __name__ == '__main__':
    unittest.main()

