"""

Utility code that provides classes helpful in choosing a suitable TVTK
class.  It does this by providing a list of all the classes along with
the option to be able to search for the documentation.

The nice thing about the UI is that it performs some kind of completion
on names typed by the user, plus it allows users to search through the
TVTK class docs very easily.  Once a search string is typed the
completion and available lists are modified so you can do completion of
the searched class names.  If a unique enough string is typed the class
docs are shown.

"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import inspect
import os
import sys

# Enthought library imports.
from traits.api import HasTraits, Property, List, Str, \
                                 Instance, Button, Int
from traitsui.api import View, Group, Item, EnumEditor,\
                                    ListEditor, TextEditor
from tvtk.api import tvtk
from tvtk.common import get_tvtk_name
import tvtk.vtk_module as vtk

# GLOBALS
TVTK_CLASSES, TVTK_SOURCES, TVTK_FILTERS, TVTK_SINKS = None, None, None, None


# ##############################################################################
# Utility functions.
# ##############################################################################
def get_tvtk_class_names():
    """Returns 4 lists:

     1. A list of all the TVTK class names that are not abstract.

     2. A list of the TVTK sources (have only outputs and no inputs)

     3. A list of the TVTK filters (both inputs and outputs)

     4. A list of the TVTK sinks (only inputs and no outputs)

    """
    # Shut of VTK warnings for the time being.
    o = vtk.vtkObject
    w = o.GetGlobalWarningDisplay()
    o.SetGlobalWarningDisplay(0)  # Turn it off.

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    verbose = os.getenv('TVTK_VERBOSE', '').lower() in ('1', 'true')

    all = []
    src = []
    filter = []
    sink = []
    bad_names = []
    ver = vtk.vtkVersion()
    if (ver.GetVTKMajorVersion(), ver.GetVTKMinorVersion()) >= (9, 2):
        bad_names.append('vtkOpenGLAvatar')

    for name in dir(vtk):
        if name.startswith('vtk') and not name.startswith('vtkQt') and \
                name not in bad_names:
            klass = getattr(vtk, name)
            if verbose:
                print(f'Trying {name}', file=sys.__stdout__)
            try:
                c = klass()
                # Some classes hijack sys.stdout/sys.stderr.
                # Restore it when that happens.
                if sys.stdout != old_stdout or sys.stderr != old_stderr:
                    sys.stdout = old_stdout
                    sys.stderr = old_stderr
            except (TypeError, NotImplementedError):
                continue

            tvtk_name = get_tvtk_name(name)
            all.append(tvtk_name)
            has_input = has_output = False
            if hasattr(klass, 'GetNumberOfInputPorts'):
                if c.GetNumberOfInputPorts() > 0:
                    has_input = True
            if hasattr(klass, 'GetNumberOfOutputPorts'):
                if c.GetNumberOfOutputPorts() > 0:
                    has_output = True

            if has_input:
                if has_output:
                    filter.append(tvtk_name)
                else:
                    sink.append(tvtk_name)
            elif has_output:
                src.append(tvtk_name)

    o.SetGlobalWarningDisplay(w)

    result = (all, src, filter, sink)
    for x in result:
        x.sort()

    return result


def get_func_doc(func, fname):
    """Returns function documentation."""
    if inspect.isfunction(func):
        func_obj = func
    elif inspect.ismethod(func):
        func_obj = func.__func__
    else:
        return ''
    args, vargs, vkw = inspect.getargs(func_obj.__code__)
    defaults = func_obj.__defaults__
    doc = fname + inspect.formatargspec(args, vargs, vkw, defaults)
    d = inspect.getdoc(func)
    if d is not None:
        doc += '\n\n' + d + '\n\n'
    return doc


def get_tvtk_class_doc(obj):
    """Return's the objects documentation."""
    doc = obj.__doc__ + '\nTraits:\n-------------------\n\n'

    ignore = ['trait_added', 'trait_modified']
    for key, trait in obj.traits().items():
        if key.startswith('_') or key.endswith('_') or key in ignore:
            continue
        doc += '\n%s: %s'%(key, trait.tooltip or trait.desc or trait.help)

    doc += '\nMethods:\n----------------------\n\n'
    traits = obj.trait_names()
    for name in dir(obj):
        if name in traits or name.startswith('_'):
            continue
        if name.find('trait') > -1 and name != 'update_traits':
            continue
        func = getattr(obj, name)
        if callable(func):
            doc += '\n' + get_func_doc(func, name)

    return doc


def _setup_tvtk_names():
    global TVTK_CLASSES, TVTK_SOURCES, TVTK_FILTERS, TVTK_SINKS
    if TVTK_CLASSES is None:
        r = get_tvtk_class_names()
        TVTK_CLASSES, TVTK_SOURCES, TVTK_FILTERS, TVTK_SINKS = r


def get_tvtk_classes():
    _setup_tvtk_names()
    return TVTK_CLASSES


def get_tvtk_sources():
    _setup_tvtk_names()
    return TVTK_SOURCES


def get_tvtk_filters():
    _setup_tvtk_names()
    return TVTK_FILTERS


def get_tvtk_sinks():
    _setup_tvtk_names()
    return TVTK_SINKS


# ##############################################################################
# `DocSearch` class.
# ##############################################################################
class DocSearch(object):

    """A simple class that provides a method to search through class
    documentation.  This code is taken from mayavi-1.x's ivtk.VtkHelp

    """

    # These are class attributes to prevent regenerating them everytime
    # this class is instantiated.
    VTK_CLASSES = []
    VTK_CLASS_DOC = []

    def __init__(self):
        self.vtk_classes = self.VTK_CLASSES
        self.vtk_c_doc = self.VTK_CLASS_DOC

        if len(self.VTK_CLASSES) == 0:
            self._setup_data()

    def _setup_data(self):
        self.vtk_classes = [x for x in dir(vtk) if x.startswith('vtk')]
        n = len(self.vtk_classes)
        # Store the class docs in the list given below.
        self.vtk_c_doc = ['']*n

        # setup the data.
        for i in range(n):
            c = self.vtk_classes[i]
            try:
                doc = getattr(vtk, c).__doc__.lower()
                self.vtk_c_doc[i] = doc
            except AttributeError:
                pass

    def search(self, word):
        """ Search for word in class documentation and return matching
        classes.  This is also case insensitive.  The searching
        supports the 'and' and 'or' keywords that allow for fairly
        complex searches.  A space between words assumes that the two
        words appear one after the other.

        Parameters
        ----------
            word -- name to search for.
        """
        assert type(word) is str, \
               "Sorry, passed argument, %s is not a string."%word
        if len(word.strip()) == 0:
            return []

        lword = word.lower().strip()
        tmp_list = lword.split()
        wlist = []
        prev = ""
        for w in tmp_list:
            z = w.strip()
            if z in ('and', 'or'):
                if prev and prev not in ('and', 'or'):
                    wlist.append(prev)
                    wlist.append(z)
                    prev = z
            else:
                if prev and prev not in ('and', 'or'):
                    prev = prev + ' ' + z
                else:
                    prev = z

        if prev in ('and', 'or'):
            del wlist[-1]
        elif prev:
            wlist.append(prev)

        ret = []
        i = 0
        vtk_classes = self.vtk_classes
        vtk_c_doc = self.vtk_c_doc
        N = len(vtk_classes)
        while i < N:
            stored_test = 0
            do_test = ''
            for w in wlist:
                if w == 'and':
                    do_test = 'and'
                elif w == 'or':
                    do_test = 'or'
                else:
                    test = (vtk_c_doc[i].find(w) > -1)
                    if do_test == 'and':
                        stored_test = stored_test and test
                    elif do_test == 'or':
                        stored_test = stored_test or test
                    elif do_test == '':
                        stored_test = test
            if stored_test:
                ret.append(vtk_classes[i])
            i = i + 1

        return [get_tvtk_name(x) for x in ret]

_search_help_doc =  """
                        Help on Searching
           ---------------------------------------

To search for a particular TVTK class, type in the 'class_name' text entry
widget.  The class names are all case sensitive.   You may also select
the class from the list of available class names at the top.

As you type you will see completion options in the completions
list, the instant a complete match is found the class documentation will
be show in the bottom.

You can also search the TVTK class documentation for strings (case
insensitive).  The search option supports the 'and' and 'or' keywords to
do advanced searches.  Press <Enter>/<Return> to perform the search.

The top 25 hits will show up in the completions, to view a particular
hit either select the choice from the available ones or type in the
name in the 'class_name' entry box.  To clear the search string click
the 'Clear search' button or erase the search string manually.

"""


################################################################################
# `TVTKClassChooser` class.
################################################################################
class TVTKClassChooser(HasTraits):

    # The selected object, is None if no valid class_name was made.
    object = Property

    # The TVTK class name to choose.
    class_name = Str('', desc='class name of TVTK class (case sensitive)')

    # The string to search for in the class docs -- the search supports
    # 'and' and 'or' keywords.
    search = Str('', desc='string to search in TVTK class documentation '\
                          'supports the "and" and "or" keywords. '\
                          'press <Enter> to start search. '\
                          'This is case insensitive.')

    clear_search = Button

    # The class documentation.
    doc = Str(_search_help_doc)

    # Completions for the choice of class.
    completions = List(Str)

    # List of available class names as strings.
    available = List

    ########################################
    # Private traits.

    finder = Instance(DocSearch)

    n_completion = Int(25)

    ########################################
    # View related traits.

    view = View(Group(Item(name='class_name',
                           editor=EnumEditor(name='available')),
                      Item(name='class_name',
                           has_focus=True
                           ),
                      Item(name='search',
                           editor=TextEditor(enter_set=True,
                                             auto_set=False)
                           ),
                      Item(name='clear_search',
                           show_label=False),
                      Item('_'),
                      Item(name='completions',
                           editor=ListEditor(columns=3),
                           style='readonly'
                           ),
                      Item(name='doc',
                           resizable=True,
                           label='Documentation',
                           style='custom')
                      ),
                id='tvtk_doc',
                resizable=True,
                width=800,
                height=600,
                title='TVTK class chooser',
                buttons=["OK", "Cancel"]
                )
    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(TVTKClassChooser, self).__init__(**traits)
        self._orig_available = list(self.available)

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _get_object(self):
        o = None
        if len(self.class_name) > 0:
            try:
                o = getattr(tvtk, self.class_name)()
            except (AttributeError, TypeError):
                pass
        return o

    def _class_name_changed(self, value):
        av = self.available
        comp = [x for x in av if x.startswith(value)]
        self.completions = comp[:self.n_completion]
        if len(comp) == 1 and value != comp[0]:
            self.class_name = comp[0]

        o = self.object
        if o is not None:
            self.doc = get_tvtk_class_doc(o)
        else:
            self.doc = _search_help_doc

    def _finder_default(self):
        return DocSearch()

    def _clear_search_fired(self):
        self.search = ''

    def _search_changed(self, value):
        if len(value) < 3:
            self.available = self._orig_available
            return

        f = self.finder
        result = f.search(str(value))
        if len(result) == 0:
            self.available = self._orig_available
        elif len(result) == 1:
            self.class_name = result[0]
        else:
            self.available = result
            self.completions = result[:self.n_completion]

    def _available_default(self):
        return get_tvtk_classes()


################################################################################
# `TVTKSourceChooser` class.
################################################################################
class TVTKSourceChooser(TVTKClassChooser):
    available = List

    def _available_default(self):
        return get_tvtk_sources()


# ##############################################################################
# `TVTKFilterChooser` class.
# ##############################################################################
class TVTKFilterChooser(TVTKClassChooser):
    available = List

    def _available_default(self):
        return get_tvtk_filters()


# ##############################################################################
# `TVTKSinkChooser` class.
# ##############################################################################
class TVTKSinkChooser(TVTKClassChooser):
    available = List

    def _available_default(self):
        return get_tvtk_sinks()


def main():
    """Pops up a class chooser which doubles as a nice help search
    documentation tool.
    """
    s = TVTKClassChooser()
    s.configure_traits()


if __name__ == '__main__':
    main()
