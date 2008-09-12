"""
Common code for mayavi tests.

The `TestEngine` class is particularly useful since it lets you create a
full-fledged (almost) Mayavi engine without the need for it poping up a
window.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from enthought.traits.api import HasTraits, Any, Event, Callable

from enthought.mayavi.core.engine import Engine

def dummy_viewer_factory():
    """Factory function for the dummy viewer."""
    return DummyViewer()

################################################################################
# `TestEngine` class.
################################################################################ 
class TestEngine(Engine):
    """
    This class represents a TestEngine which creates a DummyViewer with
    a scene set to None.  This allows us to write full mayavi scripts
    without the need for a UI and this is perfect for testing.
    """
    scene_factory = Callable(dummy_viewer_factory)


################################################################################
# `DummyViewer` class.
################################################################################ 
class DummyViewer(HasTraits):
    """Mimics the API of a viewer."""

    scene = Any
    closing = Event
    activated = Event



