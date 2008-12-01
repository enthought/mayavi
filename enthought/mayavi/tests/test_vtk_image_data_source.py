# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from StringIO import StringIO
import copy
import numpy
import unittest
import pickle
from numpy import array

# Enthought library imports.
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.core.null_engine import NullEngine
from enthought.mayavi.sources.vtk_image_data import VTKImageData
from enthought.mayavi.modules.surface import Surface
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.tools.show import show

class TestVTKImageDataSource(unittest.TestCase):    
  
    def setUp(self):
        
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()
    
        image_data = VTKImageData() 
        e.add_source(image_data)    

        outline = Outline()
        e.add_module(outline)   
        
        surface = Surface()
        e.add_module(surface)   

        image_data.vtk_image_data_source.radius = array([ 80.,  80.,  80.])
        image_data.vtk_image_data_source.center = array([ 150.,  150.,    0.])
        image_data.vtk_image_data_source.whole_extent = array([ 10, 245,  10, 245,   0,   0])

        self.e=e        
        self.scene = e.current_scene   
    
        return
        
    def tearDown(self):
        self.e.stop()
        return
    
    def test_vtk_image_data_source(self):
        s = self.scene
        src = s.children[0]     
        self.assertEqual(src.source,'ellipsoid')
        self.assertEqual(numpy.allclose(src.vtk_image_data_source.center,(150., 150., 0.)),True)
        self.assertEqual(numpy.allclose(src.vtk_image_data_source.radius,(80., 80., 80.)),True) 
        self.assertEqual(numpy.allclose(src.vtk_image_data_source.whole_extent,(10, 245,  10, 245,   0,   0)),True) 
        show()

    
    
    def test_change(self):
    s = self.scene
    src = s.children[0] 
    ot = src.children[0].children[0]
    src.source = 'gaussian' 
    #Check with the default properties of gaussian image to verify that the source has actually changed 
    self.assertEqual(src.source,'gaussian') 
    self.assertEqual(numpy.allclose(src.vtk_image_data_source.center,(0., 0., 0.)),True)
    self.assertEqual(src.vtk_image_data_source.maximum,1.0) 
    self.assertEqual(src.vtk_image_data_source.standard_deviation,100)  
    
    #Check the scalar ranges    
    self.assertEqual(numpy.allclose(src.outputs[0].point_data.scalars.range,(0.00149, 1.0),atol=1.01e-03),True)
    
    src.vtk_image_data_source.maximum = 2.0
    src.vtk_image_data_source.standard_deviation = 15
    self.assertEqual(src.vtk_image_data_source.maximum,2.0) 
    self.assertEqual(src.vtk_image_data_source.standard_deviation,15)   
    show()
    
    

if __name__ == '__main__':
    unittest.main()
