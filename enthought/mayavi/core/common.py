"""Common utility functions and classes.  This includes error/warning
messages etc.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys
import traceback
import logging

# Enthought library imports.
from enthought.persistence.state_pickler import create_instance
from enthought.pyface import api as pyface

# Setup a logger for this module.
logger = logging.getLogger(__name__)

######################################################################
# Utility functions.
######################################################################
def debug(msg):
    """Handle a debug message.
    """
    logger.debug(msg)

def warning(msg, parent=None):
    """Handle a warning message.
    """
    logger.warn(msg)
    pyface.warning(parent, msg)

def error(msg, parent=None):
    """Handle an error message.
    """
    logger.error(msg)
    pyface.error(parent, msg)

def exception(msg='Exception', parent=None):
    """This function handles any exception derived from Exception and
    prints out an error.  The optional `parent` argument is passed
    along to the dialog box.  The optional `msg` is printed and sent
    to the logger.  So you could send extra information here.
    """
    try:
        type, value, tb = sys.exc_info()
        info = traceback.extract_tb(tb)
        filename, lineno, function, text = info[-1] # last line only
        exc_msg = "%s\nIn %s:%d\n%s: %s (in %s)" %\
                  (msg, filename, lineno, type.__name__, str(value),
                   function)
        # Log and display the message.
        logger.exception(msg)
        pyface.error(parent, exc_msg, title='Exception')
    finally:
        type = value = tb = None # clean up

def handle_children_state(children, kids):
    """Given a list of children (as `children`) of a particular object
    and their states in the `kids` argument, this function sets up the
    children by removing unnecessary ones, fixing existing ones and
    adding new children if necessary (depending on the state).
    """
    n_child, n_kid = len(children),  len(kids)
    # Remove extra children we have.
    for i in range(n_child - n_kid):
        children.pop()
    # Now check existing children deleting existing ones and
    # creating new ones if needed.
    for i in range(n_child):
        child, kid = children[i], kids[i]
        md = kid.__metadata__
        if (child.__module__ != md['module']) \
               or (child.__class__.__name__ != md['class_name']):
            children[i] = create_instance(kid)
    # Add any extra kids.
    for i in range(n_kid - n_child):
        child = create_instance(kids[n_child + i])
        children.append(child)
