# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance

# Local imports.
from enthought.mayavi.components.contour import Contour
from enthought.mayavi.filters.wrapper import Wrapper

################################################################################
# `Contour` class.
################################################################################ 
class Contour(Wrapper):
    """
    A contour filter that wraps around the Contour component to generate
    iso-surfaces on any input dataset.
    """
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The contour component this wraps.
    filter = Instance(Contour, args=())

