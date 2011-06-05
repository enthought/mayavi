"""
The definition of different kinds of metadata that is put into the
mayavi registry
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import HasTraits, Str, Callable, Either, List, Instance
from mayavi.core.pipeline_info import PipelineInfo


################################################################################
# Utility functions.
################################################################################
def import_symbol(symbol_path):

    """ Import the symbol defined by the specified symbol path.
    Copied from envisage's import manager.
    """

    if ':' in symbol_path:
        module_name, symbol_name = symbol_path.split(':')

        module = import_module(module_name)
        symbol = eval(symbol_name, module.__dict__)

    else:
        components = symbol_path.split('.')

        module_name = '.'.join(components[:-1])
        symbol_name = components[-1]

        module = __import__(
            module_name, globals(), locals(), [symbol_name]
        )

        symbol = getattr(module, symbol_name)

    return symbol

def import_module(module_name):

    """This imports the given module name.  This code is copied from
    envisage's import manager!

    """

    module = __import__(module_name)

    components = module_name.split('.')
    for component in components[1:]:
        module = getattr(module, component)

    return module



################################################################################
# `Metadata` class.
################################################################################
class Metadata(HasTraits):
    """
    This class allows us to define metadata related to mayavi's sources,
    filters and modules.
    """

    # Our ID.
    id = Str

    # The class that implements the module/filter/source.
    class_name = Str

    # The factory that implements the object overrides the class_name if
    # not the empty string.  The callable will be given the filename to
    # open along with the engine (for sources).
    factory = Either(Str, Callable, allow_none=False)

    # Description of the object being described.
    desc = Str

    # Help string for the object.
    help = Str

    # The name of this object in a menu.
    menu_name = Str

    # The optional tooltip to display for this object.
    tooltip = Str

    # Information about what this object can consume.
    input_info = Instance(PipelineInfo)

    # Information about what this object can produce.
    output_info = Instance(PipelineInfo)

    ######################################################################
    # Metadata interface.
    ######################################################################
    def get_callable(self):
        """Return the callable that will create a new instance of the
        object implementing this metadata.
        """
        factory = self.factory
        if factory is not None:
            if callable(factory):
                symbol = factory
            elif isinstance(factory, str) and len(factory) > 0:
                symbol = import_symbol(factory)
            else:
                symbol = import_symbol(self.class_name)
        else:
            symbol = import_symbol(self.class_name)

        return symbol


################################################################################
# `ModuleMetadata` class.
################################################################################
class ModuleMetadata(Metadata):
    pass

################################################################################
# `FilterMetadata` class.
################################################################################
class FilterMetadata(Metadata):
    pass

################################################################################
# `SourceMetadata` class.
################################################################################
class SourceMetadata(Metadata):

    # The file name extension that this reader/source handles.  Empty if
    # it does not read a file.
    extensions = List(Str)

    # Wildcard for the file dialog.
    wildcard = Str

    # `Callable` to check if the reader can actually read the file
    # `Callable` must accept the filename to be read and it should
    # return `True` if its possible to read the file else 'False'
    can_read_test = Str
