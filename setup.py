#!/usr/bin/env python
#
# Copyright (c) 2008-2022 by Enthought, Inc.
# All rights reserved.

from setuptools import Command, setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop

import os
import time
import subprocess
import shutil
import re
from os.path import basename, dirname, exists, getmtime, isdir, join

# NOTE: tvtk is imported lazily inside the build hooks below, not at module
# scope, so that metadata/sdist builds (which do not generate the TVTK ZIP)
# do not require tvtk to be importable.

MY_DIR = os.path.dirname(__file__)

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
    from tvtk._setup import gen_tvtk_classes_zip
    gen_tvtk_classes_zip()


class MyBuildPy(build_py):
    """Build hook that generates ``tvtk_classes.zip`` and stages it into the
    build output.

    The ZIP is generated at build time from the installed VTK and is excluded
    from the sdist, so it cannot be collected as ordinary package data (it does
    not exist when the manifest is computed).  ``gen_tvtk_classes_zip`` writes
    it next to the imported ``tvtk`` package, so copy it from there into
    ``build_lib`` explicitly; ``bdist_wheel`` then packages the whole tree.
    """

    def run(self):
        build_tvtk_classes_zip()
        super().run()
        import tvtk._setup
        src = os.path.join(os.path.dirname(tvtk._setup.__file__),
                           'tvtk_classes.zip')
        dst = os.path.join(self.build_lib, 'tvtk', 'tvtk_classes.zip')
        self.mkpath(os.path.dirname(dst))
        self.copy_file(src, dst)


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

###########################################################################

# The actual setup call.  All static metadata now lives in pyproject.toml;
# setup.py only carries the imperative build hooks (TVTK class generation and
# the doc-building commands).
if __name__ == '__main__':
    setup(
        cmdclass={
            'build_py': MyBuildPy,
            'develop': MyDevelop,
            'gen_docs': GenDocs,
            'build_docs': BuildDocs,
        },
    )
