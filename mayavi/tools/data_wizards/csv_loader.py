# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


from traits.api import HasTraits, Str, Int, Array, List, \
    Instance, on_trait_change, Property, Button

from pyface.api import GUI

from traitsui.api import View, Item, HGroup, Group, \
    ListEditor, TabularEditor, spring, TextEditor, Controller, VSplit

from traitsui.tabular_adapter import TabularAdapter

from mayavi.tools.data_wizards.csv_sniff import Sniff, loadtxt, \
        array2dict


##############################################################################
# ListItem class
##############################################################################
class ListItem(HasTraits):
    """ Class used to represent an item in a list with traits UI.
    """
    column_number = Int
    name = Str
    my_name = Str
    parent = Instance(HasTraits)
    view = View(
               HGroup(
                   Item('name', style='readonly', show_label=False,
                                    resizable=False),
                   Item('my_name', style='simple', show_label=False,
                            editor=TextEditor(auto_set=False, enter_set=True),
                                    springy=True),
               )
           )


##############################################################################
# CSVLoader class
##############################################################################
class CSVLoader(HasTraits):
    """ User interface to load CSV files.
    """

    # The name of the file being loaded.
    filename = Str

    # The comment characters
    comments = Str(desc="The comment characters")

    # The character giving the delimiter between the columns.
    delimiter = Str(
        desc="The character giving the delimiter between the columns")

    # The number of rows to skip at the beginning of the file
    skiprows = Int(
        desc="The number of rows to skip at the beginning of the file")

    columns = List(ListItem)

    data = Array

    data_dict = Property(depends_on='data')

    def _get_data_dict(self):
        return array2dict(self.data)

    def guess_defaults(self):
        try:
            kwds = Sniff(self.filename).kwds()
        except:
            kwds = {'comments': '#',
                    'delimiter': ',',
                    'dtype': float,
                    'skiprows': 0}

        if kwds['delimiter']:
            self.delimiter = kwds['delimiter']
        else:
            self.delimiter = ' '
        self.comments = kwds['comments']
        self.skiprows = kwds['skiprows']
        self.names = list(kwds['dtype']['names'])
        self.formats = list(kwds['dtype']['formats'])

        self.columns = [ListItem(name='Column %i:' % (i + 1),
                                 parent=self,
                                 column_number=i,
                                 my_name=val)
                        for i, val in enumerate(self.names)]
        self.load_data()

    def load_data(self):
        kwds = {}
        kwds['delimiter'] = self.delimiter
        kwds['comments'] = self.comments
        kwds['skiprows'] = self.skiprows
        kwds['dtype'] = dict(names=self.names,
                             formats=self.formats)

        try:
            self.data = loadtxt(self.filename, **kwds)
        except:
            pass


##############################################################################
# CSVLoaderController class
##############################################################################
class CSVLoaderController(Controller):
    """ A controller for the CSVLoader.
    """

    tabular_editor = Instance(HasTraits)

    def _tabular_editor_default(self):
        class ArrayAdapter(TabularAdapter):
            columns = [(n, i) for i, n in enumerate(self.model.names)]
            font = 'Courier 10'
            alignment = 'right'
            format = '%s'

        return TabularEditor(adapter=ArrayAdapter())

    update_preview = Button('Update preview')

    @on_trait_change('update_preview')
    def load_data(self):
        self.model.load_data()

    @on_trait_change('model.columns.my_name,model.data')
    def update_table_editor(self, object, name, old, new):
        if isinstance(object, ListItem):
            self.tabular_editor.adapter.columns[object.column_number] = \
                                (new, object.column_number)
            GUI.set_trait_later(self.info.ui, 'updated', True)

    file_content = Str

    @on_trait_change('model.filename')
    def update_file(self):
        f = open(self.model.filename)
        self.file_content = f.read(300)

    def default_traits_view(self):
        view = View(
                VSplit(
                   HGroup(
                       Group(
                           spring,
                           Item('delimiter',
                                label='Column delimiter character'),
                           Item('comments',
                                label='Comment character'),
                           Item('skiprows',
                                label='Number of lines to skip at the '
                                'beginning of the file'),
                           spring,
                           Item('handler.update_preview',
                                                show_label=False),
                       ),
                       Group(
                           Item('columns',
                               show_label=False,
                               style='readonly',
                               editor=ListEditor(style='custom'),
                               springy=True,
                           ),
                           label="Column names",
                           show_border=True,
                       ),
                   ),
                   Group(
                       Group(
                        Item('data',
                            show_label=False,
                            editor=self.tabular_editor,
                            ),
                        label="Preview table",
                        ),
                        Group(
                        Item('handler.file_content', style='readonly',
                                show_label=False,
                                springy=True),
                        label="%s" % self.model.filename,
                        ),
                    layout='tab'),
               ),
               buttons=['OK', 'Cancel', 'Help'],
               id='csv_load_editor',
               resizable=True,
               width=640,
               height=580,
               title='CSV import - [%s]' % self.model.filename
           )
        return view

if __name__ == '__main__':
    from pyface.api import GUI
    csv_loader = CSVLoader(filename='mydata.csv')
    csv_loader.guess_defaults()
    controller = CSVLoaderController(model=csv_loader)
    controller.edit_traits()
    GUI().start_event_loop()
