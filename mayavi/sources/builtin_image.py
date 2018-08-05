"""
A module that offers lots of VTK image data sources
"""
#Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#        Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Enum, Dict, Str
from traitsui.api import View, Item, Group
from tvtk.api import tvtk

# Local imports
from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `BuiltinImage` class.
######################################################################
class BuiltinImage(Source):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # Flag to set the image data type.
    source = Enum('ellipsoid','gaussian','grid','mandelbrot','noise',
                  'sinusoid','rt_analytic',
                  desc='which image data source to be used')

    # Define the trait 'data_source' whose value must be an instance of
    # type ImageAlgorithm
    data_source = Instance(tvtk.ImageAlgorithm, allow_none=False,
                                     record=True)


    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])

    # Create the UI for the traits.
    view = View(Group(Item(name='source'),
                  Item(name='data_source',
                       style='custom',
                       resizable=True),
                   label='Image Source',
                    show_labels=False),
             resizable=True)

    ########################################
    # Private traits.

    # A dictionary that maps the source names to instances of the
    # image data objects.
    _source_dict = Dict(Str,
                          Instance(tvtk.ImageAlgorithm,
                                   allow_none=False))

    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        # Call parent class' init.
        super(BuiltinImage, self).__init__(**traits)

        # Initialize the source to the default mode's instance from
        # the dictionary if needed.
        if 'source' not in traits:
            self._source_changed(self.source)

    def __set_pure_state__(self, state):
        self.source = state.source
        super(BuiltinImage, self).__set_pure_state__(state)

    def has_output_port(self):
        """ Return True as the data source has output port."""
        return True

    def get_output_object(self):
        """ Return the data source output port."""
        return self.data_source.output_port

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _source_changed(self, value):
        """This method is invoked (automatically) when the `function`
        trait is changed.
        """
        self.data_source = self._source_dict[self.source]

    def _data_source_changed(self, old, new):
        """This method is invoked (automatically) when the
        image data source is changed ."""

        self.outputs = [self.data_source]

        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)

    def __source_dict_default(self):
        """The default _source_dict trait."""
        sd = {
              'ellipsoid':tvtk.ImageEllipsoidSource(),
              'gaussian':tvtk.ImageGaussianSource(),
              'grid':tvtk.ImageGridSource(),
              'mandelbrot':tvtk.ImageMandelbrotSource(),
              'noise':tvtk.ImageNoiseSource(),
              'sinusoid':tvtk.ImageSinusoidSource(),
             }
        if hasattr(tvtk, 'RTAnalyticSource'):
            sd['rt_analytic'] = tvtk.RTAnalyticSource()
        else:
            sd['rt_analytic'] = tvtk.ImageNoiseSource()
        return sd
