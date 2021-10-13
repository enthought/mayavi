"""
Script to generate the function reference for mlab.

"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

import os
import sys

DEFAULT_INPUT_DIR = os.path.join('docs', 'source')
OUT_DIR = os.sep.join(
        [os.path.dirname(os.path.abspath(__file__)), DEFAULT_INPUT_DIR,
         'mayavi','auto']
)

from mayavi.tools import auto_doc
from mayavi import mlab

from inspect import getmembers, getsource, getargspec, formatargspec
from docutils import io as docIO
from docutils import core as docCore

# We need to exec render_image, as we can't import it, because it is not
# in a python package.
_src = os.path.abspath(os.path.join('docs', 'source', 'render_images.py'))
render_images = dict(__name__='', __file__=_src)
exec(compile(open(_src).read(), _src, 'exec'), render_images)
IMAGE_DIR = render_images['IMAGE_DIR']

##############################################################################
def dedent(string):
    if string is not None:
        return auto_doc.dedent(string).lstrip(' ')
    else:
        return '\n'


def indent(lines):
    if lines is None:
        return ''
    return '\n'.join('    '+line for line in lines.split('\n'))


def relpath(target, base=os.curdir):
    """
    Return a relative path to the target from either the current dir or an
    optional base dir. Base can be a directory specified either as absolute
    or relative to current dir.

    Adapted from
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/302594
    """

    base_list = (os.path.abspath(base)).split(os.sep)
    target_list = (os.path.abspath(target)).split(os.sep)

    # Starting from the filepath root, work out how much of the filepath is
    # shared by base and target.
    for i in range(min(len(base_list), len(target_list))):
        if base_list[i] != target_list[i]: break
    else:
        # If we broke out of the loop, i is pointing to the first
        # differing path elements. If we didn't break out of the loop, i
        # is pointing to identical path elements.
        # Increment i so that in all cases it points to the first
        # differing path elements.
        i+=1

    rel_list = [os.pardir] * (len(base_list)-i) + target_list[i:]
    return os.path.join(*rel_list)


def is_valid_rst(string):
    """ Check if the given string can be compiled to rst.
    """
    publisher = docCore.Publisher( source_class = docIO.StringInput,
                        destination_class = docIO.StringOutput )
    publisher.set_components('standalone', 'restructuredtext', 'pseudoxml')
    publisher.process_programmatic_settings(None, None, None)
    publisher.set_source(string, None)

    compiled_rst = publisher.reader.read(publisher.source,
                                publisher.parser, publisher.settings)

    if compiled_rst.parse_messages:
        return False
    else:
        return True


def document_function(func, func_name=None, example_code=None,
                            image_file=None):
    """ Creates a rst documentation string for the function, with an
        image and a example code, if given.
    """
    if func_name is None:
        func_name = func.__name__

    func_doc = func.__doc__

    if func_doc is None:
        print('function %s is undocumented' % func_name)
        func_doc = '\n\n'
    else:
        if is_valid_rst(func_doc):
            func_doc = dedent(func_doc)
        else:
            func_doc = "\n::\n" + func_doc

    func_signature = formatargspec(*getargspec(func))

    documentation = """
%(func_name)s
%(title_line)s

.. function:: %(func_name)s%(func_signature)s

%(func_doc)s

    """ % {
            'func_name' : func_name,
            'title_line': '~'*len(func_name),
            'func_signature': func_signature,
            'func_doc'  : indent(dedent(func_doc))
          }

    if image_file is not None:
        documentation += """

.. image:: %s

""" % image_file

    if example_code is not None:
        documentation += """
**Example** (run in ``ipython --gui=qt``, or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

%s
""" % indent(example_code)

    return documentation


##############################################################################
class ModuleReference(object):
    """ The object representing the documentation pages for mlab.
    """

    # Filename of the entry point for the module documentation.
    filename = 'mlab_reference.rst'

    # Directory for the output rst files.
    out_dir = OUT_DIR

    # Directory where the illustration files can be found.
    image_dir = IMAGE_DIR

    # Module to document
    module = None

    # Submodule to classify by
    sub_modules = ()

    # Headers for the sub modules
    sub_headers = None

    # Filenames for the sub modules
    sub_filenames = None

    # Titles for the sub modules pages
    sub_modules_titles = None

    # Header for the main file
    header = ''

    # Footer for the main file
    footer = ''

    # Misc entries that are in no submodules.
    # If this is None, no separate page will be created
    misc_title = None

    # Misc file name
    misc_filename = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def document_function(self, func_name):
        """ Return the documentation page string for a function, with
            automatic discovery of the example and image.
        """
        func = getattr(self.module, func_name)

        print("Documenting function %s" % func_name, file=sys.stderr)

        if hasattr(self.module, 'test_' + func_name):
            example_code = getsource(
                                getattr(self.module, 'test_' + func_name))
            example_code = """
import numpy
from mayavi.mlab import *

%s
            """ % example_code
        else:
            example_code = None

        image_file = self.image_dir + os.sep + \
                        self.module.__name__.replace('.', '_') + '_' \
                        + func_name + '.jpg'

        if not os.path.exists(image_file):
            image_file = None
        else:
            image_file = relpath(image_file, self.out_dir)

        documentation = document_function(func,
                                func_name=func_name,
                                example_code=example_code,
                                image_file=image_file)

        return documentation


    def write_doc(self):
        """ Entry point of the object: goes throught the module and
            writes the docs to the disk.
        """
        self.to_document = set([name
                            for name, func in getmembers(self.module)
                            if not ( name[:5] == 'test_' or name[0] == '_')
                                                     and callable(func)])

        outfile = open(os.sep.join([self.out_dir, self.filename]), 'w')

        outfile.write(self.header)

        outfile.write("""

.. module:: %s

.. toctree::

""" % self.module.__name__)

        if self.sub_modules_titles is None:
            self.sub_modules_titles = ['' for submodule in self.sub_modules]
        if self.sub_headers is None:
            self.sub_headers = ['' for submodule in self.sub_modules]
        if self.sub_filenames is None:
            self.sub_filenames = ['%s.rst' for submodule in self.sub_modules]

        # Document the functions imported from a submodule
        for submodule, header, filename, title in zip(
                    self.sub_modules, self.sub_headers,
                    self.sub_filenames, self.sub_modules_titles):

            self.write_doc_submodule(filename, title=title,
                                     header=header,
                                     submodulename=submodule)
            outfile.write('\t%s\n' % filename)

        # And now the rest
        if self.misc_filename is None:
            misc_filename = self.module.__name__ + '.misc'
        else:
            misc_filename = self.misc_filename
        self.write_doc_submodule(misc_filename, title=self.misc_title)

        if self.misc_title is None:
            outfile.write("""

.. include:: %s

""" % misc_filename)
        else:
            outfile.write('\t%s\n' % misc_filename)

        outfile.write(self.footer)
        outfile.write('\n\n')


    def write_doc_submodule(self, filename, title=None,
                    header=None, submodulename=None):
        """ Writes the docs only for the functions defined in a given
            submodule. If submodule is none, all the non-processed
            functions are processed.
        """
        outfile = open(os.sep.join([self.out_dir, filename]), 'w')

        if header is not None:
            outfile.write(header)

        outfile.write('''

.. currentmodule:: %s

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

''' % self.module.__name__ )
        if title is not None:
            outfile.write(title + '\n')
            outfile.write('='*len(title) + '\n')

        documented = set()

        for func_name in sorted(self.to_document):
            func = getattr(self.module, func_name)

            if (    submodulename is not None
                    and not func.__module__ == submodulename ):
                continue

            outfile.write(self.document_function(func_name))
            outfile.write("\n\n")
            documented.add(func_name)

        self.to_document.difference_update(documented)


#############################################################################
# Entry point

if __name__ == '__main__':
    try:
        os.makedirs(OUT_DIR)
    except:
        pass


    #########################################################################
    # The main mlab module.
    from mayavi.tools import helper_functions, camera, \
            decorations, figure

    sub_modules = [helper_functions, figure, decorations, camera]

    mlab_reference = ModuleReference(
            filename = 'mlab_reference.rst',
            module  = mlab,
            header  = """

.. _mlab-reference:

MLab reference
=================

Reference list of all the main functions of ``mayavi.mlab``
with documentation and examples.

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to run the examples or interact with and assemble
    the functions of `mlab`.

""",
            footer = """\t../mlab_pipeline_reference.rst\n""",
            sub_modules = [module.__name__ for module in sub_modules],
            sub_filenames = ['mlab_%s.rst' % module.__name__.split('.')[-1]
                                for module in sub_modules],
            sub_modules_titles = ['Plotting functions',
                                 'Figure handling functions',
                                 'Figure decoration functions',
                                 'Camera handling functions'],
            misc_title = 'Other functions',
            misc_filename = 'mlab_other_functions.rst',
            )


    mlab_reference.write_doc()

    #########################################################################
    # The mlab.pipeline module, sources functions.
    from mayavi.tools import pipeline, sources, tools, \
                    probe_data

    pipeline_reference = ModuleReference(
            filename = 'mlab_pipeline_reference.rst',
            module  = pipeline,
            header  = """

.. _mlab-pipeline-reference:

MLab pipeline reference
========================

Reference list of all the main functions of
``pipeline`` sub module of ``mlab``. You can access these functions
using::

    mlab.pipeline.function(...)

These functions can be used for finer control of the Mayavi
pipeline than the main mlab interface. For usage examples, see
:ref:`ontrolling-the-pipeline-with-mlab-scripts`.

""",
            sub_modules = [sources.__name__, tools.__name__,
                           probe_data.__name__],
            sub_filenames = ['mlab_pipeline_sources.rst',
                             'mlab_pipeline_tools.rst',
                             'mlab_pipeline_data.rst'],
            sub_modules_titles = ['Sources', 'Tools', 'Data'],
            misc_title = 'Filters, modules, other functions',
            misc_filename = 'mlab_pipeline_other_functions.rst',
            )

    pipeline_reference.write_doc()
