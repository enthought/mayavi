""" This module helps customize the mayavi install.  It tries to import
any `site_mayavi.py` (anywhere on `sys.path`) or `user_mayavi.py`.  The
`user_mayavi.py` script is found in the users `~/.mayavi2` directory
and this directory is also injected into the path.

It is the users responsibility to import the mayavi registry
(mayavi.registry:registry) and register any new modules or
filters into mayavi using suitable metadata.

If the user desires to contribute any plugins then they may expose a
function called `get_plugins()` which returns a list of plugins that they
wish to add to the default mayavi envisage app.  The user may expose one
set of global plugins in the `site_mayavi` module and another in the
`user_mayavi` module without any problems.

The function `get_custom_plugins` returns a list of all the available
custom plugins.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2015, Prabhu Ramachandran, Enthought, Inc.
# License: BSD Style.

from __future__ import print_function

# Standard library imports.
import sys
import traceback
from os.path import join, exists

# Enthought library imports.
from traits.util.home_directory import get_home_directory
from mayavi.preferences.api import preference_manager

# The functions that return the plugins.
_get_global_plugins = lambda: []
_get_user_plugins = lambda: []

# First try the global mayavi customizations.
try:
    # This will import site_mayavi, so any plugin registrations done
    # there will be run.
    from site_mayavi import get_plugins as _get_global_plugins
except ImportError:
    pass


# Now do any local user level customizations.
#
# The following code obtains any customizations and that are imported
# from a `user_mayavi.py` provided by the user in their  `~/.mayavi2`
# directory.
#
# Note that `~/.mayavi2` is placed in `sys.path` so make sure that you
# choose your module names carefully (so as not to override any common
# module names).

home = get_home_directory()
m2dir = join(home, '.mayavi2')
user_module = join(m2dir, 'user_mayavi.py')
if exists(user_module):
    # Add ~/.mayavi2 to sys.path.
    sys.path.append(m2dir)
    # Doing an import gives user information on any errors.
    import user_mayavi
    try:
        # Now try and import the user defined plugin extension.
        from user_mayavi import get_plugins as _get_user_plugins
    except ImportError:
        # user_mayavi may not be adding any new plugins.
        pass

#  Now handle any contributions that the user has chosen via the
#  preferences.

def _import_contrib(pkg):
    mod = None
    try:
        components = pkg.split('.')
        if len(components) > 1:
            mod_name = '.'.join(components[:-1])
            sym_name = components[-1]
            mod = __import__(mod_name, globals(), locals(), [sym_name], level=0)
            mod = getattr(mod, sym_name)
        else:
            mod_name = components[0]
            mod = __import__(mod_name, globals(), locals(), [mod_name], level=0)
    except Exception:
        print("*"*80)
        traceback.print_exc(file=sys.stdout)
        print("*"*80)
    return mod

def add_contributions():
    """Import any contributions that the user has selected via
    preferences."""
    for pkg in preference_manager.root.contrib_packages:
        _import_contrib(pkg + '.user_mayavi')

def get_contrib_plugins():
    """Get plugins requested by different contributions."""
    plugins = []
    for pkg in preference_manager.root.contrib_packages:
        mod = _import_contrib(pkg + '.user_mayavi')
        if mod is not None and hasattr(mod, 'get_plugins'):
            plugins.extend(mod.get_plugins())
    return plugins

# Import the contributions.
add_contributions()

def get_custom_plugins():
    """Convenience function that returns all customization plugins as a
    list.
    """
    return _get_global_plugins() + _get_user_plugins() + \
           get_contrib_plugins()
