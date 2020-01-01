"""
 A registry for engines, sources, filters and modules.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import splitext
import logging

# Enthought library imports.
from traits.api import HasTraits, List, Instance, Dict, Str

# Local imports.
from mayavi.core.metadata import Metadata, import_symbol

# A logger for this module.
logger = logging.getLogger(__name__)


################################################################################
# `Registry` class.
################################################################################
class Registry(HasTraits):

    """
    This class is a registry for various engines, and metadata from
    sources, filters and modules
    """

    # The mayavi engines used.
    engines = Dict(Str, Instance('mayavi.core.engine.Engine'))

    # The metadata for the sources.
    sources = List(Metadata)

    # The metadata for the modules.
    modules = List(Metadata)

    # The metadata for the filters.
    filters = List(Metadata)

    ######################################################################
    # `Registry` interface.
    ######################################################################
    def register_engine(self, engine, name=''):

        """Registers a mayavi engine with an optional name.   Note that
        we allow registering an engine with the same name as another
        already registered.  """

        engines = self.engines
        if len(name) == 0:
            name = '%s%d'%(engine.__class__.__name__,
                           len(engines) + 1)

        logger.debug('Engine [%s] named %s registered', engine, name)
        engines[name] = engine

    def unregister_engine(self, engine_or_name):

        """Unregisters a mayavi engine specified either as a name or an
        engine instance."""

        engines = self.engines
        name = None
        if isinstance(engine_or_name, str):
            name = engine_or_name
        else:
            for key, engine in engines.items():
                if engine_or_name == engine:
                    name = key
                    break

        if name:
            del engines[name]
        logger.debug('Engine named %s unregistered', name)

    def get_file_reader(self, filename):

        """Given a filename, find a suitable source metadata that will
        read the file.

        Returns a suitable source metadata object that will
        handle this.
        """
        base, ext = splitext(filename)
        result = []
        if len(ext) > 0:
            ext = ext[1:]
            result = [src for src in self.sources \
                      if ext in src.extensions]

        # 'result' contains list of all source metadata that can handle
        # the file.

        # If there is only single source metadata available to handle
        # the file, we simply return it.

        # If there is a conflict i.e. more then one source metadata objects
        # capable of handling the file then we check if they are capable of
        # actually reading it using 'can_read_function' which may be a class
        # method or a simple function which returns whether the object is
        # capable of reading the file or not.

        # Finally returns the most suitable source metadata object to the engine. If
        # multiple objects are still present we return the last one in the list.

        if len(result) > 1:
            for res in result[:]:
                if len(res.can_read_test) > 0:
                    can_read = import_symbol(res.can_read_test)(filename)
                    if can_read:
                        return res
                    else:
                        result.remove(res)

        if len(result) == 0:
            return None

        return result[-1]

    def find_scene_engine(self, scene):
        """ Find the engine corresponding to a given tvtk scene.
        """
        for engine in self.engines.values():
            for s in engine.scenes:
                if scene is s:
                    return engine
                sc = s.scene
                if scene is sc:
                    return engine
                elif hasattr(sc, 'scene_editor') and \
                     scene is sc.scene_editor:
                    # This check is needed for scene model objects.
                    return engine
        else:
            raise TypeError("Scene not attached to a mayavi engine.")



# The global registry instance.
registry = Registry()

# Import the metadata from the sources, modules and filters so they are
# all registered.
from mayavi.sources.metadata import sources
registry.sources.extend(sources)

from mayavi.filters.metadata import filters
registry.filters.extend(filters)

from mayavi.modules.metadata import modules
registry.modules.extend(modules)

# Do any customizations from either the `site_mayavi.py` or the
# `user_mayavi.py` files.  This is done by importing the customize.py
# module here which in turn imports the necessary code from the users's
# customization.
from mayavi.core import customize
