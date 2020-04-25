""" Code that looks for mayavi contributions on sys.path or other
standard places, making it easy for users to add contributions to load
on startup.
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Prabhu Ramachandran
# License: BSD Style.

import sys
from os.path import isdir, exists, join
from os import listdir

from traits.api import (HasTraits, List, Str, Instance,
    DelegatesTo, Button)
from traitsui.api import View, Item, SetEditor


################################################################################
# `ContribFinder` class.
################################################################################
class ContribFinder(HasTraits):
    """
    This class helps find installed mayavi contributions.
    """

    # The preference helper whose contrib_packages trait we contribute
    # to.
    preference_helper = Instance(HasTraits)

    # The selected contributions.
    contrib_packages = DelegatesTo('preference_helper')

    # The found contrib packages.
    found_contrib = List(Str, desc='the mayavi contribution '
                                   'packages on the system')

    # Search for contributions.
    search = Button('Search for packages',
                    desc='search again for contributions')

    ########################################
    # View related code.

    view = View(Item('contrib_packages',
                     show_label=False,
                     editor=SetEditor(name='found_contrib',
                                      left_column_title='Available '\
                                                        'contributions',
                                      right_column_title='Selected '\
                                                        'contributions',
                                      can_move_all=False),
                     resizable=True,
                     ),
                 Item('search', show_label=False),
                 resizable=True
                )

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(ContribFinder, self).__init__(**traits)
        # Find the contributions by default.
        self.find()

    ######################################################################
    # `ContribFinder` interface.
    ######################################################################
    def find(self):
        """Find the contrib directories from sys.path."""
        found = []
        for d in sys.path:
            if isdir(d):
                for s in listdir(d):
                    if exists(join(d, s, 'user_mayavi.py')):
                        found.append(s)
        self.found_contrib = found

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _preference_helper_default(self):
        from .preference_manager import preference_manager
        return preference_manager.root

    def _search_fired(self):
        self.find()
