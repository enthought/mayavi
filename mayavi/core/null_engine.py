"""
A Null engine for Mayavi.

The `NullEngine` class lets you create a full-fledged (almost) Mayavi
engine without the need for it poping up a window.

It is useful for testing or for using VTK as numerical engine. It does
not allow for rendering.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Any, Event, Callable

from mayavi.core.engine import Engine

def dummy_viewer_factory():
    """Factory function for the dummy viewer."""
    return DummyViewer()

################################################################################
# `NullEngine` class.
################################################################################
class NullEngine(Engine):
    """
    This class represents a NullEngine which creates a DummyViewer with
    a scene set to None.  This allows us to write full mayavi scripts
    without the need for a UI and this is perfect for testing, or to
    use Mayavi (and VTK) as a numerical engine.

    This engine does not allow for rendring.
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

