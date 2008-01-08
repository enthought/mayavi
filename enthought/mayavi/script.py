"""This represents the scripting API for MayaVi.

The Script class provides a scriptable view of the MayaVi Engine.
Users should really use the mayavi.services.IMAYAVI service to get
hold of a script instance.  However, it is safe to instantiate as many
Script instances as desired.

"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought imports
from enthought.traits.api import HasTraits, Instance

# Local imports
from enthought.mayavi.engine import Engine, get_active_window
from enthought.mayavi.core.common import exception
from enthought.mayavi.services import IMAYAVI_ENGINE, IMAYAVI


##############################################################################
# Utility functions.
##############################################################################
def get_imayavi_engine(application):
    """Returns the MayaVi Engine given the Envisage application.
    """
    return application.get_service(IMAYAVI_ENGINE)

def get_imayavi(application):
    """Given the Envisage application, returns the
    enthought.mayavi.script.Script instance (registered as
    `mayavi.services.IMAYAVI`).
    """
    return application.get_service(IMAYAVI)


##############################################################################
# `Script` class.
##############################################################################
class Script(HasTraits):
    """This class basically presents a scriptable 'view' of the MayaVi
    Engine.  It is registered as the IMayaVi service (via an
    ApplicationObject) because this is the interface users should be
    using when they script.
    """

    # The envisage application.
    application = Instance('enthought.envisage.core.application.Application')

    # The MayaVi engine that we are managing.
    engine = Instance(Engine)

    ######################################################################
    # `Script` interface
    ######################################################################
    def add_source(self, src, scene=None):
        """Adds a given source to the MayaVi pipeline.
        """
        try:
            self.engine.add_source(src, scene=scene)
        except:
            exception()

    def add_module(self, mod, obj=None):
        """Adds a given module to the MayaVi pipeline. Adds it to the selected 
        object, or to an object passed thought the kwarg `obj`.
        """
        try:
            self.engine.add_module(mod, obj=obj)
        except:
            exception()

    def add_filter(self, fil, obj=None):
        """Adds a given filter to the MayaVi pipeline. Adds it to the selected 
        object, or to an object passed thought the kwarg `obj`.
        """
        try:
            self.engine.add_filter(fil, obj=obj)
        except:
            exception()

    def new_scene(self):
        """Creates a new VTK scene window.
        """
        self.engine.new_scene()

    def load_visualization(self, fname):
        """Given a file/file name this loads the visualization.
        """
        try:
            self.engine.load_visualization(fname)
        except:
            exception()

    def save_visualization(self, fname):
        """Given a file or a file name, this saves the current
        visualization to the file.
        """
        try:
            self.engine.save_visualization(fname)
        except:
            exception()

    def get_active_window(self):
        """Get the currently active window."""
        return get_active_window(self.application)

    ######################################################################
    # Non-public interface
    ######################################################################
    def _application_changed(self, app):
        """Traits handler for changes to application.
        """
        self.engine = app.get_service(IMAYAVI_ENGINE)
        
