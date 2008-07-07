#!/usr/bin/env python
import csv

import numpy

from enthought.traits.api import HasTraits, Str, Bool, Dict, Int, Float, Array
from enthought.traits.ui.api import View, Item



class CSV_Handler(HasTraits):

    # filename is assigned by user at object instantiation
    filename = Str
    
    # attributes assigned automatically, and
    # user can then edit them
    delimeter = Str # if " ", must be converted to None for loadtxt to work
    doublequote = Bool
    escapechar = Str
    lineterminator = Str
    quotechar = Str("'")
    quoting = 0
    skipinitialspace = Bool
    
    # storing the dictionary of arrays
    data_array = Array
    data_dict = Dict
    
    # attributes for creating the GUI
    view = View(  Item(name = 'filename',
                            label = 'name of CSV file'
                            ), 
                        Item(name = 'delimeter'
                            ),
                        Item(name = 'doublequote'
                            ),
                        Item(name = 'escapechar'
                            ),
                        Item(name = 'lineterminator'
                            ),
                        Item(name = 'quotechar'
                            ),
                        Item(name = 'quoting'
                            ),
                        Item(name = 'skipinitialspace'
                            ),
                        title = 'Data on CSV file format'
                    )

    def _filename_changed(self):
        """Called automatically when user initializes
        object with a filename.  It then guesses at formatting
        of CSV file and prompts user to verify or change those
        attributes.  Data is then loaded accordingly.
        """
        
        # making best guesses at format of the CSV file
        # by instantiating Sniff class.
        sniffed_info = trial_Sniff(self.filename)
        self.delimeter = sniffed_info.delimeter
        self.doublequote = sniffed_info.doublequote
        self.escapechar = sniffed_info.escapechar
        self.lineterminator = sniffed_info.lineterminator
        self.quotechar = sniffed_info.quotechar
        self.quoting = sniffed_info.quoting
        self.skipinitialspace = sniffed_info.skipinitialspace
        
        # allow user to change guessed-at attributes
        self.edit_traits()
        
        # load file into
        self.data_array = loadtxt( fname = self.filename,
                                            dtype = Float,
                                            comments = '#',
                                            delimeter = self._help_delimit(self.delimeter),
                                            converters = None,
                                            usecols = None,
                                            unpack = False
                                        )
                                        
        # make self.data_dict that contains approriate information
    
    def _help_delim(self, delim):
        if delim == '' or delim == ' ' or delim == '\t':
            return None
        else:
            return delim
        
        
    def sniff(self):
        print 'sniff:', self.filename

        print numpy.loadtxt(self.filename, skiprows=4)
        
        print 'Has header:', csv.Sniffer().has_header(self.filename)
        d = csv.Sniffer().sniff(self.filename)
        print 'Delimiter: %r' % d.delimiter
        print 'LineTerm : %r' % d.lineterminator
        
        
        self.quotechar = d.quotechar


class trial_Sniff(HasTraits):
    """ ONLY HERE SO THAT CSV HANDLER CAN CALL IT
    """
    filename = Str
    delimeter = Str # if " ", must be converted to None for loadtxt to work
    doublequote = False
    escapechar = Str
    lineterminator = Str
    quotechar = Str("'")
    quoting = 0
    skipinitialspace = Bool

    def __init__(self, fname):
        return

class Sniff:
    def __init__(self, filename):
        f = open(filename, 'r')



x = CSV_Handler(filename='example1.csv')

#x.configure_traits()
