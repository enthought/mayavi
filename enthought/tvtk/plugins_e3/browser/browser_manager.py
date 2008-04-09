""" Manage the TVTK pipeline browsers.

I'm actually not sure why this exists!

"""


# Enthought library imports.
from enthought.traits.api import HasTraits, List, Instance


class BrowserManager(HasTraits):
    """ Manage the TVTK pipeline browsers.
    
    I'm actually not sure why this exists!
    
    """

    # A list of all pipeline browser views.
    views = List(
        Instance('enthought.tvtk.plugins_e3.browser.browser_view.BrowserView')
    )

#### EOF ######################################################################



