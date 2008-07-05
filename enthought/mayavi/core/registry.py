"""
 A registry for engines, sources, filters and modules.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import logging

# Enthought library imports.
from enthought.traits.api import HasTraits, List, Instance, Dict, Str

# Local imports.
from enthought.mayavi.core.metadata import Metadata

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
    engines = Dict(Str, Instance('enthought.mayavi.core.engine.Engine'))

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
        if isinstance(engine_or_name, str):
            name = engine_or_name
        else:
            for key, engine in engines.iteritems():
                if engine_or_name == engine:
                    name = key
                    break

        del engines[name]
        logger.debug('Engine named %s unregistered', name)

    def get_file_reader(self, ext):

        """Given a file exension `ext` (of the form 'ext' without the
        leading dot), find a suitable source metadata that will read the file.

        Returns a list of all suitable source metadata objects that will
        handle this.
        """

        result = []
        if len(ext) > 0:
            if ext[0] == '.':
                ext = ext[1:]
            result = [src for src in self.sources \
                      if ext in src.extensions]
        return result


# The global registry instance.
registry = Registry()

# Import the metadata from the sources, modules and filters so they are
# all registered.
from enthought.mayavi.sources.metadata import sources
registry.sources.extend(sources)

from enthought.mayavi.filters.metadata import filters
registry.filters.extend(filters)

from enthought.mayavi.modules.metadata import modules
registry.modules.extend(modules)

