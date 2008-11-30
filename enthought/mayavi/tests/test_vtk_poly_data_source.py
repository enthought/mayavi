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

# Local imports.
from common import TestEngine,Engine

# Enthought library imports.
from enthought.mayavi.sources.vtk_poly_data import VTKPolyData
from enthought.mayavi.modules.surface import Surface
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.tools.show import show

class TestVTKPolyDataSource(unittest.TestCase):    
  
    def setUp(self):
	"""Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        
        e = TestEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()
	
	poly_data = VTKPolyData()	
	e.add_source(poly_data)	

	outline = Outline()
	e.add_module(outline)	
	
	surface = Surface()
	e.add_module(surface)	
	
	poly_data.vtk_poly_data_source.shaft_radius = 0.05
	poly_data.vtk_poly_data_source.shaft_resolution = 7	
	poly_data.vtk_poly_data_source.tip_radius = 0.1
    
        self.e=e       	
	self.scene = e.current_scene   
	
        return
        
    def tearDown(self):
	"""For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return
    
    def test_poly_data_source(self):
	"""Do the basic testing"""
	s = self.scene
	src = s.children[0]		

	#Check the properties of the default source
	self.assertEqual(src.source,'arrow')
	self.assertEqual(src.vtk_poly_data_source.shaft_radius,0.05)	
	self.assertEqual(src.vtk_poly_data_source.shaft_resolution,7)	
	self.assertEqual(src.vtk_poly_data_source.tip_radius,0.1)	
	show()
	
    def test_change(self):
	"""Test if it works fine on changing the source"""
	s = self.scene
	src = s.children[0]	
	ot = src.children[0].children[0]
	src.source = 'cone'	
	
	#Check with the default properties of cone to verify that the source has actually changed 
	self.assertEqual(src.source,'cone')
	
	#Check the outline bounds
	self.assertEqual(numpy.allclose(ot.outline_filter.output.bounds,(-0.5, 0.5, -0.5, 0.5, -0.433, 0.433),atol=1.01e-03),True)
	
	self.assertEqual(numpy.allclose(src.vtk_poly_data_source.angle,26.565,atol=1.01e-03),True)
	self.assertEqual(numpy.allclose(src.vtk_poly_data_source.direction,(1., 0., 0.)),True)
	self.assertEqual(src.vtk_poly_data_source.radius,0.5)	
	self.assertEqual(src.vtk_poly_data_source.height,1.0)
	self.assertEqual(numpy.allclose(src.vtk_poly_data_source.center,(0., 0., 0.)),True)	

	#Modify Properties and check again	
	src.vtk_poly_data_source.height = 1.5
	src.vtk_poly_data_source.angle = 30
	self.assertEqual(numpy.allclose(src.vtk_poly_data_source.radius,0.866,atol=1.01e-03),True)
	show()
	


if __name__ == '__main__':
    unittest.main()
