# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


from enthought.traits.api import HasTraits, Str, Int, Array, Dict, List, \
    Property, Instance

from enthought.traits.ui.api import View, Item, HGroup, VGroup, Group, \
    ListEditor, TabularEditor

from enthought.traits.ui.tabular_adapter \
    import TabularAdapter

from enthought.traits.ui.ui_editors.array_view_editor import ArrayViewEditor

from enthought.mayavi.tools.wizards.csv_sniff import Sniff, loadtxt, array2dict


class ListItem(HasTraits):
    name = Str
    my_name = Str
    view = View(
               HGroup(
                   Item('name', style='readonly'),
                   'my_name',
                   show_labels=False,
               )
           )


def tabular_editor(names):
    class ArrayAdapter(TabularAdapter):
        columns     = [(n, i) for i, n in enumerate(names)]
        font        = 'Courier 10'
        alignment   = 'right'
        format      = '%s'
        
    return TabularEditor(adapter = ArrayAdapter())

class Foo:
    pass
foo = Foo()
foo.filename = '123456789.csv'
foo.names = ('a', 'b', 'c')
        
class CSVLoader(HasTraits):
    filename  = Str
    
    comments  = Str
    delimiter = Str
    skiprows  = Int

    columns = List(ListItem)
    data = Array

    #Property(List(DataItem),
    #                depends_on=['delimiter', 'skiprows', 'comments'])

    def myview(self):
        return \
           View(
               VGroup(
                   HGroup(
                       Group(
                           Item('delimiter'),
                           Item('skiprows'),
                           Item('comments'),
                       ),
                       Group(
                           Item('columns',
                               show_label=False,
                               style='readonly',
                               editor=ListEditor(style='custom'), 
                               width=0.5,
                               height=0.5,
                           ),
                           label="Column names",
                           show_border=True,
                       ),
                   ),
                   Group(
                       Item('data',
                           show_label=False,
                           editor=tabular_editor(self.names),
                       ),
                   ),
               ),
               buttons   = ['OK', 'Cancel', 'Help'],
               id        = 'csv_load_editor',
               resizable = True,
               title = 'CSV import - [%s]' % self.filename
           )
    
    view = myview(foo)
    
    def guess_defaults(self):
        try:
            kwds = Sniff(self.filename).kwds()
        except:
            kwds = { 'comments': '#',
                     'delimiter': ',',
                     'dtype': float,
                     'skiprows': 0 }
        
        self.delimiter = kwds['delimiter'] if kwds['delimiter'] else ' '
        self.comments = kwds['comments']
        self.skiprows = kwds['skiprows']
        self.names = list(kwds['dtype']['names'])

        self.columns = [ListItem(name    = 'Column %i' % (i+1),
                                 my_name = val)
                        for i, val in enumerate(self.names)]
        
        self.view = self.myview()
        print ';;;;;;;;;;;'
#    def _get_data(self):
        kwds = { 'comments': self.comments,
                 'delimiter': self.delimiter if self.delimiter else None,
                 'dtype': { 'names': tuple(self.names),
                            'formats': ('S3', 'f', 'f') },
                 'skiprows': self.skiprows }
        print kwds
        try:
            self.data = loadtxt(self.filename, **kwds)
        except:
            pass

        print type(self.data)
        print repr(self.data)

#        self.data = [DataItem(name = k, dat = v)
#                     for k, v in tmp.iteritems()]



x = CSVLoader(filename='mydata.csv')
x.guess_defaults()
x.configure_traits()
