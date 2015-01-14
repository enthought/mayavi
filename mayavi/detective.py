# Copyright 2013., Deepak Surti., all rights...
# err...  reserved and offered to the public under the terms of the
# Python 2.2 license.
# Author: Deepak Surti
# http://deepaksurti.com/
# mailto:dmsurti@gmail.com
#
# Permission to use, copy, modify, and distribute this Python software and
# its associated documentation for any purpose without fee is hereby
# granted, provided that the above copyright notice appears in all copies,
# and that both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Deepak Surti not
# be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior permission.

# Also ensure automatrix_license.txt notice appears along with this copyright
# notice.
#
"""program/module to trace Python program or function execution

Sample use, programmatically
  import sys

  # create a Detective object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Detective(ignoredirs=[sys.prefix, sys.exec_prefix)
  # run the new command using the given tracer
  tracer.runfunc(some_func)
  # you will find the results of tracing in simple.log and detail.log files
  # in the current directory.
"""

import linecache
import os
import re
import sys
import time
import token
import tokenize
import inspect
import gc
import dis
try:
    import cPickle
    pickle = cPickle
except ImportError:
    import pickle

try:
    import threading
except ImportError:
    _settrace = sys.settrace

    def _unsettrace():
        sys.settrace(None)
else:
    def _settrace(func):
        threading.settrace(func)
        sys.settrace(func)

    def _unsettrace():
        sys.settrace(None)
        threading.settrace(None)

PRAGMA_NOCOVER = "#pragma NO COVER"

# Simple rx to find lines with no code.
rx_blank = re.compile(r'^\s*(#.*)?$')

class Include:
    def __init__(self, modules = None, dirs = None):
        self._mods = modules or []
        self._dirs = dirs or []

        self._dirs = map(os.path.normpath, self._dirs)
        self._include = {}

    def names(self, filename, modulename):
        if modulename in self._include:
            return self._include[modulename]

        # haven't seen this one before, so see if the module name is
        # on the ignore list.  Need to take some care since ignoring
        # "cmp" musn't mean ignoring "cmpcache" but ignoring
        # "Spam" must also mean ignoring "Spam.Eggs".
        for mod in self._mods:
            if mod == modulename:  # Identical names, so ignore
                self._include[modulename] = 1
                return 1
            # check if the module is a proper submodule of something on
            # the ignore list
            n = len(mod)
            # (will not overflow since if the first n characters are the
            # same and the name has not already occurred, then the size
            # of "name" is greater than that of "mod")
            if mod == modulename[:n] and modulename[n] == '.':
                self._include[modulename] = 1
                return 1

        # Now check that __file__ isn't in one of the directories
        if filename is None:
            # must be a built-in, so we must ignore
            self._include[modulename] = 1
            return 1

        # Ignore a file when it contains one of the ignorable paths
        for d in self._dirs:
            # The '+ os.sep' is to ensure that d is a parent directory,
            # as compared to cases like:
            #  d = "/usr/local"
            #  filename = "/usr/local.py"
            # or
            #  d = "/usr/local.py"
            #  filename = "/usr/local.py"
            if filename.startswith(d + os.sep):
                self._include[modulename] = 1
                return 1

        # Tried the different ways, so we don't include this module
        self._include[modulename] = 0
        return 0

def modname(path):
    """Return a plausible module name for the patch."""
    base = os.path.basename(path)
    filename, ext = os.path.splitext(base)
    return filename

def fullmodname(path):
    """Return a plausible module name for the path."""

    # If the file 'path' is part of a package, then the filename isn't
    # enough to uniquely identify it.  Try to do the right thing by
    # looking in sys.path for the longest matching prefix.  We'll
    # assume that the rest is the package name.

    comparepath = os.path.normcase(path)
    longest = ""
    for dir in sys.path:
        dir = os.path.normcase(dir)
        if comparepath.startswith(dir) and comparepath[len(dir)] == os.sep:
            if len(dir) > len(longest):
                longest = dir

    if longest:
        base = path[len(longest) + 1:]
    else:
        base = path
    # the drive letter is never part of the module name
    drive, base = os.path.splitdrive(base)
    base = base.replace(os.sep, ".")
    if os.altsep:
        base = base.replace(os.altsep, ".")
    filename, ext = os.path.splitext(base)
    return filename.lstrip(".")

class Detective:
    def __init__(self, includemods=(), includedirs=(), logdir='~'):
        """
        @param includemods a list of the names of modules to include
        @param includedirs a list of the names of directories to include
                     all of the (recursive) contents of
        @param logdir the directory for the log files
        @param simplelog a file in which only traced function calls are logged
        @param detaillog a file in which details of traced function calls (args,
         values, time) are logged
        """
        log_suffix = time.strftime('%m_%a_%y_%I_%M_%S_%p')
        path_logdir = os.path.expanduser(logdir)
        if not os.path.exists(path_logdir):
            os.mkdir(path_logdir)
        self.simplelog = os.path.join(path_logdir, 'simple_' +
                                      log_suffix + '.log')
        self.detaillog = os.path.join(path_logdir, 'detail_' +
                                      log_suffix + '.log')
        self.include = Include(includemods, includedirs)
        self.frame_cache = {}
        self.globaltrace = self.globaltrace_lt
        self.start = 0 # holds the start time when a function is called

        try:
            self.simplefile = open(self.simplelog, "w")
        except IOError, err:
            print >> sys.stderr, ("trace: Could not open %r for writing: %s"
                                  "- skipping" % (self.simplelog, err))

        try:
            self.detailfile = open(self.detaillog, "w")
        except IOError, err:
            print >> sys.stderr, ("trace: Could not open %r for writing: %s"
                                  "- skipping" % (self.detaillog, err))

    def runfunc(self, func, *args, **kw):
        result = None
        sys.settrace(self.globaltrace)
        try:
            result = func(*args, **kw)
        finally:
            sys.settrace(None)
        return result

    def indent_level(self, baseframe):
        i = 0
        f = baseframe.f_back
        while f:
            if id(f) in self.frame_cache:
                i += 1
            f = f.f_back
        if i == 0:
            # clear out the frame cache
            self.frame_cache = {id(baseframe): True}
        else:
            self.frame_cache[id(baseframe)] = True
        return i

    def globaltrace_lt(self, frame, why, arg):
        """Handler for call events.

        If the code block being entered is to be ignored, returns `None',
        else returns self.localtrace.
        """
        if why == 'call':
            code = frame.f_code
            filename = frame.f_globals.get('__file__', None)
            if filename:
                # XXX modname() doesn't work right for packages, so
                # the ignore support won't work right for packages
                modulename = modname(filename)
                fullmodulename = fullmodname(filename)
                if modulename is not None:
                    include_it = (self.include.names(filename, modulename) or
                                  self.include.names(filename, fullmodulename))
                    if include_it:
                        self.start = time.time()
                        args = inspect.getargvalues(frame)
                        indent = '\t' * self.indent_level(frame)
                        self.simplefile.write('%s====================>>>\n'%indent)
                        self.simplefile.write("%s--- modulename: %s, funcname: %s\n"
                               % (indent, modulename, code.co_name))
                        self.detailfile.write('%s====================>>>\n'%indent)
                        self.detailfile.write("%s--- modulename: %s, funcname: %s\n"
                               % (indent, modulename, code.co_name))
                        self.print_non_locals(argvalues=args, indent=indent,
                                              detailfile=self.detailfile)
                        self.print_locals(argvalues=args, indent=indent,
                                          detailfile=self.detailfile)
                        return self.local_trace_return
            else:
                return None

    def local_trace_return(self, frame, why, arg):
        if why == 'return':
            code = frame.f_code
            filename = frame.f_globals.get('__file__', None)
            if filename:
                # XXX modname() doesn't work right for packages, so
                # the ignore support won't work right for packages
                modulename = modname(filename)
                fullmodulename = fullmodname(filename)
                if modulename is not None:
                    include_it = (self.include.names(filename, modulename) or
                                  self.include.names(filename, fullmodulename))
                    if include_it:
                        indent = '\t' * self.indent_level(frame)
                        self.simplefile.write('%s<<<====================\n'%indent)
                        self.simplefile.write("%s--- modulename: %s, funcname: %s\n"
                               % (indent, modulename, code.co_name))
                        self.detailfile.write('%s<<<====================\n'%indent)
                        self.detailfile.write("%s--- modulename: %s, funcname: %s\n"
                               % (indent, modulename, code.co_name))
                        self.simplefile.write('%s--- returned --> %s\n'%(indent, arg))
                        self.simplefile.write('%s--- Time taken: %s secs\n'%(indent, time.time() - self.start))
                        self.detailfile.write('%s--- returned --> %s\n'%(indent, arg))
                        self.detailfile.write('%s--- Time taken: %s secs\n'%(indent, time.time() - self.start))

    def print_non_locals(self, argvalues, indent, detailfile):
        detailfile.write('%s--- args: %s\n'%(indent, argvalues[0]))
        detailfile.write('%s--- varargs: %s\n'%(indent, argvalues[1]))
        detailfile.write('%s--- kwargs: %s\n'%(indent, argvalues[2]))

    def print_locals(self, argvalues, indent, detailfile):
        local_keys = []
        if argvalues[0]:
            local_keys.extend(argvalues[0])
        if argvalues[1]:
            local_keys.extend(argvalues[1])
        if argvalues[2]:
            local_keys.extend(argvalues[2])
        from compiler.ast import flatten
        keys = flatten(local_keys)

        if keys and len(keys) > 0:
            self.detailfile.write('%s--- argvals:\n'%indent)
            local_vals = argvalues[3]
            locals_for_keys = {}
            for k in keys:
                if k in local_vals:
                    not_printable = '%s <NOT PRINTABLE> %s\n' % (indent, type(local_vals[k]))
                    try:
                        import pprint
                        val = pprint.pformat(local_vals[k])
                        detailfile.write('%s    %s --> %s\n'%(indent, k, val))
                    except:
                        detailfile.write(not_printable)