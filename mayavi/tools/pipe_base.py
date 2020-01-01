"""
Base class for factories for adding objects to the pipeline.

"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

import warnings

from traits.api import HasPrivateTraits, Str, TraitError,\
            Instance, Any, Bool
from mayavi.core.filter import Filter
from mayavi.core.engine import Engine
from mayavi.core.source import Source
from mayavi.core.scene import Scene
from mayavi.core.module_manager import ModuleManager

from tvtk.api import tvtk

from .auto_doc import make_doc
from . import tools
from .engine_manager import get_engine


def get_obj(obj, components):
    """ Get the target object for the specified components. """

    for component in components:
        obj = getattr(obj, component)

    return obj


def make_function(factory_class):
    def the_function(*args, **kwargs):
        factory = factory_class(*args, **kwargs)
        return factory._target

    the_function.__doc__ = make_doc(factory_class)
    the_function.__name__ = factory_class.__name__.lower()
    return the_function


def get_module_manager(obj):
    """ Returns the module manager that would be used when a module
        is added on the given object, if any, and None elsewhere.
    """
    if hasattr(obj, 'module_manager'):
        return obj.module_manager
    elif isinstance(obj, ModuleManager):
        return obj
    for child in reversed(obj.children):
        if isinstance(child, ModuleManager):
            return child
    else:
        return None


##############################################################################
class PipeFactory(HasPrivateTraits):
    """ Base class for all factories adding pipes on the pipeline """

    name = Str(adapts='name', help='the name of the vtk object created.')

    figure = Instance(Scene)

    _engine = Instance(Engine, help=('the figure on which the object '
                'should be added'))

    _target = Any

    _do_redraw = Bool

    def add_module(self, parent, kwargs=dict()):
        """ Add the target module to the given object.
        """
        # We check to see if the module-manager-related option require to
        # add a new module manager:
        if parent is not None:
            module_manager = get_module_manager(parent)
            if (module_manager is not None and
                        len(module_manager.children) > 0):
                scalar_lut = module_manager.scalar_lut_manager
                vector_lut = module_manager.vector_lut_manager
                if 'vmin' in kwargs:
                    if not scalar_lut.use_default_range and \
                            kwargs['vmin'] != scalar_lut.data_range[0]:
                        parent = self._engine.add_module(ModuleManager(),
                                                        module_manager.parent)
                    elif not scalar_lut.use_default_range and \
                            kwargs['vmin'] != scalar_lut.data_range[0]:
                        parent = self._engine.add_module(ModuleManager(),
                                                        module_manager.parent)

                elif 'vmax' in kwargs:
                    if not scalar_lut.use_default_range and \
                            kwargs['vmax'] != scalar_lut.data_range[1]:
                        parent = self._engine.add_module(ModuleManager(),
                                                        module_manager.parent)
                    elif not scalar_lut.use_default_range and \
                            kwargs['vmax'] != scalar_lut.data_range[1]:
                        parent = self._engine.add_module(ModuleManager(),
                                                        module_manager.parent)

                elif 'colormap' in kwargs:
                    cmap = kwargs['colormap']
                    if (scalar_lut.lut_mode != cmap
                                        or vector_lut.lut_mode != cmap):
                        parent = self._engine.add_module(ModuleManager(),
                                            module_manager.parent)

        self._engine.add_module(self._target, obj=parent)

    def __init__(self, parent, **kwargs):
        # We are not passing the traits to the parent class
        super(PipeFactory, self).__init__()
        # Try to find the right engine and scene to work with
        ancester = parent
        while hasattr(ancester, 'parent'):
            ancester = getattr(ancester, 'parent')
            if isinstance(ancester, Scene):
                self._scene = ancester
                self._engine = ancester.parent
                break
        else:
            if self.figure is not None:
                self._scene = self.figure
            else:
                self._scene = tools.gcf()
                self._engine = get_engine()
        scene = self._scene.scene
        if self.figure is not None and self.figure is not self._scene:
            warnings.warn('Trying to add a module on the wrong scene')
        if isinstance(parent, (Source, tvtk.DataSet)) \
                and not isinstance(parent, Filter) and self._scene is not None:
            # Search the current scene to see if the  source is already
            # in it, if not add it.
            if not parent in self._scene.children:
                parent = tools.add_dataset(parent, figure=self._scene)

        if scene is not None:
            self._do_redraw = not scene.disable_render
            scene.disable_render = True
        if issubclass(self._target.__class__, Filter):
            self._engine.add_filter(self._target, obj=parent)
        else:
            self.add_module(parent, kwargs)

        # Inject the magical mlab source trait.
        if hasattr(parent, 'mlab_source'):
            ms = parent.mlab_source
            self._target.add_trait('mlab_source', Instance(ms.__class__))
            self._target.mlab_source = ms

        traits = self.trait_get(self.class_trait_names())
        [traits.pop(key) for key in list(traits.keys())
                                    if key[0] == '_' or key is None]
        traits.update(kwargs)
        # Now calling the traits setter, so that traits handlers are
        # called
        self.trait_set(**traits)
        if scene is not None:
            scene.disable_render = not self._do_redraw

    def set(self, trait_change_notify=True, **traits):
        return self.trait_set(trait_change_notify=trait_change_notify,
                              **traits)

    def trait_set(self, trait_change_notify=True, **traits):
        """ Same as HasTraits.set except that notification is forced,
        unless trait_change_notify==False"""
        HasPrivateTraits.trait_set(
            self, trait_change_notify=trait_change_notify, **traits)
        if trait_change_notify == False:
            return
        for trait in traits:
            callback = getattr(self, '_%s_changed' % trait)
            value = getattr(self, trait)
            try:
                if callback is not None:
                    callback()
                self._anytrait_changed(trait, value)
            except TraitError:
                if value is None:
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
        if not trait.adapts is None:
            components = trait.adapts.split('.')
            obj = get_obj(self._target, components[:-1])
            setattr(obj, components[-1], value)
