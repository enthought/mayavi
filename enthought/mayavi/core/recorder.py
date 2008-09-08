"""
Code to support recording to a runnable Python script.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from os.path import isfile

from enthought.traits.api import (HasTraits, List, Str, Code, Button,
        Instance, Interface, Dict, Int)
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.common import camel2enthought
from common import error

################################################################################
# `IRecordable` interface.
################################################################################ 
class IRecordable(Interface):
    """This class represents the interface to be satisfied by recordable
    objects.
    """

    # The recorder to be used.
    recorder = Instance('Recorder', transient=True)

    # The ID of this object in the script.
    _script_id = Str(transient=True)

    # List of any listners added for script recording.
    _listners = List(transient=True)

    def record(self, obj, name, old, new):
        """This is called by child listners or when any of our traits
        change when recording to a script is enabled.

        For a convenient function you can readily use, see this module's
        do_record function.

        Parameters:
        -----------

        obj : Object which has changed.
        name : extended name of attribute that changed.
        old : Old value.
        new : New value.

        """
        # A default implementation for documentation purposes.
        do_record(self, obj, name, old, new)


################################################################################
# `Recorder` class.
################################################################################ 
class Recorder(HasTraits):

    # The lines of code recorded.
    lines = List(Str)

    # Dict used to produce unique script ids.
    _name_map = Dict(Str, Int)

    def record(self, code):
        """Record a string to be stored to the output file.

        Parameters:
        -----------

        code - A string of text.
        """
        lines = self.lines
        # Ignore repeated code.
        if code not in lines[-1:]:
            lines.append(code)

    def clear(self):
        """Clears all previous recorded state."""
        self.lines[:] = []
        self._name_map.clear()

    def get_unique_id(self, obj):
        """Return a unique object id (a string).  Note that this does
        not cache the object, so if called with the same object 3 times
        you'll get three different names.
        """
        cname = camel2enthought(obj.__class__.__name__)
        nm = self._name_map
        if cname in nm:
            id = nm[cname] + 1
            nm[cname] = id
            return '%s%d'%(cname, id)
        else:
            # The first id doesn't really need a number.
            nm[cname] = 0 
            return cname

    def get_code(self):
        """Returns the recorded lines as a string of printable code."""
        return '\n'.join(self.lines) + '\n'

    def save(self, file):
        """Save the recorded lines to the given file.  It does not close
        the file.
        """
        file.write(self.get_code())
        file.flush()

    def ui_save(self):
        """Save recording to file, pop up a UI dialog to find out where
        and close the file when done.
        """
        from enthought.pyface.api import FileDialog, OK
        wildcard = 'Python files (*.py)|*.py|' + FileDialog.WILDCARD_ALL
        dialog = FileDialog(title='Save Script',
                            action='save as', wildcard=wildcard
                            )
        if dialog.open() == OK:
            fname = dialog.path
            if not isfile(fname):
                error("File '%s' does not exist"%fname)
                return
            f = open(fname, 'w')
            self.save(f)
            f.close()


################################################################################
# `Listner` class.
################################################################################ 
class Listner(object):

    """A simple class that listens for changes to a object and calls the
    parent's record method.
    """

    def __init__(self, parent, trait_name, no_hidden=True):

        """Given the parent object, and the trait name of the object,
        this sets up listners on the object.

        Parameters:
        -----------

        parent : Instance(HasTraits)

            The parent object to which the `trait_name` belongs.

        trait_name : str
            The trait name of the object which we must listen to.
    
        no_hidden : bool
            Don't record any trait changes on attributes that start or
            end with an underscore. 

        """
        self.parent = parent
        self.trait_name = trait_name
        self.no_hidden = no_hidden
        object = getattr(parent, trait_name)
        self.object = object
        ignore = ['trait_added', 'trait_modified']
        # ignore any traits marked with record=False metadata.
        ignore.extend(object.traits(record=False).keys())
        tnames = [t for t in object.trait_names() if t not in ignore]
        if no_hidden:
            tnames = [t for t in tnames
                      if not t.startswith('_') and not t.endswith('_')]
        self.tnames = tnames
        object.on_trait_change(self.listner, tnames)

    def stop(self):
        """Stop listening to trait changes."""
        self.object.on_trait_change(self.listner, self.tnames, remove=True)

    def listner(self, object, name, old, new):
        """The callback called when a trait on the object changes."""
        p = self.parent
        tname = self.trait_name
        self.parent.record(object, '%s.%s'%(tname, name), old, new)


################################################################################
# `RecorderWithUI` class.
################################################################################ 
class RecorderWithUI(Recorder):
    """
    This class represents a Recorder but with a simple user interface.
    """

    code = Code
    save_script = Button('Save Script')

    view = View(Group(Item('code'), Item('save_script'),
                      show_labels=False),
                width=600,
                buttons=['OK'], resizable=True)

    def _lines_items_changed(self):
        self.code = self.get_code()

    def _lines_changed(self):
        self.code = self.get_code()

    def _save_script_fired(self):
        self.ui_save()


################################################################################
# Utility functions. 
################################################################################ 
def do_record(recordable, obj, name, old, new):
    """A convenient record function that may be called by the record
    method of classes that implement the `IRecordable` interface.

    This is called by child listners or when any of the recordable
    object's traits change when recording to a script is enabled.

    Parameters:
    -----------

    recordable : The object which implements IRecordable.

    obj : Object which has changed.

    name : extended name of attribute that changed.

    old : Old value.

    new : New value.

    """
    r = recordable.recorder
    if r is not None:
        new_repr = repr(new)
        sid = recordable._script_id
        if len(sid) == 0:
            msg = '%s = %r'%(name, new)
        else:
            msg = '%s.%s = %r'%(sid, name, new)
        if new_repr.startswith('<') and new_repr.endswith('>'):
            r.record('# ' + msg)
        else:
            r.record(msg)

def setup_recording(recordable, recorder, ignore=None):
    """Setup the recordable (that implements IRecorable) so it can record
    changes.  
    
    If the recorder passed is None, it cleans up the listners. By
    default this ignores any traits starting with an underscore.  This
    function works best when developers mark traits with specific
    metadata:

        - If metadata record=False is set, the trait will not be
          recorded.
        - If record=True, then the trait is treated as that which
          satisfies the IRecordable interface.
        - If listen=True, then a Listner will be added for that object.

    Parameters:
    -----------

    recordable : implements(IRecordable)
            The object to setup recording for.

    recorder : Either(None, Instance(Recorder))
        The recorder instance.  When set to None it cleans up.

    ignore : list(str)
        A list of trait names to ignore.
    """

    listners = recordable._listners
    if ignore is None:
        ignore = []
    # Always ignore these.
    ignore.extend(['trait_added', 'trait_modified'])

    sub_recordables = recordable.traits(record=True).keys()
    listenables = recordable.traits(listen=True).keys()
    # Find all the trait names we must ignore.
    ignore.extend(recordable.traits(record=False).keys())
    ignore.extend(sub_recordables)
    ignore.extend(listenables)
    # The traits to listen for.
    tnames = [t for t in recordable.trait_names() 
              if not t.startswith('_') and t not in ignore]

    if recorder is None:
        recordable.on_trait_change(recordable.record, tnames, remove=True)
        recordable._script_id = ''
        # Remove sub-object listners.
        for listner in listners:
            listner.stop()
        listners[:] = []
        # Wire up all sub-objects that specify a record=True.
        for name in sub_recordables:
            obj = getattr(recordable, name)
            obj.set(recorder = recorder, _script_id='')
    else:
        # First set our _script_id if needed.
        sid = recordable._script_id
        if len(sid) == 0 or '.' not in sid:
            recordable._script_id = recorder.get_unique_id(recordable)
        # Wire up sub-objects that specify a listen=True metadata.
        for name in listenables:
            listners.append(Listner(recordable, name))

        # Wire up all sub-objects that specify a record=True.
        for name in sub_recordables:
            obj = getattr(recordable, name)
            obj._script_id = '%s.%s'%(recordable._script_id, name)
            obj.recorder = recorder
        recordable.on_trait_change(recordable.record, tnames)

def start_recording(object, ui=True):
    """Convenience function to start recording.  Returns the recorder.

    Parameters:

    object :  object to record.
    ui : bool specifying if a UI is to be shown or not
    """
    if ui:
        r = RecorderWithUI()
        r.edit_traits(kind='live')
    else:
        r = Recorder()
    object.recorder = r
    return r

def stop_recording(object):
    """Stop recording the object.  This will pop up a UI to ask where to
    save the script.
    """
    r = object.recorder
    object.recorder = None
    r.ui_save()


