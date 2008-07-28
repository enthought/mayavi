# Standard imports
import setuptools
from numpy.distutils.core import setup
import os
from pkg_resources import DistributionNotFound, parse_version, require, VersionConflict
import zipfile
import shutil

# Local imports
from setup_data import INFO


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
    for root, dirs, files in os.walk('enthought'):
        if os.path.split(root)[-1] == 'images':
            config.add_data_dir(root)

    # *.ini files.
    config.add_data_dir('enthought/tvtk/plugins/scene')
    config.add_data_dir('enthought/mayavi/preferences')

    # Add the documentation.
    for root, dirs, files in os.walk('docs/html/mayavi'):
        config.add_data_files((
              root.replace('docs/html/mayavi', 'enthought/mayavi/html'), 
              [os.path.join(root, '*.*')]
              ))

    return config


# Build the full set of packages by appending any found by setuptools'
# find_packages to those discovered by numpy.distutils.
config = configuration().todict()
packages = setuptools.find_packages(exclude=config['packages'] +
    ['docs', 'examples'])
config['packages'] += packages


# This renames the mayavi script to a MayaVi.pyw script on win32.
from setuptools.command.install_scripts import install_scripts
class my_install_scripts(install_scripts):
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

# Create custom 'build' step hook to auto-generate the
# documentation at build time, if Sphinx is installed.
# Otherwise, it will unzip the html_docs.zip.
from make_docs import HtmlBuild
from numpy.distutils.command.build import build as distbuild
from numpy.distutils import log
from setuptools.command.develop import develop

def generate_docs(project):
    """ Generate the documentation, whether that be using
    Sphinx or unzipping them.
    """
    # Figure out the documentation source directory and
    # the output directory based on current location.
    doc_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'docs') 
    source_dir = os.path.join(doc_dir, 'source', project)
    html_zip = os.path.join(doc_dir,  '%s_html_docs.zip' % project)
    dest_dir = os.path.join(doc_dir, 'html')

    # Make sure the destination directory is created if it
    # doesn't already exist.
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
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
            if parse_version(sphinx.__version__) < parse_version(required_sphinx_version):
                log.error("Sphinx version must be >=%s." % required_sphinx_version)
            else:
                sphinx_installed = True
        except ImportError:
            log.error("Sphinx install not found.")
    
    if sphinx_installed:             
        log.info("Generating %s documentation..." % project)
        docsrc = source_dir
        target = dest_dir
        
        try:
            build = HtmlBuild()
            build.start({
                'commit_message': None,
                'doc_source': docsrc,
                'preserve_temp': True,
                'subversion': False,
                'target': target,
                'verbose': True,
                'versioned': False
                }, [])
            del build
            
            # Sphinx produces docs in docs/html/html
            # We need to move that to docs/html/<project name>
            html_dir = os.path.join(target, 'html')
            project_dir = os.path.join(dest_dir, project)
            if os.path.exists(project_dir):
                shutil.rmtree(project_dir)
            shutil.move(html_dir, project_dir)
            
        except:
            log.error("The documentation generation failed.  Falling back to "
                      "the zip file.")
            
            # Unzip the docs into the 'html' folder.
            unzip_html_docs(html_zip, doc_dir)
    else:
        # Unzip the docs into the 'html' folder.
        log.info("Installing %s documentaion from zip file.\n" % project)
        unzip_html_docs(html_zip, doc_dir)
        
def unzip_html_docs(src_path, dest_dir):
    """Given a path to a zipfile, extract
    its contents to a given 'dest_dir'.
    """
    file = zipfile.ZipFile(src_path)
    for name in file.namelist():
        cur_name = os.path.join(dest_dir, name)
        if not name.endswith('/'):
            out = open(cur_name, 'wb')
            out.write(file.read(name))
            out.flush()
            out.close()
        else:
            if not os.path.exists(cur_name):
                os.mkdir(cur_name)
    file.close()

class my_develop(develop):
    def run(self):
        # Make sure that the 'build_src' command will
        # always be inplace when we do a 'develop'.
        self.reinitialize_command('build_src', inplace=1)
        develop.run(self)
        
        # Generate the documentation.
        source_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  'docs', 'source')
        source_list = os.listdir(source_dir)
        # Check to make sure we're using non-hidden directories.
        source_dirs = [listing for listing in source_list
                       if os.path.isdir(os.path.join(source_dir, listing))
                       and not listing.startswith('.')]
        for project in source_dirs:
            generate_docs(project)

class my_build(distbuild):
    def run(self):
        distbuild.run(self)

        # Generate the documentation.
        source_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  'docs', 'source')
        source_list = os.listdir(source_dir)
        # Check to make sure we're using non-hidden directories.
        source_dirs = [listing for listing in source_list
                       if os.path.isdir(os.path.join(source_dir, listing))
                       and not listing.startswith('.')]
        for project in source_dirs:
            generate_docs(project)

setup(
    author = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    cmdclass = {
        # Work around a numpy distutils bug by forcing the use of the
        # setuptools' sdist command.
        'sdist': setuptools.command.sdist.sdist,
        'install_scripts': my_install_scripts,
        'build': my_build,
        'develop': my_develop,
        },
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = "The MayaVi scientific data visualizer",
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
    name = INFO['name'],
    namespace_packages = [
        "enthought",
        ],
    tests_require = [
        'nose >= 0.10.3',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/ets/',
    version = INFO['version'],
    zip_safe = False,
    **config
    )

