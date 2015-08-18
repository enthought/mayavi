"""
Factory used by mayavi to import csv-like files into datasets.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Callable

from mayavi.tools.data_wizards.data_source_wizard import \
        DataSourceWizardView
from mayavi.tools.data_wizards.csv_loader import \
        CSVLoader, CSVLoaderController


class CallbackCSVLoader(CSVLoaderController):
    """ Simple handler for a TraitsUI view to call a given callback on
        exit.
    """

    # A callable called when the TraitsUI view is closed. The instance
    # that the view was editing is passed to this callable.
    callback = Callable()

    def closed(self, info, is_ok):
        print("CallbackHander")
        if is_ok:
            self.callback(self.model)


class CSVSourceFactory(HasTraits):
    """ Functor to load a CSV-like data from a file.
    """

    def csv_loaded_callback(self, object):
        """
        """
        self.data_source_wizard = DataSourceWizardView(
                data_sources=self.csv_loader.data_dict)
        self.data_source_wizard.edit_traits()

    def __call__(self, fname):
        """ Pops up the dialogs required for the import of the
            CSV to happen.
        """
        self.csv_loader = CSVLoader(filename=fname)
        self.csv_loader.guess_defaults()
        controller = CallbackCSVLoader(model=self.csv_loader,
                        callback=self.csv_loaded_callback)
        controller.edit_traits()

if __name__ == '__main__':
    from pyface.api import GUI
    source_factory = CSVSourceFactory()
    source_factory('mydata.csv')
    GUI().start_event_loop()
