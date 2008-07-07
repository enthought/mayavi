#!/usr/bin/env python
import csv

import numpy

from enthought.traits.api import HasTraits, Int, Str, Float
from enthought.traits.ui.api import View



class CSV_Handler(HasTraits):

    filename = Str

    quotechar = Str("'")
    
    view = View('filename', 'quotechar')

    def _filename_changed(self, old, new):
        print 'old:', old
        print 'new:', new
        
        self.sniff()
        
        
    def sniff(self):
        print 'sniff:', self.filename

        print numpy.loadtxt(self.filename, skiprows=4)
        
        print 'Has header:', csv.Sniffer().has_header(self.filename)
        d = csv.Sniffer().sniff(self.filename)
        print 'Delimiter: %r' % d.delimiter
        print 'LineTerm : %r' % d.lineterminator
        
        
        self.quotechar = d.quotechar


class Sniff:
    def __init__(self, filename):
        f = open(filename, 'r')



x = CSV_Handler(filename='example1.csv')

#x.configure_traits()
