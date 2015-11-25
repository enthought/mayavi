import inspect
import os
import pydoc

import docscrape
from docscrape_sphinx import SphinxClassDoc, SphinxFunctionDoc
import numpydoc
import comment_eater

class SphinxTraitsDoc(SphinxClassDoc):
    def __init__(self, cls, modulename='', func_doc=SphinxFunctionDoc):
        if not inspect.isclass(cls):
            raise ValueError("Initialise using a class. Got %r" % cls)
        self._cls = cls

        if modulename and not modulename.endswith('.'):
            modulename += '.'
        self._mod = modulename
        self._name = cls.__name__
        self._func_doc = func_doc

        docstring = pydoc.getdoc(cls)
        docstring = docstring.split('\n')

        # De-indent paragraph
        try:
            indent = min(len(s) - len(s.lstrip()) for s in docstring
                         if s.strip())
        except ValueError:
            indent = 0

        for n,line in enumerate(docstring):
            docstring[n] = docstring[n][indent:]

        self._doc = docscrape.Reader(docstring)
        self._parsed_data = {
            'Signature': '',
            'Summary': '',
            'Description': [],
            'Extended Summary': [],
            'Parameters': [],
            'Returns': [],
            'Raises': [],
            'Warns': [],
            'Other Parameters': [],
            'Traits': [],
            'Methods': [],
            'See Also': [],
            'Notes': [],
            'References': '',
            'Example': '',
            'Examples': '',
            'index': {}
            }

        self._parse()

    def _str_summary(self):
        return self['Summary'] + ['']

    def _str_extended_summary(self):
        return self['Description'] + self['Extended Summary'] + ['']

    def __str__(self, indent=0, func_role="func"):
        out = []
        out += self._str_signature()
        out += self._str_index() + ['']
        out += self._str_summary()
        out += self._str_extended_summary()
        for param_list in ('Parameters', 'Traits', 'Methods',
                           'Returns','Raises'):
            out += self._str_param_list(param_list)
        out += self._str_see_also("obj")
        out += self._str_section('Notes')
        out += self._str_references()
        out += self._str_section('Example')
        out += self._str_section('Examples')
        out = self._str_indent(out,indent)
        return '\n'.join(out)

def looks_like_issubclass(obj, classname):
    """ Return True if the object has a class or superclass with the given class
    name.

    Ignores old-style classes.
    """
    t = obj
    if t.__name__ == classname:
        return True
    for klass in t.__mro__:
        if klass.__name__ == classname:
            return True
    return False

def get_doc_object(obj, what=None):
    if what is None:
        if inspect.isclass(obj):
            what = 'class'
        elif inspect.ismodule(obj):
            what = 'module'
        elif callable(obj):
            what = 'function'
        else:
            what = 'object'
    if what == 'class':
        doc = SphinxTraitsDoc(obj, '', func_doc=numpydoc.SphinxFunctionDoc)
        if looks_like_issubclass(obj, 'HasTraits'):
            for name, trait, comment in comment_eater.get_class_traits(obj):
                # Exclude private traits.
                if not name.startswith('_'):
                    doc['Traits'].append((name, trait, comment.splitlines()))
        return doc
    elif what in ('function', 'method'):
        return numpydoc.SphinxFunctionDoc(obj, '')
    else:
        return numpydoc.SphinxDocString(pydoc.getdoc(obj))

def initialize(app):
    try:
        app.connect('autodoc-process-signature', numpydoc.mangle_signature)
    except:
        numpydoc.monkeypatch_sphinx_ext_autodoc()

    # Monkeypatch numpydoc
    numpydoc.get_doc_object = get_doc_object

    fn = app.config.numpydoc_phantom_import_file
    if (fn and os.path.isfile(fn)):
        print("[numpydoc] Phantom importing modules from", fn, "...")
        numpydoc.import_phantom_module(fn)

def setup(app):
    app.connect('autodoc-process-docstring', numpydoc.mangle_docstrings)
    app.connect('builder-inited', initialize)
    app.add_config_value('numpydoc_phantom_import_file', None, True)
    app.add_config_value('numpydoc_edit_link', None, True)

    app.add_directive('autosummary', numpydoc.autosummary_directive, 1, (0, 0, False))
    app.add_role('autolink', numpydoc.autolink_role)


