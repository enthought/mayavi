"""
Central registry for figures with mlab.
"""

# Standard library imports
import warnings

# Enthought librairies imports
from traits.api import HasTraits, Instance

# Local imports
from mayavi.preferences.api import preference_manager
from mayavi.core.registry import registry
from mayavi.core.engine import Engine
from mayavi.core.off_screen_engine import OffScreenEngine
from mayavi.core.null_engine import NullEngine
from mayavi.core.common import process_ui_events
from .preferences_mirror import PreferencesMirror

# The mlab options.
options = PreferencesMirror()
options.preferences = preference_manager.mlab


######################################################################
def check_backend():
    """ Check if either we are in test mode, or if there is a
        suitable traits backend installed.
    """
    from traitsui.toolkit import toolkit
    from traits.etsconfig.api import ETSConfig
    from mayavi.tools.engine_manager import options

    toolkit()  # This forces the selection of a toolkit.
    if (options.backend != 'test' and not options.offscreen) and \
            ETSConfig.toolkit in ('null', ''):
        msg = '''Could not import backend for traitsui.  Make sure you
        have a suitable UI toolkit like PyQt/PySide or wxPython
        installed.'''
        raise ImportError(msg)


###############################################################################
# `EngineManager` class.
###############################################################################
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
        """ Returns an engine in agreement with the options.
        """

        # First check if the current engine is running and if it is in
        # the registered engines.
        ce = self.current_engine
        if ce is not None:
            if not ce.running or ce not in registry.engines.values():
                self.current_engine = None

        if self.current_engine is not None:
            engines = list((self.current_engine,))
        else:
            engines = list()
        engines.extend(list(registry.engines.values()))
        if options.backend == 'envisage':
            suitable = [e for e in engines
                        if e.__class__.__name__ == 'EnvisageEngine']
        elif options.backend == 'test':
            suitable = [e for e in engines
                        if e.__class__.__name__ == 'NullEngine']
        elif options.offscreen:
            suitable = [e for e in engines
                        if e.__class__.__name__ == 'OffScreenEngine']
        elif options.backend == 'auto':
            suitable = [e for e in engines
                        if e.__class__.__name__ not in ('NullEngine',
                                                        'OffScreenEngine')]
        else:
            suitable = [e for e in engines
                        if e.__class__.__name__ == 'Engine']
        if len(suitable) == 0:
            return self.new_engine()
        else:
            # Return the most engine add to the list most recently.
            self.current_engine = suitable[-1]
            return suitable[-1]

    def get_null_engine(self):
        """Return a suitable null engine and make that the current
        engine.
        """
        # First check if the current engine is running and if it is in
        # the registered engines.
        ce = self.current_engine
        if ce is not None:
            if not ce.running or ce not in registry.engines.values():
                self.current_engine = None

        if self.current_engine is not None:
            engines = list((self.current_engine,))
        else:
            engines = list()
        engines.extend(list(registry.engines.values()))
        engine = None
        for e in engines:
            if e.__class__.__name__ == 'NullEngine':
                engine = e
                break
        else:
            engine = NullEngine(name='Null Mlab Engine')
            engine.start()
        self.current_engine = engine
        return engine

    def set_engine(self, engine):
        """ Sets the mlab engine.
        """
        if not engine.running:
            warnings.warn('Engine is not running', stacklevel=2)
        self.current_engine = engine
        registry.register_engine(engine)

    def new_engine(self):
        """ Creates a new engine, envisage or not depending on the
            options.
        """
        check_backend()
        if options.backend == 'envisage':
            from mayavi.plugins.app import Mayavi
            m = Mayavi(start_gui_event_loop=False)
            m.main()
            process_ui_events()
            window = m.application.workbench.active_window
            engine = window.get_service(Engine)
        elif options.backend == 'test':
            engine = NullEngine(name='Null Mlab Engine')
            engine.start()
        else:
            if options.offscreen:
                engine = OffScreenEngine(name='Mlab offscreen Engine')
                engine.start()
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
            raise TypeError("Figure not attached to a mayavi engine.")

    def show_engine(self, engine=None, rich_view=True):
        """ Show a dialog with the mayavi pipeline. This dialog allows to
            edit graphicaly the properties of the different objects on
            the scenes.
        """
        if engine is None:
            engine = self.get_engine()
        if engine.__class__.__name__ == 'EnvisageEngine' or \
           options.backend == 'test':
            # FIXME: This should pop up the relevent envisage view
            pass
        elif rich_view:
            from mayavi.core.ui.engine_rich_view import \
                    EngineRichView
            figure = engine.current_scene
            view = EngineRichView(engine=engine)
            if figure is None:
                scene = None
            else:
                scene = figure.scene
            return view.scene_editing_view(scene=scene)
        else:
            from mayavi.core.ui.engine_view import \
                    EngineView
            scene = engine.current_scene
            view = EngineView(engine=engine)
            return view.edit_traits()


engine_manager = EngineManager()

get_engine = engine_manager.get_engine

get_null_engine = engine_manager.get_null_engine

set_engine = engine_manager.set_engine

show_pipeline = engine_manager.show_engine
