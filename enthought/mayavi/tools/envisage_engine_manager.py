"""
Singleton class holding the engine.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage import get_application

# MayaVi related imports.
from enthought.mayavi.services import IMAYAVI
from enthought.mayavi.app import Mayavi

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
        if (cls.application is None 
                or cls.application.stopped is not None):
            cls.create_engine()
        else:
            m = cls.application.get_service(IMAYAVI)
            cls.engine = m.engine
        return cls.engine

    @classmethod
    def create_engine(cls):
        m = Mayavi()
        m.main()
        mayavi = m.script
        cls.application = get_application()
        cls.engine = mayavi.engine

