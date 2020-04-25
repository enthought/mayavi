"""The base class for all MayaVi modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import List, Instance, Str

# Local imports
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.common import exception


######################################################################
# `Module` class.
######################################################################
class Module(PipelineBase):
    """ Base class for the Mayavi modules.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The ModuleManager associated with this module.  A Module is
    # always a child of a ModuleManager.  When the module is added to
    # the mayavi pipeline (as a child of the module manager), the
    # module manager automatically sets this trait.
    module_manager = Instance('mayavi.core.module_manager.ModuleManager',
                               record=False)

    # The (optional) components used by this module.  NOTE: This is
    # not pickled.  It is the developers responsibility to setup the
    # components when the component traits are set in the handler.
    components = List(record=False)

    # The icon
    icon = Str('module.ico')

    # The human-readable type for this object
    type = Str(' module')

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['any'])

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['none'])

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(Module, self).__init__(**traits)

        # Let the module setup its pipeline.
        self.setup_pipeline()

    def __get_pure_state__(self):
        d = super(Module, self).__get_pure_state__()
        for x in ('module_manager', 'components'):
            d.pop(x, None)
        return d


    ######################################################################
    # `Module` interface.
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        pass

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        raise NotImplementedError

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # By default, just invoke render and set data_changed.
        self.data_changed = True
        self.render()


    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.  Note that when start is invoked, all the other
        information for the pipeline should be already set.
        """
        if self.running:
            return

        # Setup event handlers.
        self._setup_event_handlers()

        # Setup the pipeline.
        self.update_pipeline()

        # Start the components.
        try:
            for component in self.components:
                component.start()
        except:
            exception()

        # Call parent method to set the running state.
        super(Module, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Teardown event handlers.
        self._teardown_event_handlers()

        # Stop the components.
        for component in self.components:
            component.stop()

        # Call parent method to set the running state.
        super(Module, self).stop()

    def add_child(self, child):
        """This method intelligently adds a child to this object in
        the MayaVi pipeline.
        """
        # Pass on the buck to our module_manager.
        self.module_manager.add_child(child)

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_has_children(self, node):
        """ Returns whether or not the object has children.
        """
        return False

    def tno_allows_children(self, node):
        """ Returns whether chidren of this object are allowed or not.
        """
        return False

    def tno_get_children(self, node):
        """ Gets the object's children.
        """
        return None

    ######################################################################
    # Non-public interface
    ######################################################################
    def _change_components(self, old, new):
        """This method sets up the `components` trait and is typically
        called from a handler for a particular component.

        For example lets say you are using a `Actor` component and
        have a `actor` trait on the module.  The `_actor_changed`
        method should setup the pipeline.  Typically inside this
        handler, you also want to change the module's `components`
        trait.  This method merely does that by removing the older
        component and adding the new one and then updating the
        pipeline just in case.
        """
        comp = self.components
        if old is not None:
            comp.remove(old)
        comp.append(new)
        if old is not None:
            self.update_pipeline()

    def _setup_event_handlers(self):
        mm = self.module_manager
        src = mm.source
        mm.on_trait_change(self.update_pipeline, 'source')
        src.on_trait_event(self.update_pipeline, 'pipeline_changed')
        src.on_trait_event(self.update_data, 'data_changed')

    def _teardown_event_handlers(self):
        mm = self.module_manager
        src = mm.source
        mm.on_trait_change(self.update_pipeline, 'source',
                           remove=True)
        src.on_trait_event(self.update_pipeline, 'pipeline_changed',
                           remove=True)
        src.on_trait_event(self.update_data, 'data_changed',
                           remove=True)

    def _scene_changed(self, old_scene, new_scene):
        for component in self.components:
            component.scene = new_scene
        super(Module, self)._scene_changed(old_scene, new_scene)

    def _components_changed(self, old, new):
        self._handle_components(old, new)

    def _components_items_changed(self, list_event):
        self._handle_components(list_event.removed, list_event.added)

    def _handle_components(self, removed, added):
        for component in removed:
            if self.running:
                component.stop()
        scene = self.scene
        for component in added:
            if scene is not None:
                component.scene = scene
            if self.running:
                component.start()

    def _visible_changed(self,value):
        for c in self.components:
            c.visible = value

        super(Module,self)._visible_changed(value)

    def _menu_helper_default(self):
        from mayavi.core.traits_menu import ModuleMenuHelper
        return ModuleMenuHelper(object=self.module_manager)
