"""An IsoSurface module that allows the user to make contours of input
point data.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance, Bool

# Local imports
from mayavi.core.module import Module
from mayavi.components.contour import Contour
from mayavi.components.poly_data_normals import PolyDataNormals
from mayavi.components.actor import Actor
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `IsoSurface` class.
######################################################################
class IsoSurface(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The contour component.
    contour = Instance(Contour, record=True)

    # Specify if normals are to be computed to make a smoother surface.
    compute_normals = Bool(True, desc='if normals are to be computed '\
                           'to make the iso-surface smoother')

    # The component that computes the normals.
    normals = Instance(PolyDataNormals, record=True)

    # The actor component that represents the iso-surface.
    actor = Instance(Actor, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars'])

    ########################################
    # The view of this object.
    # Commented out, since we are now using the iso_surface_view.py version.
    #view = View([Group(
    #                 Item( name  = 'contour',
    #                       style = 'custom' ),
    #                 show_labels = False,
    #                 show_border = True,
    #                 label       = 'Contours' ),
    #             Group(
    #                 Item( name = 'compute_normals' ),
    #                 '_',
    #                 Item( name         = 'normals',
    #                       style        = 'custom',
    #                       show_label   = False,
    #                       enabled_when = 'compute_normals' ),
    #                 show_border = True,
    #                 label       = 'Normals' ),
    #             Group(
    #                 Item( name  = 'actor',
    #                       style = 'custom' ),
    #                 show_labels = False )
    #             ]
    #            )

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
        # Create the components
        self.contour = Contour(show_filled_contours=False)
        self.normals = PolyDataNormals()
        self.actor = Actor()

        # Setup the actor suitably for this module.
        self.actor.mapper.scalar_visibility = 1

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
        self.contour.inputs = [mm.source]
        # Force the normals setting to be noted.
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
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _compute_normals_changed(self, value):
        if self.module_manager is None:
            return
        actor = self.actor
        if value:
            if actor:
                actor.inputs = [self.normals]
        else:
            if actor:
                actor.inputs = [self.contour]
        self.render()

    def _contour_changed(self, old, new):
        normals = self.normals
        if normals is not None:
            normals.inputs = [new]
        self._change_components(old, new)

    def _normals_changed(self, old, new):
        contour = self.contour
        if contour is not None:
            new.inputs = [contour]
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        # Here we set the inputs in any case to avoid VTK pipeline
        # errors.  The pipeline is corrected when update_pipeline is
        # called anyway.
        contour = self.contour
        if contour is not None:
            new.inputs = [contour]
        self._change_components(old, new)

