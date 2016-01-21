"""
Test the MousePickDispatcher.
"""

import unittest

from traits.api import HasTraits, Instance

from mayavi.core.null_engine import NullEngine, DummyViewer
from tvtk.api import tvtk
from mayavi.tools.engine_manager import engine_manager
from mayavi.core.registry import registry
from mayavi.core.mouse_pick_dispatcher import \
                MousePickDispatcher
from tvtk.pyface.picker import Picker

################################################################################
# class `DummyScene`
################################################################################
class DummyScene(HasTraits):
    """ Mimics the API of a TVTK scene.
    """
    interactor = Instance(tvtk.GenericRenderWindowInteractor, ())

    picker = Instance(Picker, (None, ))


################################################################################
# class `DummyMousePickDispatcher`
################################################################################
class DummyMousePickDispatcher(MousePickDispatcher):
    """ A MousePickDispatcher that accepts the DummyViewer as a Scene.
    """
    scene = Instance(DummyViewer)


################################################################################
# class `TestMousePickerDispatcher`
################################################################################
class TestMousePickerDispatcher(unittest.TestCase):
    """ Create a fake figure, to make sure that observers are well
        registered and removed.
    """

    def setUp(self):
        e = NullEngine()
        e.start()
        registry.register_engine(e)
        engine_manager.current_engine = e
        self.e = e
        self.s = e.new_scene()
        self.s.scene = DummyScene()


    def tearDown(self):
        engine_manager.current_engine = None
        # Unregistering the engine, to avoid side-effects between tests
        self.e.stop()
        registry.unregister_engine(self.e)

    def test_callback_registering(self):
        def test(picker):
            pass
        dispatcher = DummyMousePickDispatcher(scene=self.s)
        initial_interactor_callbacks = frozenset([i for i in range(100)
                                    if self.s.scene.interactor.has_observer(i)
                                ])
        dispatcher.callbacks.append((test, 'point', 'Left'))

        # Check that VTK observers were established
        self.assertTrue(dispatcher._mouse_mvt_callback_nb)
        self.assertTrue('Left' in dispatcher._mouse_press_callback_nbs)
        self.assertTrue('Left' in dispatcher._mouse_release_callback_nbs)

        # Check that we are back to no observers
        dispatcher.callbacks[:] = []
        interactor_callbacks = frozenset([i for i in range(100)
                                    if self.s.scene.interactor.has_observer(i)
                                ])
        self.assertEqual(interactor_callbacks,
                         initial_interactor_callbacks)



if __name__ == '__main__':
    unittest.main()
