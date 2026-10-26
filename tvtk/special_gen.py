"""This module defines classes used in tvtk code generation,

`SpecialGenerator` defines methods that write out special code for
some of the VTK classes.  `HelperGenerator` helps generate the
`tvtk_helper.py` class.

"""
# Author: Prabhu Ramachandran
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# These are relative imports for good reason.
from . import indenter
from .common import get_tvtk_name


######################################################################
# `SpecialGenerator` class.
######################################################################

# The classes that get a hand-written mixin from tvtk/mixins.py as their first
# base, by TVTK class name.  Names only: the generator must not import
# tvtk.mixins, which needs traits, and the build environment has no traits.
MIXINS = {
    'CellArray': 'CellArrayMixin',
    'Collection': 'CollectionMixin',
    'DataArray': 'DataArrayMixin',
    'IdList': 'IdListMixin',
    'Light': 'PropertyMixin',
    'Matrix4x4': 'Matrix4x4Mixin',
    'Points': 'PointsMixin',
    'Property': 'PropertyMixin',
}


class SpecialGenerator:
    """Generates special code for some of the TVTK classes.

    Hand-written *methods* belong in a mixin in tvtk/mixins.py (see
    `MIXINS`), where they are ordinary, testable Python.  Only what has to
    be in the class body itself, such as a trait definition, is written
    here, by a `_write_<TVTK class name>` method.

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
        code = """
        import vtk
        from tvtk import tvtk_base
        # not the same thing as ``vtk`` above: vtk_module is the filtered view
        # of it that the generated classes bind, with the classes that are
        # broken on this runtime VTK removed (see tvtk/WORKAROUNDS.md)
        from tvtk import vtk_module
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
            # Walk the MRO rather than assuming single inheritance: as of
            # VTK 9.7, data arrays can be returned wrapped in Python mixin
            # classes (e.g. VTKAOSArray_vtkFloatArray) whose first base is
            # the mixin, not the VTK class (see tvtk/WORKAROUNDS.md)
            for cls in type(obj).__mro__[1:]:
                try:
                    return get_class(get_tvtk_name(cls.__name__))
                except (ImportError, AttributeError):
                    continue
            raise TypeError('cannot find TVTK base class for ' +
                            repr(type(obj)))

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
                vtk_name = obj.__class__.__name__
                cname = get_tvtk_name(vtk_name)
                # VTK names some of its Python classes without the prefix --
                # vtkImageData's class is literally named "ImageData" -- while
                # vtk_module only ever holds the prefixed names
                if not vtk_name.startswith('vtk'):
                    vtk_name = 'vtk' + vtk_name
                try:
                    tvtk_class = get_class(cname)
                except ImportError:
                    tvtk_class = get_nearest_base_class(obj)
                else:
                    if not hasattr(vtk_module, vtk_name):
                        # The wrapper exists but vtk_module removed the VTK
                        # class it names on this runtime.  A same-version
                        # build never generates the wrapper at all and lands
                        # in the ImportError branch above; a wheel or conda
                        # package generated against a newer VTK still ships
                        # it, and instantiating it would raise AttributeError
                        # on vtk.<vtk_name>.  Fall back to the nearest wrapped
                        # base either way (see tvtk/WORKAROUNDS.md)
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
