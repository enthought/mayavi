"""
Base class for factories for adding objects to the pipeline.

"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

from auto_doc import make_doc
from enthought.traits.api import HasPrivateTraits, Str, TraitError,\
            Instance
from enthought.mayavi.core.filter import Filter
from enthought.mayavi.core.engine import Engine

import tools
from engine_manager import get_engine

def get_obj(obj, components):
    """ Get the target object for the specified components. """

    for component in components:
        obj = getattr(obj, component)

    return obj 


def make_function(factory_class):
    def the_function(*args, **kwargs): 
        factory = factory_class(*args, **kwargs)
        return factory._target

    the_function.__doc__  = make_doc(factory_class)
    the_function.func_name = factory_class.__name__.lower()
    return the_function

   
##############################################################################
class PipeFactory(HasPrivateTraits):
    """ Base class for all factories adding pipes on the pipeline """
        
    name = Str(adapts='name', help='the name of the vtk object created.')

    _engine = Instance(Engine)

    def __init__(self, parent, **kwargs):
        # We are not passing the traits to the parent class
        super(PipeFactory, self).__init__()
        self._scene = tools.gcf()
        self._engine = get_engine()
        self._scene.scene.disable_render = True
        if issubclass(self._target.__class__, Filter):
            self._engine.add_filter(self._target, obj=parent)
        else:
            self._engine.add_module(self._target, obj=parent)
        traits = self.get(self.class_trait_names())
        [traits.pop(key) for key in traits.keys() 
                                    if key[0]=='_' or key is None]
        traits.update(kwargs)
        # Now calling the traits setter, so that traits handlers are
        # called
        self.set(**traits)
        self._scene.scene.disable_render = False

    def set(self, trait_change_notify=True, **traits):
        """ Same as HasTraits.set except that notification is forced,
        unless trait_change_notify==False"""
        HasPrivateTraits.set(self, trait_change_notify=trait_change_notify,
                                    **traits)
        if trait_change_notify==False:
            return 
        for trait in traits.iterkeys():
            callback = getattr(self, '_%s_changed' % trait)
            value = getattr(self, trait)
            try:
                if callback is not None:
                    callback()
                self._anytrait_changed(trait, value)
            except TraitError:
                if value==None:
                    # This means "default"
                    pass
                else:
                    raise
                

    def _anytrait_changed(self, name, value):
        """ This is where we implement the adaptation code. """
        trait = self.trait(name)
        if name[0] == '_':
            # Private attribute
            return
        # hasattr(traits, "adapts") always returns True :-<.
        if not trait.adapts==None:
            components = trait.adapts.split('.')
            obj = get_obj(self._target, components[:-1])
            setattr(obj, components[-1], value)



