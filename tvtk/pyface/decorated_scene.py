"""A VTK interactor scene which provides a convenient toolbar that
allows the user to set the camera view, turn on the axes indicator
etc.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>,
#          Dave Peterson <dpeterson@enthought.com>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Import the toolkit specific version.
from tvtk.pyface.toolkit import toolkit_object
DecoratedScene = toolkit_object('decorated_scene:DecoratedScene')
