"""
Common code for mayavi tests.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) Enthought, Inc.
# License: BSD Style.
import os.path

from traits.api import HasTraits, Any, Event, Callable


def fail_instead_of_dialogs(set_attr=setattr):
    """Keep mayavi's error reporting from blocking (or hiding) a run.

    A failure inside a pipeline update -- including a warning raised as an
    error -- is swallowed by a bare ``except:`` and shown in a modal pyface
    box, so on a headed toolkit the run stops until someone clicks OK and the
    caller then carries on regardless.  Re-raise instead, and route the
    genuinely user-facing messages to the log only.

    Anything that reports through pyface directly rather than through
    `mayavi.core.common` would still get a box, so take the class those all
    end up in as well: every convenience function builds a `MessageDialog` and
    opens it, and an exception out of `open` says what the box would have said.

    `set_attr` is the hook the test fixture uses to get its changes undone
    again; the integration scripts and the docs renderer, which are whole
    processes of their own, take the default and keep them.

    This lives here rather than in conftest.py so that it can be imported
    without pytest -- the docs job installs no such thing.
    """
    from mayavi.core import common
    set_attr(common, 'reraise_exceptions', True)
    if common.pyface is not None:
        for name in ('error', 'warning', 'information'):
            set_attr(common.pyface, name,
                     lambda parent, msg, *args, _name=name, **kwargs:
                         common.logger.info('pyface.%s: %s', _name, msg))
        from pyface.message_dialog import MessageDialog

        def open_instead(self):
            raise RuntimeError(
                ' '.join(part for part in
                         (self.title, self.message, self.informative,
                          self.detail) if part))

        set_attr(MessageDialog, 'open', open_instead)


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

