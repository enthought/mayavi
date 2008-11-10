"""
Common code for mayavi tests.

The `TestEngine` class is particularly useful since it lets you create a
full-fledged (almost) Mayavi engine without the need for it poping up a
window.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.
import os.path

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

def fixpath(filename):
    """Given a relative file path it sets the path relative to this
    directory.  This allows us to run the tests from other directories
    as well.
    """
    return os.path.join(os.path.dirname(__file__), filename)


def get_example_data(fname):
    """Given a relative path to data inside the examples directory,
    obtains the full path to the file.
    """
    p = os.path.join('data', fname)
    return os.path.abspath(fixpath(p))
   
