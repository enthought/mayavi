"""This module parses the VTK methods, obtains the argument and return
type information, and organizes them.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

import collections.abc
import re
import types
import os

# Local imports (these are relative imports for a good reason).
from . import class_tree
from . import vtk_module as vtk
from .common import is_version_9


class VTKMethodParser:
    """This class provides useful methods for parsing methods of a VTK
    class or instance.

    The class allows one to categorize the methods of the VTK class
    and also obtain the method signatures in a form that is easy to
    use.  When the `parse` method is called, it in turn calls the
    `_organize_methods` method.  This method organizes the VTK methods
    into different instance variables described in the following.
    `self.toggle_meths` contains a dictionary of all the boolean
    methods of the form <Value>On/Off.  The dictionary keys are
    strings with the <Value>'s and the value of each item is the
    default value (0/1) of the item (the example below will clarify
    this).  `self.state_meths` contains a dictionary which collects
    the Set<Prop>To<Value> type of methods.  The key is the <Prop> and
    the value is a list containing the different string <Value>'s and
    their corresponding mapped value.  The first value in these is the
    default value of the <Prop>.  `self.get_set_meths` will contain a
    dictionary which collects all the methods of the form
    Set/Get<Prop> that are not already specified in
    `self.toggle_meths` or `self.state_meths`.  The default value of
    the Get<Prop> is stored.  If the value accepted by the method has
    a range (via the methods `Get<Prop>MinValue` and
    `Get<Prop>MaxValue`), then that range is computed and stored.
    `self.get_meths` stores the methods that are of the form
    `Get<Prop>`.  `self.other_meths` stores the remaining methods.
    The parsing is quite fast.  Parsing every class in the VTK API
    takes a couple of seconds (on a Pentium III @ 450Mhz).

    Here is an example::

       >>> import vtk
       >>> p = VTKMethodParser()
       >>> p.parse(vtk.vtkProperty)
       >>> print(p.get_toggle_methods())
       {'EdgeVisibility': 0, 'BackfaceCulling': 0, 'FrontfaceCulling': 0}
       >>> print(p.get_state_methods()['Representation'])
       [['Surface', 2], ['Points', 0], ['Surface', 2], ['Wireframe', 1]]
       >>> print(p.get_get_set_methods()['Opacity'])
       (1.0, (0.0, 1.0))
       >>> print(p.get_get_methods())
       ['GetClassName']
       >>> print(p.get_other_methods()[:3])
       ['BackfaceRender', 'DeepCopy', 'IsA']


    The class also provides a method called `get_method_signature`
    that obtains the Python method signature given the VTK method
    object.  Here is an example::

       >>> import vtk
       >>> o = vtk.vtkProperty
       >>> print(VTKMethodParser.get_method_signature(o.GetClassName))
       [(['string'], None)]
       >>> print(VTKMethodParser.get_method_signature(o.GetColor)[0])
       ([('float', 'float', 'float')], None)
       >>> print(VTKMethodParser.get_method_signature(o.GetColor)[1])
       ([None], (('float', 'float', 'float'),))

    The `get_method_signature` is fairly efficient and obtaining the
    signature for every method in every class in the VTK API takes
    around 6 seconds (on a Pentium III @ 450Mhz).

    """

    def __init__(self, use_tree=True):
        """Initializes the object.

        Parameters
        ----------

        - use_tree : `bool`

          If True (default), use a ClassTree instance to obtain a
          concrete subclass for an abstract base class.  This is used
          only to find the range and default values for some of the
          methods.  If False, no ClassTree instance is created.

          This is optional because, creating a ClassTree is expensive.
          The parser functionality can be very useful even without the
          use of a ClassTree.  For example, if one wants to save the
          state of a VTK object one only needs to know the names of
          the methods and not their default values, ranges etc.  In
          that case using a parser should be cheap.

        """
        # The ClassTree is needed to find an instantiable child class
        # for an abstract VTK parent class.  This instance is used to
        # obtain the state values and the ranges of the arguments
        # accepted by the Get/Set methods that have a
        # Get<Prop>{MaxValue,MinValue} method.
        if use_tree:
            self._tree = class_tree.ClassTree(vtk)
            self._tree.create()
        else:
            self._tree = None
        self._state_patn = re.compile('To[A-Z0-9]')
        self._verbose = \
            os.getenv('VTK_PARSER_VERBOSE', '').lower() in ('1', 'true')
        self._initialize()

    #################################################################
    # 'VTKMethodParser' interface.
    #################################################################

    def parse(self, obj, no_warn=True):
        """Parse the methods for a given VTK object/class.

        Given a VTK class or object, this method parses the methods
        and orgaizes them into useful categories.  The categories and
        their usage is documented in the documentation for the class.

        Parameters
        ----------

        - obj : VTK class or instance

        - no_warn : `bool` (default: True)

          If True (default), it suppresses any warnings generated by
          the VTK object when parsing the methods.  This is safe to
          use.

        """
        if not hasattr(obj, '__bases__'):
            klass = obj.__class__
        else:
            klass = obj

        methods = self.get_methods(klass)

        if no_warn:
            # Save warning setting and shut it off before parsing.
            warn = vtk.vtkObject.GetGlobalWarningDisplay()
            if klass.__name__ != 'vtkObject':
                vtk.vtkObject.GlobalWarningDisplayOff()

        self._organize_methods(klass, methods)

        if no_warn:
            # Reset warning status.
            vtk.vtkObject.SetGlobalWarningDisplay(warn)

    def _get_parent_methods(self, klass):
        """Returns all the methods of the classes parents."""
        methods = {}
        while len(klass.__bases__) > 0:
            klass = klass.__bases__[0]
            meths = dir(klass)
            d = methods.fromkeys(meths)
            methods.update(d)
        return list(methods.keys())

    def get_methods(self, klass):
        """Returns all the relevant methods of the given VTK class."""
        methods = dir(klass)[:]
        if hasattr(klass, '__members__'):
            # Only VTK versions < 4.5 have these.
            for m in klass.__members__:
                methods.remove(m)
        # Ignore the parent methods.
        ignore = self._get_parent_methods(klass)

        # Skip some of the ignores.
        skip = ['GetInput', 'SetInput']
        # Sometimes the child has only GetInput while the parent has
        # SetInput.
        if hasattr(klass, 'SetInput') and \
            'SetInput' not in methods and \
            'GetInput' in methods:
            methods.append('SetInput')

        # Get/set pairs that are overridden.  Basically, if a parent
        # class has a 'GetThing' and the child overrides/has a
        # 'SetThing' (or vice-versa), then the removal of the parent
        # methods is wrong since the child changes the trait definition
        # which breaks things.  We therefore do not remove any of the
        # Get/SetThings that are ignored due to them being in the
        # parent.  However one has to be careful about cases where these are
        # really Toggle (ThingOn) or State (SetThingToThong) etc. methods and
        # in those cases we really should ignore the method.  So in essence,
        # any Get/Set pair that is not a State or Toggle should be redefined.
        for m in methods:
            check = False
            if m.startswith('Get'):
                m1 = 'Set' + m[3:]
                check = True
            elif m.startswith('Set'):
                m1 = 'Get' + m[3:]
                check = True
            if check:
                if m1 in methods and (m1 in ignore or m in ignore):
                    skip_method = True
                    if hasattr(klass, 'mro'):
                        # New in VTK 6.3.x with Python 3 support.  In this
                        # case  dir(klass) produces all methods so we check if
                        # the definition is the same as the parent.
                        base_cls = klass.__bases__[0]
                        if getattr(klass, m) is getattr(base_cls, m, None) \
                            and getattr(klass, m1) is getattr(base_cls, m1, None):
                            skip_method = False

                    if skip_method:
                        # Skips are stored as Set followed by Get.
                        skip.extend(['Set' +m[3:], 'Get'+m[3:]])

        for m in skip[:]:
            if m.startswith('Set'):
                base = m[3:]
                mg, ms = 'Get' + base, 'Set' + base
                m_st = 'Set' + base + 'To'
                m_t = base + 'Off'
                for method in methods:
                    if m_st in method or m_t == method:
                        skip.remove(ms)
                        skip.remove(mg)
                        break

        if 'GetViewProp' in methods and 'GetProp' in methods:
            ignore.extend(['GetProp', 'SetProp'])
        if 'GetViewProps' in methods and 'GetProps' in methods:
            ignore.extend(['GetProps', 'SetProps'])
        # Remove any deprecated traits.
        if 'GetScaledText' in methods and 'GetTextScaleMode' in methods:
            ignore.extend(['GetScaledText', 'SetScaledText',
                           'ScaledTextOn', 'ScaledTextOff'])

        # Now we can safely remove the methods.
        for m in methods[:]:
            if m in ignore and m not in skip:
                methods.remove(m)

        return methods

    def get_toggle_methods(self):
        """Returns a dictionary of the parsed <Value>On/Off methods
        along with the default value.

        """
        return self.toggle_meths

    def get_state_methods(self):
        """Returns a dict of the parsed Set<Prop>To<Value>.

        The keys are the <Prop> string with a list of the different
        <Value> strings along with their corresponding value (if
        obtainable).  The first value is the default value of the
        state.

        """
        return self.state_meths

    def get_get_set_methods(self):
        """Returns a dict of the parsed Get/Set<Value> methods.

        The keys of the dict are the <Value> strings and contain a
        two-tuple containing the default value (or None if it is not
        obtainable for some reason) and a pair of numbers specifying
        an acceptable range of values (or None if not obtainable).

        """
        return self.get_set_meths

    def get_get_methods(self):
        """Return a list of parsed Get<Value> methods.

        All of these methods do NOT have a corresponding Set<Value>.

        """
        return self.get_meths

    def get_other_methods(self):
        """Return list of all other methods, that are not
        categorizable.

        """
        return self.other_meths

    @staticmethod
    def get_method_signature(method):
        """Returns information on the Python method signature given
        the VTK method.

        The doc string of the given method object to get the method
        signature.  The method returns a list of tuples, each of which
        contains 2 items, the first is a list representing the return
        value the second represents the arguments to be passed to the
        function.  If the method supports different return values and
        arguments, this function returns all of their signatures.

        Parameters
        ----------

        - method : `method`

          A VTK method object.

        """
        # Remove all the C++ function signatures.
        doc = method.__doc__
        if doc is None:
            return None
        doc = doc[:doc.find('\n\n')]
        new_sig = not doc.startswith('V.')
        sig = []
        c_sig = [] # The C++ signature
        in_sig = False
        in_c_sig = False
        counter = 0
        py_sig_pat = re.compile(r'(V\.)|(\w+\()')
        for line in doc.split('\n'):
            if py_sig_pat.match(line):
                in_sig = True
                in_c_sig = False
                sig.append(line.strip())
            elif line.startswith('C++:'):
                in_sig = False
                in_c_sig = True
                c_sig.append(line.strip())
                counter += 1
            elif in_sig:
                sig[counter] = sig[counter] + line.strip()
            elif in_c_sig:
                c_sig[counter-1] = c_sig[counter-1] + line.strip()

        # Remove the V.<method_name>
        def _process(x):
            if new_sig:
                x = x.replace(method.__name__, '')
                return x.replace('(self, ', '(').replace('(self', '(')
            else:
                return x.replace('V.' + method.__name__, '')

        sig = [_process(x) for x in sig]
        c_sig = [x[x.find('('):] for x in c_sig]

        pat = re.compile(r'\b')

        # Split into [return_value, arguments] after processing them.
        tmp = list(sig)
        sig = []
        for sig_idx, i in enumerate(tmp):
            # Split to get return values.
            x = i.split('->')
            # Strip each part.
            x = [y.strip() for y in x]

            if len(x) == 1: # No return value
                x = [None, x[0]]
            elif x[1] == 'None':
                x = [None, x[0]]
            else:
                x.reverse()

            ret, arg = x

            # Remove leading and trailing parens for arguments.
            arg = arg[1:-1]
            if not arg:
                arg = None
            if arg and arg[-1] in [')', ']']:
                arg = arg + ','

            # Check if we are able to parse all the arguments -- some
            # unstable versions of VTK have problems generating the
            # docstring and in this case we will try to use the C++
            # docstring signature.

            n_arg = 0
            arg_map = {'unsigned int': 'int', 'unsigned char': 'int',
                       'unsigned long': 'long', 'unsigned short': 'int'}
            if arg is not None and c_sig:
                n_arg = arg.count(',') + 1
                # The carguments have parenthesis like: (int, int)
                carg = c_sig[sig_idx][1:-1].split(',')
                if n_arg > 0:
                    args = []
                    if len(carg) == n_arg:
                        for idx, x in enumerate(arg.split(',')):
                            if len(x.strip()) == 0:
                                carg_val = carg[idx].strip()
                                if 'unsigned' in carg_val and \
                                    carg_val in arg_map:
                                    args.append(arg_map[carg_val])
                                elif 'void' in carg_val:
                                    args.append("string")
                                else:
                                    args.append(x)
                            else:
                                args.append(x)
                        arg = ', '.join(args)
            # sanitize type hints
            if arg is not None:
                # thing:value -> value
                arg = re.sub(r'\w+:', lambda mo: '', arg)
                # str -> string
                arg = re.sub(r'\bstr\b', lambda mo: 'string', arg)
                # float=1.0 -> float
                arg = re.sub(r'=[\-e0-9.]+', lambda mo: '', arg)
                # Callback -> function
                arg = re.sub(r'\bCallback\b', lambda mo: 'function', arg)

            if ret is not None and ret.startswith('(') and '...' in ret:
                # A tuple (new in VTK-5.7)
                ret = "tuple"
            if ret == 'str':
                ret = 'string'

            if arg is not None:
                if '[float, ...]' in arg:
                    arg = arg.replace('[float, ...]', 'tuple')
                elif '(float, ...)' in arg:
                    arg = arg.replace('(float, ...)', 'tuple')

            if ret == '(, )':
                ret = None

            # Now quote the args and eval them.  Easy!
            try:
                if ret:
                    ret = eval(pat.sub('\"', ret))
                if arg:
                    arg = eval(pat.sub('\"', arg))
                    if type(arg) == type('str'):
                        arg = [arg]
            except SyntaxError:  # e.g., ret = 'vtkFXAAOptions.DebugOption'
                pass
            else:
                sig.append(([ret], arg))

        return sig

    def get_tree(self):
        """Return the ClassTree instance used by this class."""
        return self._tree

    #################################################################
    # Non-public interface.
    #################################################################

    def _initialize(self):
        """Initializes the method categories."""
        # Collects the <Value>On/Off methods.
        self.toggle_meths = {}
        # Collects the Set<Prop>To<Value> methods.
        self.state_meths = {}
        # Collects the Set/Get<Value> pairs.
        self.get_set_meths = {}
        # Collects the Get<Value> methods.
        self.get_meths = []
        # Collects all the remaining methods.
        self.other_meths = []

    def _organize_methods(self, klass, methods):
        """Organizes the given methods of a VTK class into different
        categories.

        Parameters
        ----------

        - klass : A VTK class

        - methods : `list` of `str`

          A list of the methods to be categorized.

        """
        self._initialize()
        meths = methods[:]
        meths = self._find_toggle_methods(klass, meths)
        meths = self._find_state_methods(klass, meths)
        meths = self._find_get_set_methods(klass, meths)
        meths = self._find_get_methods(klass, meths)
        self.other_meths = [
            x for x in meths \
            if isinstance(getattr(klass, x), collections.abc.Callable)
        ]

    def _remove_method(self, meths, method):
        try:
            meths.remove(method)
        except ValueError:
            pass

    def _find_toggle_methods(self, klass, methods):
        """Find/store methods of the form <Value>{On,Off} in the given
        `methods`.  Returns the remaining list of methods.

        """
        meths = methods[:]
        tm = self.toggle_meths
        klass_name = klass.__name__
        problem_methods = ['CopyVectors', 'CopyTensors',
                           'CopyTCoords', 'CopyScalars',
                           'CopyNormals', 'CopyGlobalIds',
                           'CopyPedigreeIds']
        for method in meths[:]:
            if klass_name == 'vtkDataSetAttributes' and \
               method[:-2] in problem_methods:
                continue
            elif method[:-2] == 'AlphaBitPlanes':
                continue
            if method[-2:] == 'On':
                key = method[:-2]
                if (key + 'Off') in meths and ('Get' + key) in meths:
                    tm[key] = None
                    meths.remove(method)
                    meths.remove(key + 'Off')
                    self._remove_method(meths, 'Set' + key)
                    self._remove_method(meths, 'Get' + key)
        # get defaults
        if tm:
            obj = self._get_instance(klass)
            if obj:
                for key in tm:
                    try:
                        tm[key] = getattr(obj, 'Get%s'%key)()
                    except (TypeError, AttributeError):
                        print(klass.__name__, key)
        return meths

    def _find_state_methods(self, klass, methods):
        """Find/store methods of the form Set<Prop>To<Value> in the
        given `methods`.  Returns the remaining list of methods.  The
        method also computes the mapped value of the different
        <Values>.

        """
        # These ignored ones are really not state methods.
        ignore = ['SetUpdateExtentToWholeExtent',
                  'SetDataExtentToWholeExtent',
                  'SetOutputSpacingToDefault', # In vtkImageReslice.
                  'SetOutputOriginToDefault', # In vtkImageReslice
                  'SetOutputExtentToDefault' # In vtkImageReslice
                  ]
        meths = methods[:]
        sm = self.state_meths
        for method in meths[:]:
            if method not in ignore and method[:3] == 'Set':
                # Methods of form Set<Prop>To<Value>
                match = self._state_patn.search(method)
                # Second cond. ensures that this is not an accident.
                if match and (('Get'+method[3:]) not in meths):
                    key = method[3:match.start()] # The <Prop> part.
                    if (('Get' + key) in methods):
                        val = method[match.start()+2:] # <Value> part.
                        meths.remove(method)
                        if key in sm:
                            sm[key].append([val, None])
                        else:
                            sm[key] = [[val, None]]
                            meths.remove('Get'+ key)
                            self._remove_method(meths, 'Set'+ key)
                            if ('Get' + key + 'MaxValue') in meths:
                                meths.remove('Get' + key + 'MaxValue')
                                meths.remove('Get' + key + 'MinValue')
                            try:
                                meths.remove('Get' + key + 'AsString')
                            except ValueError:
                                pass
        # Find the values for each of the states, i.e. find that
        # vtkProperty.SetRepresentationToWireframe() corresponds to
        # vtkProperty.SetRepresentation(1).
        if sm:
            obj = self._get_instance(klass)
            klass_name = klass.__name__
            if obj and not klass_name.endswith('Viewer'):
                # We do not try to inspect viewers, because they'll
                # trigger segfaults during the inspection
                for key, values in sm.items():
                    default = getattr(obj, 'Get%s'%key)()
                    for x in values[:]:
                        try:
                            getattr(obj, 'Set%sTo%s'%(key, x[0]))()
                        except TypeError:
                            # vtkRenderedGraphRepresentation has some of
                            # its SetIvarToState methods that have
                            # non-standard arguments, this throws off
                            # the parser and we ignore these.
                            #print(klass.__name__, key)
                            pass
                        else:
                            val = getattr(obj, 'Get%s'%key)()
                            x[1] = val
                            if val == default:
                                values.insert(0, [x[0], val])
        return meths

    def _find_get_set_methods(self, klass, methods):
        """Find/store methods of the form {Get,Set}Prop in the given
        `methods` and returns the remaining list of methods.

        Note that it makes sense to call this *after*
        `_find_state_methods` is called in order to avoid incorrect
        duplication.  This method also computes the default value and
        the ranges of the arguments (when possible) by using the
        Get<Prop>{MaxValue,MinValue} methods.

        """
        meths = methods[:]
        gsm = self.get_set_meths
        klass_name = klass.__name__

        for method in meths[:]:
            # Methods of the Set/Get form.
            if method[:3] != 'Set':
                continue
            elif method == 'Set':
                # This occurs with the vtkInformation class.
                continue
            elif (klass_name == 'vtkProp' and
                  method[3:] == 'AllocatedRenderTime'):
                # vtkProp.Get/SetAllocatedRenderTime is private and
                # SetAllocatedRenderTime takes two args, don't wrap it.
                continue
            elif (not is_version_9()) and (
                (klass_name == 'vtkGenericAttributeCollection' and
                 method[3:] == 'AttributesToInterpolate') or
                (klass_name == 'vtkOverlappingAMR' and
                 method[3:] == 'Origin') or
                (klass_name == 'vtkOrientationMarkerWidget' and
                 method[3:] in ['OutlineColor', 'Viewport']) or
                (klass_name == 'vtkImageDataGeometryFilter' and
                 method[3:] == 'Extent') or
                (klass_name == 'vtkVolumeMapper' and
                 method[3:] == 'CroppingRegionPlanes')):
                continue
            elif (klass_name == 'vtkContextMouseEvent' and
                  method[3:] == 'Interactor'):
                continue
            # VTK 9 uses function handles that we don't parse properly yet
            elif (klass_name == 'vtkPiecewisePointHandleItem' and
                  method[3:] == 'PiecewiseFunction'):
                continue
            # These hang on Windows (and maybe Fedora 34)
            elif (klass_name in ('vtkDataEncoder', 'vtkWebApplication')):
                continue
            # we can actually process it
            elif ('Get' + method[3:]) in methods:
                key = method[3:]
                meths.remove('Set' + key)
                meths.remove('Get' + key)
                if ('Get' + key + 'MaxValue') in meths:
                    meths.remove('Get' + key + 'MaxValue')
                    meths.remove('Get' + key + 'MinValue')
                    gsm[key] = 1
                else:
                    gsm[key] = None

        # Find the default and range of the values.
        if gsm:
            if self._verbose:
                print(f'Instantiating {klass}')
            obj = self._get_instance(klass)
            # print('got instance', obj.__class__)
            if obj:
                for key, value in gsm.items():
                    if not is_version_9() and (
                        # Evil hack, these classes segfault!
                        (klass_name in ['vtkPolyData', 'vtkContext2D']) or
                        # On VTK 8.1.0 this segfaults when uninitialized.
                        (klass_name == 'vtkContextMouseEvent' and
                         key == 'Interactor')):
                        default = None
                    elif not is_version_9() and (
                            klass_name == 'vtkHyperOctree' and
                            key == 'Dimension'):
                        # This class breaks standard VTK conventions.
                        gsm[key] = (3, (1, 3))
                        continue
                    # On VTK 9.0.0 vtkHigherOrderTetra.GetParametricCorods
                    # segfauts when uninitialized, see:
                    #
                    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6729#note_732848  # noqa: E501
                    #
                    # vtkGenericAttributeCollection.GetAttributesToInterpolate
                    # might only be a problem if VTK is built in debug mode,
                    # but let's keep it just to be safe.
                    elif is_version_9() and (
                            (klass_name == 'vtkHigherOrderTetra' and
                             key == 'ParametricCoords') or
                            (klass_name == 'vtkGenericAttributeCollection' and
                             key == 'AttributesToInterpolate') or
                            (klass_name == 'vtkPlotBar' and
                             key == 'LookupTable') or
                            (klass_name == 'vtkLagrangianParticleTracker' and
                             key == 'IntegrationModel') or
                            False):  # just to simplify indentation/updates
                        default = None
                    else:
                        try:
                            if self._verbose:
                                print(f'  Calling {klass_name}.Get{key}()')
                            default = getattr(obj, 'Get%s' % key)()
                        except TypeError:
                            default = None

                    # If we don't turn these into integers, they won't instantiate
                    if is_version_9():
                        if klass_name == "vtkAxisActor":
                            if key in (
                                "AxisOnOrigin", "Use2DMode", "UseTextActor3D",
                            ):
                                default = int(bool(default))
                        elif klass_name in ("vtkCubeAxesActor", "vtkPolarAxesActor"):
                            if key in (
                                "EnableDistanceLOD", "EnableViewAngleLOD", "Use2DMode",
                                "UseAxisOrigin", "UseOrientedBounds", "UseTextActor3D",
                            ):
                                default = int(bool(default))

                    if value:
                        low = getattr(obj, 'Get%sMinValue' % key)()
                        high = getattr(obj, 'Get%sMaxValue' % key)()
                        gsm[key] = (default, (low, high))
                    else:
                        gsm[key] = (default, None)
                del obj
                # Segfaults can be exposed by uncommenting these lines,
                # leave them commented while running because they
                # slow things down quite a bit
                # print('GC', klass_name)
                # import gc
                # gc.collect()
            else:
                # We still might have methods that have a default range.
                for key, value in gsm.items():
                    if value == 1:
                        gsm[key] = None

        return meths

    def _find_get_methods(self, klass, methods):
        """Find/store methods of the form Get<Value> in the given
        `methods` and returns the remaining list of methods.

        """
        meths = methods[:]
        gm = self.get_meths
        for method in meths[:]:
            if method == 'Get':
                # Occurs with vtkInformation
                continue
            elif method[:3] == 'Get':
                gm.append(method)
                meths.remove(method)
        return meths

    def _get_instance(self, klass):
        """Given a VTK class, `klass`, returns an instance of the
        class.

        If the class is abstract, it uses the class tree to return an
        instantiable subclass.  This is necessary to get the values of
        the 'state' methods and the ranges for the Get/Set methods.

        """
        obj = None
        try:
            obj = klass()
        except (TypeError, NotImplementedError):
            if self._tree:
                t = self._tree
                n = t.get_node(klass.__name__)
                if n is not None:
                    for c in n.children:
                        obj = self._get_instance(t.get_class(c.name))
                        if obj:
                            break
        return obj
