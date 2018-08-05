"""
Defines a GenericModule which is a collection of mayavi
filters/components put together.  This is very convenient and useful to
create new modules.
"""

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Bool, Enum, Instance
from traitsui.api import Item, Group, View, ListEditor
from apptools.persistence import state_pickler

# Local imports.
from mayavi.core.module import Module
from mayavi.core.common import handle_children_state
from mayavi.components.actor import Actor


##############################################################################
# Utility function.
##############################################################################
def find_object_given_state(needle, haystack, object):
    """
    Find the object which corrsponds to given state instance (`needle`)
    in the given state (`haystack`) and object representing that
    haystack.

    Parameters
    ----------

    `needle` -- The `State` instance to find
    haystack -- The source State in which we are to find the state
    `object` -- the object corresponding to the `haystack`
    """
    if needle is haystack:
        return object
    if hasattr(object, 'filter'):
        return find_object_given_state(needle,
                                       haystack.filter,
                                       object.filter)
    elif hasattr(object, 'filters'):
        for h, obj in zip(haystack.filters, object.filters):
            r = find_object_given_state(needle, h, obj)
            if r is not None:
                return r
    return None


###############################################################################
# `GenericModule` class.
###############################################################################
class GenericModule(Module):
    """
    Defines a GenericModule which is a collection of mayavi
    filters/components put together.  This is very convenient and useful
    to create new modules.

    Note that all components including the actor must be passed as a
    list to set the components trait.
    """

    # The *optional* Contour component to which we must listen to if
    # any.  This is needed for modules that use a contour component
    # because when we turn on filled contours the mapper must switch to
    # use cell data.
    contour = Instance('mayavi.components.contour.Contour',
                       allow_none=True)

    # The *optional* Actor component for which the LUT must be set.  If
    # None is specified here, we will attempt to automatically determine
    # it.
    actor = Instance(Actor, allow_none=True)

    # Should we use the scalar LUT or the vector LUT?
    lut_mode = Enum('scalar', 'vector')

    ########################################
    # Private traits.

    # Is the pipeline ready?  Used internally.
    _pipeline_ready = Bool(False)

    ######################################################################
    # `object` interface.
    ######################################################################
    def __get_pure_state__(self):
        # Need to pickle the components.
        d = super(GenericModule, self).__get_pure_state__()
        d['components'] = self.components
        d.pop('_pipeline_ready', None)
        return d

    def __set_pure_state__(self, state):
        # If we are already running, there is a problem since the
        # components will be started automatically in the module's
        # handle_components even though their state is not yet set call
        # so we disable it here and restart it later.
        running = self.running
        self.running = False

        # Remove the actor states since we don't want these unpickled.
        actor_st = state.pop('actor', None)
        contour_st = state.pop('contour', None)
        # Create and set the components.
        handle_children_state(self.components, state.components)
        components = self.components

        # Restore our state using set_state.
        state_pickler.set_state(self, state)

        # Now set our actor and component by finding the right one to get from
        # the state.
        if actor_st is not None:
            for cst, c in zip(state.components, components):
                actor = find_object_given_state(actor_st, cst, c)
                if actor is not None:
                    self.actor = actor
                    break
        if contour_st is not None:
            for cst, c in zip(state.components, components):
                contour = find_object_given_state(contour_st, cst, c)
                if contour is not None:
                    self.contour = contour
                    break
        # Now start all components if needed.
        self._start_components()
        self.running = running

    ######################################################################
    # `HasTraits` interface.
    ######################################################################
    def default_traits_view(self):
        """Returns the default traits view for this object."""
        le = ListEditor(use_notebook=True,
                        deletable=False,
                        export='DockWindowShell',
                        page_name='.name')
        view = View(Group(Item(name='components',
                               style='custom',
                               show_label=False,
                               editor=le,
                               resizable=True),
                          show_labels=False),
                    resizable=True)
        return view

    ######################################################################
    # `Module` interface.
    ######################################################################
    def setup_pipeline(self):
        """Setup the pipeline."""
        # Needed because a user may have setup the components by setting
        # the default value of the trait in the subclass in which case
        # the components_changed handler will never be called leading to
        # problems.
        if len(self.components) > 0 and not self._pipeline_ready:
            self._components_changed([], self.components)

    def update_pipeline(self):
        """This method *updates* the tvtk pipeline when data upstream is
        known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        self._setup_pipeline()
        # Propagate the event.
        self.pipeline_changed = True

    def update_data(self):
        """This method does what is necessary when upstream data
        changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Propagate the data_changed event.
        self.data_changed = True

    ######################################################################
    # Private interface.
    ######################################################################
    def _setup_pipeline(self):
        """Sets up the objects in the pipeline."""
        mm = self.module_manager
        if mm is None or len(self.components) == 0:
            return
        # Our input.
        my_input = mm.source
        components = self.components
        if not self._pipeline_ready:
            # Hook up our first component.
            first = self.components[0]
            first.inputs = [my_input]
            # Hook up the others to each other.
            for i in range(1, len(components)):
                component = components[i]
                component.inputs = [components[i-1]]
            self._pipeline_ready = True
        # Start components.
        self._start_components()
        # Setup the LUT of any actors.
        self._lut_mode_changed(self.lut_mode)

    def _handle_components(self, removed, added):
        super(GenericModule, self)._handle_components(removed, added)
        for component in added:
            if len(component.name) == 0:
                component.name = component.__class__.__name__
            if self.actor is None:
                if isinstance(component, Actor):
                    self.actor = component

        if len(self.components) == 0:
            self.input_info.datasets = ['none']
        else:
            self.input_info.copy_traits(self.components[0].input_info)

        self._pipeline_ready = False
        self._setup_pipeline()

    def _lut_mode_changed(self, value):
        """Static traits listener."""
        mm = self.module_manager
        if mm is None:
            return
        lm = mm.scalar_lut_manager
        if value == 'vector':
            lm = mm.vector_lut_manager

        if self.actor is not None:
            self.actor.set_lut(lm.lut)

    def _actor_changed(self, old, new):
        self._lut_mode_changed(self.lut_mode)

    def _filled_contours_changed_for_contour(self, value):
        """When filled contours are enabled, the mapper should use the
        the cell data, otherwise it should use the default scalar
        mode.
        """
        if self.actor is None:
            return
        if value:
            self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _start_components(self):
        for component in self.components:
            if len(component.inputs) > 0 and \
               len(component.inputs[0].outputs) > 0:
                component.start()
