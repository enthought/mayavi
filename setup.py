#!/usr/bin/env python
#
# Copyright (c) 2008 by Enthought, Inc.
# All rights reserved.
#

"""
The MayaVi scientific data 3-dimensional visualizer.

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

"""


# NOTE: Setuptools must be imported BEFORE numpy.distutils or else
# numpy.distutils does the Wrong(TM) thing.
import setuptools


from distutils.command.clean import clean
from make_docs import HtmlBuild, DEFAULT_HTML_ZIP, DEFAULT_HTML_TARGET_DIR, \
    DEFAULT_INPUT_DIR
from numpy.distutils import log
from numpy.distutils.command.build import build as distbuild
from numpy.distutils.command.install_data import install_data
from numpy.distutils.core import setup
from pkg_resources import DistributionNotFound, parse_version, require, \
    VersionConflict
from setuptools.command.develop import develop
from setuptools.command.install_scripts import install_scripts
from traceback import print_exc
import os
import shutil
import zipfile

# FIXME: This works around a setuptools bug which gets setup_data.py metadata
# from incorrect packages. Ticket #1592
#from setup_data import INFO
setup_data = dict(__name__='', __file__='setup_data.py')
execfile('setup_data.py', setup_data)
INFO = setup_data['INFO']

##############################################################################
# Pull the description values for the setup keywords from our file docstring.
##############################################################################
DOCLINES = __doc__.split("\n")


##############################################################################
# Functions to generate the docs
##############################################################################
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

def generate_docs(project):
    """ Generate the documentation, whether that be using
        Sphinx or by unzipping it.
    """
    project_target_dir = os.path.join(DEFAULT_HTML_TARGET_DIR, project)

    required_sphinx_version = "0.4.1"
    sphinx_installed = False
    try:
        require("Sphinx>=%s" % required_sphinx_version)
        sphinx_installed = True
    except (DistributionNotFound, VersionConflict):
        log.warn('Sphinx install of version %s could not be verified.'
            ' Trying simple import...' % required_sphinx_version)
        try:
            import sphinx
            if parse_version(sphinx.__version__) < parse_version(
                required_sphinx_version):
                log.error("Sphinx version must be >=%s." %\
                    required_sphinx_version)
            if False:
                pass
            else:
                sphinx_installed = True
        except ImportError:
            log.error("Sphinx install not found.")

    if sphinx_installed:
        log.info("Generating %s documentation..." % project)

        try:
            build = HtmlBuild()
            build.start({
                'commit_message': None,
                'preserve_temp': True,
                'subversion': False,
                'verbose': True,
                'versioned': False,
                'target':
                    os.path.join(DEFAULT_HTML_TARGET_DIR, project),
                'doc_source':
                    os.path.join(DEFAULT_INPUT_DIR, project),
                }, [])
            del build

        except:
            print_exc()
            log.error("The documentation generation failed.  Falling back to "
                "the zip file.")

            # Unzip the docs into the 'html' folder.
            unzip_html_docs(DEFAULT_HTML_ZIP % project,
                os.path.join(DEFAULT_HTML_TARGET_DIR, project))
    else:
        # Unzip the docs into the 'html' folder.
        log.info("Installing %s documentation from zip file.\n" % project)
        unzip_html_docs(DEFAULT_HTML_ZIP % project, project_target_dir)

def unzip_html_docs(src_path, dest_dir):
    """ Given a path to a zipfile, extract its contents to a given 'dest_dir'.
    """
    file = zipfile.ZipFile(src_path)
    for name in file.namelist():
        cur_name = os.path.join(dest_dir, name)
        cur_name = cur_name.replace('/', os.sep)
        if not os.path.exists(os.path.dirname(cur_name)):
            os.makedirs(os.path.dirname(cur_name))
        if not cur_name.endswith(os.sep):
            out = open(cur_name, 'wb')
            out.write(file.read(name))
            out.flush()
            out.close()
    file.close()

def list_docs_data_files(project):
    """ List the files to add to a project by inspecting the
        documentation directory. This works only if called after the
        build step, as the files have to be builts.

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


##############################################################################
# Our custom distutils hooks
##############################################################################
class my_develop(develop):
    """ A hook to have the docs rebuilt during develop.
    """
    def run(self):
        for project in list_doc_projects():
            generate_docs(project)

        # Make sure that the 'build_src' command will
        # always be inplace when we do a 'develop'.
        self.reinitialize_command('build_src', inplace=1)
        develop.run(self)


class my_build(distbuild):
    """ A build hook to generate the documentation.
    """
    def run(self):
        for project in list_doc_projects():
            generate_docs(project)
        distbuild.run(self)


class my_install_data(install_data):
    """ An install hook to copy the generated documentation.
    """
    def run(self):
        install_data_command = self.get_finalized_command('install_data')
        for project in list_doc_projects():
            install_data_command.data_files.extend(
                                    list_docs_data_files(project))
        install_data.run(self)


class my_clean(clean):
    """ A hook to remove the generated documentation when cleaning.
    """
    def run(self):
        clean.run(self)
        if os.path.exists(DEFAULT_HTML_TARGET_DIR):
            log.info("Removing '%s' (and everything under it)" %
                                            DEFAULT_HTML_TARGET_DIR)
            shutil.rmtree(DEFAULT_HTML_TARGET_DIR)


class my_install_scripts(install_scripts):
    """ Hook to rename the  mayavi script to a MayaVi.pyw script on win32.
    """
    def run(self):
        install_scripts.run(self)
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


##############################################################################
# Configure our extensions to Python
##############################################################################
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

    # Image files.
    for root, dirs, files in os.walk('enthought'):
        if os.path.split(root)[-1] == 'images':
            config.add_data_dir(root)

    # *.ini files.
    config.add_data_dir('enthought/tvtk/plugins/scene')
    config.add_data_dir('enthought/mayavi/preferences')

    # The mayavi documentation.
    # Take a peak at the zip file to know which path to add:
    zip = zipfile.ZipFile(DEFAULT_HTML_ZIP % 'mayavi')
    return config


# Build the full set of packages by appending any found by setuptools'
# find_packages to those discovered by numpy.distutils.
config = configuration().todict()
packages = setuptools.find_packages(exclude=config['packages'] +
    ['docs', 'examples'])
config['packages'] += packages


##############################################################################
# The actual setup call
##############################################################################
setup(
    author = "Prabhu Ramachandran, et. al.",
    author_email = "prabhu_r@users.sf.net",
    classifiers = [c.strip() for c in """\
        Development Status :: 4 - Beta
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

        'install_scripts': my_install_scripts,
        'install_data': my_install_data,
        'build': my_build,
        'develop': my_develop,
        'clean': my_clean,
        },
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = DOCLINES[1],
    entry_points = {
        'console_scripts': [
            'mayavi2 = enthought.mayavi.scripts.mayavi2:main',
            'tvtk_doc = enthought.tvtk.tools.tvtk_doc:main'
            ],

        'enthought.envisage.plugins': [
            'scene = enthought.tvtk.plugins.scene.scene_plugin:ScenePlugin',
            'scene_ui = enthought.tvtk.plugins.scene.ui.scene_ui_plugin:SceneUIPlugin',
            'browser = enthought.tvtk.plugins.browser.browser_plugin:BrowserPlugin',
            'mayavi = enthought.mayavi.plugins.mayavi_plugin:MayaviPlugin',
            'mayavi_ui = enthought.mayavi.plugins.mayavi_ui_plugin:MayaviUIPlugin'
            ],
        },
    extras_require = INFO['extras_require'],
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
    tests_require = [
        'nose >= 0.10.3',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/projects/mayavi/',
    version = INFO['version'],
    zip_safe = False,
    **config
    )

