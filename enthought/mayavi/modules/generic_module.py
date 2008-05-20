"""
Defines a GenericModule which is a collection of mayavi
filters/components put together.  This is very convenient and useful to
create new modules.
"""

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Bool, Str, List, Enum, Instance
from enthought.traits.ui.api import Item, Group, View, ListEditor

# Local imports.
from enthought.mayavi.core.module import Module
from enthought.mayavi.components.actor import Actor


# FIXME:  This cannot be persisted due to the broken nature of
# our persistence framework.  This should work when we use the new
# pickle approach.

################################################################################
# `GenericModule` class.
################################################################################
class GenericModule(Module):
    """
    Defines a GenericModule which is a collection of mayavi
    filters/components put together.  This is very convenient and useful
    to create new modules.

    Note that all components including the actor must be set in the
    components trait.

    """

    # Our name.
    name = Str('GenericModule')

    # The *optional* Contour component to which we must listen to if
    # any.  This is needed for modules that use a contour component
    # because when we turn on filled contours the mapper must switch to
    # use cell data.
    contour = Instance('enthought.mayavi.components.contour.Contour',
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
        if mm is None:
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
        for component in components:
            component.start()

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

        self._pipeline_ready = False

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


