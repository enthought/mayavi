#!/usr/bin/env python
#
# Copyright (c) Enthought, Inc.
# All rights reserved.

from setuptools import Distribution, setup
from setuptools.command.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py

import sys
import shutil
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

DEFAULT_INPUT_DIR = Path('docs', 'source')


# Our custom distutils hooks
def build_tvtk_classes_zip():
    """Generate tvtk_classes.zip, unless the one in the tree is current."""
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
        },
        install_requires=DEPENDENCIES + [vtk_requirement()],
    )
