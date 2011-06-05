"""The  Optional filter is one which may be turned on and off and wraps
around any mayavi filter or component.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

from mayavi.filters.wrapper import Wrapper

################################################################################
# `Optional` class.
################################################################################
class Optional(Wrapper):
    """
    This class wraps around any mayavi filter or component and allows a
    user to turn it on or off.
    """

    # This filter should allow us to turn on/off the filter.
    _show_enabled = True

