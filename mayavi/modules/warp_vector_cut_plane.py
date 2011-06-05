# -*- coding: UTF-8 -*-
"""Takes an arbitrary slice of the input data using an implicit cut
plane and warps it according to the vector field data.  The scalars
are displayed on the warped surface as colors.

"""
# Authors: Fr�d�ric Petit and Prabhu Ramachandran
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance, Bool
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk

# Local imports
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.components.implicit_plane import ImplicitPlane
from mayavi.components.cutter import Cutter
from mayavi.filters.warp_vector import WarpVector
from mayavi.components.poly_data_normals import PolyDataNormals
from mayavi.components.actor import Actor


######################################################################
# `VectorCutPlane` class.
######################################################################
class WarpVectorCutPlane(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The implicit plane widget used to place the implicit function.
    implicit_plane = Instance(ImplicitPlane, allow_none=False,
                              record=True)

    # The cutter.  Takes a cut of the data on the implicit plane.
    cutter = Instance(Cutter, allow_none=False, record=True)

    # The WarpVectorCutPlane component that warps the data.
    warp_vector = Instance(WarpVector, allow_none=False, record=True)

    # Specify if vector normals are to be computed to make a smoother surface.
    compute_normals = Bool(False, desc='if normals are to be computed '\
                           'to make the warped surface smoother')

    # The component that computes the normals.
    normals = Instance(PolyDataNormals, record=True)

    # The Actor component.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    ########################################
    # View related traits.

    _warp_group = Group(Item(name='filter',
                             style='custom',
                             editor=\
                             InstanceEditor(view=
                                            View(Item('scale_factor')))),
                        show_labels=False)

    view = View(Group(Item(name='implicit_plane', style='custom'),
                      label='ImplicitPlane',
                      show_labels=False),
                Group(Group(Item(name='warp_vector',
                                 style='custom',
                                 resizable=True,
                                 show_label=False,
                                 editor=InstanceEditor(view=View(_warp_group))
                                 ),
                            ),
                      Item(name='_'),
                      Item(name='compute_normals'),
                      Group(Item(name='normals',
                                 style='custom',
                                 show_label=False,
                                 enabled_when = 'compute_normals'),
                            ),
                      label='WarpVector',
                      show_labels=True),
                Group(Item(name='actor', style='custom'),
                      label='Actor',
                      show_labels=False),
                resizable=True,
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
        # Create the objects and set them up.
        self.implicit_plane = ImplicitPlane()
        self.cutter = Cutter()
        self.warp_vector = WarpVector()
        self.normals = PolyDataNormals()
        actor = self.actor = Actor()
        actor.mapper.scalar_visibility = 1

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        self.implicit_plane.inputs = [mm.source]

        # Force the vector normals setting to be noted.
        self._compute_normals_changed(self.compute_normals)

        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the other components should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public traits.
    ######################################################################
    def _compute_normals_changed(self, value):
        if self.module_manager is None:
            return
        actor = self.actor
        if actor is not None:
            if value:
                actor.inputs = [self.normals]
            else:
                actor.inputs = [self.warp_vector]
        self.render()

    def _normals_changed(self, old, new):
        warp_vector = self.warp_vector
        compute_normals = self.compute_normals
        if compute_normals is not None:
            new.inputs = [warp_vector]
        self._compute_normals_changed(self.compute_normals)
        self._change_components(old, new)

    def _implicit_plane_changed(self, old, new):
        cutter = self.cutter
        if cutter is not None:
            cutter.cut_function = new.plane
            cutter.inputs = [new]
        self._change_components(old, new)

    def _warp_vector_changed(self, old, new):
        cutter = self.cutter
        if cutter is not None:
            new.inputs = [cutter]
        self._compute_normals_changed(self.compute_normals)
        self._change_components(old, new)

    def _cutter_changed(self, old, new):
        ip = self.implicit_plane
        if ip is not None:
            new.cut_function = ip.plane
            new.inputs = [ip]
        w = self.warp_vector
        if w is not None:
            w.inputs = [new]
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        self._compute_normals_changed(self.compute_normals)
        self._change_components(old, new)

