"""
 Code related to traits UI menu items for the tree view of mayavi.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import splitext, isfile

# Enthought library imports.
from traits.api import HasTraits, Any, List
from traitsui.menu import Action, Menu
from pyface.api import FileDialog, OK, GUI

# Local imports.
from mayavi.core.registry import registry
from mayavi.core.common import error, get_engine


################################################################################
# `MenuHelper` class.
################################################################################
class MenuHelper(HasTraits):

    # The object this menu generates the menus for.
    object = Any

    # The actions this helper generates.
    actions = List()

    ######################################################################
    # Public interface.
    ######################################################################
    def check_active(self, metadata):
        """Check if the `metadata` passed can be added to `self.object`.
        """
        # FIXME: This should also have logic for checking the attributes
        # and attribute_types.
        output_info = self.object.output_info
        input_info = metadata.input_info
        if output_info is None:
            return True
        elif input_info is None:
            return True
        output_datasets = output_info.datasets
        input_datasets = input_info.datasets
        if 'none' in output_datasets:
            return False
        if 'any' in input_datasets:
            return True
        for d in input_datasets:
            if d in output_datasets:
                return True
        return False

    def open_file_action(self):
        wildcard = 'All files (*.*)|*.*'
        for src in registry.sources:
            if len(src.extensions) > 0:
                if wildcard.endswith('|') or \
                   src.wildcard.startswith('|'):
                       wildcard += src.wildcard
                else:
                    wildcard += '|' + src.wildcard

        dialog = FileDialog(parent=None,
                            title='Open supported data file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path)
                return
            # FIXME: Ask for user input if a filetype is unknown and
            # choose appropriate reader.
            object = self.object
            engine = get_engine(object)
            engine.open(dialog.path, object)

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _create_source(self, metadata, select=True):
        """Create source object given its metadata.  If `select` is
        `True` make the created object the active selection.
        """
        callable = metadata.get_callable()
        obj = callable()
        parent = self.object
        engine = get_engine(parent)
        engine.add_source(obj, parent)
        if select:
            self._make_active(obj)

    def _create_object(self, metadata, select=True):
        """Create mayavi pipeline object given its metadata.  If
        `select` is `True` make the created object the active selection.
        """
        callable = metadata.get_callable()
        obj = callable()
        parent = self.object
        engine = get_engine(parent)
        engine.add_filter(obj, parent)
        if select:
            self._make_active(obj)

    def _make_active(self, obj):
        """Make the object given, `obj`, the current selection of the
        engine."""
        engine = get_engine(obj)
        if engine is not None:
            # This is required when running mayavi in envisage.
            GUI.set_trait_later(engine, 'current_selection', obj)
        else:
            print("No engine")

    def _build_source_actions(self):
        actions = []
        a = Action(name='Open File ...',
                   action='object.menu_helper.open_file_action',
                   tooltip='Open a supported data file')
        actions.append(a)

        for src in registry.sources:
            if len(src.extensions) == 0:
                # The method that creates the source.
                setattr(self, src.id,
                        lambda self=self, md=src, select=True:
                        self._create_source(md, select))
                a = Action(name=src.menu_name,
                           action='object.menu_helper.'+src.id,
                           tooltip=src.tooltip)
                actions.append(a)
        return actions

    def _build_filter_actions(self):
        actions = []
        for fil in registry.filters:
            # The method that creates the object.
            setattr(self, fil.id,
                    lambda self=self, md=fil, select=True:
                    self._create_object(md, select))
            # The method that checks if the menu can be activated or
            # not.
            setattr(self, 'check_' + fil.id,
                    lambda self=self, md=fil: self.check_active(md))
            a = Action(name=fil.menu_name,
                       action='object.menu_helper.' + fil.id,
                       enabled_when='object.menu_helper.check_%s()'%fil.id,
                       tooltip=fil.tooltip)
            actions.append(a)
        return actions

    def _build_module_actions(self):
        actions = []
        for mod in registry.modules:
            # The method that creates the module.
            setattr(self, mod.id,
                    lambda self=self, md=mod, select=True:
                    self._create_object(md, select))
            # The method that checks if the menu can be activated or
            # not.
            setattr(self, 'check_' + mod.id,
                    lambda self=self, md=mod: self.check_active(md))
            a = Action(name=mod.menu_name,
                       action='object.menu_helper.' + mod.id,
                       enabled_when='object.menu_helper.check_%s()'%mod.id,
                       tooltip=mod.tooltip)
            actions.append(a)
        return actions


################################################################################
# `SourceMenuHelper` class.
################################################################################
class SourceMenuHelper(MenuHelper):

    def _actions_default(self):
        actions = self._build_source_actions()
        return [Menu(name='Add Source', *actions)]


################################################################################
# `FilterMenuHelper` class.
################################################################################
class FilterMenuHelper(MenuHelper):

    def _actions_default(self):
        filter_actions = self._build_filter_actions()
        module_actions = self._build_module_actions()
        return [Menu(name='Add Filter', *filter_actions),
                Menu(name='Add Module', *module_actions)]

################################################################################
# `ModuleMenuHelper` class.
################################################################################
class ModuleMenuHelper(MenuHelper):

    def _actions_default(self):
        module_actions = self._build_module_actions()
        return [Menu(name='Add Module', *module_actions)]
