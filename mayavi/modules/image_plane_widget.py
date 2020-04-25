"""A simple ImagePlaneWidget module to view image data.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool, on_trait_change
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.core.common import error
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ImagePlaneWidget` class.
######################################################################
class ImagePlaneWidget(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    ipw = Instance(tvtk.ImagePlaneWidget, allow_none=False, record=True)

    use_lookup_table = Bool(True,
            help='Use a lookup table to map input scalars to colors')

    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['scalars'])

    view = View(Group(Item(name='ipw', style='custom', resizable=True),
                      show_labels=False
                      ),
                width=600,
                height=600,
                resizable=True,
                scrollable=True
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
        # Create the various objects for this module.
        self.ipw = tvtk.ImagePlaneWidget(display_text=1,
                                         key_press_activation=0,
                                         left_button_action=1,
                                         middle_button_action=0,
                                         user_controlled_lookup_table=True)
        self.setup_lut()


    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mod_mgr = self.module_manager
        if mod_mgr is None:
            return

        # Data is available, so set the input for the IPW.
        input = mod_mgr.source.outputs[0]
        dataset = mod_mgr.source.get_output_dataset()
        if not (dataset.is_a('vtkStructuredPoints') \
                or dataset.is_a('vtkImageData')):
            msg = 'ImagePlaneWidget only supports structured points or '\
                  'image data.'
            error(msg)
            raise TypeError(msg)

        self.configure_input(self.ipw, input)
        self.setup_lut()

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True


    @on_trait_change('use_lookup_table')
    def setup_lut(self):
        # Set the LUT for the IPW.
        if self.use_lookup_table:
            if self.module_manager is not None:
                self.ipw.lookup_table = \
                                self.module_manager.scalar_lut_manager.lut
        else:
            self.ipw.color_map.lookup_table = None
        self.render()

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _ipw_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
            self.widgets.remove(old)
        new.on_trait_change(self.render)
        self.widgets.append(new)
        if old is not None:
            self.update_pipeline()
        self.pipeline_changed = True
