#!/usr/bin/env python
#
# Copyright (c) 2008-2020 by Enthought, Inc.
# All rights reserved.

# NOTE: Setuptools must be imported BEFORE numpy.distutils or else
# numpy.distutils does the Wrong(TM) thing.
import setuptools
from setuptools import Command

try:
    import numpy
    from numpy.distutils.command import build, install_data
    from numpy.distutils.core import setup
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    from distutils.command import build, install_data
    from distutils.core import setup
import io
import os
import subprocess
import shutil
import re
import sys
import traceback
from os.path import (abspath, basename, dirname, exists, getmtime, isdir,
                     join, split)

from distutils.command import clean
from distutils import log
from setuptools.command import develop


MODE = 'normal'
if len(sys.argv) >= 2 and \
   ('--help' in sys.argv[1:] or
    sys.argv[1] in ('--help-commands', 'egg_info', '--version',
                    'clean', 'sdist')):
    MODE = 'info'

info = {}
fname = join('mayavi', '__init__.py')
exec(compile(open(fname).read(), fname, 'exec'), info)

DEFAULT_HTML_TARGET_DIR = join('docs', 'build')
DEFAULT_INPUT_DIR = join('docs', 'source',)


class GenDocs(Command):

    description = (
        "This command generates generated part of the documentation "
        "when needed. It's run automatically before a build_docs, and that's "
        "the only time it needs to be run."
    )
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

        if not exists(the_path):
            return 0, the_path
        if isdir(the_path):
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
                    current_file_time = getmtime(join(root, file))
                    if current_file_time > latest_time:
                        latest_time = current_file_time
                        latest_path = join(root, file)
            return latest_time, latest_path

        else:
            return getmtime(the_path), the_path

    def mlab_reference(self):
        """ If mayavi is installed, run the mlab_reference generator.
        """
        # XXX: This is really a hack: the script is not made to be used
        # for different projects, but it ended up being. This part is
        # mayavi-specific.

        mlab_ref_dir = join(DEFAULT_INPUT_DIR, 'mayavi', 'auto')

        source_path = 'mayavi'
        sources = '(\.py)|(\.rst)$'
        excluded_dirs = '^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path,
                                           ignore_dirs=excluded_dirs)[0]

        if (self.latest_modified(source_path, filetypes=sources,
                                 ignore_dirs=excluded_dirs)[0] > target_time
            or self.latest_modified('mlab_reference.py')[0] > target_time
            or not exists(join('docs', 'source', 'mayavi', 'auto',
                               'mlab_reference.rst'))):
            try:
                from mayavi import mlab
                from mayavi.tools import auto_doc
                print("Generating the mlab reference documentation")
                os.system('python mlab_reference.py')
            except:
                pass

    def example_files(self):
        """ Generate the documentation files for the examples.
        """
        mlab_ref_dir = join(DEFAULT_INPUT_DIR, 'mayavi', 'auto')

        source_path = join('examples', 'mayavi')
        sources = '(\.py)|(\.rst)$'
        excluded_dirs = '^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path,
                                           ignore_dirs=excluded_dirs)[0]

        script_file_name = join('docs', 'source', 'render_examples.py')

        if (self.latest_modified(source_path, filetypes=sources,
                                 ignore_dirs=excluded_dirs)[0] > target_time
            or  self.latest_modified(script_file_name)[0] > target_time
            or not  exists(join('docs', 'source', 'mayavi', 'auto',
                                'examples.rst'))
            ):
            try:
                from mayavi import mlab
                from mayavi.tools import auto_doc
                print("Generating the example list")
                subprocess.call('python %s' %
                                basename(script_file_name), shell=True,
                                cwd=dirname(script_file_name))
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
            print("Please impelemnt sphinx building on windows here.")
        else:
            subprocess.call(['make', 'html'], cwd='docs')

    def run(self):
        self.make_docs()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


# Functions to generate the docs
def list_doc_projects():
    """ List the different source directories under DEFAULT_INPUT_DIR
        for which we have docs.
    """
    source_dir = join(abspath(dirname(__file__)),
                      DEFAULT_INPUT_DIR)
    source_list = os.listdir(source_dir)
    # Check to make sure we're using non-hidden directories.
    source_dirs = [listing for listing in source_list
                   if isdir(join(source_dir, listing))
                   and not listing.startswith('.')]
    return source_dirs


def list_docs_data_files(project):
    """ List the files to add to a project by inspecting the
        documentation directory. This works only if called after the
        build step, as the files have to be built.

        returns a list of (install_dir, [data_files, ]) tuples.
    """
    project_target_dir = join(DEFAULT_HTML_TARGET_DIR, project, 'html')
    return_list = []
    for root, dirs, files in os.walk(project_target_dir, topdown=True):
        # Modify inplace the list of directories to walk
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if len(files) == 0:
            continue
        install_dir = root.replace(project_target_dir, join(project, 'html'))
        return_list.append((install_dir, [join(root, f) for f in files]))
    return return_list


# Our custom distutils hooks
def build_tvtk_classes_zip():
    MY_DIR = os.path.dirname(__file__)
    sys.path.insert(0, MY_DIR)
    import tvtk
    tvtk_dir = 'tvtk'
    sys.path.insert(0, tvtk_dir)
    from setup import gen_tvtk_classes_zip
    gen_tvtk_classes_zip()
    sys.path.remove(tvtk_dir)
    sys.path.remove(MY_DIR)


class MyBuild(build.build):
    """ A build hook to generate the documentation.

        We sub-class numpy.distutils' build command because we're relying on
        numpy.distutils' setup method to build python extensions.

    """

    def run(self):
        build_tvtk_classes_zip()
        build.build.run(self)
        try:
            self.run_command('gen_docs')
        except:
            log.warn("Couldn't generate documentation:\n%s" %
                     traceback.format_exception(*sys.exc_info()))
        try:
            self.run_command('build_docs')
        except:
            log.warn("Couldn't build documentation:\n%s" %
                     traceback.format_exception(*sys.exc_info()))


class MyDevelop(develop.develop):
    """ A hook to build the TVTK ZIP file on develop.

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
        for project in list_doc_projects():
            install_data_command.data_files.extend(
                                    list_docs_data_files(project))

        # make sure tvtk_classes.zip always get created before putting it
        # in the install data.
        build_tvtk_classes_zip()
        tvtk_dir = 'tvtk'
        install_data_command.data_files.append(
            (tvtk_dir, [join(tvtk_dir, 'tvtk_classes.zip')]))

        install_data.install_data.run(self)


class MyClean(clean.clean):
    """Reimplements to remove the extension module array_ext to guarantee a
    fresh rebuild every time. The module hanging around could introduce
    problems when doing develop for a different vtk version."""
    def run(self):
        MY_DIR = os.path.dirname(__file__)

        ext_file = os.path.join(
            MY_DIR,
            "tvtk",
            "array_ext" + (".pyd" if sys.platform == "win32" else ".so")
        )

        if os.path.exists(ext_file):
            print("Removing in-place array extensions {}".format(ext_file))
            os.unlink(ext_file)

        clean.clean.run(self)


# Configure our extensions to Python
def configuration(parent_package=None, top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )

    config.add_subpackage('tvtk')
    config.add_data_dir('mayavi/core/lut')
    config.add_data_dir('mayavi/tests/data')
    config.add_data_dir('mayavi/tests/csv_files')
    config.add_data_dir('mayavi/tools/static')

    # Image files.
    for pkgdir in ('mayavi', 'tvtk'):
        for root, dirs, files in os.walk(pkgdir):
            if split(root)[-1] == 'images':
                config.add_data_dir(root)

    # *.ini files.
    config.add_data_dir('tvtk/plugins/scene')
    config.add_data_dir('mayavi/preferences')

    return config


###########################################################################
# Similar to package_data, but installed before build
build_package_data = {'mayavi.images': ['docs/source/mayavi/_static/m2_about.jpg']}

# Install our data files at build time. This is iffy,
# but we need to do this before distutils kicks in.
for package, files in build_package_data.items():
    target_path = package.replace('.', os.sep)
    for filename in files:
        shutil.copy(filename, target_path)
###########################################################################

# Build the full set of packages by appending any found by setuptools'
# find_packages to those discovered by numpy.distutils.
if HAS_NUMPY:
    config = configuration().todict()
else:
    # This is just a dummy so the egg_info command works.
    config = {'packages': []}
packages = setuptools.find_packages(exclude=config['packages'] +
                                    ['docs', 'examples'])
config['packages'] += packages


if MODE != 'info' and not HAS_NUMPY:
    msg = '''
    Numpy is required to build Mayavi correctly, please install it first.
    '''
    print('*'*80)
    print(msg)
    print('*'*80)
    raise RuntimeError(msg)


# The actual setup call
if __name__ == '__main__':
    setup(
        name='mayavi',
        version=info['__version__'],
        author="Prabhu Ramachandran, et al.",
        author_email="prabhu@aero.iitb.ac.in",
        maintainer='ETS Developers',
        maintainer_email='mayavi-users@lists.sf.net',
        url='http://docs.enthought.com/mayavi/mayavi/',
        classifiers=[c.strip() for c in """\
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
        cmdclass={
            # Work around a numpy distutils bug by forcing the use of the
            # setuptools' sdist command.
            'sdist': setuptools.command.sdist.sdist,
            'build': MyBuild,
            'clean': MyClean,
            'develop': MyDevelop,
            'install_data': MyInstallData,
            'gen_docs': GenDocs,
            'build_docs': BuildDocs,
            },
        description='3D scientific data visualization library and application',
        download_url=('https://www.github.com/enthought/mayavi'),
        entry_points={
            'gui_scripts': [
                'mayavi2 = mayavi.scripts.mayavi2:main',
                'tvtk_doc = tvtk.tools.tvtk_doc:main'
                ],
            'envisage.plugins': [
                'tvtk.scene = tvtk.plugins.scene.scene_plugin:ScenePlugin',
                'tvtk.scene_ui = tvtk.plugins.scene.ui.scene_ui_plugin:SceneUIPlugin',
                'tvtk.browser = tvtk.plugins.browser.browser_plugin:BrowserPlugin',
                'mayavi = mayavi.plugins.mayavi_plugin:MayaviPlugin',
                'mayavi_ui = mayavi.plugins.mayavi_ui_plugin:MayaviUIPlugin'
                ],
            'tvtk.toolkits': [
                'qt4 = tvtk.pyface.ui.qt4.init:toolkit_object',
                'qt = tvtk.pyface.ui.qt4.init:toolkit_object',
                'wx = tvtk.pyface.ui.wx.init:toolkit_object',
                'null = tvtk.pyface.ui.null.init:toolkit_object',
            ]
        },
        extras_require=info['__extras_require__'],
        include_package_data=True,
        install_requires=info['__requires__'],
        license="BSD",
        long_description=io.open('README.rst', encoding='utf-8').read(),
        platforms=["Windows", "Linux", "Mac OS-X", "Unix", "Solaris"],
        zip_safe=False,
        **config
    )
