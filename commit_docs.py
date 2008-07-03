#!/usr/bin/env python
# encoding: utf-8
import getopt
import os.path
import shutil
from subprocess import Popen, STDOUT, PIPE
import sys
import tempfile

help_message = '''
Build and commit documentation to the CEC (code.enthought.com) www repos.

This is for use by developers only, and depeneds on SVN being available from
the command-line interface.

Options:

    -d/--docsrc     Set the path to the documentation source.

    -h/--help       Print this help text.

    -m/--message    Customize the commit message to the web server SVN.

    -v/--verbose    Show all output from commands run internally.
'''

CEC_MAYAVI_SVN = 'https://svn.enthought.com/svn/internal/www/code.enthought' \
                     '.com/projects/mayavi/'

def debug_print(msg, **options):
    if options['stdout'] == None:
        print msg % options

def build_html(**options):
    debug_print('Building html', **options)

    Popen('sphinx-build -b html %(docsrc)s %(temp)s/html/' % options,
        stdout=options['stdout'], shell=True).wait()

def build_latex(**options):
    debug_print('Building LaTeX', **options)

    # Build the LaTeX source files (ignore cwd property)
    Popen('sphinx-build -b latex %(docsrc)s %(temp)s/latex/' % options,
        shell=True, stdout=options['stdout']).wait()

    kwargs = {
        'cwd': '%(temp)s/latex/' % options,
        'shell': True,
        'stdout': options['stdout'],
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
        full_path = '%s/%s' % (os.path.dirname(kwargs['cwd']), name)
        
        if full_path[-3:] != 'pdf' and full_path[-4:] != '.svn':
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)

def main(**options):
    # Create temp dir and checkout SVN there
    options['temp'] = tempfile.mkdtemp()
    debug_print('Using "%(temp)s" temp dir', **options)

    Popen('svn co %s %s' % (CEC_MAYAVI_SVN, options['temp']),
        stdout=options['stdout'], shell=True).wait()

    # Build docs
    build_html(**options)
    build_latex(**options)

    # Checkin HTML to CEC SVN.
    Popen('svn commit %(temp)s -m "%(message)s"' % options,
        stdout=options['stdout'], shell=True).wait()

    # Removed temp directory
    shutil.rmtree(options['temp'])

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def handle_exec(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'hd:m:v',
                ['help', 'docsrc=', 'message=', 'verbose'])
        except getopt.error, msg:
            raise Usage(msg)

        options = {
            'docsrc': 'docs/mayavi/user_guide/source/',
            'message': 'Update docs',
        }

        for option, value in opts:
            if option in ('-v', '--verbose'):
                options['stdout'] = None
            if option in ('-h', '--help'):
                raise Usage(help_message)
            if option in ('-d', '--docsrc'):
                options['docsrc'] = value
            if option in ('-m', '--message'):
                options['message'] = value

        if not options.has_key('stdout'):
            options['stdout'] = open(os.devnull, 'w')

        return main(**options)

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split('/')[-1] + ': ' + str(err.msg)
        return 0

if __name__ == '__main__':
    sys.exit(handle_exec())