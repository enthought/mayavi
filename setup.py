#!/usr/bin/env python
#
# Copyright (c) 2008-2011 by Enthought, Inc.
# All rights reserved.

"""
The Mayavi scientific data 3-dimensional visualizer.

The Mayavi *project* includes two related *packages* for 3-dimensional
visualization:

- **Mayavi2**: A tool for easy and interactive visualization of data.
- **TVTK**: A Traits-based wrapper for the Visualization Toolkit, a popular
  open-source visualization library.

These libraries operate at different levels of abstraction. TVTK manipulates
visualization objects, while Mayavi2 lets you operate on your data, and then
see the results. Most users either use the Mayavi user interface or program
to its scripting interface; you probably don't need to interact with TVTK
unless you want to create a new Mayavi module.

Mayavi2
-------
Mayavi2 seeks to provide easy and interactive visualization of 3-D data.
It offers:

- An (optional) rich user interface with dialogs to interact with all data
  and objects in the visualization.
- A simple and clean scripting interface in Python, including one-liners,
  or an object-oriented programming interface.
- The power of the VTK toolkit, harnessed through these interfaces, without
  forcing you to learn it.

Additionally Mayavi2 is a reusable tool that can be embedded in your
applications in different ways or combined with the Envisage
application-building framework to assemble domain-specific tools.



TVTK
----

TVTK wraps VTK objects to provide a convenient, Pythonic API, while supporting
Traits attributes and NumPy/SciPy arrays. TVTK is implemented mostly in pure
Python, except for a small extension module.

Developers typically use TVTK to write Mayavi modules, and then use Mayavi to
interact with visualizations or create applications.

Prerequisites
-------------
You must have the following libraries installed before installing the Mayavi
project:

* `Numpy <http://pypi.python.org/pypi/numpy/1.1.1>`_ version 1.1.0 or later is
  preferred. Version 1.0.4 will work, but some tests may fail.
* `VTK <http://www.vtk.org/>`_ version 5.0 or later.
* `wxPython <http://www.wxpython.org/>`_ version 2.8 or later.
* `setuptools <http://pypi.python.org/pypi/setuptools/0.6c8>`_.

"""


# NOTE: Setuptools must be imported BEFORE numpy.distutils or else
# numpy.distutils does the Wrong(TM) thing.
import setuptools
from setuptools import Command

import numpy
import os
import subprocess
import shutil
import re
import sys
import zipfile
import traceback

from numpy.distutils.command import build, install_data
from distutils import log
from setuptools.command import develop, install_scripts


# FIXME: This works around a setuptools bug which gets setup_data.py metadata
# from incorrect packages. Ticket #1592
#from setup_data import INFO
setup_data = dict(__name__='', __file__='setup_data.py')
execfile('setup_data.py', setup_data)
INFO = setup_data['INFO']

DEFAULT_HTML_TARGET_DIR = os.path.join('build', 'docs', 'html')
DEFAULT_INPUT_DIR = os.path.join('docs', 'source',)
DEFAULT_HTML_ZIP = os.path.abspath(os.path.join('docs', 'html.zip'))

class GenDocs(Command):

    description = \
        "This command generates generated part of the documentation " \
        "when needed. It's run automatically before a build_docs, and that's " \
        "the only time it needs to be run."

    user_options = [
        ('None', None, 'this command has no options'),
        ]

    def latest_modified(self, the_path, filetypes='', ignore_dirs=''):
        """Traverses a path looking for the most recently modified file

        Parameters
        ----------
        the_path : string
            Contains path to be traversed or filename to be inspected.
        filetypes : string
            Regular expression pattern of files to examine. If specified, other
            files are ignored. Otherwise, all files are examined.
        ignore_dirs : string
            Regular expression pattern of directories to be ignored. If ignore
            specified, all directories are walked.

        Returns
        -------
        latest_time : float
            Modification time of latest_path.
        latest_path : string
            Most recently modified file.

        Description
        -----------

        """

        file_re = re.compile(filetypes)
        dir_re = re.compile(ignore_dirs)

        if not os.path.exists(the_path):
            return 0, the_path
        if os.path.isdir(the_path):
            latest_time = 0
            latest_path = the_path
            for root, dirs, files in os.walk(the_path):
                if ignore_dirs != '':
                    # This needs to iterate over a copy of the list. Otherwise,
                    # as things get removed from the original list, the indices
                    # become invalid.
                    for dir in dirs[:]:
                        if dir_re.search(dir):
                            dirs.remove(dir)
                for file in files:
                    if filetypes != '':
                        if not file_re.search(file):
                            continue
                    current_file_time = os.path.getmtime(os.path.join(root,
                        file))
                    if current_file_time > latest_time:
                        latest_time = current_file_time
                        latest_path = os.path.join(root, file)
            return latest_time, latest_path

        else:
            return os.path.getmtime(the_path), the_path

    def mlab_reference(self):
        """ If mayavi is installed, run the mlab_reference generator.
        """
        # XXX: This is really a hack: the script is not made to be used
        # for different projects, but it ended up being. This part is
        # mayavi-specific.

        mlab_ref_dir = os.path.join(DEFAULT_INPUT_DIR, 'mayavi','auto')

        source_path = os.path.join('enthought', 'mayavi')
        sources = '(\.py)|(\.rst)$'
        excluded_dirs = '^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path, ignore_dirs=excluded_dirs)[0]

        if self.latest_modified(source_path, filetypes=sources,
            ignore_dirs=excluded_dirs)[0] > target_time or \
            self.latest_modified('mlab_reference.py')[0] > target_time or\
            not os.path.exists(
                os.path.join('docs', 'source', 'mayavi', 'auto',
                'mlab_reference.rst')):
            try:
                from enthought.mayavi import mlab
                from enthought.mayavi.tools import auto_doc
                print "Generating the mlab reference documentation"
                os.system('python mlab_reference.py')
            except:
                pass

    def example_files(self):
        """ Generate the documentation files for the examples.
        """
        mlab_ref_dir = os.path.join(DEFAULT_INPUT_DIR, 'mayavi','auto')

        source_path = os.path.join('examples', 'mayavi')
        sources = '(\.py)|(\.rst)$'
        excluded_dirs = '^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path, ignore_dirs=excluded_dirs)[0]

        script_file_name = os.path.join('docs', 'source', 'render_examples.py')

        if self.latest_modified(source_path, filetypes=sources,
            ignore_dirs=excluded_dirs)[0] > target_time or \
            self.latest_modified(script_file_name)[0] > target_time or\
            not os.path.exists(
                os.path.join('docs', 'source', 'mayavi', 'auto',
                'examples.rst')):
            try:
                from enthought.mayavi import mlab
                from enthought.mayavi.tools import auto_doc
                print "Generating the example list"
                subprocess.call('python %s' %
                            os.path.basename(script_file_name), shell=True,
                            cwd=os.path.dirname(script_file_name))
            except:
                pass


    def run(self):
        self.mlab_reference()
        self.example_files()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

class BuildDocs(Command):

    description = \
        "This command generates the documentation by running Sphinx. " \
        "It then zips the docs into an html.zip file."

    user_options = [
        ('None', None, 'this command has no options'),
        ]


    def make_docs(self):
        if os.name == 'nt':
            print "Please impelemnt sphinx building on windows here."
        else:
            subprocess.call(['make', 'html'], cwd='docs')

    def zip_docs(self):
        zf = zipfile.ZipFile(DEFAULT_HTML_ZIP, 'w')

        for project in list_doc_projects():
            project_dir = os.path.join('docs', 'build', project, 'html')
            for root, dirs, files in os.walk(project_dir):
                relative_root = root[len(project_dir)+1:]
                for name in files:
                    src = os.path.join(root, name)
                    dest = os.path.join('html', project, relative_root, name)
                    zf.write(src, dest)

        zf.close()

    def run(self):
        self.make_docs()
        self.zip_docs()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


# Functions to generate the docs
def list_doc_projects():
    """ List the different source directories under DEFAULT_INPUT_DIR
        for which we have docs.
    """
    source_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        DEFAULT_INPUT_DIR)
    source_list = os.listdir(source_dir)
    # Check to make sure we're using non-hidden directories.
    source_dirs = [listing for listing in source_list
        if os.path.isdir(os.path.join(source_dir, listing))
        and not listing.startswith('.')]
    return source_dirs


def list_docs_data_files(project):
    """ List the files to add to a project by inspecting the
        documentation directory. This works only if called after the
        build step, as the files have to be built.

        returns a list of (install_dir, [data_files, ]) tuples.
    """
    project_target_dir = os.path.join(DEFAULT_HTML_TARGET_DIR, project)
    return_list = []
    for root, dirs, files in os.walk(project_target_dir, topdown=True):
        # Modify inplace the list of directories to walk
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if len(files) == 0:
            continue
        install_dir = root.replace(project_target_dir,
            os.path.join('enthought', project, 'html'))
        return_list.append(
            (install_dir, [os.path.join(root, f) for f in files]))
    return return_list


# Our custom distutils hooks
def build_tvtk_classes_zip():
    tvtk_dir = os.path.join('enthought', 'tvtk')
    sys.path.insert(0, tvtk_dir)
    from setup import gen_tvtk_classes_zip
    gen_tvtk_classes_zip()
    sys.path.remove(tvtk_dir)


class MyBuild(build.build):
    """ A build hook to generate the documentation.

        We sub-class numpy.distutils' build command because we're relying on
        numpy.distutils' setup method to build python extensions.

    """

    def run(self):
        build_tvtk_classes_zip()
        build.build.run(self)
        self.run_command('gen_docs')
        try:
            self.run_command('build_docs')
        except:
            log.warn("Couldn't build documentation:\n%s" %
                     traceback.format_exception(*sys.exc_info()))



class MyDevelop(develop.develop):
    """ A hook to have the docs rebuilt during develop.

        Subclassing setuptools' command because numpy.distutils doesn't
        have an implementation.

    """

    def run(self):
        self.run_command('gen_docs')
        try:
            self.run_command('build_docs')
        except:
            log.warn("Couldn't build documentation:\n%s" %
                     traceback.format_exception(*sys.exc_info()))

        # Make sure that the 'build_src' command will
        # always be inplace when we do a 'develop'.
        self.reinitialize_command('build_src', inplace=1)

        # tvtk_classes.zip always need to be created on 'develop'.
        build_tvtk_classes_zip()

        develop.develop.run(self)


class MyInstallData(install_data.install_data):
    """ An install hook to copy the generated documentation.

        We subclass numpy.distutils' command because we're relying on
        numpy.distutils' setup method to build python extensions.

    """

    def run(self):
        install_data_command = self.get_finalized_command('install_data')
        for project in list_doc_projects():
            install_data_command.data_files.extend(
                                    list_docs_data_files(project))

        # make sure tvtk_classes.zip always get created before putting it
        # in the install data.
        build_tvtk_classes_zip()
        tvtk_dir = os.path.join('enthought', 'tvtk')
        install_data_command.data_files.append(
            (tvtk_dir, [os.path.join(tvtk_dir, 'tvtk_classes.zip')]))

        install_data.install_data.run(self)


class MyInstallScripts(install_scripts.install_scripts):
    """ Hook to rename the  mayavi script to a MayaVi.pyw script on win32.

        Subclassing setuptools' command because numpy.distutils doesn't
        have an implementation.

    """

    def run(self):
        install_scripts.install_scripts.run(self)
        if os.name != 'posix':
            # Rename <script> to <script>.pyw. Executable bits
            # are already set in install_scripts.run().
            for file in self.get_outputs():
                if file[-4:] != '.pyw':
                    if file[-7:] == 'mayavi2':
                        new_file = file[:-7] + 'MayaVi2.pyw'
                    else:
                        new_file = os.path.splitext(file)[0] + '.pyw'
                    self.announce("renaming %s to %s" % (file, new_file))
                    if not self.dry_run:
                        if os.path.exists(new_file):
                            os.remove (new_file)
                        os.rename (file, new_file)


# Configure our extensions to Python
def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )

    config.add_subpackage('enthought.tvtk')
    config.add_subpackage('enthought')
    config.add_data_dir('enthought/mayavi/core/lut')
    config.add_data_dir('enthought/mayavi/tests/data')
    config.add_data_dir('enthought/mayavi/tests/csv_files')

    # Image files.
    for root, dirs, files in os.walk('enthought'):
        if os.path.split(root)[-1] == 'images':
            config.add_data_dir(root)

    # *.ini files.
    config.add_data_dir('enthought/tvtk/plugins/scene')
    config.add_data_dir('enthought/mayavi/preferences')

    # The mayavi documentation.
    # Take a peak at the zip file to know which path to add:
    zip = zipfile.ZipFile(DEFAULT_HTML_ZIP)
    return config

################################################################################
# Similar to package_data, but installed before build
build_package_data = {'enthought.mayavi.images':
                            ['docs/source/mayavi/m2_about.jpg']}

# Instal our data files at build time. This is iffy,
# but we need to do this before distutils kick in.
for package, files in build_package_data.iteritems():
    target_path = package.replace('.', os.sep)
    for filename in files:
        shutil.copy(filename, target_path)
################################################################################

# Build the full set of packages by appending any found by setuptools'
# find_packages to those discovered by numpy.distutils.
config = configuration().todict()
packages = setuptools.find_packages(exclude=config['packages'] +
    ['docs', 'examples'])
config['packages'] += packages


# The actual setup call
DOCLINES = __doc__.split("\n")
numpy.distutils.core.setup(
    author = "Prabhu Ramachandran, et. al.",
    author_email = "prabhu@aero.iitb.ac.in",
    classifiers = [c.strip() for c in """\
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        Intended Audience :: Science/Research
        License :: OSI Approved :: BSD License
        Operating System :: MacOS
        Operating System :: Microsoft :: Windows
        Operating System :: OS Independent
        Operating System :: POSIX
        Operating System :: Unix
        Programming Language :: C
        Programming Language :: Python
        Topic :: Scientific/Engineering
        Topic :: Software Development
        Topic :: Software Development :: Libraries
        """.splitlines() if len(c.split()) > 0],
    cmdclass = {
        # Work around a numpy distutils bug by forcing the use of the
        # setuptools' sdist command.
        'sdist': setuptools.command.sdist.sdist,
        'build': MyBuild,
        'develop': MyDevelop,
        'install_scripts': MyInstallScripts,
        'install_data': MyInstallData,
        'gen_docs': GenDocs,
        'build_docs': BuildDocs,
        },
    description = DOCLINES[1],
    docs_in_egg = True,
    docs_in_egg_location = 'enthought/docs',
    download_url = ('http://www.enthought.com/repo/ETS/Mayavi-%s.tar.gz' %
        INFO['version']),
    entry_points = {
        'console_scripts': [
            'mayavi2 = enthought.mayavi.scripts.mayavi2:main',
            'tvtk_doc = enthought.tvtk.tools.tvtk_doc:main'
            ],

        'enthought.envisage.plugins': [
            'enthought.tvtk.scene = enthought.tvtk.plugins.scene.scene_plugin:ScenePlugin',
            'enthought.tvtk.scene_ui = enthought.tvtk.plugins.scene.ui.scene_ui_plugin:SceneUIPlugin',
            'enthought.tvtk.browser = enthought.tvtk.plugins.browser.browser_plugin:BrowserPlugin',
            'enthought.mayavi = enthought.mayavi.plugins.mayavi_plugin:MayaviPlugin',
            'enthought.mayavi_ui = enthought.mayavi.plugins.mayavi_ui_plugin:MayaviUIPlugin'
            ],
        },
    extras_require = INFO['extras_require'],
    html_doc_repo = 'https://svn.enthought.com/svn/cec/trunk/projects/mayavi/docs/development/',
    include_package_data = True,
    install_requires = INFO['install_requires'],
    license = "BSD",
    long_description = '\n'.join(DOCLINES[3:]),
    maintainer = 'ETS Developers',
    maintainer_email = 'enthought-dev@enthought.com',
    name = INFO['name'],
    namespace_packages = [
        "enthought",
        ],
    platforms = ["Windows", "Linux", "Mac OS-X", "Unix", "Solaris"],
    ssh_server = 'code.enthought.com',
    ssh_remote_dir = '/www/htdocs/code.enthought.com/projects/mayavi/',
    tests_require = [
        'nose >= 0.10.3',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/projects/mayavi/',
    version = INFO['version'],
    zip_safe = False,
    **config
)
