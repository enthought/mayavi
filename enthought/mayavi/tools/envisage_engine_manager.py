"""
Singleton class holding the engine.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.api import Service
from enthought.pyface.api import GUI

# MayaVi related imports.
from enthought.mayavi.plugins_e3.script import Script
from enthought.mayavi.plugins_e3.app import Mayavi

def get_application():
    return Service.application

######################################################################
# EngineManager singleton class
class EngineManager(object):
    """ Singleton to store a pointer to the engine to be used by mlab.
    """

    # The mayavi engine
    engine = None

    # The envisage application, if any.
    application = None

    @classmethod
    def get_engine(cls):
        cls.application = get_application()
        # FIXME: need a way to determine if an app is running or not.
        if (cls.application is None): 
                #or cls.application.stopped is not None):
            cls.create_engine()
        else:
            app = cls.application
            m = app.workbench.active_window.get_service(Script)
            cls.engine = m.engine
        return cls.engine

    @classmethod
    def create_engine(cls):
        m = Mayavi()
        m.main()
        GUI.process_events()
        mayavi = m.script
        cls.application = get_application()
        cls.engine = mayavi.engine

