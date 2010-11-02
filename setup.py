#!/usr/bin/env python
#
# Copyright (c) 2008-2010 by Enthought, Inc.
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


class MyDevelop(develop.develop):
    """ A hook to have the docs rebuilt during develop.

        Subclassing setuptools' command because numpy.distutils doesn't
        have an implementation.

    """

    def run(self):
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
    setup_requires = 'setupdocs>=1.0',
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
