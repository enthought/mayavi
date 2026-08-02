"""Common utility functions and classes.  This includes error/warning
messages etc.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import logging
import os
import sys
import traceback

# Enthought library imports.
from apptools.persistence.state_pickler import create_instance
from traits.etsconfig.api import ETSConfig
if (ETSConfig.toolkit == 'null') or os.environ.get('CI'):
    pyface = None
else:
    from pyface import api as pyface

# Setup a logger for this module.
logger = logging.getLogger(__name__)

# Flipped by the test suite (see conftest.py): the callers of exception() below
# are bare ``except:`` blocks, so a swallowed failure is invisible to a test.
reraise_exceptions = False

######################################################################
# Utility functions.
######################################################################


def debug(msg):
    """Handle a debug message.
    """
    logger.debug(msg)


def _has_ui():
    """Whether pyface found a usable GUI toolkit.

    A successful pyface import is not enough: in an environment with no
    (working) toolkit, pyface resolves GUI to an ``Unimplemented`` stub and
    the dialog helpers to the null backend's placeholders, and touching
    either raises -- which took down even the offscreen path, where no UI
    is wanted in the first place (see enthought/mayavi#1308).
    """
    if pyface is None:
        return False
    try:
        return getattr(pyface.GUI, 'process_events', None) is not None
    except Exception:
        # resolving the toolkit itself can raise on broken installs; that
        # must not mask the error currently being reported
        return False


def warning(msg, parent=None):
    """Handle a warning message.
    """
    logger.warning(msg)
    if _has_ui():
        pyface.warning(parent, msg)


def error(msg, parent=None):
    """Handle an error message.
    """
    logger.error(msg)
    if _has_ui():
        pyface.error(parent, msg)


def exception(msg='Exception', parent=None):
    """This function handles any exception derived from Exception and
    prints out an error.  The optional `parent` argument is passed
    along to the dialog box.  The optional `msg` is printed and sent
    to the logger.  So you could send extra information here.
    """
    if reraise_exceptions:
        raise
    try:
        type, value, tb = sys.exc_info()
        info = traceback.extract_tb(tb)
        filename, lineno, function, text = info[-1] # last line only
        exc_msg = "%s\nIn %s:%d\n%s: %s (in %s)" %\
                  (msg, filename, lineno, type.__name__, str(value),
                   function)
        # Log and display the message.
        logger.exception(msg)
        if _has_ui():
            pyface.error(parent, exc_msg, title='Exception')
    finally:
        type = value = tb = None # clean up


def process_ui_events():
    """Process GUI events.

    This function merely abstracts the function so nothing is done when
    no UI is running.
    """
    if _has_ui():
        pyface.GUI.process_events()


def get_engine(obj):
    """Try and return the engine given an object in the mayavi
    pipeline.  This basically walks up the parent's of the object till
    the engine is found.
    """
    from mayavi.core.engine import Engine
    while obj is not None:
        if isinstance(obj, Engine):
            return obj
        else:
            obj = obj.parent
    return None


def get_output(obj):
    """Given an object, extracts the output object, hiding differences
    between old and new pipeline."""
    if obj.is_a('vtkDataSet'):
        return obj
    else:
        return obj.output


def get_object_path(object, parent, path='engine'):
    """Given a mayavi object on the tree view, this should find its
    "path" with respect to the parent object that contains it.
    """
    def _get_child_trait(obj):
        if hasattr(obj, 'scenes'):
            return 'scenes'
        elif hasattr(obj, 'children'):
            return 'children'
        return ''

    def _finder(obj, to_find, path):
        if obj is to_find:
            return path
        else:
            child_t = _get_child_trait(obj)
            if child_t == '':
                return ''
            for i, o in enumerate(getattr(obj, child_t)):
                pth = _finder(o, to_find, '%s.%s[%d]'%(path, child_t, i))
                if len(pth) > 0:
                    return pth
        return ''

    return _finder(parent, object, path)


def handle_children_state(children, kids):
    """Given a list of children (as `children`) of a particular object
    and their states in the `kids` argument, this function sets up the
    children by removing unnecessary ones, fixing existing ones and
    adding new children if necessary (depending on the state).
    """
    # Make a copy of the list so adding/removing does not trigger events
    # each time.
    m_children = list(children)

    n_child, n_kid = len(m_children),  len(kids)
    # Remove extra children we have.
    for i in range(n_child - n_kid):
        m_children.pop()
    # Now check existing children deleting existing ones and
    # creating new ones if needed.
    for i in range(n_child):
        child, kid = m_children[i], kids[i]
        md = kid.__metadata__
        if (child.__module__ != md['module']) \
               or (child.__class__.__name__ != md['class_name']):
            m_children[i] = create_instance(kid)
    # Add any extra kids.
    for i in range(n_kid - n_child):
        child = create_instance(kids[n_child + i])
        m_children.append(child)

    # Now set the children in one shot.
    children[:] = m_children
