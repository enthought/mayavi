"""Takes a cut plane of any input data set using an implicit plane and
plots the data with optional contouring and scalar warping.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool
from traitsui.api import View, Group, Item, InstanceEditor

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.implicit_plane import ImplicitPlane
from mayavi.components.cutter import Cutter
from mayavi.filters.warp_scalar import WarpScalar
from mayavi.components.poly_data_normals import PolyDataNormals
from mayavi.components.contour import Contour
from mayavi.components.actor import Actor


######################################################################
# `ScalarCutPlane` class.
######################################################################
class ScalarCutPlane(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The implicit plane widget used to place the implicit function.
    implicit_plane = Instance(ImplicitPlane, allow_none=False,
                              record=True)

    # The cutter.  Takes a cut of the data on the implicit plane.
    cutter = Instance(Cutter, allow_none=False, record=True)

    # Specifies if contouring is to be done or not.
    enable_contours = Bool(False, desc='if contours are generated')

    # The Contour component that contours the data.
    contour = Instance(Contour, allow_none=False, record=True)

    # Specifies if scalar warping is to be done or not.
    enable_warp_scalar = Bool(False, desc='if scalar warping is enabled')

    # The WarpScalarCutPlane component that warps the data.
    warp_scalar = Instance(WarpScalar, allow_none=False, record=True)

    # Specify if scalar normals are to be computed to make a smoother surface.
    compute_normals = Bool(False, desc='if normals are to be computed '\
                           'to make the warped scalar surface smoother')

    # The component that computes the scalar normals.
    normals = Instance(PolyDataNormals, allow_none=False, record=True)

    # The actor component that represents the visualization.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars'])

    ########################################
    # View related code.

    _warp_group = Group(Item(name='filter',
                             style='custom',
                             editor=\
                             InstanceEditor(view=
                                            View(Item('scale_factor')))),
                        show_labels=False)

    view = View(Group(Item(name='implicit_plane',
                           style='custom'),
                      label='ImplicitPlane',
                      show_labels=False),
                Group(Group(Item(name='enable_contours')),
                      Group(Item(name='contour',
                                 style='custom',
                                 enabled_when='object.enable_contours'),
                            show_labels=False),
                      label='Contours',
                      show_labels=False),
                Group(Item(name='enable_warp_scalar'),
                      Group(Item(name='warp_scalar',
                                 enabled_when='enable_warp_scalar',
                                 style='custom',
                                 editor=InstanceEditor(view=
                                                       View(_warp_group))
                                 ),
                            show_labels=False,
                            ),
                      Item(name='_'),
                      Item(name='compute_normals',
                           enabled_when='enable_warp_scalar'),
                      Item(name='normals',
                           style='custom',
                           show_label=False,
                           enabled_when='compute_normals and enable_warp_scalar'),
                      label='WarpScalar',
                      show_labels=True),
                Group(Item(name='actor',
                           style='custom'),
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
        # Create the objects.
        self.implicit_plane = ImplicitPlane()
        self.cutter = Cutter()
        self.contour = Contour(auto_contours=True, number_of_contours=10)
        self.warp_scalar = WarpScalar()
        self.normals = PolyDataNormals()
        self.actor = Actor()

        # Setup the actor suitably for this module.
        prop = self.actor.property
        prop.line_width = 2.0

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        # Data is available, so set the input for the grid plane.
        self.implicit_plane.inputs = [mm.source]

        # Ensure that the warped scalar surface's normal is setup right.
        self.warp_scalar.filter.normal = self.implicit_plane.normal

        # This makes sure that any changes made to enable_warp when
        # the module is not running are updated when it is started --
        # this in turn calls the other functions (normals and
        # contours) internally.
        self._enable_warp_scalar_changed(self.enable_warp_scalar)

        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

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
    def _get_warp_output(self):
        """Helper function to return the warped (or not) output
        depending on settings.
        """
        if self.enable_warp_scalar:
            if self.compute_normals:
                return self.normals
            else:
                return self.warp_scalar
        else:
            return self.cutter

    def _get_contour_output(self):
        """Helper function to return the contoured (and warped (or
        not)) output depending on settings.
        """
        if self.enable_contours:
            return self.contour
        else:
            return self._get_warp_output()

    def _filled_contours_changed_for_contour(self, value):
        """When filled contours are enabled, the mapper should use the
        the cell data, otherwise it should use the default scalar
        mode.
        """
        if value:
            self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _enable_warp_scalar_changed(self, value):
        """Turns on and off the scalar warping."""
        if self.module_manager is None:
            return

        if value:
            self.warp_scalar.inputs = [self.cutter]
        else:
            self.warp_scalar.inputs = []
        self._compute_normals_changed(self.compute_normals)
        self.render()

    def _compute_normals_changed(self, value):
        if self.module_manager is None:
            return

        if self.enable_warp_scalar:
            normals = self.normals
            if value:
                normals.inputs = [self.warp_scalar]
            else:
                normals.inputs = []
        self._enable_contours_changed(self.enable_contours)
        self.render()

    def _enable_contours_changed(self, value):
        """Turns on and off the contours."""
        if self.module_manager is None:
            return

        actor = self.actor
        if value:
            self.contour.inputs = [self._get_warp_output()]
            actor.inputs = [self._get_contour_output()]
            if self.contour.filled_contours:
                actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.contour.inputs = []
            actor.inputs = [self._get_warp_output()]
            actor.mapper.scalar_mode = 'default'
        self.render()

    def _normals_changed(self, old, new):
        warp_scalar = self.warp_scalar
        if warp_scalar is not None:
            new.inputs = [warp_scalar]
            self._compute_normals_changed(self.compute_normals)
        self._change_components(old, new)

    def _implicit_plane_changed(self, old, new):
        cutter = self.cutter
        if cutter is not None:
            cutter.cut_function = new.plane
            cutter.inputs = [new]
            # Update the pipeline.
            self._enable_warp_scalar_changed(self.enable_warp_scalar)
        # Hook up events to set the normals of the warp filter.
        if old is not None:
            old.widget.on_trait_change(self._update_normal, 'normal', remove=True)
        new.widget.on_trait_change(self._update_normal, 'normal')
        self._change_components(old, new)

    def _cutter_changed(self, old, new):
        ip = self.implicit_plane
        if ip is not None:
            new.cut_function = ip.plane
            new.inputs = [ip]
            # Update the pipeline.
            self._enable_warp_scalar_changed(self.enable_warp_scalar)
        self._change_components(old, new)

    def _contour_changed(self, old, new):
        # Update the pipeline.
        self._enable_contours_changed(self.enable_contours)
        self._change_components(old, new)

    def _warp_scalar_changed(self, old, new):
        # Update the pipeline.
        self._enable_warp_scalar_changed(self.enable_warp_scalar)
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        # Update the pipeline.
        self._enable_contours_changed(self.enable_contours)
        self._change_components(old, new)

    def _update_normal(self):
        """Invoked when the orientation of the implicit plane changes.
        """
        ws = self.warp_scalar
        if ws is not None:
            ws.filter.normal = self.implicit_plane.widget.normal

