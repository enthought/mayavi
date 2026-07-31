#!/usr/bin/env python
#
# Copyright (c) Enthought, Inc.
# All rights reserved.

from setuptools import Command, Distribution, setup
from setuptools.command.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop

import os
import sys
import time
import subprocess
import shutil
import re
from pathlib import Path

# NOTE: tvtk is imported lazily inside the build hooks below, not at module
# scope, so that metadata/sdist builds (which do not generate the TVTK ZIP)
# do not require tvtk to be importable.

MY_DIR = Path(__file__).resolve().parent

# The PEP 517 ``setuptools.build_meta`` backend does not put the source
# directory on sys.path (only the legacy ``:__legacy__`` variant does), so the
# in-tree ``tvtk`` package that the build hooks below import would not be
# importable during a build.  Put it on sys.path explicitly.
if str(MY_DIR) not in sys.path:
    sys.path.insert(0, str(MY_DIR))

DEFAULT_HTML_TARGET_DIR = Path('docs', 'build')
DEFAULT_INPUT_DIR = Path('docs', 'source')


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
        the_path : path-like
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
        latest_path : Path
            Most recently modified file.
        """
        the_path = Path(the_path)
        file_re = re.compile(filetypes)
        dir_re = re.compile(ignore_dirs)

        if not the_path.exists():
            return 0, the_path
        if the_path.is_dir():
            latest_time = 0
            latest_path = the_path
            # os.walk (rather than Path.rglob) so that ignored directories can
            # be pruned from the traversal in place
            for root, dirs, files in os.walk(the_path):
                root = Path(root)
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
                    current_file_time = (root / file).stat().st_mtime
                    if current_file_time > latest_time:
                        latest_time = current_file_time
                        latest_path = root / file
            return latest_time, latest_path

        else:
            return the_path.stat().st_mtime, the_path

    def mlab_reference(self):
        """If mayavi is installed, run the mlab_reference generator."""
        # XXX: This is really a hack: the script is not made to be used
        # for different projects, but it ended up being. This part is
        # mayavi-specific.

        mlab_ref_dir = DEFAULT_INPUT_DIR / 'mayavi' / 'auto'

        source_path = Path('mayavi')
        sources = r'(\.py)|(\.rst)$'
        excluded_dirs = r'^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path,
                                           ignore_dirs=excluded_dirs)[0]

        if (self.latest_modified(source_path, filetypes=sources,
                                 ignore_dirs=excluded_dirs)[0] > target_time
            or self.latest_modified('mlab_reference.py')[0] > target_time
                or not (mlab_ref_dir / 'mlab_reference.rst').exists()):
            try:
                from mayavi import mlab
                from mayavi.tools import auto_doc
                print("Generating the mlab reference documentation")
                os.system('python mlab_reference.py')
            except Exception:
                pass

    def example_files(self):
        """Generate the documentation files for the examples."""
        mlab_ref_dir = DEFAULT_INPUT_DIR / 'mayavi' / 'auto'

        source_path = Path('examples', 'mayavi')
        sources = r'(\.py)|(\.rst)$'
        excluded_dirs = r'^\.'
        target_path = mlab_ref_dir
        target_time = self.latest_modified(target_path,
                                           ignore_dirs=excluded_dirs)[0]

        script_file_name = DEFAULT_INPUT_DIR / 'render_examples.py'

        if (self.latest_modified(source_path, filetypes=sources,
                                 ignore_dirs=excluded_dirs)[0] > target_time
            or self.latest_modified(script_file_name)[0] > target_time
                or not (mlab_ref_dir / 'examples.rst').exists()):
            try:
                from mayavi import mlab
                from mayavi.tools import auto_doc
                print("Generating the example list")
                subprocess.call('python %s' % script_file_name.name,
                                shell=True, cwd=script_file_name.parent)
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


def _tvtk_built_recently(zipfile, delay):
    """Returns True if the TVTK classes in zipfile was built in the last
    delay seconds.
    """
    if not zipfile.exists():
        return False

    ctime = zipfile.stat().st_ctime
    tdiff = time.time() - ctime
    return tdiff < delay


# Our custom distutils hooks
def build_tvtk_classes_zip():
    zipfile = MY_DIR / 'tvtk' / 'tvtk_classes.zip'
    if _tvtk_built_recently(zipfile, delay=120):
        print("Already built tvtk_classes.zip")
        return
    else:
        print("Building tvtk_classes.zip")
    from tvtk._setup import gen_tvtk_classes_zip
    gen_tvtk_classes_zip()


class MyBuildPy(build_py):
    """Build hook that generates ``tvtk_classes.zip`` and stages it into the
    build output.

    The ZIP is generated at build time from the installed VTK and is excluded
    from the sdist, so it cannot be collected as ordinary package data (it does
    not exist when the manifest is computed).  ``gen_tvtk_classes_zip`` writes
    it into the source tree next to the ``tvtk`` package, so copy it from there
    into ``build_lib`` explicitly; ``bdist_wheel`` then packages the whole tree.

    For editable installs the source tree *is* the install, so the ZIP written
    by ``build_tvtk_classes_zip`` is already in the right place and the copy
    below is a no-op as far as the installed package is concerned.
    """

    def run(self):
        build_tvtk_classes_zip()
        super().run()
        src = MY_DIR / 'tvtk' / 'tvtk_classes.zip'
        dst = Path(self.build_lib) / 'tvtk' / 'tvtk_classes.zip'
        self.mkpath(str(dst.parent))
        self.copy_file(str(src), str(dst))


class MyDevelop(develop):
    """A hook to build the TVTK ZIP file on develop."""

    def run(self):
        build_tvtk_classes_zip()
        super().run()


class MyDistribution(Distribution):
    """Claim ext modules so the whole build/install/wheel path uses the
    platlib layout: the code is pure Python, but the generated TVTK classes
    are platform-specific (X11 vs Cocoa vs Win32)."""

    def has_ext_modules(self):
        return True


class MyBdistWheel(bdist_wheel):
    """Tag wheels py3-none-<platform> (pure Python, platform-specific)."""

    def get_tag(self):
        _, _, plat = super().get_tag()
        # PyPI rejects plain linux_* tags; with no native code any glibc
        # floor is valid, so use manylinux_2_17 (understood by pip >= 20.3)
        if plat.startswith('linux_'):
            plat = plat.replace('linux_', 'manylinux_2_17_', 1)
        return 'py3', 'none', plat


###########################################################################
# Similar to package_data, but installed before build
build_package_data = {
    'mayavi.images': [DEFAULT_INPUT_DIR / 'mayavi' / '_static' / 'm2_about.jpg']
}

# Install our data files at build time. This is iffy,
# but we need to do this before distutils kicks in.
for package, files in build_package_data.items():
    target_path = Path(*package.split('.'))
    for filename in files:
        shutil.copy(filename, target_path)

###########################################################################

# Dependencies are dynamic (PEP 643): tvtk_classes.zip bakes in the
# build-time VTK API.  Older runtimes degrade gracefully but newer ones may
# remove API the generated code references, so wheels cap VTK at the next
# minor.  The sdist generates against the installer's VTK, so no cap.
DEPENDENCIES = [
    'apptools',
    'configobj',
    'envisage',
    'numpy',
    'pyface>=6.1.1',
    'pygments',  # only needed for the Qt backend but we add it anyway
    'traits>=6.0.0',
    'traitsui>=7.0.0',
    'packaging',
    "importlib_resources; python_version<'3.11'",
    'puremagic',
]


# Oldest supported VTK, per SPEC 0-style two-year support window.  When
# raising this, cull the workarounds it makes dead -- see tvtk/WORKAROUNDS.md.
MIN_VTK = '9.4'
# First VTK the generated wrappers are *not* known to work with.  Raise it
# once the vtk-dev CI row has been green against that version's prereleases.
MAX_VTK = '9.8'


def vtk_requirement():
    """The VTK requirement, with an upper bound when building a wheel."""
    if 'sdist' in sys.argv[1:]:
        return 'vtk>=%s' % MIN_VTK
    return 'vtk>=%s,<%s' % (MIN_VTK, MAX_VTK)


# Static metadata lives in pyproject.toml; setup.py carries only the dynamic
# dependencies and the imperative build hooks.
if __name__ == '__main__':
    setup(
        distclass=MyDistribution,
        cmdclass={
            'bdist_wheel': MyBdistWheel,
            'build_py': MyBuildPy,
            'develop': MyDevelop,
            'gen_docs': GenDocs,
            'build_docs': BuildDocs,
        },
        install_requires=DEPENDENCIES + [vtk_requirement()],
    )
