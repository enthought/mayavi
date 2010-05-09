import os, re, pydoc
from docscrape_sphinx import SphinxDocString, SphinxClassDoc, SphinxFunctionDoc
import inspect

def mangle_docstrings(app, what, name, obj, options, lines,
                      reference_offset=[0]):
    if what == 'module':
        # Strip top title
        title_re = re.compile(r'^\s*[#*=]{4,}\n[a-z0-9 -]+\n[#*=]{4,}\s*',
                              re.I|re.S)
        lines[:] = title_re.sub('', "\n".join(lines)).split("\n")
    else:
        doc = get_doc_object(obj, what)
        lines[:] = str(doc).split("\n")

    if app.config.numpydoc_edit_link and hasattr(obj, '__name__') and \
           obj.__name__:
        v = dict(full_name=obj.__name__)
        lines += [''] + (app.config.numpydoc_edit_link % v).split("\n")

    # replace reference numbers so that there are no duplicates
    references = []
    for l in lines:
        l = l.strip()
        if l.startswith('.. ['):
            try:
                references.append(int(l[len('.. ['):l.index(']')]))
            except ValueError:
                print "WARNING: invalid reference in %s docstring" % name

    # Start renaming from the biggest number, otherwise we may
    # overwrite references.
    references.sort()
    if references:
        for i, line in enumerate(lines):
            for r in references:
                new_r = reference_offset[0] + r
                lines[i] = lines[i].replace('[%d]_' % r,
                                            '[%d]_' % new_r)
                lines[i] = lines[i].replace('.. [%d]' % r,
                                            '.. [%d]' % new_r)

    reference_offset[0] += len(references)

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
        return SphinxClassDoc(obj, '', func_doc=SphinxFunctionDoc)
    elif what in ('function', 'method'):
        return SphinxFunctionDoc(obj, '')
    else:
        return SphinxDocString(pydoc.getdoc(obj))

def mangle_signature(app, what, name, obj, options, sig, retann):
    # Do not try to inspect classes that don't define `__init__`
    if (inspect.isclass(obj) and
        'initializes x; see ' in pydoc.getdoc(obj.__init__)):
        return '', ''

    if not (callable(obj) or hasattr(obj, '__argspec_is_invalid_')): return
    if not hasattr(obj, '__doc__'): return

    doc = SphinxDocString(pydoc.getdoc(obj))
    if doc['Signature']:
        sig = re.sub("^[^(]*", "", doc['Signature'])
        return sig, ''

def initialize(app):
    try:
        app.connect('autodoc-process-signature', mangle_signature)
    except:
        monkeypatch_sphinx_ext_autodoc()

    fn = app.config.numpydoc_phantom_import_file
    if (fn and os.path.isfile(fn)):
        print "[numpydoc] Phantom importing modules from", fn, "..."
        import_phantom_module(fn)

def setup(app):
    app.connect('autodoc-process-docstring', mangle_docstrings)
    app.connect('builder-inited', initialize)
    app.add_config_value('numpydoc_phantom_import_file', None, True)
    app.add_config_value('numpydoc_edit_link', None, True)

    app.add_directive('autosummary', autosummary_directive, 1, (0, 0, False))
    app.add_role('autolink', autolink_role)

#------------------------------------------------------------------------------
# .. autosummary::
#------------------------------------------------------------------------------
from docutils.statemachine import ViewList
from docutils import nodes

import sphinx.addnodes, sphinx.roles
from sphinx.util import patfilter
import posixpath

def autosummary_directive(dirname, arguments, options, content, lineno,
                          content_offset, block_text, state, state_machine):
    """
    Pretty table containing short signatures and summaries of functions etc.

    autosummary also generates a (hidden) toctree:: node.

    """

    # XXX: make the signatures and signature abbreviations optional
    
    names = []
    names += [x for x in content if x.strip()]

    result, warnings, titles = get_autosummary(names, state.document)

    node = nodes.paragraph()
    state.nested_parse(result, 0, node)

    env = state.document.settings.env
    suffix = env.config.source_suffix
    all_docnames = env.found_docs.copy()
    dirname = posixpath.dirname(env.docname)

    docnames = []
    doctitles = {}
    for name in titles.keys():
        docname = 'generated/' + name
        doctitles[docname] = ""
        doctitles[docname + '.xhtml'] = ""
        if docname.endswith(suffix):
            docname = docname[:-len(suffix)]
        docname = posixpath.normpath(posixpath.join(dirname, docname))
        if docname not in env.found_docs:
            warnings.append(state.document.reporter.warning(
                'toctree references unknown document %r' % docname,
                line=lineno))
        docnames.append(docname)

    tocnode = sphinx.addnodes.toctree()
    tocnode['includefiles'] = docnames
    tocnode['includetitles'] = doctitles
    tocnode['maxdepth'] = -1
    tocnode['glob'] = None

    return warnings + node.children + [tocnode]

def get_autosummary(names, document):
    """
    Generate a proper table node for autosummary:: directive.

    Parameters
    ----------
    names : list of str
        Names of Python objects to be imported and added to the table.
    document : document
        Docutils document object
    
    """
    result = ViewList()
    warnings = []
    titles = {}

    prefixes = ['']
    prefixes.insert(0, document.settings.env.currmodule)

    rows = []

    for name in names:
        try:
            obj, real_name = import_by_name(name, prefixes=prefixes)
        except ImportError:
            warnings.append(document.reporter.warning(
                'failed to import %s' % name))
            rows.append((":obj:`%s`" % name, ""))
            continue

        doc = get_doc_object(obj)

        if doc['Summary']:
            titles[real_name] = " ".join(doc['Summary'])
        else:
            titles[real_name] = ""
        
        col1 = ":obj:`%s`" % name
        if doc['Signature']:
            sig = re.sub('^[a-zA-Z_0-9.-]*', '',
                         doc['Signature'].replace('*', r'\*'))
            if '=' in sig:
                # abbreviate optional arguments
                sig = re.sub(r', ([a-zA-Z0-9_]+)=', r'[, \1=', sig, count=1)
                sig = re.sub(r'\(([a-zA-Z0-9_]+)=', r'([\1=', sig, count=1)
                sig = re.sub(r'=[^,)]+,', ',', sig)
                sig = re.sub(r'=[^,)]+\)$', '])', sig)
                # shorten long strings
                sig = re.sub(r'(\[.{16,16}[^,)]*?),.*?\]\)', r'\1, ...])', sig)
            else:
                sig = re.sub(r'(\(.{16,16}[^,)]*?),.*?\)', r'\1, ...)', sig)
            col1 += " " + sig
        col2 = titles[real_name]
        
        rows.append((col1, col2))

    if not rows:
        return result, warnings, titles
    
    max_name_len = max([len(x[0]) for x in rows])
    row_fmt = "%%-%ds  %%s" % max_name_len
    table_banner = ('='*max_name_len) + '  ' + '==============='
    
    result.append(table_banner, '<autosummary>')
    for row in rows:
        result.append(row_fmt % row, '<autosummary>')
    result.append(table_banner, '<autosummary>')
    result.append('', '<autosummary>')

    return result, warnings, titles

def import_by_name(name, prefixes=[None]):
    """
    Import a Python object that has the given name, under one of the prefixes.

    Parameters
    ----------
    name : str
        Name of a Python object, eg. 'numpy.ndarray.view'
    prefixes : list of (str or None), optional
        Prefixes to prepend to the name (None implies no prefix).
        The first prefixed name that results to successful import is used.

    Returns
    -------
    obj
        The imported object
    name
        Name of the imported object (useful if `prefixes` was used)
    
    """
    for prefix in prefixes:
        try:
            if prefix:
                prefixed_name = '.'.join([prefix, name])
            else:
                prefixed_name = name
            return _import_by_name(prefixed_name), prefixed_name
        except ImportError:
            pass
    raise ImportError

def _import_by_name(name):
    """Import a Python object given its full name"""
    try:
        name_parts = name.split('.')
        last_j = 0
        modname = None
        for j in reversed(range(1, len(name_parts)+1)):
            last_j = j
            modname = '.'.join(name_parts[:j])
            try:
                __import__(modname)
            except ImportError:
                continue
            if modname in sys.modules:
                break

        if last_j < len(name_parts):
            obj = sys.modules[modname]
            for obj_name in name_parts[last_j:]:
                obj = getattr(obj, obj_name)
            return obj
        else:
            return sys.modules[modname]
    except (ValueError, ImportError, AttributeError, KeyError), e:
        raise ImportError(e)

#------------------------------------------------------------------------------
# :autolink: (smart default role)
#------------------------------------------------------------------------------

def autolink_role(typ, rawtext, etext, lineno, inliner,
                  options={}, content=[]):
    """
    Smart linking role.

    Expands to ":obj:`text`" if `text` is an object that can be imported;
    otherwise expands to "*text*".
    """
    r = sphinx.roles.xfileref_role('obj', rawtext, etext, lineno, inliner,
                                   options, content)
    pnode = r[0][0]

    prefixes = [None]
    #prefixes.insert(0, inliner.document.settings.env.currmodule)
    try:
        obj, name = import_by_name(pnode['reftarget'], prefixes)
    except ImportError:
        content = pnode[0]
        r[0][0] = nodes.emphasis(rawtext, content[0].astext(),
                                 classes=content['classes'])
    return r

#------------------------------------------------------------------------------
# Monkeypatch sphinx.ext.autodoc to accept argspecless autodocs (Sphinx < 0.5)
#------------------------------------------------------------------------------

def monkeypatch_sphinx_ext_autodoc():
    global _original_format_signature
    import sphinx.ext.autodoc

    if sphinx.ext.autodoc.format_signature is our_format_signature:
        return

    print "[numpydoc] Monkeypatching sphinx.ext.autodoc ..."
    _original_format_signature = sphinx.ext.autodoc.format_signature
    sphinx.ext.autodoc.format_signature = our_format_signature

def our_format_signature(what, obj):
    r = mangle_signature(None, what, None, obj, None, None, None)
    if r is not None:
        return r[0]
    else:
        return _original_format_signature(what, obj)

#------------------------------------------------------------------------------
# Creating 'phantom' modules from an XML description
#------------------------------------------------------------------------------
import imp, sys, compiler, types

def import_phantom_module(xml_file):
    """
    Insert a fake Python module to sys.modules, based on a XML file.

    The XML file is expected to conform to Pydocweb DTD. The fake
    module will contain dummy objects, which guarantee the following:

    - Docstrings are correct.
    - Class inheritance relationships are correct (if present in XML).
    - Function argspec is *NOT* correct (even if present in XML).
      Instead, the function signature is prepended to the function docstring.
    - Class attributes are *NOT* correct; instead, they are dummy objects.

    Parameters
    ----------
    xml_file : str
        Name of an XML file to read
    
    """
    import lxml.etree as etree

    object_cache = {}

    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Sort items so that
    # - Base classes come before classes inherited from them
    # - Modules come before their contents
    all_nodes = dict([(n.attrib['id'], n) for n in root])
    
    def _get_bases(node, recurse=False):
        bases = [x.attrib['ref'] for x in node.findall('base')]
        if recurse:
            j = 0
            while True:
                try:
                    b = bases[j]
                except IndexError: break
                if b in all_nodes:
                    bases.extend(_get_bases(all_nodes[b]))
                j += 1
        return bases

    type_index = ['module', 'class', 'callable', 'object']
    
    def base_cmp(a, b):
        x = cmp(type_index.index(a.tag), type_index.index(b.tag))
        if x != 0: return x

        if a.tag == 'class' and b.tag == 'class':
            a_bases = _get_bases(a, recurse=True)
            b_bases = _get_bases(b, recurse=True)
            x = cmp(len(a_bases), len(b_bases))
            if x != 0: return x
            if a.attrib['id'] in b_bases: return -1
            if b.attrib['id'] in a_bases: return 1
        
        return cmp(a.attrib['id'].count('.'), b.attrib['id'].count('.'))

    nodes = root.getchildren()
    nodes.sort(base_cmp)

    # Create phantom items
    for node in nodes:
        name = node.attrib['id']
        doc = (node.text or '').decode('string-escape') + "\n"
        if doc == "\n": doc = ""

        # create parent, if missing
        parent = name
        while True:
            parent = '.'.join(parent.split('.')[:-1])
            if not parent: break
            if parent in object_cache: break
            obj = imp.new_module(parent)
            object_cache[parent] = obj
            sys.modules[parent] = obj

        # create object
        if node.tag == 'module':
            obj = imp.new_module(name)
            obj.__doc__ = doc
            sys.modules[name] = obj
        elif node.tag == 'class':
            bases = [object_cache[b] for b in _get_bases(node)
                     if b in object_cache]
            bases.append(object)
            init = lambda self: None
            init.__doc__ = doc
            obj = type(name, tuple(bases), {'__doc__': doc, '__init__': init})
            obj.__name__ = name.split('.')[-1]
        elif node.tag == 'callable':
            funcname = node.attrib['id'].split('.')[-1]
            argspec = node.attrib.get('argspec')
            if argspec:
                argspec = re.sub('^[^(]*', '', argspec)
                doc = "%s%s\n\n%s" % (funcname, argspec, doc)
            obj = lambda: 0
            obj.__argspec_is_invalid_ = True
            obj.func_name = funcname
            obj.__name__ = name
            obj.__doc__ = doc
            if inspect.isclass(object_cache[parent]):
                obj.__objclass__ = object_cache[parent]
        else:
            class Dummy(object): pass
            obj = Dummy()
            obj.__name__ = name
            obj.__doc__ = doc
            if inspect.isclass(object_cache[parent]):
                obj.__get__ = lambda: None
        object_cache[name] = obj

        if parent:
            if inspect.ismodule(object_cache[parent]):
                obj.__module__ = parent
                setattr(object_cache[parent], name.split('.')[-1], obj)

    # Populate items
    for node in root:
        obj = object_cache.get(node.attrib['id'])
        if obj is None: continue
        for ref in node.findall('ref'):
            if node.tag == 'class':
                if ref.attrib['ref'].startswith(node.attrib['id'] + '.'):
                    setattr(obj, ref.attrib['name'],
                            object_cache.get(ref.attrib['ref']))
            else:
                setattr(obj, ref.attrib['name'],
                        object_cache.get(ref.attrib['ref']))
