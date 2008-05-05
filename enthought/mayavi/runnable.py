"""A runnable that creates starts the MayaVi engine and binds the
IMAYAVI (which is a script.Script instance) service to the python
shell (if possible).

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.api import Runnable
from enthought.pyface.timer.api import do_later

# Local imports
from enthought.mayavi.services import IMAYAVI, IMAYAVI_ENGINE

##########################################################################
# `MayaviRunnable` class.
##########################################################################
class MayaviRunnable(Runnable):
    """ A runnable that starts the mayavi engine and binds the IMAYAVI
    service to the python shell."""

    ###########################################################################
    # 'Runnable' interface.
    ###########################################################################

    def run(self, application):
        """ Runs the runnable.  This simply 'starts' the MayaVi Engine
        and adds a callback that is called once the GUI is started.

        """
        engine = application.get_service(IMAYAVI_ENGINE)
        engine.start()
        # Calls the method once the GUI starts.
        do_later(self._bind_to_shell, application)

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _bind_to_shell(self, application):
        """Binds the MayaVi engine instance to the Python shell if
        possible."""
        try:
            ps = application.get_service('enthought.plugins.IPythonShell')
        except SystemError:
            pass
        else:
            mv = application.get_service(IMAYAVI)
            ps.bind('mayavi', mv)
