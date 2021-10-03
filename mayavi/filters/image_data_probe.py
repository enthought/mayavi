# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import numpy

# Enthought library imports.
from traits.api import Instance, Bool, Array, Button, Str
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
import tvtk.common as tvtk_common

# Local imports.
from mayavi.core.filter import Filter
from mayavi.core.pipeline_info import PipelineInfo


################################################################################
# `ImageDataProbe` class.
################################################################################
class ImageDataProbe(Filter):
    """
    A filter that can be used to probe any dataset using a Structured
    Points dataset.  The filter also allows one to convert the scalar
    data to an unsigned short array so that the scalars can be used for
    volume visualization.
    """

    # The image data onto which the data is probed.
    probe_data = Instance(tvtk.ImageData, args=())

    # The probe filter.
    filter = Instance(tvtk.ProbeFilter, args=())

    rescale_scalars = Bool(False, desc='if the input scalars are '\
                                       'rescaled to an unsigned short '\
                                       'array')

    # Specifies if we can change the spacing/dimensions -- not allowed
    # for imagedata/structured points data.
    allow_changes = Bool(True)

    # Spacing of points in the image data.
    spacing = Array(value=(0.0, 0.0, 0.0),
                    shape=(3,),
                    cols=1,
                    dtype=float,
                    enter_set=True,
                    auto_set=False,
                    labels=['sx', 'sy', 'sz'],
                    desc='the spacing of points')

    # Dimensions of the image data.
    dimensions = Array(value=(0, 0, 0),
                       shape=(3,),
                       cols=1,
                       dtype=int,
                       enter_set=True,
                       auto_set=False,
                       labels=['nx', 'ny', 'nz'],
                       desc='the dimensions of the image data')

    # Reset settings to defaults.
    reset_defaults = Button(desc='if probe data is reset to defaults')

    # Name of rescaled scalar to generate.
    rescaled_scalar_name = Str('probe_us_array')

    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])

    ########################################
    # Private traits.

    # A trait to prevent static handlers from firing unnecessarily.
    _event_handled = Bool(False)

    ########################################
    # View related traits.

    view = View(Group(Item(name='dimensions',
                           enabled_when='allow_changes'
                           ),
                      Item(name='spacing',
                           enabled_when='allow_changes'),
                      Item(name='rescale_scalars'),
                      Item(name='reset_defaults',
                           show_label=False),
                      ),
                resizable=True)


    ######################################################################
    # `Filter` interface.
    ######################################################################
    def setup_pipeline(self):
        """Creates the pipeline."""
        self.configure_input_data(self.filter, self.probe_data)

    def update_pipeline(self):
        """Connect and update the pipeline."""
        inputs = self.inputs
        if len(inputs) == 0:
            return

        fil = self.filter
        self.configure_source_data(fil, inputs[0].outputs[0])
        reset = False
        if self.dimensions.sum() == 0:
            reset = True
        self._setup_probe_data(reset)
        fil.update()
        self._rescale_scalars_changed(self.rescale_scalars)
        self._set_outputs([fil])

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _setup_probe_data(self, reset=False):
        pd = self.probe_data
        input = self.inputs[0].get_output_dataset()
        if input.is_a('vtkImageData'):
            self.allow_changes = False
            self.trait_set(spacing=input.spacing,
                           dimensions=input.dimensions)
            pd.trait_set(origin=input.origin,
                         dimensions=input.dimensions,
                         spacing=input.spacing)
            pd.update()
        elif reset:
            self.allow_changes = True
            b = numpy.array(input.bounds)
            pd.origin = b[::2]
            l = b[1::2] - b[::2]
            tot_len = sum(l)
            npnt = pow(input.number_of_points, 1./3.) + 0.5
            fac = 3.0*npnt/tot_len
            dims = (l*fac).astype(int) + 1
            extent = (0, dims[0] - 1, 0, dims[1] - 1, 0, dims[2] - 1)
            pd.trait_set(extent=extent,
                         dimensions=dims)

            max_dim = dims.max()
            dims = (dims-1).clip(min=1, max=max_dim+1)
            l = l.clip(min=1e-3, max=l.max()+1.0)
            pd.spacing = l/dims
            self._event_handled = True
            self.trait_set(spacing=pd.spacing,
                           dimensions=pd.dimensions)
            self._event_handled = False

    def _rescale_scalars_changed(self, value):
        out = self.filter.output
        pd = out.point_data
        sc = pd.scalars
        if sc is None:
            # no input scalars
            return

        if not value:
            dataset = self.inputs[0].get_output_dataset()
            orig_sc = dataset.point_data.scalars
            if sc.is_a('vtkUnsignedShortArray') and \
               sc.name == self.rescaled_scalar_name:
                pd.set_active_scalars(orig_sc.name)
                pd.update()
                self.pipeline_changed = True
                self.render()

            return

        s_min, s_max = sc.range
        # checking to see if input array is constant.
        avg = (s_max + s_min)*0.5
        diff = 1
        if (s_max > avg) and (avg > s_min):
            diff = s_max - s_min

        arr = (sc.to_array() - s_min)*65535.0/diff
        uc = tvtk.UnsignedShortArray(name=self.rescaled_scalar_name)
        uc.from_array(arr)
        pd.add_array(uc)
        pd.set_active_scalars(self.rescaled_scalar_name)
        pd.update()
        self.pipeline_changed = True
        self.render()

    def _dimensions_changed(self, value):
        if not self.allow_changes or self._event_handled:
            return

        max_d = value.max()
        dims = (value-1).clip(min=1, max=max_d)
        b = numpy.array(self.inputs[0].get_output_dataset().bounds)
        l = b[1::2] - b[::2]
        self.spacing = l/dims
        self._update_probe()

    def _spacing_changed(self, value):
        if not self.allow_changes or self._event_handled:
            return
        b = numpy.array(self.inputs[0].get_output_dataset().bounds)
        l = b[1::2] - b[::2]
        dims = (l/value + 0.5).astype(int) + 1
        # Recalculate space because of rounding.
        maxd = dims.max()
        dims1 = (dims - 1).clip(min=1, max=maxd)
        sp = l/dims1
        self._event_handled = True
        self.trait_set(spacing=sp, dimensions=dims)
        self._event_handled = False
        self._update_probe()

    def _update_probe(self):
        pd = self.probe_data
        dims = self.dimensions
        spacing = self.spacing
        extent = (0, dims[0] - 1, 0, dims[1] - 1, 0, dims[2] - 1)
        pd.trait_set(extent=extent,
                     dimensions=dims,
                     spacing=spacing)
        pd.modified()
        fil = self.filter
        w = fil.global_warning_display
        fil.global_warning_display = False
        fil.remove_all_inputs()
        self.configure_input_data(fil, pd)
        fil.update_whole_extent()
        fil.update()
        self._rescale_scalars_changed(self.rescale_scalars)
        fil.global_warning_display = w
        self.data_changed = True

    def _reset_defaults_fired(self):
        self._setup_probe_data(reset=True)
        self._rescale_scalars_changed(self.rescale_scalars)
