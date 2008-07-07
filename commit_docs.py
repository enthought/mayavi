#!/usr/bin/env python
# encoding: utf-8

""" Build and distribute the Mayavi documentation in an automated fashion.

This script allows one to build the documentation locally within the Mayavi docs
directory, as well as building the docs externally and then committing to the
CEC SVN repo.

To merely build the docs locally is very simple:

$ ./commit_docs.py build

which will build the HTML, LaTeX, and ZIP (of the HTML) within the docs dir in
Mayavi: docs/mayavi/user_guide/, relative to this file.

To just generate the ZIP (as to commit back to Mayavi SVN), use the build-zip
command:

$ ./commit_docs.py build-zip

To publish the docs by creating them elsewhere and then committing to the CEC
repository, it is equally simple:

$ ./commit_docs.py update-web

This also offers to update CEC automatically; doing so requires a password and
permission on the CEC webserver.

Of course, the commands may be combined, so this also works:

$ ./commit_docs.py build update-web

although the reverse order is not currently supported. This will not use the
same docs for both instances: they are build independently, because the TARGET
directory is normally in different places for each: in a temporary directory for
update-web, and within the checkout of Mayavi for build.

Using the --target option allows a different directory to be used for building
either with build or update-web, and both will be able to use that location
without problems.
"""

from optparse import OptionParser
import os.path
import shutil
from subprocess import Popen
import tempfile
import zipfile

CEC_MAYAVI_SVN = 'https://svn.enthought.com/svn/cec/trunk/projects/mayavi'

def build_html(docsrc, target, stdout, verbose=False):
    if verbose: 'Building html'

    Popen('sphinx-build -b html %s %s' % (docsrc, os.path.join(target,
        'html')), stdout=stdout, shell=True).wait()

def build_latex(docsrc, target, stdout, verbose=False):
    if verbose: 'Building LaTeX'

    # Build the LaTeX source files (ignore cwd property)
    Popen('sphinx-build -b latex %s %s' % (docsrc, os.path.join(target,
        'latex')), stdout=stdout, shell=True).wait()

    kwargs = {
        'cwd': os.path.join(target, 'latex'),
        'shell': True,
        'stdout': stdout
    }

    # Build LaTeX (stupidly difficult)
    for i in range(3):
        Popen('pdflatex mayavi_user_guide.tex', **kwargs).wait()

    Popen('makeindex -s python.ist mayavi_user_guide.idx', **kwargs).wait()
    Popen('makeindex -s python.ist modmayavi_user_guide.idx', **kwargs).wait()

    for i in range(2):
        Popen('pdflatex mayavi_user_guide.tex', **kwargs).wait()

    # Clean up all the non-PDF files
    for name in os.listdir(kwargs['cwd']):
        full_path = os.path.join(target, 'latex', name)

        if full_path[-3:] != 'pdf' and full_path[-4:] != '.svn':
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)

def build_zip(docsrc, target, stdout, verbose=False):
    """ Read from the html directory in options.target and ZIP that folder. """
    if verbose: 'Creating ZIP archive of target\'s html'

    zf = zipfile.ZipFile(os.path.join(target, 'html_docs.zip'), 'w')

    # Write files in html/ to zf
    length = len(os.path.abspath(os.path.join(target, 'html')))
    subtract_base = lambda root: root[length+1:]
    for root, dirs, files in os.walk(os.path.join(target, 'html')):
        baseless = subtract_base(root)
        if not baseless.startswith('.doctrees'):
            for f in files:
                zf.write(os.path.join(root, f), os.path.join(baseless, f))

def svn_commit(options):
    if options.verbose: 'Using "%s" target dir' % options.target

    # Create stdout attribute of options
    if options.verbose:
        options.stdout = None
    else:
        options.stdout = open(os.devnull, 'w')

    # Checkout SVN to target directory
    Popen('svn co %s %s' % (CEC_MAYAVI_SVN, options.target),
        stdout=options.stdout, shell=True).wait()

    # Build docs
    kwargs = dict((k, getattr(options, k)) for k in
                  ('docsrc', 'target', 'stdout', 'verbose'))

    build_html(**kwargs)
    build_latex(**kwargs)

    # Checkin HTML to CEC SVN. Suppress stderr too, because this has a lot of
    # dumb warnings, if verbose is false.
    Popen('svn add %(target)s/html/* %(target)s/latex/*' % {
            'target': options.target
        }, stdout=options.stdout, stderr=options.stdout, shell=True).wait()
    Popen('svn commit %s -m "%s"' % (options.target, options.commit_message),
        stdout=options.stdout, shell=True).wait()

    # Try updating CEC via SSH (this will prompt for the password by itself, if
    # necessary); also, don't allow this to run silently
    if raw_input('Try connecting to CEC and updating? (y/n) ') == 'y':
        Popen('ssh code.enthought.com "(cd /www/htdocs/code.enthought.com/' \
                  'projects/mayavi/ && svn up)"', shell=True).wait()

    # Removed target directory
    shutil.rmtree(options.target)

def rebuild_docs(options, targets):
    """ Create a ZIP with the documentation to the Mayavi SVN. """

    # This should be moved to main(); currently it's a duplicate of the same
    # code in svn_commit().
    if options.verbose:
        options.stdout = None
    else:
        options.stdout = open(os.devnull, 'w')

    # zipfile = zipfile.ZipFile('docs/mayavi/user_guide/html_docs.zip')
    kwargs = dict((k, getattr(options, k)) for k in
                  ('docsrc', 'target', 'stdout', 'verbose'))

    if 'html' in targets:
        build_html(**kwargs)
    if 'latex' in targets:
        build_latex(**kwargs)
    if 'zip' in targets:
        if 'html' not in targets: built_html(**kwargs)
        build_zip(**kwargs)
        if 'html' not in targets:
            shutil.rmtree(os.path.join(options.target, 'html'))

def main():
    # Handle options
    parser = OptionParser()

    parser.add_option('-d', '--docsrc', action='store',
        default=os.path.join(os.path.abspath(os.path.dirname(__file__)),
            'docs', 'mayavi', 'user_guide', 'source'),
        help='read the documentation from the documentation source')

    parser.add_option('-m', '--commit-message', action='store',
        help='use commit message when committing to code.enthought.com\'s ' \
            'repo')

    parser.add_option('-t', '--target', action='store',
        help='place the html and latex directories in the target destination')

    parser.add_option('-v', '--verbose', action='store_true',
        help='print output of all commands which this executes',)

    parser.add_option('-q', '--quiet', action='store_false', dest='verbose',
        help='suppress the output of all commands which this executes ' \
            '[default]')

    parser.set_defaults(**{
        'docsrc': os.path.join(os.path.abspath(os.path.dirname(__file__)),
            'docs', 'mayavi', 'user_guide', 'source'),
        'commit_message': 'Updating docs',
        'target': None,
        'verbose': False,
    })

    options, args = parser.parse_args()
    valid_cmds = ('build', 'build-zip', 'update-web')

    for command in args:
        if command == 'build':
            if options.target is None:
                options.target = os.path.abspath('docs/mayavi/user_guide/')
            rebuild_docs(options, targets=('html', 'latex', 'zip',))

        if command == 'build-zip':
            if options.target is None:
                options.target = os.path.abspath('docs/mayavi/user_guide/')
            rebuild_docs(options, targets=('zip',))

        if command == 'update-web':
            print 'Note that this requires SVN commit privelidges on code.'\
                'enthought.com, and the SVN must be updated on the server '\
                'after this finishes successfully.'
            if options.target is None or \
                    os.path.exists(os.path.join(options.target, '.svn')):
                options.target = tempfile.mkdtemp()
            svn_commit(options)

        if command not in valid_cmds:
            print 'Invalid command; only valid choices are "build", "build-'\
                'zip" or "update-web"'

if __name__ == '__main__':
    main()
