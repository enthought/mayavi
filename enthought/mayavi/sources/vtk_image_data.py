"""
A module that offers lots of VTK image data sources
"""
#Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#        Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Enum, Dict, Str
from enthought.traits.ui.api import View, Item, Group
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.core.source import Source
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `VTKImageData` class.
######################################################################
class VTKImageData(Source):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # Flag to set the image data type.
    source = Enum('ellipsoid','gaussian','grid','mandelbrot','noise',
                  'sinusoid','rt_analytic',
                  desc='which image data source to be used')

    # Define the trait 'vtk_image_data_source' whose value must be an instance of
    # type ImageAlgorithm
    vtk_image_data_source = Instance(tvtk.ImageAlgorithm, allow_none=False, 
                                     record=True)


    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['image_data'], 
                               attribute_types=['any'],
                               attributes=['any'])

    # Create the UI for the traits.
    view = View(Group(Item(name='source'),
                  Item(name='vtk_image_data_source',
                       style='custom',
                       resizable=True),
                   label='VTKImageDataSource',
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
        super(VTKImageData, self).__init__(**traits)

        # Initialize the source to the default mode's instance from
        # the dictionary if needed.
        if 'source' not in traits:
            self._source_changed(self.source)
        
    ######################################################################
    # Non-public methods.
    ######################################################################
    def _source_changed(self, value):
        """This method is invoked (automatically) when the `function`
        trait is changed.
        """
        self.vtk_image_data_source = self._source_dict[self.source]
     
    
    def _vtk_image_data_source_changed(self, old, new):
        """This method is invoked (automatically) when the
        image data source is changed ."""

        self.outputs = [self.vtk_image_data_source.output]
        
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
              'rt_analytic':tvtk.RTAnalyticSource()
             }
        return sd
    

   
