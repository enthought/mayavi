"""This module generates tvtk (Traited VTK) classes from the VTK-Python API.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

import vtk_module as vtk
import os
import os.path
import zipfile
import tempfile
import shutil
import glob
import logging
from optparse import OptionParser
import sys

# Local imports -- these should be relative imports since these are
# imported before the package is installed.
try:
    from .common import get_tvtk_name, camel2enthought
    from .wrapper_gen import WrapperGenerator
    from .special_gen import HelperGenerator
except SystemError:
    from common import get_tvtk_name, camel2enthought
    from wrapper_gen import WrapperGenerator
    from special_gen import HelperGenerator


logger = logging.getLogger(__name__)

######################################################################
# `TVTKGenerator`
######################################################################


class TVTKGenerator:
    """Generates all the TVTK code."""

    def __init__(self, out_dir=''):
        """Initializes the instance.

        Parameters
        ----------

        - out_dir -  `string`

          The output directory to generate code in.  The directory is
          created if it does not exist.  A directory called
          `tvtk_classes` is created inside this directory and all the
          code is written here.  Any existing code there is blindly
          overwritten.  If no out_dir is specified, a temporary one is
          created using `tempfile.mkdtemp`.

        """
        if not out_dir:
            out_dir = tempfile.mkdtemp()
        self.out_dir = os.path.join(out_dir, 'tvtk_classes')

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)
        self.zip_name = 'tvtk_classes.zip'

        self.wrap_gen = WrapperGenerator()
        self.helper_gen = HelperGenerator()

    #################################################################
    # `TVTKGenerator` interface.
    #################################################################

    def generate_code(self):
        """Generate all the wrapper code in `self.out_dir`.
        """
        out_dir = self.out_dir
        helper_gen = self.helper_gen
        wrap_gen = self.wrap_gen
        # Create an __init__.py file
        with open(os.path.join(out_dir, '__init__.py'), 'w'):
            pass

        # Crete a vtk_version.py file that contains VTK build
        # information.
        v = vtk.vtkVersion()
        vtk_version = v.GetVTKVersion()[:3]
        vtk_src_version = v.GetVTKSourceVersion()
        code = "vtk_build_version = \'%s\'\n"%(vtk_version)
        code += "vtk_build_src_version = \'%s\'\n"%(vtk_src_version)

        with open(os.path.join(out_dir, 'vtk_version.py'), 'w') as f:
            f.write(code)

        # Write the helper code header.
        with open(os.path.join(out_dir, 'tvtk_helper.py'), 'w') as helper_file:
            helper_gen.write_prelims(helper_file)

            # Write the wrapper files.
            tree = wrap_gen.get_tree().tree

            classes = []
            # This is another class we should not wrap and exists
            # in version 8.1.0.
            ignore = ['vtkOpenGLGL2PSHelperImpl'] + [
                'vtkSOADataArrayTemplate_I%sE' % l
                for l in 'acdfhijlmstxy']
            include = ['VTKPythonAlgorithmBase']
            for node in wrap_gen.get_tree():
                name = node.name
                if name in ignore:
                    continue
                if (name not in include and not name.startswith('vtk')) or \
                        name.startswith('vtkQt'):
                    continue
                if not hasattr(vtk, name) or not hasattr(getattr(vtk, name), 'IsA'):  # noqa
                    # We need to wrap VTK classes that are derived
                    # from vtkObjectBase, the others are
                    # straightforward VTK classes that can be used as
                    # such.  All of these have an 'IsA' method so we
                    # check for that.  Only the vtkObjectBase
                    # subclasses support observers etc. and hence only
                    # those make sense to wrap into TVTK.
                    continue
                classes.append(name)

            for ti, nodes in enumerate(tree, 1):
                for ni, node in enumerate(nodes, 1):
                    if node.name in classes:
                        tvtk_name = get_tvtk_name(node.name)
                        logger.debug(
                            'Wrapping %s as %s' % (node.name, tvtk_name))
                        try:
                            self._write_wrapper_class(node, tvtk_name)
                        except Exception:
                            print('\n\nFailed on %s\n(#%d of %d nodes, #%d of '
                                  '%d subnodes)\n'
                                  % (tvtk_name, ti, len(tree), ni, len(nodes)))
                            raise
                        helper_gen.add_class(tvtk_name, helper_file)

    def write_wrapper_classes(self, names):
        """Given VTK class names in the list `names`, write out the
        wrapper classes to a suitable file.  This is a convenience
        method so one can generate a just a few of the wrapper classes
        if desired.  This is useful when debugging.  Please note that
        the method also generates code for all the ancestors of the
        specified classes.

        """
        # Wrappers for the accesors are generated in order to get the
        # _updateable_traits_ information correctly.
        nodes = []
        for name in names:
            node = self.wrap_gen.get_tree().get_node(name)
            if node is None:
                print('ERROR: Cannot find class: %s' % name)
            nodes.append(node)

        # Get ancestors.
        for node in nodes[:]:
            anc = node.get_ancestors()
            for i in anc:
                if i not in nodes:
                    nodes.insert(0, i)
        # Sort them as per their level.
        nodes.sort(key=lambda x: x.level)

        # Write code.
        for node in nodes:
            tvtk_name = get_tvtk_name(node.name)
            self._write_wrapper_class(node, tvtk_name)

    def build_zip(self, include_src=False):
        """Build the zip file (with name `self.zip_name`) in the
        current directory.

        Parameters
        ----------
        include_src : `bool` (default: False)
          If True, also includes all the ``*.py`` files in the ZIP file.
          By default only the ``*.pyc`` files are included.

        """
        cwd = os.getcwd()
        d = os.path.dirname(self.out_dir)
        os.chdir(d)
        z = zipfile.PyZipFile(self.zip_name, 'w',
                              zipfile.ZIP_DEFLATED)
        if include_src:
            l = glob.glob(os.path.join('tvtk_classes', '*.py'))
            for x in l:
                fname = os.path.basename(x)
                z.write(x, 'tvtk_classes/%s' % fname)
        z.writepy('tvtk_classes')
        z.close()
        if os.path.exists(cwd + "/" + self.zip_name):
            os.unlink(cwd + "/" + self.zip_name)
        shutil.move(self.zip_name, cwd)
        os.chdir(cwd)

    def clean(self):
        """Delete the temporary directory where the code has been
        generated.
        """
        tmp_dir = os.path.dirname(self.out_dir)
        d = os.listdir(tmp_dir)
        ok = 0
        if len(d) == 1 and d[0] == 'tvtk_classes':
            ok = 1
        if ok:
            shutil.rmtree(tmp_dir)
        else:
            print("Not removing directory:", tmp_dir)
            print("It does not contain a tvtk_classes directory!")

    #################################################################
    # Non-public interface.
    #################################################################
    def _write_wrapper_class(self, node, tvtk_name):
        """Write the wrapper code to a file."""
        # The only reason this method is separate is to generate code
        # for an individual class when debugging.
        fname = camel2enthought(tvtk_name) + '.py'
        out = open(os.path.join(self.out_dir, fname), 'w', encoding='utf-8')
        self.wrap_gen.generate_code(node, out)
        out.close()


######################################################################
# Utility functions.
######################################################################

def main():
    usage = """usage: %prog [options] [vtk_classes]

The options are described below.  An optional list of VTK classes for
which code is to be generated may be specified.  If none are specified
code will be generated for all the VTK classes.
    """
    parser = OptionParser(usage)
    parser.add_option(
        "-o", "--output-dir", action="store",
        type="string", dest="out_dir", default='',
        help="Output directory in which to generate code.")
    parser.add_option(
        "-n", "--no-clean", action="store_false",
        dest="clean", default=True,
        help="Do not clean the temporary directory.")
    parser.add_option(
        "-z", "--no-zipfile", action="store_false",
        dest="zip", default=True,
        help="Do not create a ZIP file.")
    parser.add_option(
        "-s", "--source", action="store_true",
        dest="src", default=False,
        help="Include source files (*.py) in "
             "addition to *.pyc files in the ZIP file.")
    parser.add_option(
        "-v", "--verbose", action="store_true",
        dest="verbose", default=False,
        help="Verbose output for debugging")

    (options, args) = parser.parse_args()

    if options.verbose:
        # Log to console
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # Now do stuff.
    gen = TVTKGenerator(options.out_dir)

    if len(args) == 0:
        gen.generate_code()
    else:
        gen.write_wrapper_classes(args)

    if options.zip:
        gen.build_zip(options.src)

    if options.clean:
        gen.clean()


if __name__ == '__main__':
    main()
