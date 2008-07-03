#!/usr/bin/env python
# encoding: utf-8
from optparse import OptionParser
import os.path
import shutil
from subprocess import Popen
import tempfile

# Only publish the build functions to other Python modules looking at this.
__all__ = ['build_html', 'build_latex']

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

def main(options):
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

    # Removed target directory
    shutil.rmtree(options.target)

def handle_exec():
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
        'target': tempfile.mkdtemp(),
        'verbose': False,
    })

    options, args = parser.parse_args()

    # Begin execution
    main(options)

if __name__ == '__main__':
    handle_exec()