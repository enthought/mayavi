"""
Central registry for figures with mlab.
"""

# Enthought librairies imports
from enthought.traits.api import HasTraits, Instance
from enthought.pyface.api import GUI

# Local imports
from enthought.mayavi.preferences.api import preference_manager
from enthought.mayavi.core.registry import registry
from enthought.mayavi.core.engine import Engine
from preferences_mirror import PreferencesMirror

# The mlab options.
options = PreferencesMirror()
options.preferences = preference_manager.mlab


class EngineManager(HasTraits):
    """ Central registry for figures with mlab.

        This is a container for a list of engines having declared
        themselves as usable by mlab.

        This object is meant to be a thin wrapper on top of the different
        Engine classes, making sure that mlab knows how to start an
        engine and get a figure.
    """

    current_engine = Instance(Engine)

    def get_engine(self):
        """ Returns an engine in agreement with the options."""
        if not self.current_engine is None:
            engines = list((self.current_engine,))
        else:
            engines = list()
        engines.extend(registry.engines.values())
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

    def set_engine(self, engine):
        """ Sets the mlab engine.
        """
        self.current_engine = engine


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
        self.current_engine = engine
        return engine


    def find_figure_engine(self, fig):
        """ Find the engine corresponding to a given mayavi scene.
        """
        for engine in registry.engines.values():
            if fig in engine.scenes:
                return engine
        else:
            raise TypeError, "Figure not attached to a mayavi engine."


    def show_engine(self, engine=None):
        if engine is None:
            engine = self.get_engine()
        if engine.__class__.__name__ == 'EnvisageEngine':
            # FIXME: This should pop up the relevent envisage view
            pass
        else:
            from enthought.mayavi.core.ui.engine_view import EngineView
            return EngineView(engine=engine).edit_traits()


engine_manager = EngineManager()

get_engine = engine_manager.get_engine

set_engine = engine_manager.set_engine

show_engine = engine_manager.show_engine

