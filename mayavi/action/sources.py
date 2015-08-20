"""An action to open various source files.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import isfile

# Enthought library imports.
from traits.api import Instance, Str
from pyface.api import FileDialog, OK
from pyface.action.api import Action

# Local imports
from mayavi.plugins.script import get_imayavi
from mayavi.core.common import error
from mayavi.core.metadata import Metadata
from mayavi.core.registry import registry

from .filters import new_class

######################################################################
# Utility functions
######################################################################
def get_scene(mayavi):
    """Given a mayavi script instance, get the current scene.  If none
    is available create a new one.
    """
    s = mayavi.engine.current_scene
    if s is None:
        mayavi.engine.new_scene()
        s = mayavi.engine.current_scene
    return s


######################################################################
# `OpenFile` class.
######################################################################
class OpenFile(Action):
    """ An action that opens a data file depending on the supported
    extensions.  """

    tooltip       = "Open a supported data file"

    description   = "Open any supported data file"

    path        =  Str("MenuBar/File/LoadDataMenu")

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = 'All files (*.*)|*.*'
        for src in registry.sources:
            if len(src.extensions) > 0:
                if wildcard.endswith('|') or \
                   src.wildcard.startswith('|'):
                       wildcard += src.wildcard
                else:
                    wildcard += '|' + src.wildcard

        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open supported data file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            # FIXME: Ask for user input if a filetype is unknown and
            # choose appropriate reader.
            src = mv.open(dialog.path)
            if src is not None:
                mv.engine.current_selection = src


######################################################################
# `SourceAction` class.
######################################################################
class SourceAction(Action):

    # The Metadata associated with this particular action.
    metadata = Instance(Metadata)

    def perform(self, event):
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return
        callable = self.metadata.get_callable()
        obj = callable()
        mv.add_source(obj)
        mv.engine.current_selection = obj


######################################################################
# Creating the source actions automatically.
for src in registry.sources:
    if len(src.extensions) == 0:
        d = {'tooltip': src.tooltip,
             'description': src.desc,
             'metadata': src}
        action = new_class(src.id, (SourceAction,), d)
        globals()[src.id] = action

