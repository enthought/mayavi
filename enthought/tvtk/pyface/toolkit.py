#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
# 
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
#------------------------------------------------------------------------------

# Standard library imports.
import sys

# Enthought library imports.
from enthought.etsconfig.api import ETSConfig

# This is set to the toolkit selection.
_toolkit = None

def _init_toolkit():
    """ Initialise the current toolkit. """

    global _toolkit
    if _toolkit is not None:
        return
    
    # Toolkits to check for if none is explicitly specified.
    known_toolkits = ('wx', 'qt4', 'null')

    # Get the toolkit.
    toolkit = ETSConfig.toolkit

    if toolkit:
        toolkits = (toolkit, )
    else:
        toolkits = known_toolkits

    for tk in toolkits:
        # Try and import the toolkit's pyface backend init module.
        be = 'enthought.tvtk.pyface.ui.%s.' % tk

        try:
            __import__(be + 'init')
            # In case we have just decided on a toolkit, tell everybody else.
            ETSConfig.toolkit = tk
            break
        except ImportError:
            pass
    else:
        # Try to import the null toolkit but don't set the ETSConfig toolkit
        try:
            tk = 'null'
            be = 'enthought.tvtk.pyface.ui.%s.' % tk
            __import__(be + 'init')
            import warnings
            warnings.warn("Unable to import the %s backend for pyface; using the 'null' toolkit instead." % ", ".join(toolkits))
        except:
            if toolkit:
                raise ImportError("unable to import a pyface backend for the %s toolkit" % toolkit)
            else:
                raise ImportError("unable to import a pyface backend for any of the %s toolkits" % ", ".join(known_toolkits))

    # Save the imported toolkit name.
    _toolkit = tk


def toolkit_object(name):
    """ Return the toolkit specific object with the given name.  The name
    consists of the relative module path and the object name separated by a
    colon.
    """

    # Set the value of the _toolkit variable. Nothing is done if it is already
    # set.
    _init_toolkit()

    mname, oname = name.split(':')
    be = 'enthought.tvtk.pyface.ui.%s.' % _toolkit
    be_mname = be + mname

    class Unimplemented(object):
        """ This is returned if an object isn't implemented by the selected
        toolkit.  It raises an exception if it is ever instantiated.
        """

        def __init__(self, *args, **kwargs):
            raise NotImplementedError("the %s pyface backend doesn't implement %s" % (be, oname))

    be_obj = Unimplemented

    try:
        __import__(be_mname)

        try:
            be_obj = getattr(sys.modules[be_mname], oname)
        except AttributeError:
            pass
    except ImportError:
        pass

    return be_obj
