"""This module defines classes used in tvtk code generation,

`SpecialGenerator` defines methods that write out special code for
some of the VTK classes.  `HelperGenerator` helps generate the
`tvtk_helper.py` class.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2007, Enthought, Inc.
# License: BSD Style.

import vtk

# These are relative imports for good reason.
from . import indenter
from .common import get_tvtk_name


######################################################################
# `SpecialGenerator` class.
######################################################################

class SpecialGenerator:
    """Generates special code for some of the TVTK classes.

    For example vtkMatrix4x4 objects can be pickled nicely if the
    elements of the matrix are stored and restored.  So we define a
    `_write_Matrix4x4` method that generates the appropriate code.

    """

    def __init__(self, indent):
        """`indent` is a reference to the `Indenter` instance of the
        WrapperGenerator.

        """
        self.indent = indent

    #################################################################
    # `SpecialGenerator` interface.
    #################################################################

    def generate_code(self, node, out):
        """Write the code given the node in the class tree, `node`,
        and output file-like object, `out`.
        """
        self._write_special(node.name, out)

    #################################################################
    # Non-public interface.
    #################################################################

    def _write_special(self, name, out):
        """Given the name of the class, call appropriate method, if
        available.

        """
        tname = get_tvtk_name(name)
        writer = '_write_%s'%tname
        if hasattr(self, writer):
            getattr(self, writer)(out)

    def _write_InteractorEventRecorder(self, out):
        # This class is a pain because it must always take highest
        # priority, the default value is therefore set to a huge
        # number so that it catches all events first.
        code = '''
        priority = traits.Trait(1.0, traits.Float, traits.Range(0.0, 1.0))
        def _priority_changed(self, old_val, new_val):
            self._do_change(self._vtk_obj.SetPriority,
                            self.priority)
        priority.help = \
            """
            Set/Get the priority at which events are processed. This is used when
            multiple interactor observers are used simultaneously. The default value
            is 0.0 (lowest priority.) Note that when multiple interactor observer
            have the same priority, then the last observer added will process the
            event first. (Note: once the set_interactor() method has been called,
            changing the priority does not effect event processing. You will have
            to set_interactor(_null), change priority, and then set_interactor(iren)
            to have the priority take effect.)
            """
        '''
        out.write(self.indent.format(code))

    def _write_Matrix4x4(self, out):
        code = """
        def __getstate__(self):
            d = tvtk_base.TVTKBase.__getstate__(self)
            obj = self._vtk_obj
            e = [obj.GetElement(i, j) for i in range(4) for j in range(4)]
            d['elements'] = e
            return d

        def __setstate__(self, dict):
            e = dict.pop('elements')
            tvtk_base.TVTKBase.__setstate__(self, dict)
            self._in_set = 1
            obj = self._vtk_obj
            [obj.SetElement(i, j, e[4*i+j]) for i in range(4) for j in range(4)]
            self._in_set = 0
            self.update_traits()

        def from_array(self, arr):
            '''Set the value of the matrix using the passed
            Numeric array or Python list.
            '''
            obj = self._vtk_obj
            [obj.SetElement(i, j, arr[i,j]) for i in range(4) for j in range(4)]

        def to_array(self):
            '''Return the object as a numpy array.'''
            obj = self._vtk_obj
            e = [obj.GetElement(i, j) for i in range(4) for j in range(4)]
            arr = array_handler.numpy.array(e, dtype=float)
            arr.shape = (4,4)
            return arr

        """
        out.write(self.indent.format(code))

    def _write_Property(self, out):
        # Color is made from the other specified colors.
        code = """
        def __getstate__(self):
            d = tvtk_base.TVTKBase.__getstate__(self)
            if 'color' in d:
                del d['color']
            return d

        def __setstate__(self, dict):
            tvtk_base.TVTKBase.__setstate__(self, dict)
            self.update_traits()
        """
        out.write(self.indent.format(code))

    _write_Light = _write_Property

    def _write_Collection(self, out):
        code = """
        def __len__(self):
            return self._vtk_obj.GetNumberOfItems()

        def __iter__(self):
            self._vtk_obj.InitTraversal()
            return self

        def next(self):
            try:
                val = self._vtk_obj.GetNextItem()
            except AttributeError:
                val = self._vtk_obj.GetNextProp()
            if val is None:
                raise StopIteration
            return wrap_vtk(val)

        __next__ = next

        def __getitem__(self, key):
            obj = self._vtk_obj
            if type(key) != type(1):
                raise TypeError("Only integers are valid keys.")
            ni = obj.GetNumberOfItems()
            if key < 0:
                key =  ni + key
            ret = obj.GetItemAsObject(key)
            if ret is None:
                raise IndexError("Index %s out of range."%key)
            return wrap_vtk(ret)

        def __setitem__(self, key, val):
            obj = self._vtk_obj
            if type(key) != type(1):
                raise TypeError("Only integers are valid keys.")
            ni = obj.GetNumberOfItems()
            if key < 0:
                key =  ni + key
            if key < 0 or key >= ni:
                raise IndexError("Index out of range.")
            obj.ReplaceItem(key, deref_vtk(val))

        def __delitem__(self, key):
            obj = self._vtk_obj
            if type(key) != type(1):
                raise TypeError("Only integers are valid keys.")
            ni = obj.GetNumberOfItems()
            if key < 0:
                key =  ni + key
            if key < 0 or key >= ni:
                raise IndexError("Index %s out of range."%key)
            obj.RemoveItem(key)

        def __repr__(self):
            return repr([repr(x) for x in self])

        def append(self, val):
            self._vtk_obj.AddItem(deref_vtk(val))

        def extend(self, arr):
            obj = self._vtk_obj
            for i in arr:
                obj.AddItem(deref_vtk(i))
        """
        out.write(self.indent.format(code))

    def _write_DataArray(self, out):
        code = """
        def __len__(self):
            return self._vtk_obj.GetNumberOfTuples()

        def __iter__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfTuples()
            nc = obj.GetNumberOfComponents()
            if nc in [1,2,3,4,9]:
                meth = getattr(obj, 'GetTuple%d'%nc)
                for i in range(n):
                    yield meth(i)
            else:
                for i in range(n):
                    yield tuple([obj.GetComponent(i, x) for x in range(nc)])

        def _check_key(self, key, n):
            if type(key) not in [int, long]:
                raise TypeError("Only integers are valid keys.")
            if key < 0:
                key =  n + key
            if key < 0 or key >= n:
                raise IndexError("Index %s out of range."%key)
            return key

        def __getitem__(self, key):
            obj = self._vtk_obj
            n = obj.GetNumberOfTuples()
            key = self._check_key(key, n)
            nc = obj.GetNumberOfComponents()
            if nc in [1,2,3,4,9]:
                return getattr(obj, 'GetTuple%d'%nc)(key)
            else:
                return tuple([obj.GetComponent(key, x) for x in range(nc)])

        def __setitem__(self, key, val):
            obj = self._vtk_obj
            n = obj.GetNumberOfTuples()
            key = self._check_key(key, n)
            nc = obj.GetNumberOfComponents()
            if nc == 1:
                obj.SetValue(key, val)
            elif nc in [2,3,4,9]:
                getattr(obj, 'SetTuple%d'%nc)(key, *val)
            else:
                assert len(val) == nc, \
                       'length of %s != %s.'%(val, nc)
                for x in range(nc):
                    obj.SetComponent(key, x, val[x])

        def __repr__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfTuples()
            if n <= 10:
                return repr([x for x in self])
            else:
                first, last = self[0], self[-1]
                return '[%s, ..., %s], length = %s'%(first, last, n)

        def append(self, val):
            obj = self._vtk_obj
            nc = obj.GetNumberOfComponents()
            if nc == 1:
                obj.InsertNextTuple1(val)
            elif nc in [2,3,4,9]:
                meth = getattr(obj, 'InsertNextTuple%d'%nc)
                meth(*val)
            else:
                n = obj.GetNumberOfTuples()
                for x in range(nc):
                    obj.InsertComponent(n, x, val[x])
            self.update_traits()

        def extend(self, arr):
            obj = self._vtk_obj
            nc = obj.GetNumberOfComponents()
            if nc == 1:
                for i in arr:
                    obj.InsertNextTuple1(i)
            elif nc in [2,3,4,9]:
                meth = getattr(obj, 'InsertNextTuple%d'%nc)
                for i in arr:
                    meth(*i)
            else:
                n = obj.GetNumberOfTuples()
                for i in range(len(arr)):
                    for x in range(nc):
                        obj.InsertComponent(n+i, x, arr[i][x])
            self.update_traits()

        def from_array(self, arr):
            '''Set the value of the data array using the passed
            Numeric array or Python list.  This is implemented
            efficiently.
            '''
            array_handler.array2vtk(arr, self._vtk_obj)
            self.update_traits()

        def to_array(self):
            '''Return the object as a Numeric array.'''
            return array_handler.vtk2array(self._vtk_obj)

        """
        out.write(self.indent.format(code))

    def _write_Points(self, out):
        code = """
        def __len__(self):
            return self._vtk_obj.GetNumberOfPoints()

        def __iter__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfPoints()
            for i in range(n):
                yield obj.GetPoint(i)

        def _check_key(self, key, n):
            ##############################################
            # Allow int and long keys. Fixes GH Issue 173.
            ##############################################
            if not isinstance(key, (int, long)):
                raise TypeError("Only int and long are valid keys.")
            if key < 0:
                key =  n + key
            if key < 0 or key >= n:
                raise IndexError("Index %s out of range."%key)
            return key

        def __getitem__(self, key):
            obj = self._vtk_obj
            n = obj.GetNumberOfPoints()
            key = self._check_key(key, n)
            return obj.GetPoint(key)

        def __setitem__(self, key, val):
            obj = self._vtk_obj
            n = obj.GetNumberOfPoints()
            key = self._check_key(key, n)
            obj.SetPoint(key, val)

        def __repr__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfPoints()
            if n <= 10:
                return repr([x for x in self])
            else:
                meth = obj.GetPoint
                return '[%s, ..., %s], length = %s'%(meth(0),
                                                     meth(n-1), n)

        def append(self, val):
            self._vtk_obj.InsertNextPoint(val)
            self.update_traits()

        def extend(self, arr):
            obj = self._vtk_obj
            for i in arr:
                obj.InsertNextPoint(i)
            self.update_traits()

        def from_array(self, arr):
            '''Set the value of the data array using the passed
            Numeric array or Python list.  This is implemented
            efficiently.
            '''
            array_handler.array2vtkPoints(arr, self._vtk_obj)
            self.update_traits()

        def to_array(self):
            '''Return the object as a Numeric array.'''
            return array_handler.vtk2array(self._vtk_obj.GetData())

        """
        out.write(self.indent.format(code))

    def _write_IdList(self, out):
        code = """
        def __len__(self):
            return self._vtk_obj.GetNumberOfIds()

        def __iter__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfIds()
            for i in range(n):
                yield obj.GetId(i)

        def _check_key(self, key, n):
            if type(key) != type(1):
                raise TypeError("Only integers are valid keys.")
            if key < 0:
                key =  n + key
            if key < 0 or key >= n:
                raise IndexError("Index %s out of range."%key)
            return key

        def __getitem__(self, key):
            obj = self._vtk_obj
            n = obj.GetNumberOfIds()
            key = self._check_key(key, n)
            return obj.GetId(key)

        def __setitem__(self, key, val):
            obj = self._vtk_obj
            n = obj.GetNumberOfIds()
            key = self._check_key(key, n)
            obj.SetId(key, val)

        def __repr__(self):
            obj = self._vtk_obj
            n = obj.GetNumberOfIds()
            if n <= 10:
                return repr([x for x in self])
            else:
                meth = obj.GetId
                return '[%s, ..., %s], length = %s'%(meth(0),
                                                     meth(n-1), n)

        def append(self, val):
            self._vtk_obj.InsertNextId(val)
            self.update_traits()

        def extend(self, arr):
            obj = self._vtk_obj
            for i in arr:
                obj.InsertNextId(i)
            self.update_traits()

        def from_array(self, arr):
            '''Set the value of the data array using the passed
            Numeric array or Python list.  This is implemented
            efficiently.
            '''
            array_handler.array2vtkIdList(arr, self._vtk_obj)
            self.update_traits()

        """
        out.write(self.indent.format(code))

    def _write_CellArray(self, out):
        code = """
        def from_array(self, arr):
            '''Set the value of the data array using the passed
            Numeric array or Python list.  This is implemented
            efficiently.
            '''
            array_handler.array2vtkCellArray(arr, self._vtk_obj)
            self.update_traits()

        def to_array(self):
            '''Return the object as a Numeric array.'''
            return array_handler.vtk2array(self._vtk_obj.GetData())
        """
        out.write(self.indent.format(code))

######################################################################
# `HelperGenerator` class.
######################################################################

class HelperGenerator:
    """Writes out the tvtk_helper.py file that makes it easy to use
    tvtk objects efficiently.

    """

    def __init__(self):
        self.indent = indenter.Indent()

    #################################################################
    # `HelperGenerator` interface.
    #################################################################

    def write_prelims(self, out):
        """ Write out the preliminary data."""
        indent = self.indent
        v = vtk.vtkVersion()
        vtk_version = v.GetVTKVersion()[:3]
        vtk_src_version = v.GetVTKSourceVersion()
        code = """
        import vtk
        from tvtk import tvtk_base
        from tvtk.common import get_tvtk_name, camel2enthought

        # Caches all the classes.
        _cache = {}

        def set_ancestors(klass):
            tmp = klass.__bases__
            if not tmp:
                return
            # Assuming a single inheritance.
            tmp = tmp[0]
            name = tmp.__name__
            while name not in _cache and \
                    name not in ['TVTKBase', 'object']:
                _cache[name] = tmp
                tmp = tmp.__bases__[0]
                name = tmp.__name__

        def get_module(fname):
            try:
                mod = __import__('tvtk.custom.%%s'%%fname,
                                 globals(), locals(), [fname])
            except ImportError:
                # This is a local import since the tvtk modules are all
                # inside the tvtk_classes ZIP file and are local to the
                # current module: tvtk_helper.py
                mod = __import__('tvtk.tvtk_classes.%%s'%%fname, globals(), locals(), [fname])
            return mod

        def get_nearest_base_class(obj):
            base = None
            cls = obj.__class__.__bases__[0]
            while base is None:
                try:
                    tvtk_name = get_tvtk_name(cls.__name__)
                    base = get_class(tvtk_name)
                except ImportError:
                    cls = cls.__bases__[0]
            return base

        def get_class(name):
            if name in _cache:
                return _cache[name]
            else:
                fname = camel2enthought(name)
                mod = get_module(fname)
                klass = getattr(mod, name)
                _cache[name] = klass
                set_ancestors(klass)
                return klass

        def wrap_vtk(obj):
            if isinstance(obj, tvtk_base.TVTKBase):
                return obj
            elif isinstance(obj, vtk.vtkObjectBase):
                cached_obj = tvtk_base.get_tvtk_object_from_cache(obj)
                if cached_obj is not None:
                    return cached_obj
                cname = get_tvtk_name(obj.__class__.__name__)
                try:
                    tvtk_class = get_class(cname)
                except ImportError:
                    tvtk_class = get_nearest_base_class(obj)
                return tvtk_class(obj)
            else:
                return obj


        class TVTK(object):
            to_tvtk = staticmethod(wrap_vtk)
            to_vtk = staticmethod(tvtk_base.deref_vtk)

        """%locals()
        out.write(indent.format(code))
        indent.incr()

    def add_class(self, name, out):
        """Add a tvtk class with name, `name` as a property to the
        helper class output file-like object, `out`.
        """
        code = """
        %(name)s = property(lambda self: get_class('%(name)s'))
        """%locals()
        out.write(self.indent.format(code))
