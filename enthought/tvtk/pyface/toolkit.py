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


# This is set to the root part of the module path for the selected backend.
_toolkit_backend = None


def _init_toolkit():
    """ Initialise the current toolkit. """

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
            break
        except ImportError:
            pass
    else:
        # Try to import the null toolkit but don't set the ETSConfig toolkit
        try:
            be = 'enthought.tvtk.pyface.ui.null.'
            __import__(be + 'init')
            import warnings
            warnings.warn("Unable to import the %s backend for pyface; using the 'null' toolkit instead.")
        except:
            if toolkit:
                raise ImportError("unable to import a pyface backend for the %s toolkit" % toolkit)
            else:
                raise ImportError("unable to import a pyface backend for any of the %s toolkits" % ", ".join(known_toolkits))

    # In case we have just decided on a toolkit, tell everybody else.
    ETSConfig.toolkit = tk

    # Save the imported toolkit module.
    global _toolkit_backend
    _toolkit_backend = be


# Do this once then disappear.
_init_toolkit()
del _init_toolkit


def toolkit_object(name):
    """ Return the toolkit specific object with the given name.  The name
    consists of the relative module path and the object name separated by a
    colon.
    """

    mname, oname = name.split(':')
    be_mname = _toolkit_backend + mname

    class Unimplemented(object):
        """ This is returned if an object isn't implemented by the selected
        toolkit.  It raises an exception if it is ever instantiated.
        """

        def __init__(self, *args, **kwargs):
            raise NotImplementedError("the %s pyface backend doesn't implement %s" % (ETSConfig.toolkit, oname))

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
