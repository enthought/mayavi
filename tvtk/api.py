# Author: Prabhu Ramachandran
# License: BSD style

# The external API for tvtk.

# The version of TVTK that is installed
from tvtk.version import version, version as __version__

# The TVTK pseudo-module.
from tvtk.tvtk_access import tvtk

# Handy colors from VTK.
from vtk.util import colors

# Some miscellaneous functionality.
from tvtk.misc import write_data

from tvtk.tvtk_base import global_disable_update
