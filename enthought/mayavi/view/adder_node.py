"""
A custom node for a Tree Editor that provides views for adding various nodes
to the tree.
"""
# Author: Judah De Paula <judah@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.
from enthought.mayavi.core.base import Base
from enthought.traits.api import List

class AdderNode(Base):
    def _get_children_ui_list(self):
        """ Adder Nodes should never have children.
        """
        return []