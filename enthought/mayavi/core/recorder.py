"""
Code to support recording to a runnable Python script.

TODO:
    - Add support for recording decorated functions.
    - Support for dictionaries?
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import logging
from os.path import isfile

from enthought.traits.api import (HasTraits, List, Str, Code, Button,
        Dict, Bool, Unicode, Property, TraitError)
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.common import camel2enthought
from common import error

# Setup a logger for this module.
logger = logging.getLogger(__name__)


################################################################################
# `_RegistryData` class.
################################################################################ 
class _RegistryData(HasTraits):
    # Object's script ID
    script_id = Str

    # Path to object in object hierarchy.
    path = Str

    # List of traits we are listening for on this object.
    names = List(Str)

    # Nested recordable instances on the object.
    sub_recordables = List(Str)

    # List of traits that are lists.
    list_names = List(Str)


################################################################################
# `RecorderError` class.
################################################################################ 
class RecorderError(Exception):
    pass


################################################################################
# `Recorder` class.
################################################################################ 
class Recorder(HasTraits):

    # The lines of code recorded.
    lines = List(Str)

    # Are we recording or not?
    recording = Bool(False)

    # The Python script we have recorded so far.  This is just a
    # convenience trait for the `get_code()` method.
    script = Property(Unicode)

    ########################################
    # Private traits.

    # Dict used to store information on objects registered.  It stores a
    # unique name for the object and its path in the object hierarchy
    # traversed.
    _registry = Dict

    # Reverse registry with keys as script_id and object as value.
    _reverse_registry = Dict

    # A mapping to generate unique names for objects.
    _name_map = Dict(Str, int)

    # What are the known names in the script?  By known names we mean
    # names which are actually bound to objects.
    _known_ids = List(Str)

    ######################################################################
    # `Recorder` interface.
    ######################################################################
    def record(self, code):
        """Record a string to be stored to the output file.

        Parameters:
        -----------

        code - A string of text.
        """
        if self.recording:
            lines = self.lines
            # Analyze the code and add extra code if needed.
            self._analyze_code(code)
            # Add the code.
            lines.append(code)

    def register(self, object, parent=None, trait_name_on_parent='',
                 ignore=None, known=False):
        """Register an object with the recorder.  This sets up the
        object for recording.  
        
        By default all traits (except those starting and ending with
        '_') are recorded.  For attributes that are themselves
        recordable, one may mark traits with a 'record' metadata as
        follows:

        - If metadata `record=False` is set, the nested object will not be
          recorded.

        - If `record=True`, then that object is also recorded if it is
          not `None`.

        If the object is a list or dict that is marked with
        `record=True`, the list is itself not listened to for changes
        but all its contents are registered.

        If the `object` has a trait named `recorder` then this recorder
        instance will be set to it if possible.

        Parameters:
        -----------

        object : Instance(HasTraits)
            The object to register in the registry.

        parent : Instance(HasTraits)
            An optional parent object in which `object` is contained

        trait_name_on_parent : str
            An optional trait name of the `object` in the `parent`.

        ignore : list(str)
            An optional list of trait names on the `object` to be
            ignored.

        known : bool
            Optional specification if the `object` id is known on the
            interpreter.  This is needed if you are manually injecting
            code to define/create an object.
        """
        registry = self._registry
        #logger.info('Registering object %r', object)
        if object in registry:
            logger.warning('Object %r already registered: ignoring', object)
            return

        # When parent is specified the trait_name_on_parent must also be.
        if parent is not None:
            assert len(trait_name_on_parent) > 0

        if ignore is None:
            ignore = []
        # Always ignore these.
        ignore.extend(['trait_added', 'trait_modified'])

        sub_recordables = object.traits(record=True).keys()
        # Find all the trait names we must ignore.
        ignore.extend(object.traits(record=False).keys())
        ignore.extend(sub_recordables)
        # The traits to listen for.
        tnames = [t for t in object.trait_names() 
                  if not t.startswith('_') and not t.endswith('_') \
                     and t not in ignore]
        # Find all list traits.
        trts = object.traits()
        list_names = []
        for t in tnames:
            tt = trts[t].trait_type
            if hasattr(tt, 'default_value_type') and \
                    tt.default_value_type == 5:
                list_names.append(t)

        # Setup the registry data.
        if parent is None:
            sid = self._get_unique_name(object)
            path = ''
        else:
            pdata = self._get_registry_data(parent)
            pid = pdata.script_id
            ppath = pdata.path 
            tnop = trait_name_on_parent
            if '[' in tnop:
                # If the object is a nested object through an iterator,
                # we instantiate it and don't refer to it through the
                # path, this makes scripting convenient.
                sid = self._get_unique_name(object)
                if len(ppath) == 0:
                    path = pid + '.' + tnop
                else:
                    path = ppath + '.' + tnop
            else:
                sid = pid + '.' + tnop
                path = ppath + '.' + tnop

        # Register the object with the data.
        data = _RegistryData(script_id=sid, path=path, names=tnames,
                             sub_recordables=sub_recordables, 
                             list_names=list_names)
        registry[object] = data
        self._reverse_registry[sid] = object
        if known:
            self._known_ids.append(sid)

        # Try and set the recorder attribute if necessary.
        if hasattr(object, 'recorder'):
            try:
                object.recorder = self
            except TraitError, e:
                msg = "Cannot set 'recorder' trait of object %r: %s"
                logger.warning(msg, object, e)

        # Add handler for lists.
        for name in list_names:
            object.on_trait_change(self._list_items_listner,
                                   '%s_items'%name)

        # Register all sub-recordables.
        for name in sub_recordables:
            obj = getattr(object, name)
            if isinstance(obj, list):
                # Don't register the object itself but register its
                # children.
                for i, child in enumerate(obj):
                    attr = '%s[%d]'%(name, i)
                    self.register(child, parent=object,
                                  trait_name_on_parent=attr)
            elif obj is not None:
                self.register(obj, parent=object, 
                              trait_name_on_parent=name)
            # Listen for changes to the trait itself so the newly
            # assigned object can also be listened to.
            object.on_trait_change(self._object_changed_handler, name)
        # Now add listner for the object itself.
        object.on_trait_change(self._listner, tnames)

    def unregister(self, object):
        """Unregister the given object from the recorder.  This inverts
        the logic of the `register(...)` method.
        """
        registry = self._registry
        #logger.info('Unregistering object %r', object)
        if object not in registry:
            logger.warning('Object %r not registered: ignoring', object)
            return

        data = registry[object]

        # Try and unset the recorder attribute if necessary.
        if hasattr(object, 'recorder'):
            try:
                object.recorder = None
            except TraitError, e:
                msg = "Cannot unset 'recorder' trait of object %r: %s"
                logger.warning(msg, object, e)

        # Remove all list_items handlers.
        for name in data.list_names:
            object.on_trait_change(self._list_items_listner,
                                   '%s_items'%name, remove=True)

        # Unregister all sub-recordables.
        for name in data.sub_recordables:
            obj = getattr(object, name)
            if isinstance(obj, list):
                # Unregister the children.
                for i, child in enumerate(obj):
                    self.unregister(child)
            elif obj is not None:
                self.unregister(obj)
            # Remove the trait handler for trait assignments.
            object.on_trait_change(self._object_changed_handler,
                                   name, remove=True)
        # Now remove listner for the object itself.
        object.on_trait_change(self._listner, data.names, remove=True)

        # Remove the object data from the registry etc.
        if data.script_id in self._known_ids:
            self._known_ids.remove(data.script_id)
        del self._reverse_registry[data.script_id]
        del registry[object]

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
            f = open(fname, 'w')
            self.save(f)
            f.close()

    def clear(self):
        """Clears all previous recorded state and unregisters all
        registered objects."""
        # First unregister any registered objects.
        registry = self._registry
        while len(registry) > 0:
            self.unregister(registry.keys()[0])
        # Clear the various lists.
        self.lines[:] = []
        self._registry.clear()
        self._known_ids[:] = []
        self._name_map.clear()
        self._reverse_registry.clear()

    def get_code(self):
        """Returns the recorded lines as a string of printable code."""
        return '\n'.join(self.lines) + '\n'

    def get_script_id(self, object):
        """Returns the script_id of a registered object.  Useful when
        you want to manually add a record statement."""
        return self._get_registry_data(object).script_id

    def get_object_path(self, object):
        """Returns the path in the object hierarchy of a registered
        object.  Useful for debugging."""
        return self._get_registry_data(object).path

    def write_script_id_in_namespace(self, script_id):
        """If a script_id is not known in the current script's namespace,
        this sets it using the path of the object or actually
        instantiating it.  If this is not possible (since the script_id
        matches no existing object), nothing is recorded but the
        framework is notified that the particular script_id is available
        in the namespace.  This is useful when you want to inject code
        in the namespace to create a particular object.
        """
        if not self.recording:
            return
        known_ids = self._known_ids
        if script_id not in known_ids:
            obj = self._reverse_registry.get(script_id)
            # Add the ID to the known_ids.
            known_ids.append(script_id)
            if obj is not None:
                data = self._registry.get(obj)
                if len(data.path) > 0:
                    # Record code for instantiation of object.
                    result = '%s = %s'%(script_id, data.path)
                else:
                    # This is not the best thing to do but better than
                    # nothing.
                    mod, cls = obj.__module__, obj.__class__.__name__
                    result = '#from %s import %s\n'%(mod, cls)
                    result += '#%s = %s()'%(script_id, cls)

                if len(result) > 0:
                    self.lines.extend(result.split('\n'))

    ######################################################################
    # Non-public interface.
    ###################################################################### 
    def _get_unique_name(self, obj):
        """Return a unique object name (a string).  Note that this does
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

    def _get_registry_data(self, object):
        """Get the data for an object from registry."""
        data = self._registry.get(object)
        if data is None:
            msg = "Recorder: Can't get script_id since object %s not registered"
            logger.error(msg, object)
            raise RecorderError(msg%(object))
        return data

    def _listner(self, object, name, old, new):
        """The listner for trait changes on an object.
        
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
        if self.recording:
            new_repr = repr(new)
            sid = self._get_registry_data(object).script_id
            if len(sid) == 0:
                msg = '%s = %r'%(name, new)
            else:
                msg = '%s.%s = %r'%(sid, name, new)
            if new_repr.startswith('<') and new_repr.endswith('>'):
                self.record('# ' + msg)
            else:
                self.record(msg)

    def _list_items_listner(self, object, name, old, event):
        """The listner for *_items on list traits of the object.
        """
        if self.recording:
            sid = self._get_registry_data(object).script_id
            index = event.index
            removed = event.removed
            nr = len(removed)
            if nr > 1:
                # A slice.
                slice = '[%d:%d]'%(index, index + nr)
            else:
                slice = '[%d]'%index
            added = event.added
            na = len(added)
            if nr > 1:
                rhs = '%r'%added
            elif nr == 1:
                rhs = '%r'%added[0]
            else:
                rhs = '[]'
                
            obj = '%s.%s'%(sid, name[:-6])
            msg = '%s%s = %s'%(obj, slice, rhs)
            self.record(msg)

    def _object_changed_handler(self, object, name, old, new):
        """Called when a child recordable object has been reassigned."""
        registry = self._registry
        if old is not None:
            if old in registry:
                self.unregister(old)
        if new is not None:
            if new not in registry:
                self.register(new, parent=object,
                              trait_name_on_parent=name)

    def _get_script(self):
        return self.get_code()

    def _analyze_code(self, code):
        """Analyze the code and return extra code if needed.
        """
        known_ids = self._known_ids
        lhs = ''
        try:
            lhs = code.split()[0]
        except IndexError:
            pass

        if '.' in lhs:
            ob_name = lhs.split('.')[0]
            self.write_script_id_in_namespace(ob_name)


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
                width=600, height=400,
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
def start_recording(object, ui=True, known=True):
    """Convenience function to start recording.  Returns the recorder.

    Parameters:

    object :  object to record.
    ui : bool specifying if a UI is to be shown or not
    known : bool specifying if the object is known in the script
    namespace.
    """
    if ui:
        r = RecorderWithUI()
        r.edit_traits(kind='live')
    else:
        r = Recorder()
    r.recording = True
    r.register(object, known=known)
    return r

def stop_recording(object, recorder=None):
    """Stop recording the object given the recorder.  This will pop up a
    UI to ask where to save the script.  If recorder is not passed it
    will try to get it assuming that the object has a recorder trait.
    """
    if recorder is None:
        if hasattr(object, 'recorder'):
            recorder = object.recorder
        else:
            raise RecorderError('Unable to find recorder to stop!')
    recorder.recording = False
    recorder.unregister(object)
    recorder.ui_save()

