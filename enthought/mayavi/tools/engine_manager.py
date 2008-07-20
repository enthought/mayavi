"""
Central registry for figures with mlab.
"""
from enthought.traits.api import HasTraits, List
from enthought.mayavi.preferences.api import preference_manager
from enthought.pyface.api import GUI

from enthought.mayavi.core.registry import registry

options = preference_manager.mlab

from enthought.mayavi.core.engine import Engine

class EngineManager(HasTraits):
    """ Central registry for figures with mlab.

        This is a container for a list of engines having declared
        themselves as usable by mlab.

        This object is meant to be a thin wrapper on top of the different
        Engine classes, making sure that mlab knows how to start an
        engine and get a figure.
    """


    def get_engine(self):
        """ Returns an engine in agreement with the options."""
        engines = registry.engines.values()
        if options.backend == 'auto':
            suitable = engines
        elif options.backend == 'envisage':
            suitable = [e for e in engines 
                                if e.__class__.__name__ == 'EnvisageEngine']
        else:
            suitable = [e for e in engines 
                                if e.__class__.__name__ == 'Engine']
        if len(suitable) == 0:
            return self.new_engine()
        else:
            # Return the most engine add to the list most recently.
            return suitable[-1]

    
    def new_engine(self):
        """ Creates a new engine, envisage or not depending on the
            options.
        """
        if options.backend == 'envisage':
            from enthought.mayavi.plugins.app import Mayavi
            m = Mayavi()
            m.main()
            GUI.process_events()
            engine = m.script.engine
        else:
            engine = Engine(name='Mlab Engine')
            engine.start()
        return engine


    def show_engine(self):
        engine = self.get_engine()
        if engine.__class__.__name__ == 'EnvisageEngine':
            # FIXME: This should pop up the relevent envisage view
            pass
        else:
            from enthought.mayavi.core.ui.engine_view import EngineView
            return EngineView(engine=engine).edit_traits()


engine_manager = EngineManager()

get_engine = engine_manager.get_engine

show_engine = engine_manager.show_engine

