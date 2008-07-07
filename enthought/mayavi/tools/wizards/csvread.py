# This function returns an object that contains the information in a CSV file

from numpy import loadtxt,  array
from enthought.traits.api import HasTraits, Dict, Str
from enthought.traits.ui.api import View, Item, Group

class csvObject(HasTraits):
	
	""" 	This class contains information from a CSV file
		and makes it accessible to the user."""
	
	filename = Str
	
	dictionary = Dict
	
	view = View(
			Item(name = 'filename',
				label = 'name of CSV file: '
				)#,
			#Item(name = 'dictionary',
			#	label = 'dictionary of information'
			#	)
			)
	
	
	
	def _filename_changed(self):
		readfile = open(self.filename)
		names = [name.strip() for name in readfile.readline().split(', ')]
		print 'names: ', names
		data = [float(elem.strip(',')) for elem in readfile.read().split()]
		print 'data: ', data
		self.dictionary = {}
		for i, name in enumerate(names):
			self.dictionary.update({name : data[i::len(names)]})	
			


# script statement tests the csvObject class on a sample CSV file
myObj = csvObject(filename = 'csvtest.txt')
print "dict: ", myObj.dictionary
print "column 2: ", myObj.dictionary['col2']