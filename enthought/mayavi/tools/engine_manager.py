"""
Singleton class holding the engine.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from enthought.mayavi.core.engine import Engine

######################################################################
# EngineManager singleton class
class EngineManager(object):
    """ Singleton keeping the engine used by mlab. 
    """

    # The mayavi engine
    engine = None

    @classmethod
    def get_engine(cls):
        if cls.engine is None:
            cls.create_engine()
        return cls.engine

    @classmethod
    def create_engine(cls):
        cls.engine = Engine()
        cls.engine.start()

