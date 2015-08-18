"""
Automatic documentation from traited objects.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007-2015, Enthought, Inc.
# License: BSD Style.

from textwrap import wrap, dedent
import types

old_dedent = dedent


def dedent(text):
    """ Removes as much indentation as possible from some text, but does
    not modify the first line.
    """
    text_lines = [line.rstrip() for line in text.split("\n")]
    if len(text_lines) > 0:
        return text_lines[0] + "\n" + old_dedent(
                                            "\n".join(text_lines[1:]))
    else:
        return text


def make_doc(klass):
    """ Builds a docstring from the object's docstring, and it's traits
    help.
    """
    if hasattr(klass, '__doc__'):
        doc = dedent(klass.__doc__) + "\n"
    else:
        doc = ""
    doc += dedent("""**Keyword arguments:**""")
    traits = klass.class_traits().copy()
    traits.pop('trait_added')
    traits.pop('trait_modified')
    doc += traits_doc(traits)
    return doc


def traits_doc(traits):
    doc = ""
    traits_names = sorted(traits.keys())
    for trait_name in traits_names:
        trait_obj = traits[trait_name]
        if not trait_name[0] == '_':
            doc += format_argument(trait_name, trait_obj)
    return doc


def format_argument(trait_name, trait_obj):
    doc = "\n    :%s: " % trait_name
    pad = "\n" + (len(doc) - 1) * " "
    help = trait_obj.help
    if help is not None:
        arg_desc = help
    else:
        arg_desc = ''
        desc = trait_obj.desc
        if desc is not None:
            arg_desc += desc.rstrip()
        handler = trait_obj.handler
        if handler is not None:
            if (not hasattr(handler, 'aType') or
                        not handler.aType in (int, float)):
                # These types are simple enough
                arg_desc += ' Must be %s.' % handler.info()
        default = trait_obj.default_value()[1]
        if not default in ('', None) and not trait_obj.array:
            arg_desc = arg_desc.rstrip() + " Default: %s" % str(default)
    desc_width = 75 - len(doc)
    for line in wrap(arg_desc, width=desc_width):
        doc += line
        doc += pad
    return doc
