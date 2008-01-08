"""Actions to save and load a MayaVi2 visualization file.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import isfile

# Enthought library imports.
from enthought.pyface.api import FileDialog, OK
from enthought.mayavi.core.common import error

# Local imports
from enthought.mayavi.action.common import WorkbenchAction, get_imayavi


######################################################################
# `SaveVisualization` class.
######################################################################
class SaveVisualization(WorkbenchAction):
    """ An action that saves the current visualization. """

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self):
        """ Performs the action. """
        wildcard = 'MayaVi2 files (*.mv2)|*.mv2|' + FileDialog.WILDCARD_ALL
        dialog = FileDialog(parent=self.window.control,
                            title='Save MayaVi2 file',
                            action='save as', wildcard=wildcard
                            )
        if dialog.open() == OK:
            mv = get_imayavi(self.window)
            mv.save_visualization(dialog.path)

######################################################################
# `LoadVisualization` class.
######################################################################
class LoadVisualization(WorkbenchAction):
    """ An action that loads a visualization from file. """

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self):
        """ Performs the action. """
        wildcard = 'MayaVi2 files (*.mv2)|*.mv2|' + FileDialog.WILDCARD_ALL
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open MayaVi2 file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist"%dialog.path, parent)
                return
            
            mv = get_imayavi(self.window)
            mv.load_visualization(dialog.path)

