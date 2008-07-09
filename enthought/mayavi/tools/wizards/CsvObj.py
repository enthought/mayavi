#!/usr/bin/env python
import csv
import numpy
from csv_sniff import Sniff

# fixme: should be loadtxt from scipy
#from enthought.mayavi.tools.wizards.loadtxt import loadtxt
from loadtxt import loadtxt as loadtxt

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
    _dtype = Any # Tuple(_ColumnSpec) or Enum('Float',  'Str')
    dtype = Any # dict if store_as_cols, else just one of string, float
    data_type_if_large = Type
    delimiter = Str
    skiprows = Int
    store_as_cols = Bool(True)
    comments = Str
        
    # storing the data
    _ndarray = Array
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
    view_ascols  =  View(Item(name = '_dtype',
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
                    
    view_notascols = View(Item(name = 'data_type_if_large',
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
                view = ('view_ascols' if self.store_as_cols else 'view_notascols') )
        
        # loading the data set
        self._load_data()    
        
    def _sniff(self):
        """Makes educated guesses about the formatting of the CSV
        file and assigns these guesses to the object's attributes.
        """
        
        #sniffed_info = TrialSniff(filename = self.filename)
        
        #self.delimiter = sniffed_info.delimiter
        #self.skiprows = sniffed_info.skiprows
        #self.dtype = sniffed_info.dtype # Currently a dictionary.
                                                  # to be changed later if store_as_cols == False
        #self.comment = sniffed_info.comment
        try:
            # make educated guesses about formatting parameters and store
            # them in kwds
            kwds = Sniff(self.filename)
        except:
            # default formatting parameters
            kwds = {'delimiter':None , 'skiprows':0 , 'dtype':float , 'comments':'#'}
        
        # assign preliminary values for formatting parameters
        self.delimiter = kwds['delimiter']
        self.skiprows = kwds['skiprows']
        self.dtype = kwds['dtype']
        self.comments = kwds['coments']
        self.store_as_cols = \
            ( len(self.dtype['names']) < self.max_length_to_store_as_cols )

    def _load_data(self): 
        """Uses formatting attributes to load data from
        the file and store it appropriately.
        """
        
        # if store as one large array of a single type, change
        # self.dtype from dict to float or string
        if ~self.store_as_cols:
            self.dtype = self.dtype['formats'][0]
        
        # load file into a NumPy array
        self._array = loadtxt( fname = self.filename,
                                            dtype = self.dtype,
                                            comments = self.comment,
                                            delimiter = (self.delimiter if self.delimiter else None),
                                                # None if file is separated by whitespace
                                            converters = None,
                                            skiprows = self.skiprows,
                                            usecols = None,
                                            unpack = False
                                            )
        
        # make self.data according to whether the file
        # should be stored as columns or one large array
        if self.store_as_cols:
            self.data = array2dict(self._array)            
            
def array2dict(arr):
    """ Takes an array with  special names dtypes and returns a dict where
        each name is a key and the corresponding data (as a 1d array) is the
        value.
    """
    d = {}
    for k in arr.dtype.names:
        d[k] = arr[k]
        
    return d

class TrialSniff(HasTraits):
    """ ONLY HERE SO THAT CSV HANDLER CAN CALL IT
    """
    filename = Str
    delimiter = Str(' ') # if " ", must be converted to None for loadtxt to work
    dtype = Dict({'names':('a','b','c','d'), 'formats':(float, float, float, float)})
    skiprows = Int(0)
    comment = Str('#')

x = CSVObj()
x.format_file('example3.csv')