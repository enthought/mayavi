# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Ilan Schnell, Enthought, Inc.
# License: BSD Style.


from enthought.traits.api import HasTraits, Str, Int, Array, Dict, List
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.ui_editors.array_view_editor import ArrayViewEditor

from enthought.mayavi.tools.wizards.csv_sniff import Sniff, loadtxt, array2dict


class CSVLoader(HasTraits):
    filename  = Str
    
    delimiter = Str
    skiprows  = Int
    comments  = Str
    
    def view_csv(self):
        return View(
            Item('delimiter'),
            Item('skiprows'),
            Item('comments'),
            Item('data',
                 show_label = False,
                 editor = ArrayViewEditor( titles = ['x', 'y', 'z'] )
                 ),
            buttons   = ['OK', 'Cancel', 'Help'],
            id        = 'csv_load_editor',
            resizable = True,
            title = 'CSV import - [%s]' % self.filename
            )
    
    def guess_defaults(self):
        try:
            kwds = Sniff(self.filename).kwds()
        except:
            kwds = { 'comments': '#',
                     'delimiter': ',',
                     'dtype': float,
                     'skiprows': 0 }
        
        #print kwds['dtype']['names']
        
        self.delimiter = kwds['delimiter'] if kwds['delimiter'] else ' '
        self.comments = kwds['comments']
        self.skiprows = kwds['skiprows']
        
        try:
            self.data = loadtxt(self.filename, **kwds)
        except:
            pass
        
        print self.data
        print self.data.dtype


x = CSVLoader(filename='mydata.csv')
x.guess_defaults()
x.configure_traits(view = x.view_csv())
