"""
Handles the configuration for Mayavi. 
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from tconfig import TConfigManager, TConfig
import enthought.traits.api as T

import os

#############################################################################
def get_home():
    """Find user's home directory if possible.
    Otherwise raise error.

    see http://mail.python.org/pipermail/python-list/2005-February/263921.html
    """
    path = ''
    try:
        path = os.path.expanduser("~")
    except:
        pass
    if not os.path.isdir(path):
        for evar in ('HOME', 'USERPROFILE', 'TMP'):
            try:
                path = os.environ[evar]
                if os.path.isdir(path):
                    break
            except: pass
    if path:
        return path
    else:
        raise RuntimeError('please define environment variable $HOME')

config_file_name = get_home() + os.sep + '.mayavi.conf'


##############################################################################
# This is the class declaration for the configuration:
class MayaviConfig(TConfig):
    """Configuration for mayavi."""

    backend = T.Trait('auto', 'envisage', 'simple')
    
#    class mlab(TConfig):
#        """Configuration for mlab."""

        

#############################################################################

config_manager = TConfigManager(MayaviConfig, config_file_name)

# This is the object where the config is actually stored.
options = config_manager.tconf

