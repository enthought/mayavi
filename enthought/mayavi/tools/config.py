"""
Modules dealing with options for mayavi.

This is _very_ temporary. Better will come soon.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from enthought.mayavi.config.config import options
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.menu import NoButtons

def get_engine():
    """ Returns the mayavi engine used to create the visualisations.
    """
    if options.backend == 'envisage':
        from enthought.mayavi.tools.envisage_engine_manager import \
                EngineManager
    elif options.backend == 'auto':
        import sys
        if 'enthought.envisage' in sys.modules:
            from enthought.mayavi.tools.envisage_engine_manager import \
                    EngineManager
        else: 
            from enthought.mayavi.tools.engine_manager import \
                    EngineManager
    else:
        from enthought.mayavi.tools.engine_manager import \
                EngineManager
    return EngineManager.get_engine()

def show_engine():
    """ Show the UI for the mayavi engine used to create the
        visualisations.
    """
    if options.backend == 'envisage':
        # FIXME: This should pop up the relevent envisage view.
        pass
    else:
        from enthought.mayavi.view.engine_view import EngineView
        return EngineView(engine=get_engine()).edit_traits()



