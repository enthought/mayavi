#!/usr/bin/env python
import csv
import numpy

from enthought.traits.api import HasTraits, Str, Bool, Dict, \
        Int, Float, Array, true, false, Any, Type, Enum, List, Tuple
from enthought.traits.ui.api import View, Item
#from Sniff import Sniff

class _ColumnSpec(HasTraits):
    name = Str
    type = Enum('float', 'string')
    view = View(Item(name = 'name', 
                            style = 'readonly'
                        ),
                        Item(name = 'type'
                        )
                    )

class CSVObj(HasTraits):
    """An object for accessing the information stored in a
    CSV file, allowing for significant variation in the formatting
    of the file.
    """
    #TODO:
    #better GUI (inc casting of the type so it's more readable)
    #    plus make OK button work

    # filename is assigned by user at object instantiation
    filename = Str
    
    # formatting attributes.
    # These are pre-assigned automatically, and the
    # user can edit them.
    _dtype = Any # Tuple(_ColumnSpec) or Enum('Float', 'Int',  'Str')
    dtype = Dict #Dict # Dict if store_as_cols, else just a type
    data_type_if_large = Type
    delimiter = Str
    skiprows = Int
    store_as_cols = Bool(True)
    comments = Str
        
    # storing the data
    _array = Array
    data = Any # used to access data in _array.  Type depends on intended interpretation of _array
    
    # attributes for creating the GUI
    view_store_as_cols = View(Item( name = 'store_as_cols',
                                                    label = """Store columns individually and by name,
                                                    rather than as a single large array.
                                                    """
                                                ),
                                        resizable = True,
                                        buttons = ['OK', 'Cancel', 'Help'],
                                        title = 'store columns individually?',
                                        )
    view_cols  =  View(Item(name = '_dtype',
                                label = 'data type of each column',                               
                            ),
                        Item(name = 'delimiter',
                                label = 'delimiter within a row',
                            ),
                        Item(name = 'skiprows',
                                label = 'number of rows to skip',
                            ),
                        #Item(name = 'store_as_cols',
                         #      label = 'store data as columns?',
                         # ),
                        Item(name = 'comments',
                                label = 'character to denote a comment line',
                            ),
                        resizable = True,
                        buttons = ['OK', 'Cancel', 'Help'],
                        title = 'Data on CSV file format',
                    )
                    
    view_noncols = View(Item(name = 'data_type_if_large',
                                label = 'type of data',                               
                            ),
                        Item(name = 'delimiter',
                                label = 'delimiter within a row',
                            ),
                        Item(name = 'skiprows',
                                label = 'number of rows to skip',
                            ),
                        #Item(name = 'store_as_cols',
                         #       label = 'store data as columns?',
                         #   ),
                        Item(name = 'comments',
                                label = 'character to denote a comment line',
                            ),
                        resizable = True,
                        buttons = ['OK', 'Cancel', 'Help'],
                        title = 'Data on CSV file format',
                    )
    
    # class parameters
    # not intended to be regularly modified
    max_length_to_store_as_cols = Int(20) # less than this many columns means columns
                                                            # are stored separately
             
    # primary function: this one uses initialized filename to configure
    # the rest of the object    
    def format_file(self, filename):
        """Called by user and passed a filename.  It then 
        guesses at formatting of CSV file and prompts 
        user to verify or change those attributes.  
        Data is then loaded accordingly.
        """
        
        # assigning file name
        self.filename = filename
        
        # making best guesses at format of the CSV file and
        # assigning it preliminarily
        self._sniff()
        
        # allow user to specify if store_as_cols
        self.configure_traits(kind = 'modal', view = 'view_store_as_cols')
        
        # allow user to modify formatting attributes
        self.configure_traits(kind = 'modal', \
                view = ('view_cols' if self.store_as_cols else 'view_noncols') )
        
        # loading the data set
        self._load_data()    
        
    def _sniff(self):
        """Makes educated guesses about the formatting of the CSV
        file and assigns these guesses to the object's attributes.
        """
        sniffed_info = TrialSniff(filename = self.filename)
        self.delimiter = sniffed_info.delimiter
        self.skiprows = sniffed_info.skiprows
        self.dtype = sniffed_info.dtype
        self.comment = sniffed_info.comment
        #self.store_as_cols = ( len(self.dtype['name']) < self.max_length_to_store_as_cols )

    def _load_data(self): 
        """Uses formatting attributes to load data from
        the file and store it appropriately.
        """
        
        # This function converts self.delimiter into the
        # appropriate input for loadtxt        
        delimiter_input = lambda delimiter: \
                                delimiter if delimiter not in ['', ' ', '  '] \
                                    else None
        
        # load file into a NumPy array
        self._array = numpy.loadtxt( fname = self.filename,
                                            dtype = self.dtype,
                                            comments = self.comment,
                                            delimiter = delimiter_input(self.delimiter),
                                            converters = None,
                                            skiprows = self.skiprows,
                                            usecols = None,
                                            unpack = False,
                                            )
        
        # make self.data according to whether the file
        # should be stored as columns or one large array
        if self.store_as_cols:
            self.data = \
                    dict(zip( self.dtype['names'] , self._array.transpose() ))
        else:
            self.data = self._array


class TrialSniff(HasTraits):
    """ ONLY HERE SO THAT CSV HANDLER CAN CALL IT
    """
    filename = Str
    delimiter = Str(' ') # if " ", must be converted to None for loadtxt to work
    dtype = Dict({'names':('col1','col2','col3','col4'), 'formats':(float, float, float, float)})
    skiprows = Int(0)
    comment = Str('#')

x = CSVObj()
x.format_file('example3.csv')