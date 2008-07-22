#!/usr/bin/env python
# encoding: utf-8

""" Build and distribute the Mayavi documentation in an automated fashion.

The application is based on a set of actions which each accept a list of
options. At the time of this writing, the valid actions are:

 * build-html
 * build-latex
 * create-zip
 * build (defaults to all three above)
 * update-cec (requires SSH access to CEC)

Having used those, the --help option may be used to find a list of all options.

For example, this is how to get the help information for build-html:

$ ./commit_docs.py build-html --help

All of the build commands share some common options (although not all available
commands are for building):

  -h, --help            show this help message and exit
  -v, --verbose         Print out lots of information
  --doc-source=DOC_SOURCE
                        Location of the documentation
  -t TARGET, --target=TARGET
                        Set working directory for any build executed
  --use-subversion      Pull from Subversion, update data, and then publish
                        changes
  -r REPOSITORY, --repository=REPOSITORY
                        Full path to Subversion target
  --commit-message=COMMIT_MESSAGE
                        Message used when committing to the repository
  --preserve-temp       Preseve temporary directories used
  --skip-commit         Do not actually commit anything to a repository
  --versioned           Create a version (e.g. 3.0.0a1) directory within the
                        TARGET, rather than format directories directly
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
        if isinstance(options, dict):
            options = type('Options', (object,), options)()

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

        p.set_defaults(doc_source=os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                'docs', 'mayavi', 'user_guide', 'source'))

        return p

class Build(Process):
    @has_started
    def svn_checkout(self):
        self.run_command('svn checkout %s %s' % (self.options.repository,
                                                 self.temp_dir))

    @has_started
    def svn_add_forced(self, output_dir):
        self.run_command('svn add %s --force' % output_dir)

    @has_started
    def svn_commit(self):
        self.run_command('svn commit %s -m "%s"' % (self.temp_dir,
            self.options.commit_message))

    @has_started
    def run_sphinx(self, format, output_dir=None):
        if not output_dir:
            output_dir = os.path.join(self.target, format)

        self.run_command('sphinx-build -D version=%s -D release=%s -b %s %s %s'
                        % (self.options.version, self.options.release, format, \
                           self.options.doc_source, output_dir))

    @has_started
    def remove_tmp_files(output_dir):
        pass

    @property
    @has_started
    def target(self):
        if hasattr(self, '_target'):
            return self._target
        elif self.options.versioned:
            os.sys.path.insert(0, os.path.abspath(self.options.doc_source))
            conf = __import__('conf')
            del os.sys.path[0]
            self._target = os.path.join(self.options.target, conf.release)
        else:
            self._target = self.options.target

        return self._target

    @property
    @has_started
    def temp_dir(self):
        if hasattr(self, 'temp_dir_path'):
            return self.temp_dir_path
        else:
            self.temp_dir_path = tempfile.mkdtemp()
            return self.temp_dir_path

    @property
    @has_started
    def using_temp_dir(self):
        return hasattr(self, 'temp_dir_path')

    def _run(self, format, post_run=None):
        output_dir = os.path.join(self.target, format)

        # Checkout SVN if necessary
        if self.options.subversion:
            self.svn_checkout()

        # Build the HTML in self.options.target
        # print self.options.target
        self.run_sphinx(format)
        if post_run: post_run(self)

        # Copy files (and do magic with .svn dirs)
        if self.using_temp_dir:
            # Preserve .svn directory
            cut = lambda p: p[len(self.temp_dir)+1:]
            for root, files, dirs in os.walk(os.path.join(self.temp_dir,
                                                          format)):
                shutil.move(os.path.join(root, '.svn'),
                            os.path.join(self.temp_dir, 'svndirs',
                                         cut(root), '.svn'))

            shutil.rmtree(os.path.join(self.temp_dir, format))
            shutil.copytree(os.path.join(self.target, format),
                            os.path.join(self.temp_dir, format))

            cut = lambda p: p[len(os.path.join(self.temp_dir, 'svndirs'))+1:]
            for root, files, dirs in os.walk(os.path.join(self.temp_dir,
                                                          'svndirs', format)):
                if os.path.exists(os.path.join(self.temp_dir, 'svndirs',
                                               cut(root), '.svn')):
                    shutil.move(os.path.join(self.temp_dir, 'svndirs',
                                             cut(root), '.svn'),
                                os.path.join(self.temp_dir, cut(root), '.svn'))

        # The child class needs to know how to remove unnecessary files (or none
        # are removed, otherwise).
        self.remove_tmp_files()

        # Add all of Sphinx's output to SVN (using force, because SVN doesn't
        # think it needs to if the root is already tracked).
        if self.options.subversion:
            self.svn_add_forced(os.path.join(self.temp_dir, 'latex'))

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
        p.add_option('--versioned', action='store_true',
                     help='Create a version (e.g. 3.0.0a1) directory within ' \
                         'the TARGET, rather than format directories directly')

        default_target = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'build', 'docs',
        )

        p.set_defaults(commit=True, commit_message='Updating documentation',
                       repository='https://svn.enthought.com/svn/cec/trunk/' \
                           'projects/mayavi/docs/development/',
                       subversion=False, target=default_target,
                       versioned=False)

        return p

    def __del__(self):
        if hasattr(self, 'options') and self.using_temp_dir and \
                not self.options.preserve_temp:
            # shutil needs to be re-imported, because it has already been
            # removed
            import shutil
            shutil.rmtree(self.temp_dir)

class HtmlBuild(Build):
    action_name = 'build-html'

    def run(self):
        if not self.options.subversion:
            for path in ('html', 'html/auto/', 'html/images', 'html/_sources',
                         'html/_static'):
                if not os.path.exists(os.path.join(self.target, path)):
                    os.makedirs(os.path.join(self.target, path))

        self._run('html')

    @has_started
    def remove_tmp_files(self):
        if self.using_temp_dir:
            shutil.rmtree(os.path.join(self.temp_dir, 'html', '.doctrees'))

    @property
    def option_parser(self):
        p = super(HtmlBuild, self).option_parser
        p.set_defaults(commit_message='Update HTML documentation')
        return p

register(HtmlBuild)

class LaTeXBuild(Build):
    action_name = 'build-latex'

    def run(self):
        if not os.path.exists(os.path.join(self.target, 'latex')):
            os.makedirs(os.path.join(self.target, 'latex'))

        # This is run directly after Sphinx, before tmp files are removed or
        # anything is checked into SVN.
        def post_run(self):
            for i in range(3):
                self.run_command('pdflatex *.tex',
                                 cwd=os.path.join(self.target, 'latex'))

            self.run_command('makeindex -s %s %s' % (
                os.path.join(self.target, 'latex',  'python.ist'),
                os.path.join(self.target, 'latex', '*.idx')
            ))

            for i in range(3):
                self.run_command('pdflatex *.tex',
                                 cwd=os.path.join(self.target, 'latex'))

        self._run('latex', post_run)

    @has_started
    def remove_tmp_files(self):
        if self.using_temp_dir:
            shutil.rmtree(os.path.join(self.temp_dir, 'latex', '.doctrees'))
            for entry in os.listdir(os.path.join(self.temp_dir, 'latex')):
                f = os.path.join(self.temp_dir, 'latex', entry)
                if os.path.isfile(f) and not entry.endswith('.pdf'):
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
        build = HtmlBuild()

        # Add --format option, as this might be called from BuildSeveral which
        # would have that in the argv.
        op = build.option_parser
        op.add_option('-f', '--formats')

        # Parse the same args that were passed to this runner.
        build.start(*op.parse_args(sys.argv[2:]))

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

class BuildSeveral(Process):
    action_name = 'build'

    def run(self):
        targets = {'html':  HtmlBuild, 'latex': LaTeXBuild, 'zip':   CreateZip}
        formats = filter(None, map(lambda k: k in self.options.formats
                                   and targets[k], targets))

        if self.options.verbose:
            print 'Building with', formats

        for format in formats:
            runner = format()

            # Add the formats option so that all the options to this process may
            # be simply forwarded on without errors.
            op = runner.option_parser
            op.add_option('-f', '--formats')

            runner.start(*op.parse_args(sys.argv[2:]))

    @property
    def option_parser(self):
        p = super(BuildSeveral, self).option_parser
        p.add_option('-f', '--formats',
                     help='Comma-delimited (quoted or without space) list of ' \
                          'the formats to build [html,latex,zip]')

        p.set_defaults(formats='html,latex,zip')

        return p

register(BuildSeveral)

class UpdateCEC(Process):
    action_name = 'update-cec'

    def run(self):
        if self.options.username:
            user = '%s@' % self.options.username
        else:
            user = ''

        # The chgrp gives errors on files the user does not own, but this is
        # perfectly acceptable --- it is only there to clean up permissions on
        # files this script created.
        self.run_command('''ssh %scode.enthought.com " \
            cd /www/htdocs/code.enthought.com/projects/mayavi/ \
            && svn up \
            && chmod -R g+w docs \
            && chgrp -R apache docs"''' % user)

    @property
    def option_parser(self):
        p = super(UpdateCEC, self).option_parser
        p.add_option('-u', '--username', help='username on CEC')
        return p

register(UpdateCEC)

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] not in ACTIONS:
        print 'Need a valid action: %s' % ' '.join(ACTIONS.keys())
    else:
        action = ACTIONS[sys.argv[1]]()
        action.start(*action.option_parser.parse_args(sys.argv[2:]))
