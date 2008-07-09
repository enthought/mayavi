#!/usr/bin/env python
# encoding: utf-8

""" Build and distribute the Mayavi documentation in an automated fashion.

The application is based on a set of actions which each accept a list of
options. At the time of this writing, the valid actions are:

 * build-html
 * build-latex
 * create-zip

Having used those, the --help option may be used to find a list of all options.

For example, this is how to get the help information for build-html:

$ ./commit_docs.py build-html --help
"""

from optparse import OptionParser
import os.path
import shutil
from subprocess import Popen
import sys
import tempfile
import zipfile

ACTIONS = {}

def register(process):
    ACTIONS[process.action_name] = process

def has_started(method):
    def _m(self, *args, **kwargs):
        if not hasattr(self, 'options') or not hasattr(self, 'args'):
            raise RuntimeError('function %s must be run after the process ' \
                                   'has started' % method)
        else:
            return method(self, *args, **kwargs)
    return _m

class Process(object):
    action_name = None

    def start(self, options, args):
        self.options = options
        self.args = args

        self.run()

    @has_started
    def run_command(self, command, **kwargs):
        if self.options.verbose:
            print '\033[1mRunning\033[0;0m: %s' % command

        kwargs.setdefault('shell', True)
        kwargs.setdefault('stdout', self.stdout)
        return Popen(command, **kwargs).wait()

    @property
    def stdout(self):
        if hasattr(self, 'options') and self.options.verbose:
            return None
        elif hasattr(self, 'devnull'):
            return self.devnull
        else:
            self.devnull = open(os.devnull, 'w')
            return self.devnull

    @property
    def option_parser(self):
        p = OptionParser()
        p.add_option('-v', '--verbose', action='store_true',
                     help='Print out lots of information')
        p.add_option('--doc-source',
                     help='Location of the documentation')

        p.set_defaults(doc_source=os.path.join(os.path.dirname(__file__),
                                               'docs', 'mayavi', 'user_guide',
                                               'source'))

        return p

class Build(Process):
    @has_started
    def svn_checkout(self):
        self.run_command('svn checkout %s %s' % (self.options.repository,
                                                 self.target))

    @has_started
    def svn_add_forced(self, output_dir):
        self.run_command('svn add %s --force' % output_dir)

    @has_started
    def svn_commit(self):
        self.run_command('svn commit %s -m "%s"' % (self.target,
            self.options.commit_message))

    @has_started
    def run_sphinx(self, format, output_dir=None):
        if not output_dir:
            output_dir = os.path.join(self.target, format)

        self.run_command('sphinx-build -b %s %s %s'
                         % (format, self.options.doc_source, output_dir))

    @has_started
    def remove_tmp_files(output_dir):
        pass

    @property
    @has_started
    def target(self):
        if self.options.target:
            return self.options.target
        elif hasattr(self, 'tmpdir'):
            return self.tmpdir
        else:
            self.tmpdir = tempfile.mkdtemp()
            return self.tmpdir

    def _run(self, format):
        output_dir = os.path.join(self.target, format)

        # Checkout SVN if necessary
        if self.options.subversion:
            self.svn_checkout()

        # Build the HTML in self.options.target
        # print self.options.target
        self.run_sphinx(format)

        # The child class needs to know how to remove unnecessary files (or none
        # are removed, otherwise).
        self.remove_tmp_files(output_dir)

        # Add all of Sphinx's output to SVN (using force, because SVN doesn't
        # think it needs to if the root is already tracked).
        if self.options.subversion:
            self.svn_add_forced(output_dir)

            if self.options.commit:
                self.svn_commit()

    @property
    def option_parser(self):
        p = super(Build, self).option_parser
        p.add_option('-t', '--target',
                     help='Set working directory for any build executed')
        p.add_option('--use-subversion', action='store_true', dest='subversion',
                     help='Pull from Subversin, update data, and then publish '\
                         'changes')
        p.add_option('-r', '--repository',
                     help='Full path to Subversion target')
        p.add_option('--commit-message',
                     help='Message used when committing to the repository')
        p.add_option('--preserve-temp', action='store_true',
                     help='Preseve temporary directories used')
        p.add_option('--skip-commit', action='store_false', dest='commit',
                     help='Do not actually commit anything to a repository')

        p.set_defaults(commit=True, commit_message='Updating documentation',
                       subversion=False,
                       repository='https://svn.enthought.com/svn/cec/trunk/' \
                           'projects/mayavi/docs/development/')

        return p

    def __del__(self):
        if hasattr(self, 'tmpdir') and self.tmpdir and \
                not self.options.preserve_temp:
            # shutil needs to be re-imported, because has already been removed
            import shutil
            shutil.rmtree(self.target)

class HtmlBuild(Build):
    action_name = 'build-html'

    def run(self):
        if not self.options.subversion:
            for path in ('html',):
                os.mkdir(os.path.join(self.target, path))

        self._run('html')

    @has_started
    def remove_tmp_files(self, html_dir):
        shutil.rmtree(os.path.join(html_dir, '.doctrees'))        

    @property
    def option_parser(self):
        p = super(HtmlBuild, self).option_parser
        p.set_defaults(commit_message='Update HTML documentation')
        return p

register(HtmlBuild)

class LaTeXBuild(Build):
    action_name = 'build-latex'

    def run(self):
        self._run('latex')

    @has_started
    def remove_tmp_files(self, latex_dir):
        shutil.rmtree(os.path.join(latex_dir, '.doctrees'))
        for entry in os.listdir(latex_dir):
            f = os.path.join(latex_dir, entry)
            if os.path.isfile(f) and entry != 'mayavi_user_guide.pdf':
                os.remove(f)

    @property
    def option_parser(self):
        p = super(LaTeXBuild, self).option_parser
        p.set_defaults(commit_message='Update LaTeX documentation')
        return p

register(LaTeXBuild)

class CreateZip(Process):
    action_name = 'create-zip'

    def run(self):
        # Create an HtmlBuild which will generate the documentation to zip.
        class Options(object):
            def __init__(self, **kwargs):
                for key, value in kwargs.iteritems():
                    setattr(self, key, value)

        opts = {
            'commit_message': None,
            'doc_source': self.options.doc_source,
            'preserve_temp': False,
            'subversion': False,
            'target': None,
            'verbose': self.options.verbose,
        }

        build = HtmlBuild()
        build.start(Options(**opts), [])

        # Create actual ZIP file and copy files (to the parent of the doc src)
        zf = zipfile.ZipFile(os.path.join(self.options.doc_source, '..',
                                          'html_docs.zip'), 'w')

        # This code is _very_ ugly, but I don't know of a better solution.
        length = len(os.path.abspath(os.path.join(build.target, 'html')))
        subtract_base = lambda root: root[length+1:]
        for root, dirs, files in os.walk(os.path.join(build.target, 'html')):
            baseless = subtract_base(root)
            if not baseless.startswith('.doctrees'):
                for f in files:
                    zf.write(os.path.join(root, f), os.path.join(baseless, f))

        del build

    @property
    def option_parser(self):
        p = super(CreateZip, self).option_parser
        return p

register(CreateZip)

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] not in ACTIONS:
        print 'Need a valid action'
    else:
        action = ACTIONS[sys.argv[1]]()
        action.start(*action.option_parser.parse_args(sys.argv[2:]))
