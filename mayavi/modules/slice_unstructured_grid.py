"""This module takes a slice of the unstructured grid data and shows
the cells that intersect or touch the slice."""

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.implicit_plane import ImplicitPlane
from mayavi.components.actor import Actor
from mayavi.core.common import error


######################################################################
# `MyModule` class.
######################################################################
class SliceUnstructuredGrid(Module):
    """This module takes a slice of the unstructured grid data and
    shows the cells that intersect or touch the slice."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The implicit plane widget.
    implicit_plane = Instance(ImplicitPlane, allow_none=False,
                              record=True)

    # Extract the cells to display.
    extract_geometry = Instance(tvtk.ExtractGeometry, allow_none=False,
                                record=True)

    # The geometry filter.
    geom_filter = Instance(tvtk.GeometryFilter, allow_none=False,
                           record=True)

    # The actor component that represents the visualization.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # View related code.

    view = View(Group(Item(name='implicit_plane', style='custom'),
                      label='ImplicitPlane',
                      show_labels=False),
                Group(Item(name='extract_geometry', style='custom',
                           resizable=True),
                      label='Extract Geometry',
                      show_labels=False),
                Group(Item(name='geom_filter', style='custom',
                           resizable=True),
                      label='Geometry Filter',
                      show_labels=False),
                Group(Item(name='actor', style='custom'),
                      label='Actor',
                      show_labels=False)
                )

    ######################################################################
    # `Module` interface
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
        # Create the components and set them up.
        self.implicit_plane = ImplicitPlane()
        ex = tvtk.ExtractGeometry(extract_only_boundary_cells=1,
                                  extract_boundary_cells=1)
        self.extract_geometry = ex
        self.geom_filter = tvtk.GeometryFilter()

        # Setup the actor suitably for this module.
        self.actor = Actor()
        self.actor.property.representation = 'w'

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mod_mgr = self.module_manager
        if mod_mgr is None:
            return

        # Data is available, so set the input for the grid plane.
        input = mod_mgr.source.get_output_dataset()
        if not input.is_a('vtkUnstructuredGrid'):
            error('SliceUnstructuredGrid only works with input '\
                  'unstructured grids')
        self.implicit_plane.inputs = [mod_mgr.source]
        src = self.module_manager.source
        self.configure_connection(self.extract_geometry, src)

        # Set the LUT for the mapper.
        self.actor.set_lut(self.module_manager.scalar_lut_manager.lut)

        # Now flush the pipeline
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the components should do the rest if
        # they are connected.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _implicit_plane_changed(self, old, new):
        ex = self.extract_geometry
        if ex is not None:
            ex.implicit_function = new.plane
        self._change_components(old, new)

    def _extract_geometry_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)

        mm = self.module_manager
        if mm is not None:
            src = mm.source
            self.configure_connection(new, src)
        ip = self.implicit_plane
        if ip is not None:
            new.implicit_function = ip.plane
        gf = self.geom_filter
        if gf is not None:
            gf.input_connection = new.output_port

        new.on_trait_change(self.render)
        self.update_pipeline()

    def _geom_filter_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)

        ex = self.extract_geometry
        if ex is not None:
            new.input_connection = ex.output_port

        new.on_trait_change(self.render)
        self.outputs = [new.output_port]

    def _actor_changed(self, old, new):
        new.scene = self.scene
        new.inputs = [self]
        self._change_components(old, new)
