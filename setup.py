#!/usr/bin/env python
#
# Copyright (c) 2008-2022 by Enthought, Inc.
# All rights reserved.

from setuptools import Command, Extension, setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.install import install

import os
import time
import subprocess
import shutil
import re
import sys
from os.path import (abspath, basename, dirname, exists, getmtime, isdir,
                     join, split)
from pathlib import Path

from tvtk._setup import can_compile_extensions, gen_tvtk_classes_zip  # noqa

MY_DIR = os.path.dirname(__file__)
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
        """Traverse a path looking for the most recently modified file.

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
        """If mayavi is installed, run the mlab_reference generator."""
        # XXX: This is really a hack: the script is not made to be used
        # for different projects, but it ended up being. This part is
        # mayavi-specific.

        mlab_ref_dir = join(DEFAULT_INPUT_DIR, 'mayavi', 'auto')

        source_path = 'mayavi'
        sources = r'(\.py)|(\.rst)$'
        excluded_dirs = r'^\.'
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
            except Exception:
                pass

    def example_files(self):
        """Generate the documentation files for the examples."""
        mlab_ref_dir = join(DEFAULT_INPUT_DIR, 'mayavi', 'auto')

        source_path = join('examples', 'mayavi')
        sources = r'(\.py)|(\.rst)$'
        excluded_dirs = r'^\.'
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
    source_dir = join(abspath(MY_DIR), DEFAULT_INPUT_DIR)
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


def _tvtk_built_recently(zipfile, delay):
    """Returns True if the TVTK classes in zipfile was built in the last
    delay seconds.
    """
    if not os.path.exists(zipfile):
        return False

    ctime = os.stat(zipfile).st_ctime
    tdiff = time.time() - ctime
    return tdiff < delay


# Our custom distutils hooks
def build_tvtk_classes_zip():
    zipfile = os.path.join(MY_DIR, 'tvtk', 'tvtk_classes.zip')
    if _tvtk_built_recently(zipfile, delay=120):
        print("Already built tvtk_classes.zip")
        return
    else:
        print("Building tvtk_classes.zip")
    gen_tvtk_classes_zip()


class MyBuildPy(build_py):
    """A build hook to generate the documentation."""

    def run(self):
        build_tvtk_classes_zip()
        super().run()


class MyDevelop(develop):
    """A hook to build the TVTK ZIP file on develop."""

    def run(self):
        build_tvtk_classes_zip()
        super().run()


###########################################################################
# Similar to package_data, but installed before build
build_package_data = {'mayavi.images': ['docs/source/mayavi/_static/m2_about.jpg']}

# Install our data files at build time. This is iffy,
# but we need to do this before distutils kicks in.
for package, files in build_package_data.items():
    target_path = package.replace('.', os.sep)
    for filename in files:
        shutil.copy(filename, target_path)

try:
    import numpy as np
except Exception:
    HAS_NUMPY = False
else:
    HAS_NUMPY = True
if not HAS_NUMPY and MODE != 'info':
    msg = '''
    Numpy is required to build Mayavi correctly, please install it first.
    '''
    print('*'*80)
    print(msg)
    print('*'*80)
    raise RuntimeError(msg)

###########################################################################

# The actual setup call
if __name__ == '__main__':
    ext_modules = list()
    packages = find_packages(exclude=["docs", "examples"])
    packages += [  # otherwise we get warnings. Maybe these should be excluded?
        "mayavi.core.images",
        "mayavi.core.ui.images",
        "mayavi.images",
        "mayavi.preferences.images",
        "mayavi.tests.csv_files",
        "mayavi.tests.data",
        "mayavi.tools.static.x3d",
        "tvtk.pipeline.images",
        "tvtk.pyface.images",
        "tvtk.src",
        "tvtk.tools.images",
    ]
    if can_compile_extensions():
        import numpy as np
        ext_modules.append(
            Extension(
                "tvtk.array_ext",
                sources=[join("tvtk", "src", "array_ext.c")],
                depends=[join("tvtk", "src", "array_ext.pyx")],
                include_dirs=[np.get_include()],
            )
        )

    setup(
        name='mayavi',
        version=info['__version__'],
        author="Prabhu Ramachandran, et al.",
        author_email="prabhu@aero.iitb.ac.in",
        maintainer='ETS Developers',
        python_requires='>=3.9',
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
            'build_py': MyBuildPy,
            'develop': MyDevelop,
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
        packages=packages,
        include_package_data=True,
        package_data={"tvtk": ["tvtk_classes.zip"]},
        ext_modules=ext_modules,
        install_requires=info['__requires__'],
        license="BSD",
        long_description=Path('README.rst').read_text(encoding='utf-8'),
        platforms=["Windows", "Linux", "Mac OS-X", "Unix", "Solaris"],
        zip_safe=False,
    )
