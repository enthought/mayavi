"""This module generates the tvtk (Traited VTK) wrapper classes for
VTK classes.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

import re
import sys
import vtk
import textwrap
import keyword
import copy
from itertools import chain

# Local imports (these are relative imports because the package is not
# installed when these modules are imported).
from .common import (get_tvtk_name, camel2enthought, is_version_58,
                     vtk_major_version)

from . import vtk_parser
from . import indenter
from . import special_gen

try:
    import faulthandler
except ImportError:
    pass
else:
    faulthandler.enable()


def get_trait_def(value, **kwargs):
    """ Return the appropriate trait type, reformatted string and
    the associated traits meta data for a given `value`

    If a sequence is given, traits.Array is returned instead of
    traits.Tuple or traits.List

    Parameters
    ----------
    value
       can be anything

    kwargs : dict
       keyword arguments for the trait definition

    Returns
    -------
    tuple : (str, str, str)
       (trait_type, value, keyword_arguments)

    Raises
    ------
    TypeError
        if this function cannot find an appropriate Trait type for `value`

    Example
    -------
    >>> get_trait_def([100., 200.], enter_set=True, auto_set=False)
    ('traits.Array', '', 'auto_set=False, enter_set=True, shape=(2,), dtype=float, value=[100.0, 200.0], cols=2')
    >>> get_trait_def(100, enter_set=True, auto_set=False)
    ('traits.Int', '100', 'auto_set=False, enter_set=True')
    >>> get_trait_def(u'something', enter_set=True, auto_set=False)
    ('traits.Unicode', "u'something'", 'auto_set=False, enter_set=True')
    >>> get_trait_def(True, enter_set=True, auto_set=False)
    ('traits.Bool', 'True', 'auto_set=False, enter_set=True')
    """

    kwargs_code = ', '.join('{0}={1}'.format(key, value)
                            for key, value in kwargs.items())

    type_ = type(value)

    number_map = {int: 'traits.Int',
                  float: 'traits.Float'}

    if type_ in number_map:
        return number_map[type_], str(value), kwargs_code

    elif type_ is str:
        if value == '\x00':
            value = ''
        return 'traits.String', '{!r}'.format(value), kwargs_code

    elif type_ in (tuple, list):
        shape = (len(value),)
        dtypes = set(type(element) for element in value)
        dtype = dtypes.pop().__name__ if len(dtypes) == 1 else None
        if dtype == 'int' and sys.platform.startswith('win'):
            dtype = 'int64'
        elif dtype == 'long':
            dtype = 'int64'
        dtype = '"{}"'.format(dtype) if dtype is not None else 'None'

        cols = len(value)

        if kwargs_code:
            kwargs_code += ', '

        kwargs_code += ('shape={shape}, dtype={dtype}, '
                        'value={value!r}, cols={cols}').format(
                            shape=shape, dtype=dtype,
                            value=value, cols=min(3, cols))

        return 'traits.Array', '', kwargs_code

    elif type_ is bool:
        return 'traits.Bool', str(value), kwargs_code

    else:
        raise TypeError("Could not understand type: {}".format(type_))


def patch_default(vtk_get_meth, vtk_set_meth, default):
    """Patch the initial default value for an attribute of
    a VTK class that does not initialise it properly.

    Parameters
    ----------
    vtk_get_meth : Method for getting the position attribute

    vtk_set_meth : Method for setting the position attribute

    default : initial default value

    Returns
    -------
    default
       If patching fails, the initial default is returned

    Examples
    --------
    >>> import vtk
    >>> vtk.vtkVersion.GetVTKVersion()
    '6.3.0'
    >>> obj = vtk.vtkXOpenGLRenderWindow()
    >>> obj.GetPosition()
    '_000000000351c458_p_void'

    >>> patch_default(vtk.vtkXOpenGLRenderWindow.GetPosition,
                      vtk.vtkXOpenGLRenderWindow.SetPosition,
                      '_000000000351c458_p_void')
    (0, 0)
    """
    # We will attempt to guess the default by looking into the
    # arguments of the Set method
    # SetPosition(int, int) has a signature of ("int", "int")
    # SetPosition(int position[2]) has a signature of (["int", "int"],)
    # Some method even has a signature of (["int", "int"], "vtkInformation")
    arg_formats = []

    # Collect the signatures of the get method
    # We only use the arguments
    all_sigs = vtk_parser.VTKMethodParser.get_method_signature(vtk_get_meth)

    # Collect the signatures of the set method
    all_sigs.extend(
        vtk_parser.VTKMethodParser.get_method_signature(vtk_set_meth))

    for sig in all_sigs:
        if sig[1] is None:
            continue

        if len(sig[1]) == 1:
            # This unpacks tuple of something e.g. (('int', 'int', 'int'))
            arg_formats.append(tuple(chain.from_iterable(sig[1])))

        arg_formats.append(tuple(sig[1]))

    default_mappings = {
        'int' : 0,
        'float': 0.0,
        'string': ''
        }

    for arg_format in arg_formats:
        try:
            all_same_type = len(set(arg_format)) == 1
        except TypeError:  # Unhashable
            continue

        if all_same_type and arg_format[0] in default_mappings:
            # All types in `arg_format` are the same and they are
            # in the mapping (e.g. arg_format = ('int', 'int')
            default = default_mappings[arg_format[0]]

            if len(arg_format) > 1:
                return (default,)*len(arg_format)
            else:
                return default
    else:
        return default


######################################################################
# `WrapperGenerator` class.
######################################################################

class WrapperGenerator:
    """Generates the wrapper code for all the TVTK classes.

    """
    def __init__(self):
        self.indent = indenter.Indent()
        self.parser = vtk_parser.VTKMethodParser()
        self.special = special_gen.SpecialGenerator(self.indent)
        self.dm = indenter.VTKDocMassager()

    #################################################################
    # `WrapperGenerator` interface.
    #################################################################

    def get_tree(self):
        """Returns the parser's class tree."""
        return self.parser.get_tree()

    def generate_code(self, node, out):
        """Generates the code for the given node in the parse tree
        along with an opened file-like object.

        Parameters
        ----------

        - node

          A node in the ClassTree.

        - out :  file-like object.

          Must support a `write` method.  Code is written to it.

        """
        self.indent.reset()

        self._write_prelims(node, out)

        # Write the class decl and __init__
        self._gen_class_init(node, out)

        # Write the other methods.
        self._gen_methods(node, out)

        # Write any special code if available.
        self.special.generate_code(node, out)

        out.write('\n')

    #################################################################
    # Non-public interface.
    #################################################################

    def _write_prelims(self, node, out):
        """Write preliminary information given the node in the class
        tree, `node`, and output file-like object, `out`.

        """
        prelim = """
        # Automatically generated code: EDIT AT YOUR OWN RISK
        from traits import api as traits
        from traitsui.item import Item, spring
        from traitsui.group import HGroup
        from traitsui.view import View

        from tvtk import vtk_module as vtk
        from tvtk import tvtk_base
        from tvtk.tvtk_base_handler import TVTKBaseHandler
        from tvtk import messenger
        from tvtk.tvtk_base import deref_vtk
        from tvtk import array_handler
        from tvtk.array_handler import deref_array
        from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

        nan = float('nan')


        def InstanceEditor(*args, **kw):
            from traitsui.editors.api import InstanceEditor as Editor
            return Editor(view_name="handler.view")

        try:
            long
        except NameError:
            # Silly workaround for Python3.
            long = int

        inf = float('inf')

        """
        out.write(self.indent.format(prelim))

    def _gen_class_init(self, node, out):
        indent = self.indent
        klass = self.get_tree().get_class(node.name)
        vtk_class_name = klass.__name__
        class_name = self._get_class_name(klass)

        if node.level == 0 or node.name == 'vtkObjectBase':
            base_name = 'tvtk_base.TVTKBase'
        else:
            base_name = self._get_class_name(klass.__bases__)[0]
            if base_name != 'object':
                # Import the base class.
                base_fname = camel2enthought(base_name)
                _imp = "from tvtk.tvtk_classes.%(base_fname)s import %(base_name)s"%locals()
                out.write(indent.format(_imp))
                out.write('\n\n')

        # Write the class declaration.
        cdef = """
        class %(class_name)s(%(base_name)s):
        """%locals()
        out.write(indent.format(cdef))

        self.dm.write_class_doc(klass.__doc__, out, indent)
        indent.incr()

        # Write __init__
        decl = """
        def __init__(self, obj=None, update=True, **traits):
            tvtk_base.TVTKBase.__init__(self, vtk.%(vtk_class_name)s, obj, update, **traits)

        """%locals()
        out.write(indent.format(decl))

        if 'vtk3DWidget' in [x.name for x in node.get_ancestors()]:
            # In this case we also update the traits on the
            # EndInteractionEvent.  Note that we don't need to change
            decl = '''
            def setup_observers(self):
                """Setup the observers for the object."""
                super(%(class_name)s, self).setup_observers()
                tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                              'EndInteractionEvent',
                                              self.update_traits)
            '''%locals()
            out.write(indent.format(decl))

    def _gen_methods(self, node, out):
        klass = self.get_tree().get_class(node.name)
        self.parser.parse(klass)

        if klass.__name__ == 'vtkCamera':
            # 'vtkCamera.Roll' has conflicting signatures --
            # Get/SetRoll() plus an additional Roll() method.  So we
            # wrap all of them as methods and not as traits.
            p = self.parser
            p.get_set_meths.pop('Roll')
            p.other_meths.extend(['GetRoll', 'SetRoll'])

        # ----------------------------------------
        # Generate the code.

        # The return values are editable traits.
        toggle, toggle_allow_failure = self._gen_toggle_methods(klass, out)
        state = self._gen_state_methods(klass, out)

        # The first return value contains updateable traits
        # the second return value contains dubious traits that
        # are initialised by VTK on init
        get_set, allow_update_failure = self._gen_get_set_methods(klass, out)

        allow_update_failure.update(toggle_allow_failure)
        # These do not produce editable traits.
        self._gen_get_methods(klass, out)
        self._gen_other_methods(klass, out)

        # ----------------------------------------
        # Now write out the _updateable_traits_ and View related code.

        # Store the data in the node after updating from parents.
        # Note that this data is generated and stored at run
        # time. This is the reason why the wrapper code for the
        # classes are generated in the reverse order of their depth in
        # the inheritance tree.
        data = {'toggle':toggle, 'state':state, 'get_set':get_set,
                'allow_update_failure': allow_update_failure}
        if node.level != 0 and node.parents[0].name != 'object':
            pd = node.parents[0].data
            for i in data.keys():
                data[i].update(pd[i])
        node.data = data

        # ----------------------------------------
        # Write out the updateable traits, this is used by
        # the `update_traits` method.
        ut = {}
        for i in (data['toggle'], data['state'], data['get_set']):
            ut.update(i)
        junk = textwrap.fill(repr(tuple(ut.items())))
        code = "\n_updateable_traits_ = \\" + "\n%s\n\n"%junk
        out.write(self.indent.format(code))

        # ----------------------------------------
        # Write out the allow_update_failure traits, this is used by
        # the `update_traits` method.
        junk = textwrap.fill(repr(tuple(data['allow_update_failure'])))
        code = "\n_allow_update_failure_ = \\" + "\n%s\n\n"%junk
        out.write(self.indent.format(code))

        # ----------------------------------------
        # Write out the full_traits_view and the more compact
        # traits_view

        # First copy the data over (we're going to edit it and don't
        # want the node's version to be changed).
        d = copy.deepcopy(data)

        # Add support for property trait delegation.
        #Commented out because of problems.
        #self._generate_delegates(node, d, out)

        toggle, state, get_set = d['toggle'], d['state'], d['get_set']

        # Remove unwanted stuff.
        def _safe_remove(d, keys):
            for key in keys:
                try:
                    del d[key]
                except KeyError:
                    pass

        # No point having these in the GUI.
        _safe_remove(get_set, ['reference_count', 'progress'])

        class_name = get_tvtk_name(node.name)
        title = 'Edit %s properties'%class_name

        # Write the full_traits_view.
        # The full traits view displays all of the relevant traits in a table
        # editor. For this, we first write out the _full_traitnames_list: this
        # is used by the TVTKBaseHandler to build a TableEditor for all of
        # the (relevant) traits in the tvtk object.
        t_g = sorted(toggle.keys())
        s_g = sorted(state.keys())
        gs_g = sorted(get_set.keys())

        junk = textwrap.fill("(%s)" % (t_g + s_g + gs_g))
        code = "\n_full_traitnames_list_ = \\" + "\n%s\n\n"%junk
        out.write(self.indent.format(code))

        # Start the trait_view() method.
        code = "\ndef trait_view(self, name=None, view_element=None):"
        out.write(self.indent.format(code))
        self.indent.incr()
        code = "\nif view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):"
        out.write(self.indent.format(code))
        self.indent.incr()
        code = "\nreturn super(%s, self).trait_view(name, view_element)" % class_name
        out.write(self.indent.format(code))
        self.indent.decr()

        # Now write the full traits view.
        code = "\nif name == 'full_traits_view':"
        out.write(self.indent.format(code))
        self.indent.incr()
        item_contents = (
              'Item("handler._full_traits_list",show_label=False)')
        junk = 'View((%s),'% item_contents
        code = "\nfull_traits_view = \\" + \
               "\n%s\ntitle=\'%s\', scrollable=True, resizable=True,"\
               "\nhandler=TVTKBaseHandler,"\
               "\nbuttons=['OK', 'Cancel'])"\
               "\nreturn full_traits_view"%(junk, title)
        out.write(self.indent.format(code))
        self.indent.decr()

        # Next, we write a compact traits_view (which we call 'view'), which
        # removes some generally unused items.
        code = "\nelif name == 'view':"
        out.write(self.indent.format(code))
        self.indent.incr()
        _safe_remove(get_set, ['progress_text'])
        _safe_remove(toggle, ['abort_execute', 'release_data_flag',
                              'dragable', 'pickable',
                              'debug', 'global_warning_display'])
        t_g = sorted(toggle.keys())
        s_g = sorted(state.keys())
        gs_g = sorted(get_set.keys())
        junk = textwrap.fill('View((%s, %s, %s),'%(t_g, s_g, gs_g))
        code = "\nview = \\" + \
               "\n%s\ntitle=\'%s\', scrollable=True, resizable=True,"\
               "\nhandler=TVTKBaseHandler,"\
               "\nbuttons=['OK', 'Cancel'])"\
               "\nreturn view"%(junk, title)
        out.write(self.indent.format(code))
        self.indent.decr()

        # Finally, we write the default traits_view which includes a field
        # for specifying the view type (basic or advanced) and the
        # corresponding view (basic->view and advanced->full_traits_view)
        code = "\nelif name in (None, 'traits_view'):"
        out.write(self.indent.format(code))
        self.indent.incr()
        viewtype_contents = (
            'HGroup(spring, "handler.view_type", ' +\
                             'show_border=True)')
        view_contents = (
            '\nItem("handler.info.object", ' +\
            'editor = InstanceEditor(view_name="handler.view"), ' +\
            'style = "custom", show_label=False)')
        junk = 'View((%s, %s),'% (viewtype_contents, view_contents)
        code = "\ntraits_view = \\" + \
               "\n%s\ntitle=\'%s\', scrollable=True, resizable=True,"\
               "\nhandler=TVTKBaseHandler,"\
               "\nbuttons=['OK', 'Cancel'])"\
               "\nreturn traits_view\n\n"%(junk, title)
        out.write(self.indent.format(code))
        self.indent.decr()

        self.indent.decr()

    def _generate_delegates(self, node, n_data, out):
        """This method generates delegates for specific classes.  It
        modifies the n_data dictionary."""
        prop_name = {'vtkActor': 'vtkProperty',
                     'vtkActor2D': 'vtkProperty2D',
                     'vtkVolume': 'vtkVolumeProperty'}
        if node.name in prop_name:
            prop_node = self.get_tree().get_node(prop_name[node.name])
            prop_data = prop_node.data
            # Update the data of the node so the view includes the
            # property traits.
            code = ''
            for key in n_data:
                props = prop_data[key]
                n_data[key].update(props)
                # Write the delegates.
                for p in props:
                    code += '%s = tvtk_base.vtk_property_delegate\n'%p
            code += '\n'
            out.write(self.indent.format(code))

    def _gen_toggle_methods(self, klass, out):
        meths = self.parser.get_toggle_methods()
        updateable_traits = {}
        allow_update_failure = set()
        for m in meths:
            name = self._reform_name(m)
            #-----------------------------------------------------------
            # Some traits have special API or the VTK API is broken that
            # we need to handle them separately.
            # Warning: Be critical about whether the case is special
            # enthough to be added to the `special_traits` mapping
            # -----------------------------------------------------------
            if self._is_special(klass, m):
                updateable, can_fail = self._get_special_updateable_failable(
                    klass, m)

                if not updateable:
                    # We cannot update this trait
                    del updateable_traits[name]
                elif can_fail:
                    # We will update this trait but updating can fail
                    allow_update_failure.add(name)

                self._write_special_trait(klass, out, m)
                continue

            updateable_traits[name] = 'Get' + m
            t_def = 'tvtk_base.false_bool_trait'
            if meths[m]:
                t_def = 'tvtk_base.true_bool_trait'
            try:
                vtk_set_meth = getattr(klass, 'Set' + m)
            except AttributeError:
                # Broken VTK API (4.2) where sometimes GetProp and
                # PropOn/Off exist but no SetProp method is available.
                vtk_get_meth = getattr(klass, 'Get' + m)
                self._write_trait(out, name, t_def, vtk_get_meth,
                                  mapped=True, broken_bool=True)
            else:
                self._write_trait(out, name, t_def, vtk_set_meth,
                                  mapped=True)
        return updateable_traits, allow_update_failure

    def _gen_state_methods(self, klass, out):
        parser = self.parser
        indent = self.indent
        meths = parser.get_state_methods()
        updateable_traits = {}

        for m in meths:
            name = self._reform_name(m)
            updateable_traits[name] = 'Get' + m
            d = {}
            vtk_val = 0
            for key, val in meths[m]:
                d[self._reform_name(key)] = val
                if isinstance(val, vtk.vtkObjectBase):
                    vtk_val = 1

            # Setting the default value of the traits of these classes
            # Else they are not instantiable
            if klass.__name__ == 'vtkCellQuality' \
                    and m == 'QualityMeasure':
                vtk_val = 1
            if klass.__name__ == 'vtkRenderView' \
                    and m == 'InteractionMode':
                vtk_val = 1
            if klass.__name__ == 'vtkMatrixMathFilter' \
                    and m == 'Operation':
                vtk_val = 1
            if klass.__name__ == 'vtkResliceImageViewer' \
                    and m == 'ResliceMode':
                vtk_val = 'axis_aligned'
            if  klass.__name__ == 'vtkThreshold' \
                   and m == 'PointsDataType':
                vtk_val = 10

            if (not hasattr(klass, 'Set' + m)):
                # Sometimes (very rarely) the VTK method is
                # inconsistent.  For example in VTK-4.4
                # vtkExtentTranslator::SetSplitMode does not exist.
                # In this case wrap it specially.
                vtk_val = 1
            if  vtk_val == 0 and m in ['DataScalarType', 'OutputScalarType',
                                       'UpdateExtent']:
                vtk_val = 2

            # Sometimes, some methods have default values that are
            # outside the specified choices.  This is to special case
            # these.
            extra_val = None
            if vtk_val == 0 and klass.__name__ == 'vtkGenericEnSightReader' \
                   and m == 'ByteOrder':
                extra_val = 2
            if vtk_val == 0 and klass.__name__ == 'vtkImageData' \
                   and m == 'ScalarType':
                extra_val = list(range(0, 22))
            if vtk_val == 0 and klass.__name__ == 'vtkImagePlaneWidget' \
                   and m == 'PlaneOrientation':
                extra_val = 3
            if (vtk_val == 0) and (klass.__name__ == 'vtkThreshold') \
                   and (m == 'AttributeMode'):
                extra_val = -1
            if (sys.platform == 'darwin') and (vtk_val == 0) \
                   and (klass.__name__ == 'vtkRenderWindow') \
                   and (m == 'StereoType'):
                extra_val = 0

            if not vtk_val:
                default = self._reform_name(meths[m][0][0])
                if extra_val is None:
                    t_def = """tvtk_base.RevPrefixMap(%(d)s, default_value='%(default)s')""" % locals()
                elif hasattr(extra_val, '__iter__'):
                    extra_val = str(extra_val)[1:-1]

            if (not hasattr(klass, 'Set' + m)):
                # Sometimes (very rarely) the VTK method is
                # inconsistent.  For example in VTK-4.4
                # vtkExtentTranslator::SetSplitMode does not exist.
                # In this case wrap it specially.
                vtk_val = 1
            if  vtk_val == 0 and m in ['DataScalarType', 'OutputScalarType',
                                       'UpdateExtent']:
                vtk_val = 2

            # Sometimes, some methods have default values that are
            # outside the specified choices.  This is to special case
            # these.
            extra_val = None
            if vtk_val == 0 and klass.__name__ == 'vtkGenericEnSightReader' \
                   and m == 'ByteOrder':
                extra_val = 2
            if vtk_val == 0 and klass.__name__ == 'vtkImageData' \
                   and m == 'ScalarType':
                extra_val = list(range(0, 22))
            if vtk_val == 0 and klass.__name__ == 'vtkImagePlaneWidget' \
                   and m == 'PlaneOrientation':
                extra_val = 3
            if (vtk_val == 0) and (klass.__name__ == 'vtkThreshold') \
                   and (m == 'AttributeMode'):
                extra_val = -1
            if (sys.platform == 'darwin') and (vtk_val == 0) \
                   and (klass.__name__ == 'vtkRenderWindow') \
                   and (m == 'StereoType'):
                extra_val = 0

            if not vtk_val:
                default = self._reform_name(meths[m][0][0])
                if extra_val is None:
                    t_def = """tvtk_base.RevPrefixMap(%(d)s, default_value='%(default)s')""" % locals()
                elif hasattr(extra_val, '__iter__'):
                    extra_val = str(extra_val)[1:-1]
                    t_def = """tvtk_base.RevPrefixMap(%(d)s, %(extra_val)s, default_value='%(default)s')""" % locals()
                else:
                    t_def = """tvtk_base.RevPrefixMap(%(d)s, %(extra_val)s, default_value='%(default)s')""" % locals()
                vtk_set_meth = getattr(klass, 'Set' + m)
                self._write_trait(out, name, t_def, vtk_set_meth,
                                  mapped=True)
            else:
                del updateable_traits[name]
                vtk_meth = getattr(klass, 'Get' + m)
                self._write_tvtk_method(klass, out, vtk_meth)
                if vtk_val == 2:
                    vtk_meth = getattr(klass, 'Set' + m)
                    self._write_tvtk_method(klass, out, vtk_meth)
                for key, val in meths[m][1:]:
                    x = self._reform_name(key)
                    vtk_meth = getattr(klass, 'Set%sTo%s'%(m, key))
                    decl = 'def set_%s_to_%s(self):'%(name, x)
                    body = 'self._vtk_obj.Set%(m)sTo%(key)s()\n'%locals()
                    self._write_generic_method(out, decl, vtk_meth, body)

        return updateable_traits

    def _gen_get_set_methods(self, klass, out):
        parser = self.parser
        meths = parser.get_get_set_methods()
        updateable_traits = {}
        allow_update_failure = set()

        for vtk_attr_name in meths:   # VTK Attribute name (e.g. PropColorValue)
            # trait name
            name = self._reform_name(vtk_attr_name)
            updateable_traits[name] = 'Get' + vtk_attr_name
            vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
            vtk_get_meth = getattr(klass, 'Get' + vtk_attr_name)
            get_sig = parser.get_method_signature(vtk_get_meth)
            set_sig = parser.get_method_signature(vtk_set_meth)

            #- ----------------------------------------------------------
            # Some traits have special API or the VTK API is broken that
            # we need to handle them separately.
            # Warning: Be critical about whether the case is special
            # enthough to be added to the `special_traits` mapping
            # -----------------------------------------------------------
            if self._is_special(klass, vtk_attr_name):
                updateable, can_fail = self._get_special_updateable_failable(
                    klass, vtk_attr_name)

                if not updateable:
                    # We cannot update this trait
                    del updateable_traits[name]
                elif can_fail:
                    # We will update this trait but updating can fail
                    allow_update_failure.add(name)

                self._write_special_trait(klass, out, vtk_attr_name)
                continue

            # --------------------------------------------------------
            # If it is an abstract class with no concrete subclass
            # and if we can read the get method signature, we write
            # the get and set methods and done
            # --------------------------------------------------------
            if not meths[vtk_attr_name] and get_sig[0][1]:
                self._write_tvtk_method(klass, out, vtk_get_meth, get_sig)
                self._write_tvtk_method(klass, out, vtk_set_meth)
                continue

            # -------------------------------
            # Get default values
            # -------------------------------
            if meths[vtk_attr_name]:
                default, rng = meths[vtk_attr_name]
            else:
                # In some rare cases, the vtk class is an abstract class
                # that does not have a concrete subclass
                # We patch the default using the get/set method
                # while the below seems a hack, this is the best we could do
                default, rng = (patch_default(vtk_get_meth, vtk_set_meth, None),
                                None)

            # --------------------------------------------------------
            # Has a specified range of valid values.  Write and done
            # --------------------------------------------------------
            if rng:
                self._write_trait_with_range(klass, out, vtk_attr_name)
                continue

            # ----------------------------------------------------------
            # The VTK Get method for the attribute returns the address
            # to a pointer, this is therefore, a VTK python bug
            # ----------------------------------------------------------
            if isinstance(default, str) and default.endswith('_p_void'):
                try:
                    self._write_trait_with_default_undefined(klass, out,
                                                             vtk_attr_name)
                except TypeError as exception:
                    # We could not write the trait
                    # we will let the next clause handle it
                    print('Warning:', str(exception))
                    default = None
                else:
                    # Getting the trait value using the get method
                    # without argument will continue to return an address to
                    # a pointer, so there is no point in updating.
                    # However, some VTK Get methods have multiple signatures
                    # among which you could pass a numpy array of the right
                    # size and the Get method would populate the array with
                    # the value of the attribute
                    # e.g. x = numpy.empty(9); ImageConvolve.GetKernel3x3(x)
                    # FIXME: we could try harder in retrieving these values
                    # in TVTKBase.update_traits
                    del updateable_traits[name]
                    continue

            # ------------------------------------------------------
            # The default is None, depending on the get/set methods
            # signature, we will either have the trait as a Property
            # and write getter/setter or we would just write the
            # VTK get and set methods
            # -------------------------------------------------------
            if default is None or isinstance(default, vtk.vtkObjectBase):
                # Bunch of hacks to work around issues.
                #print get_sig, vtk_get_meth, klass.__name__
                if len(get_sig) == 0:
                    get_sig = [([None], None)]

                if len(set_sig) == 0:
                    set_sig = [([None], [None])]
                    get_sig = [([None], None)]

                elif set_sig[0][1] is None or set_sig[0][1] == '':
                    set_sig[0] = list(set_sig[0])
                    set_sig[0][1] = [None]

                if get_sig[0][0][0] == 'string' and get_sig[0][1] is None:
                    # If the get method really returns a string
                    # wrap it as such.
                    t_def = 'traits.Trait(None, None, '\
                            'traits.String(enter_set=True, auto_set=False))'
                    self._write_trait(out, name, t_def, vtk_set_meth,
                                      mapped=False)
                else:
                    if (get_sig[0][1] is None) and (len(set_sig[0][1]) == 1):
                        # Get needs no args and Set needs one arg
                        self._write_property(out, name, vtk_get_meth,
                                             vtk_set_meth)
                    else: # Get has args or Set needs many args.
                        self._write_tvtk_method(klass, out, vtk_get_meth, get_sig)
                        self._write_tvtk_method(klass, out, vtk_set_meth, set_sig)

                    # We cannot update the trait
                    del updateable_traits[name]

            # ---------------------------------------------------------
            # This is a color, we want RGBEditor for the trait
            # ---------------------------------------------------------
            elif (isinstance(default, tuple) and len(default) == 3 and
                      (name.find('color') > -1 or name.find('bond_color') > -1 or
                       name.find('background') > -1)):
                # This is a color
                force = 'False'
                # 'vtkProperty' and 'vtkLight' are special because if you change
                # one color the GetColor changes value so we must force an
                # update.
                if klass.__name__ in ['vtkProperty', 'vtkLight']:
                    force = 'True'

                t_def = 'tvtk_base.vtk_color_trait({default})'.format(default=default)
                self._write_trait(out, name, t_def, vtk_set_meth,
                                  mapped=False, force_update=force)

            # ------------------------------------------------------
            # Try to get the trait type using the default
            # ------------------------------------------------------
            else:
                try:
                    # That would give the trait definition as
                    # {trait_type}({default}, {kwargs})
                    trait_type, default, kwargs = get_trait_def(default,
                                                                enter_set=True,
                                                                auto_set=False)
                except TypeError:
                    # ------------------------------------------
                    # Nothing works, print what we ignore
                    # ------------------------------------------
                    print("%s:"%klass.__name__, end=' ')
                    print("Ignoring method: Get/Set%s"%vtk_attr_name)
                    print("default: %s, range: None"%default)
                    del updateable_traits[name]
                else:
                    if default:
                        t_def = '{0}({1}, {2})'.format(trait_type, default,
                                                       kwargs)
                    else:
                        t_def = '{0}({1})'.format(trait_type, kwargs)

                    self._write_trait(out, name, t_def, vtk_set_meth,
                                      mapped=False)

        return updateable_traits, allow_update_failure

    def _gen_get_methods(self, klass, out):
        parser = self.parser
        meths = parser.get_get_methods()
        for m in meths:
            vtk_get_meth = getattr(klass, m)
            if m == 'GetOutput':  # GetOutput is special.
                self._write_get_output_method(klass, out, set=False)
            elif m == 'GetInput':  # GetInput is special.
                self._write_pure_get_input_method(klass, out)
            elif m == 'GetOutputPort':
                # This method sometimes prints warnings so we handle
                # it specially.GetInput is special.
                self._write_pure_get_output_port_method(klass, out)
            else:
                name = self._reform_name(m[3:])
                sig = parser.get_method_signature(vtk_get_meth)
                write_prop = False
                write_getter = True
                if len(sig) == 1 and sig[0][1] is None:
                    write_prop = True
                    # No need for a getter in this case.
                    write_getter = False
                elif len(sig) > 1:
                    for i in sig:
                        if i[1] is None:
                            # There is a getter which takes no args too, so
                            # expose that as a property.
                            write_prop = True
                            break
                if write_prop:
                    self._write_property(out, name, vtk_get_meth, None)
                if write_getter:
                    self._write_tvtk_method(klass, out, vtk_get_meth, sig)

    def _gen_other_methods(self, klass, out):
        parser = self.parser
        meths = parser.get_other_methods()
        for m in meths:
            vtk_meth = getattr(klass, m)
            self._write_tvtk_method(klass, out, vtk_meth)


    #################################################################
    # Private utility methods.
    #################################################################

    def _reform_name(self, name, method=False):
        """Converts a VTK name to an Enthought style one.  If `method`
        is True it does not touch names that are all upper case."""
        if name == 'TeX':
            # Special case for some of the names.  TeX occurs in the
            # vtkGL2PSExporter class.
            return 'tex'
        if name.isupper() and method:
            # All upper case names should remain the same since they
            # are usually special methods.
            return name

        res = camel2enthought(name)
        if keyword.iskeyword(res):
            return res + '_'
        else:
            return res

    def _get_class_name(self, klasses):
        """Returns renamed VTK classes as per TVTK naming style."""
        ret = []
        if type(klasses) in (list, tuple):
            return  [get_tvtk_name(x.__name__) \
                     for x in klasses]
        else:
            return get_tvtk_name(klasses.__name__)

    def _find_type(self, val):
        """Given `val` which is extracted from the method call
        signature, this returns the type of the value.  Right now this
        is in ['vtk', 'array', 'basic'].  'vtk' refers to a VTK type,
        'array' to a vtkDataArray/vtkCellArray/vtkPoints/vtkIdList,
        'basic' refers to a non-VTK, basic Python type.
        """
        _arr_types = ['Array', 'vtkPoints', 'vtkIdList']
        s = repr(val)
        if s.find('vtk') > -1:
            for i in _arr_types:
                if s.find(i) > -1:
                    return 'array'
            return 'vtk'
        else:
            return 'basic'

    def _find_arg_type(self, sig):
        """Given a method signature `sig`, this finds the argument
        types.  It uses the `_find_type` method to obtain its result.
        If no arguments are present in *all* of the signatures, then
        it returns `None`.

        """
        if len(sig) == 1:
            if sig[0][1] is None:
                return None
        args = [s[1] for s in sig]
        return self._find_type(args)

    def _find_return_type(self, sig):
        """Given a method signature `sig`, this finds the return
        types.
        """
        rets = [s[0] for s in sig]
        return self._find_type(rets)

    def _find_sig_type(self, sig):
        """Given a method signature `sig`, this finds the return and
        argument types using.  This is a convenience type and returns
        a tuple containing (ret_type, arg_type).
        """
        return self._find_return_type(sig), self._find_arg_type(sig)

    def _find_array_arg_sig(self, sig):
        """Returns a list of argument signatures from the signature
        information for a method.
        """
        return [s[1] for s in sig]

    #################################################################
    # The following methods do the writing.
    #################################################################

    def _write_get_output_method(self, klass, out, set=False):
        """Write the get_output method.  This method is special and
        needs special care.  `klass` is the class for which the method
        is being wrapped, `out` is the output file.  If `set` is True,
        a set_output method is also wrapped.  This defaults to False.
        """
        vtk_get_meth = getattr(klass, 'GetOutput')
        sig = self.parser.get_method_signature(vtk_get_meth)

        # First write out a property.
        doc = "Output of this source, i.e. the result of `get_output()`."
        if set:
            trait_def = """
            def _get_output(self):
                return wrap_vtk(self._vtk_obj.GetOutput())

            def _set_output(self, obj):
                old_val = self._get_output()
                self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
                self.trait_property_changed('output', old_val, obj)
            output = traits.Property(_get_output, _set_output,
                                     desc=\"%(doc)s\")

            """%locals()
        else:
            trait_def = """
            def _get_output(self):
                return wrap_vtk(self._vtk_obj.GetOutput())
            output = traits.Property(_get_output,
                                     desc=\"%(doc)s\")

            """%locals()
        out.write(self.indent.format(trait_def))

        # Now write the generic method.
        if len(sig) == 1:
            decl = "def get_output(self):"
            body = "return wrap_vtk(self._vtk_obj.GetOutput())"
        else:
            decl = "def get_output(self, idx=None):"
            body = """
            if idx is None:
                return wrap_vtk(self._vtk_obj.GetOutput())
            else:
                return wrap_vtk(self._vtk_obj.GetOutput(idx))
            """
        self._write_generic_method(out, decl, vtk_get_meth, body)

        if set:
            decl = "def set_output(self, obj):"
            body = "old_val = self._get_output()\n"
            body += "self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))\n"
            body += "self.trait_property_changed('output', old_val, obj)\n"
            vtk_set_meth = getattr(klass, 'SetOutput')
            self._write_generic_method(out, decl,
                                       vtk_set_meth, body)

    def _write_get_source_method(self, klass, out):
        """Write the set/get_source method.  This method needs special
        care.  `klass` is the class for which the method is being
        wrapped, `out` is the output file.
        """
        vtk_get_meth = getattr(klass, 'GetSource')
        vtk_set_meth = getattr(klass, 'SetSource')
        set_sig = self.parser.get_method_signature(vtk_set_meth)
        if len(set_sig) > 1:
            # Special case.  First write the property for the first source.
            doc = "The first source of this object, i.e. the result of `get_source(0)`."
            trait_def = """
            def _get_source(self):
                return wrap_vtk(self._vtk_obj.GetSource(0))

            def _set_source(self, obj):
                old_val = self._get_source()
                self._wrap_call(self._vtk_obj.SetSource, deref_vtk(obj))
                self.trait_property_changed('source', old_val, obj)
            source = traits.Property(_get_source, _set_source,
                                     desc=\"%(doc)s\")

            """%locals()
            out.write(self.indent.format(trait_def))
            # Now wrap the set_source and get_source.
            self._write_tvtk_method(klass, out, vtk_get_meth)
            self._write_tvtk_method(klass, out, vtk_set_meth, set_sig)
        else:
            self._write_property(out, 'source', vtk_get_meth, vtk_set_meth)

    def _write_pure_get_output_port_method(self, klass, out):
        """Handle the GetOutputPort method so that it does not print
        unnecessary warning messages.  `klass` is the class for which
        the method is being wrapped, `out` is the output file.
        """
        vtk_get_meth = getattr(klass, 'GetOutputPort')
        t_def = """
        def _get_output_port(self):
            if self._vtk_obj.GetNumberOfOutputPorts():
                return wrap_vtk(self._vtk_obj.GetOutputPort())
            else:
                return None
        """%locals()
        indent = self.indent
        out.write(indent.format(t_def))
        t_def = """output_port = traits.Property(_get_output_port, desc=\\"""
        out.write(indent.format(t_def))
        doc = vtk_get_meth.__doc__
        self.dm.write_trait_doc(doc, out, indent)
        # Close the function definition.
        out.write(indent.format(')'))
        out.write('\n')

    def _write_pure_get_input_method(self, klass, out):
        """Write the get_input method when the class only has the
        getter and no setter.  `klass` is the class for which the
        method is being wrapped, `out` is the output file.
        """
        vtk_get_meth = getattr(klass, 'GetInput')
        get_sig = self.parser.get_method_signature(vtk_get_meth)
        if len(get_sig) > 1:
            # Special case.  First write the property for the first input.
            doc = "The first input of this object, i.e. the result of `get_input(0)`."
            trait_def = """
            def _get_input(self):
                try:
                    return wrap_vtk(self._vtk_obj.GetInput(0))
                except TypeError:
                    return wrap_vtk(self._vtk_obj.GetInput())
            input = traits.Property(_get_input,
                                    desc=\"%(doc)s\")

            """%locals()
            out.write(self.indent.format(trait_def))
            # Now wrap the get_input with args.
            self._write_tvtk_method(klass, out, vtk_get_meth)
        else:
            self._write_property(out, 'input', vtk_get_meth, None)

    def _write_get_input_method(self, klass, out):
        """Write the set/get_input method.  This method needs special
        care.  `klass` is the class for which the method is being
        wrapped, `out` is the output file.
        """
        vtk_get_meth = getattr(klass, 'GetInput')
        vtk_set_meth = getattr(klass, 'SetInput')
        set_sig = self.parser.get_method_signature(vtk_set_meth)
        if len(set_sig) > 1:
            # Special case.  First write the property for the first input.
            doc = "The first input of this object, i.e. the result of `get_input(0)`."
            trait_def = """
            def _get_input(self):
                try:
                    return wrap_vtk(self._vtk_obj.GetInput(0))
                except TypeError:
                    return wrap_vtk(self._vtk_obj.GetInput())

            def _set_input(self, obj):
                old_val = self._get_input()
                self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
                self.trait_property_changed('input', old_val, obj)
            input = traits.Property(_get_input, _set_input,
                                    desc=\"%(doc)s\")

            """%locals()
            out.write(self.indent.format(trait_def))
            # Now wrap the set_input and get_input.
            self._write_tvtk_method(klass, out, vtk_get_meth)
            self._write_tvtk_method(klass, out, vtk_set_meth, set_sig)
        else:
            self._write_property(out, 'input', vtk_get_meth, vtk_set_meth)

    def _write_get_input_connection_method(self, klass, out):
        """Write the set/get_input_connection method.  This method
        needs needs to be wrapped as a property and a method for
        convenience.  `klass` is the class for which the method is
        being wrapped, `out` is the output file.
        """
        vtk_get_meth = getattr(klass, 'GetInputConnection')
        vtk_set_meth = getattr(klass, 'SetInputConnection')
        doc = "The first input connection for this object, i.e. the result of `get_input_connection(0, 0)`."
        trait_def = """
        def _get_input_connection(self):
            if self._vtk_obj.GetTotalNumberOfInputConnections():
                return wrap_vtk(self._vtk_obj.GetInputConnection(0, 0))
            else:
                return None

        def _set_input_connection(self, obj):
            old_val = self._get_input_connection()
            self._wrap_call(self._vtk_obj.SetInputConnection, deref_vtk(obj))
            self.trait_property_changed('input_connection', old_val, obj)
        input_connection = traits.Property(_get_input_connection,
                                           _set_input_connection,
                                           desc=\"%(doc)s\")

        """%locals()
        out.write(self.indent.format(trait_def))
        # Now wrap the set_input_connection and get_input_connection.
        self._write_tvtk_method(klass, out, vtk_get_meth)
        self._write_tvtk_method(klass, out, vtk_set_meth)

    def _write_tvtk_method(self, klass, out, vtk_meth, sig=None):
        """Write a generic tvtk_method to `out`.

        Parameters
        ----------

        - out : file like object

        - vtk_meth : VTK method

          The VTK method to wrap.  A docstring is extracted from
          this.

        - sig : Signature of vtk_method (default: None)

          If None, this is computed.  If not, the passed signature
          information is used.
        """
        if sig is None:
            sig = self.parser.get_method_signature(vtk_meth)

        # VTK 6.2: There exists no method signature for false built in
        # functions/methods
        if sig is None:
            return

        # Figure out if we really need to wrap the return and deref
        # the args.
        ret_type, arg_type = self._find_sig_type(sig)

        vtk_m_name = vtk_meth.__name__
        name = self._reform_name(vtk_m_name, method=True)
        if keyword.iskeyword(name):
            name = name + '_'
        method_affects_input = vtk_m_name in ['AddInput', 'RemoveInput',
                                              'RemoveAllInputs',
                                              'SetInputByNumber']
        method_needs_update = (vtk_m_name in ['InsertNextCell'] and
                               klass.__name__ in ['vtkCellArray'])

        if arg_type is None:
            decl = 'def %s(self):'%name
            body = ""
            if method_affects_input:
                body += "old_val = self._get_input()\n"
            if ret_type in ['vtk', 'array']:
                body += "ret = wrap_vtk(self._vtk_obj.%s())\n"\
                        %vtk_m_name
            else:
                body += "ret = self._vtk_obj.%s()\n"\
                        %vtk_m_name
            if method_affects_input:
                body += "self.trait_property_changed('input', old_val, self._get_input())\n"
            body += "return ret\n\n"

        else:
            decl = 'def %s(self, *args):'%name
            if arg_type == 'vtk':
                body = ""
                if method_affects_input:
                    body += "old_val = self._get_input()\n"
                body += "my_args = [deref_vtk(x) for x in args]\n"\
                        "ret = self._wrap_call(self._vtk_obj.%s, *my_args)\n"\
                        %vtk_m_name
                if method_affects_input:
                    body += "self.trait_property_changed('input', old_val, self._get_input())\n"

            elif arg_type == 'array':
                arr_sig = self._find_array_arg_sig(sig)
                body = "my_args = deref_array(args, %s)\n"\
                       "ret = self._wrap_call(self._vtk_obj.%s, *my_args)\n"\
                       %(arr_sig, vtk_m_name)
                ##########################################################
                # When a cell is inserted, number of cells is not updated.
                # Fixes GH Issue 178.
                ##########################################################
                if method_needs_update:
                    body += "self.update_traits()\n"
            else:
                body = "ret = self._wrap_call(self._vtk_obj.%s, *args)\n"\
                       %vtk_m_name
            if ret_type in ['vtk', 'array']:
                body += "return wrap_vtk(ret)\n"
            else:
                body += "return ret\n"

        self._write_generic_method(out, decl, vtk_meth, body)

    def _write_generic_method(self, out, decl, vtk_doc_meth, body):
        """Write out a method given the declaration, `decl`, the VTK
        method, `vtk_doc_meth`, from which the docstring is to be
        extracted and the code body, `body`.  Each of these is set as
        per the current indentation level.  output is written to the
        `out` object.

        `vtk_doc_meth` could also be a string, in which case the
        string is used directly.

        """
        if type(vtk_doc_meth) is str:
            doc = vtk_doc_meth
        else: # Must be a method so get the docstring.
            doc = self.dm.get_method_doc(vtk_doc_meth.__doc__)
        indent = self.indent
        out.write(indent.format(decl))
        indent.incr()
        if doc:
            out.write(indent.format('"""\n' + doc + '"""\n'))
        out.write(indent.format(body))
        out.write('\n')
        indent.decr()

    def _write_trait(self, out, t_name, t_def, vtk_set_meth,
                     mapped, force_update=None, broken_bool=False):
        """Write out a complete trait definition to `out`.

        Parameters
        ----------
        - out : File like object.

        - t_name : `string`: Name of the trait.

        - t_def : `string` : Trait definition.

        - vtk_set_meth : VTK setter method.

        - mapped : `bool` : Specifies if the trait is mapped.

        - force_update : `string` or `None` : force_update argument.

        - broken_bool : `bool` (default: `False`)

          If `True` the bool method does not have a 'Set' method and
          must be handled specially.  In this case make sure that the
          vtk_set_meth points to the 'Get' method.

        """
        changed = '_%s_changed'%t_name
        vtk_m_name = vtk_set_meth.__name__
        map_str = ''
        if mapped:
            map_str = '_'
        force_str = ''
        if force_update is not None:
            force_str = ', %s'%force_update

        # Fixing the trait definition in order to handle the help trait.
        if t_def.endswith(')'):
            t_def = t_def[:-1] + ', desc=\\'
        else:
            t_def += '(desc=\\'
        trait_def = '%(t_name)s = %(t_def)s'%locals()

        if broken_bool:
            msg = "If broken_bool is true, make sure vtk_set_meth "\
                  "is of form 'GetProp'"
            assert vtk_m_name[:3] == 'Get', msg
            vtk_on_name = vtk_m_name[3:] + 'On'
            vtk_off_name = vtk_m_name[3:] + 'Off'
            changed_def = """
            def %(changed)s(self, old_val, new_val):
                def _bool_change(val, obj=self._vtk_obj):
                    if val:
                        obj.%(vtk_on_name)s()
                    else:
                        obj.%(vtk_off_name)s()
                self._do_change(_bool_change, self.%(t_name)s%(map_str)s%(force_str)s)
            """%locals()
        else:
            changed_def = """
            def %(changed)s(self, old_val, new_val):
                self._do_change(self._vtk_obj.%(vtk_m_name)s,
                                self.%(t_name)s%(map_str)s%(force_str)s)
            """%locals()

        indent = self.indent
        # First write the trait definition.
        out.write(indent.format(trait_def))
        # Write the help docs.
        doc = vtk_set_meth.__doc__
        self.dm.write_trait_doc(doc, out, indent)
        # End the function definition.
        out.write(indent.format(')'))
        out.write('\n')
        # Write the handler method.
        out.write(indent.format(changed_def))
        out.write('\n')

    def _write_property(self, out, t_name, vtk_get_meth, vtk_set_meth,
                        multi_arg=False):
        """Writes out a traited property to `out` given the trait
        name, `t_name`, the VTK get method, `vtk_get_meth` an optional
        VTK set method for read-write traits as, `vtk_set_meth` plus a
        boolean value for `multi_arg`.  If `multi_arg` is True, the
        setter is treated as if it accepts a list of parameters.  If
        not the setter is treated as if it accepts a single parameter.
        """
        indent = self.indent
        getter = '_get_%s'%t_name
        vtk_get_name = vtk_get_meth.__name__
        sig = self.parser.get_method_signature(vtk_get_meth)
        ret_type = self._find_return_type(sig)

        if ret_type in ['vtk', 'array']:
            trait_def = """
            def %(getter)s(self):
                return wrap_vtk(self._vtk_obj.%(vtk_get_name)s())
            """%locals()
        else:
            trait_def = """
            def %(getter)s(self):
                return self._vtk_obj.%(vtk_get_name)s()
            """%locals()
        out.write(indent.format(trait_def))

        if vtk_set_meth:
            setter = '_set_%s'%t_name
            vtk_set_name = vtk_set_meth.__name__
            sig = self.parser.get_method_signature(vtk_set_meth)
            arg_type = self._find_arg_type(sig)
            if multi_arg:
                if arg_type == 'vtk':
                    trait_def = """
                    def %(setter)s(self, *args):
                        old_val = self.%(getter)s()
                        my_args = [deref_vtk(x) for x in args]
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        *my_args)
                        self.trait_property_changed('%(t_name)s', old_val, args)
                    """%locals()
                elif arg_type == 'array':
                    arr_sig = self._find_array_arg_sig(sig)
                    trait_def = """
                    def %(setter)s(self, *args):
                        old_val = self.%(getter)s()
                        my_args = deref_array(args, %(arr_sig)s)
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        *my_args)
                        self.trait_property_changed('%(t_name)s', old_val, args)
                    """%locals()

                else:
                    trait_def = """
                    def %(setter)s(self, *args):
                        old_val = self.%(getter)s()
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        *args)
                        self.trait_property_changed('%(t_name)s', old_val, args)
                    """%locals()
            else:
                if arg_type == 'vtk':
                    trait_def = """
                    def %(setter)s(self, arg):
                        old_val = self.%(getter)s()
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        deref_vtk(arg))
                        self.trait_property_changed('%(t_name)s', old_val, arg)
                    """%locals()
                elif arg_type == 'array':
                    arr_sig = self._find_array_arg_sig(sig)
                    trait_def = """
                    def %(setter)s(self, arg):
                        old_val = self.%(getter)s()
                        my_arg = deref_array([arg], %(arr_sig)s)
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        my_arg[0])
                        self.trait_property_changed('%(t_name)s', old_val, arg)
                    """%locals()

                else:
                    trait_def = """
                    def %(setter)s(self, arg):
                        old_val = self.%(getter)s()
                        self._wrap_call(self._vtk_obj.%(vtk_set_name)s,
                                        arg)
                        self.trait_property_changed('%(t_name)s', old_val, arg)
                    """%locals()
            out.write(indent.format(trait_def))
            t_def = "traits.Property(%(getter)s, %(setter)s, desc=\\"%locals()
        else:
            t_def = "traits.Property(%(getter)s, desc=\\"%locals()

        trait_def = """%(t_name)s = %(t_def)s"""%locals()
        out.write(indent.format(trait_def))
        doc = vtk_get_meth.__doc__
        self.dm.write_trait_doc(doc, out, indent)
        # Close the function definition.
        out.write(indent.format(')'))
        out.write('\n')

    def _write_trait_with_default_undefined(self, klass, out, vtk_attr_name):
        name = self._reform_name(vtk_attr_name)
        vtk_get_meth = getattr(klass, 'Get' + vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)

        # `patch_default` use the Get and Set method to propose a default
        # However we are only using it to get the trait type
        value_for_type = patch_default(vtk_get_meth, vtk_set_meth, None)

        if value_for_type:
            # we should not set the default to arbitrary value without
            # further information.  We will set the default as Undefined
            # or a tuple of Undefined
            if type(value_for_type) in (tuple, list):
                default = "({})".format(", ".join(
                    ("traits.Undefined",)*len(value_for_type)))
            else:
                default = "traits.Undefined"

            trait_type, _, kwargs = get_trait_def(value_for_type)
            t_def = ('traits.Trait({default}, '    # traits.Undefined
                     '{trait_type}({kwargs}), '    # the new default trait
                     'enter_set=True, auto_set=False)').format(
                         default=default,
                         trait_type=trait_type,
                         kwargs=kwargs)
            self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)
        else:
            # we cannot determine the type
            message = 'We cannot determine the trait type of {}.{}'
            raise TypeError(message.format(klass.__name__, vtk_attr_name))

    def _write_trait_with_range(self, klass, out, vtk_attr_name):
        default, rng = self.parser.get_get_set_methods()[vtk_attr_name]

        # If the default is just a little off from the range
        # then extend the range.
        assert default is not None, ('add to vtk_parser exception list: %r %r'
                                     % (klass.__name__.split('.')[-1],
                                        vtk_attr_name))
        if (default < rng[0]) and (rng[0] - default) < 2:
            rng = (default, rng[1])
        if (default > rng[1]) and (default - rng[1]) < 2:
            rng = (rng[0], default)
        # Sometimes the default is not in the valid range to
        # perhaps indicate that the class is not initialized
        if (default < rng[0]) or (default > rng[1]):
            t_def = 'traits.Trait(%(default)s, %(default)s, '\
                    'traits.Range%(rng)s'%locals()
            t_def = t_def[:-1] + ', enter_set=True, auto_set=False))'
        else:
            t_def = 'traits.Trait(%(default)s, '\
                    'traits.Range%(rng)s'%locals()
            t_def = t_def[:-1] + ', enter_set=True, auto_set=False))'

        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        self._write_trait(out, name, t_def, vtk_set_meth,
                          mapped=False)


    # ------------------------------------------------------
    # Traits that need special handling
    # ------------------------------------------------------
    # To add a trait for special handling,
    # add an item to the `special_traits` below,
    # then add a method that handles the trait.
    # The method name should be referred to by the `special_traits`
    # mapping.

    # special_traits = {
    #        expr: (updateable, allow_to_fail, name_of_method)
    #      }
    # where
    # `expr` is a regular expression pattern for matching
    #         {vtkObject}.{Attribute}
    # `updateable` is whether the trait should
    #         be in the `updateable_traits` tuple,
    # `allow_to_fail` is whether the trait should be in the
    #         the `allow_update_failure` tuple
    # `name_of_method` is the name of the method for writing
    #         the code for this trait,
    #         i.e. getattr(self, name_of_method)(...)
    special_traits = {
        '[a-zA-Z0-9]+\.Output$': (
            False, False, '_write_any_output'),
        '[a-zA-Z0-9]+\.Source$': (
            False, False, '_write_any_source'),
        '[a-zA-Z0-9]+\.ScalarType$': (
            False, False, '_write_any_scalar_type'),

        # In VTK > 4.5, Set/GetInput have multiple signatures
        '[a-zA-Z0-9]+\.Input$': (
            False, False, '_write_any_input'),

        '[a-zA-Z0-9]+\.InputConnection$': (
            False, False, '_write_any_input_connection'),
        '[a-zA-Z0-9\.]+FileName$': (
            True, False, '_write_any_something_file_name'),
        '[a-zA-Z0-9\.]+FilePrefix$': (
            True, False, '_write_any_something_file_prefix'),
        'vtkImageReader2.HeaderSize$': (
            True, False, '_write_image_reader2_header_size'),

        # PropColorValue is not initialised, GetPropColorValue
        # gives random values as a tuple of float[3] that are
        'vtkHardwareSelector.PropColorValue$': (
            True, True, '_write_hardware_selector_prop_color_value'),

        # In VTK 5.8, tolerance is initialised as 0 while the range
        # is 1-100
        'vtkAxesTransformRepresentation.Tolerance$': (
            True, True, '_write_axes_transform_representation_tolerance'),

        # In VTK 7.x, vtkSpanSpace.GetResolution is supposed to be between
        # 1 and 2147483647L but can be much larger when un-initialized.
        'vtkSpanSpace.Resolution$': (
            True, True, '_write_span_space_resolution'
        ),

        # In VTK 8.x, vtkSmartVolumeMapper.Get/Set VectorComponent is
        # supposed to be between 0 and 3 but is initialized to some random
        # value.
        'vtkSmartVolumeMapper.VectorComponent$': (
            True, True, '_write_smart_volume_mapper_vector_component'
        ),

        # In VTK 8.x, HyperTreeGridCellCenter's Get/Set VertexCells is supposed
        # to be a boolean but the initialized value can be an arbitrary
        # integer.
        'vtkHyperTreeGridCellCenters.VertexCells$': (
            True, True, '_write_hyper_tree_grid_cell_centers_vertex_cells'
        ),
    }

    @classmethod
    def _get_special_matched_key(cls, klass, vtk_attr_name):
        """ Return the key in `special_traits` that matches klass.vtk_attr_name
        using regular expression

        Parameters
        ----------
        klass : class
           VTK class

        vtk_attr_name : str
           VTK class attribute name

        Returns
        -------
        key
           key is None if nothing matches
        """
        full_name = ".".join((klass.__name__, vtk_attr_name))
        for re_expr in cls.special_traits.keys():
            if re.match(re_expr, full_name):
                return re_expr
        else:
            return None

    @classmethod
    def _get_special_updateable_failable(cls, klass, vtk_attr_name):
        """ Return (updateable, failable) for the klass.vtk_attr_name

        Parameters
        ----------
        klass : class
           VTK class

        vtk_attr_name : str
           VTK class attribute name

        Raises
        ------
        ValueError
           if klass.vtk_attr_name does not match anything in
           `special_traits`
        """
        key = cls._get_special_matched_key(klass, vtk_attr_name)

        if key is None:
            message = '{0}.{1} does not have a special method for get/set code'
            raise ValueError(message.format(klass.__name__, vtk_attr_name))

        return cls.special_traits[key][:2]

    @classmethod
    def _is_special(cls, klass, vtk_attr_name):
        """ Returns True if klass.vtk_attr_name matches anything
        in `special_traits`

        Parameters
        ----------
        klass : class
           VTK class

        vtk_attr_name : str
           VTK class attribute name

        Returns
        -------
        boolean
        """
        full_name = ".".join((klass.__name__, vtk_attr_name))
        return re.match('|'.join(cls.special_traits.keys()),
                        full_name) is not None

    def _write_special_trait(self, klass, out, vtk_attr_name):
        key = self._get_special_matched_key(klass, vtk_attr_name)
        _, _, method_name = self.special_traits[key]
        getattr(self, method_name)(klass, out, vtk_attr_name)

    def _write_any_output(self, klass, out, vtk_attr_name):
        self._write_get_output_method(klass, out, set=True)

    def _write_any_source(self, klass, out, vtk_attr_name):
        self._write_get_source_method(klass, out)

    def _write_any_scalar_type(self, klass, out, vtk_attr_name):
        """ This method does nothing """
        pass

    def _write_any_input(self, klass, out, vtk_attr_name):
        self._write_get_input_method(klass, out)

    def _write_any_input_connection(self, klass, out, vtk_attr_name):
        self._write_get_input_connection_method(klass, out)

    def _write_any_something_file_name(self, klass, out, vtk_attr_name):
        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)

        t_def = 'tvtk_base.vtk_file_name("")'
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_any_something_file_prefix(self, klass, out, vtk_attr_name):
        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        t_def = 'tvtk_base.vtk_file_prefix("")'
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_image_reader2_header_size(self, klass, out, vtk_attr_name):

        if vtk_attr_name != 'HeaderSize':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with HeaderSize. Panicking.")

        default, _ = self.parser.get_get_set_methods()[vtk_attr_name]

        t_def = ('traits.Int({default}, '
                    'enter_set=True, auto_set=False)').format(default=default)

        # trait name
        name = self._reform_name(vtk_attr_name)

        # vtk set method
        vtk_set_meth = getattr(klass, 'Set'+vtk_attr_name)

        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_hardware_selector_prop_color_value(self, klass, out,
                                                  vtk_attr_name):

        if vtk_attr_name != 'PropColorValue':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with PropColorValue. Panicking.")

        # FIXME: Don't we need to tell the vtk object that we set it
        # to some value?
        t_def = ('tvtk_base.vtk_color_trait('
                 '(1.0, 1.0, 1.0))')

        # trait name
        name = self._reform_name(vtk_attr_name)

        # VTK set method
        vtk_set_meth = getattr(klass, 'Set'+vtk_attr_name)

        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False,
                               force_update='False')

    def _write_axes_transform_representation_tolerance(self, klass, out,
                                                       vtk_attr_name):

        if vtk_attr_name != 'Tolerance':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with Tolerance. Panicking.")

        default, rng = self.parser.get_get_set_methods()[vtk_attr_name]

        if is_version_58():
            message = ("vtkAxesTransformRepresentation: "
                       "tolerance not updatable "
                       "(VTK 5.8 bug - value not properly initialized)")
            print(message)
            default = rng[0]
        t_def = ('traits.Trait({default}, traits.Range{rng}, '
                 'enter_set=True, auto_set=False)').format(default=default,
                                                           rng=rng)
        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_smart_volume_mapper_vector_component(self, klass, out,
                                                    vtk_attr_name):
        if vtk_attr_name != 'VectorComponent':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with VectorComponent. Panicking.")

        default, rng = self.parser.get_get_set_methods()[vtk_attr_name]

        if vtk_major_version >= 8:
            message = ("vtkSmartVolumeMapper: "
                       "VectorComponent not updatable "
                       "(VTK 8.x bug - value not properly initialized)")
            print(message)
            default = rng[0]
        t_def = ('traits.Trait({default}, traits.Range{rng}, '
                 'enter_set=True, auto_set=False)').format(default=default,
                                                           rng=rng)
        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_span_space_resolution(self, klass, out,
                                     vtk_attr_name):
        if vtk_attr_name != 'Resolution':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with Resolution. Panicking.")

        default, rng = self.parser.get_get_set_methods()[vtk_attr_name]

        if vtk_major_version == 7:
            message = ("vtkSpanSpace: "
                       "Resolution not updatable "
                       "(VTK 7.x bug - value not properly initialized)")
            print(message)
            default = rng[0]
        t_def = ('traits.Trait({default}, traits.Range{rng}, '
                 'enter_set=True, auto_set=False)').format(default=default,
                                                           rng=rng)
        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)

    def _write_hyper_tree_grid_cell_centers_vertex_cells(self, klass, out,
                                                         vtk_attr_name):
        if vtk_attr_name != 'VertexCells':
            raise RuntimeError("Not sure why you ask for me! "
                               "I only deal with VertexCells. Panicking.")

        if vtk_major_version >= 8:
            message = ("vtkHyperTreeGridCellCenters: "
                       "VertexCells not updatable "
                       "(VTK 8.x bug - value not properly initialized)")
            print(message)

        t_def = 'tvtk_base.true_bool_trait'

        name = self._reform_name(vtk_attr_name)
        vtk_set_meth = getattr(klass, 'Set' + vtk_attr_name)
        self._write_trait(out, name, t_def, vtk_set_meth, mapped=False)
