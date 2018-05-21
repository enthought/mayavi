#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#------------------------------------------------------------------------------
""" Initialize this backend.
"""

# There is nothing for us to initialize, but the toolkit switching code depends
# on the existence of this module.
from pyface.base_toolkit import Toolkit

toolkit_object = Toolkit('tvtk', 'null', 'tvtk.pyface.ui.null')

#### EOF ######################################################################
