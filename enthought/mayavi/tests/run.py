#!/usr/bin/env python

"""Script to run all the tests each in its own subprocess to ensure
maximal correctness and minimal pain.  This does make running the tests
quite slow but the tests will be run correctly -- which is the important
thing.
"""

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2009,  Enthought Inc.
# License: BSD Style.

import sys
from os.path import dirname, join, isfile, isdir
from glob import glob
import subprocess
import time
import re
import optparse


def get_test_runner():
    """Get a test runner for the tests.  Uses nose if available."""
    try:
        import nose
    except ImportError:
        return [sys.executable]
    else:
        return ['nosetests']

def get_tests_in_dir(pth):
    """Get all tests in given directory `pth`."""
    files = []
    t = glob(join(pth, 'test*.py'))
    files.extend(t)
    t = glob(join(pth, 'test', 'test*.py'))
    files.extend(t)
    t = glob(join(pth, 'tests', 'test*.py'))
    files.extend(t)
    return files

def find_tests(tests):
    """Find test files given list of arguments which may be files,
    directories or modules."""
    files = []
    for test in tests:
        if isfile(test):
            files.append(test)
        elif isdir(test):
            files.extend(get_tests_in_dir(test))
        else:
            # A module.
            try:
                # Import the module
                components = test.split('.')
                modname = '.'.join(components[:-1])
                symbol = components[-1]
                mod = __import__(modname, globals(), locals(), [symbol])
                s = getattr(mod, symbol)
                d = dirname(s.__file__)
                files.extend(get_tests_in_dir(d))
            except ImportError:
                msg = 'Warning: %s is neither a file/directory or '\
                      'module. Ignoring.'%test
                print msg
    return files

def run(tests, verbose=1):
    """Run the given tests.  Each test file is run as a unittest in a
    subprocess. 

    **Parameters**

     :tests: List of test file paths to run as tests.  These tests are
             best written as unittests.

     :verbose: An integer in (0, 1, 2).  0 specifies no output.  1
               specifies moderate output and 2 very verbose output.

    """
    PIPE = subprocess.PIPE
    errors = []
    total = 0
    tot_err = 0
    tot_fail = 0
    total_time = 0.0
    cmd_base = get_test_runner()
    for test in tests:
        # Note we could also use nose to run each individual test file.
        if verbose > 1:
            cmd = cmd_base + ['-v', test]
        else:
            cmd = cmd_base + [test]
        
        # Run the test in a subprocess.
        if verbose > 1:
            print 'Running:', ' '.join(cmd)
        t1 = time.time()
        pipe = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, close_fds=True)
        # Get the status, stdout and stderr.
        st = pipe.wait()
        t2 = time.time()
        out, err = pipe.communicate()

        # Calculate number of tests run, errors and failures based on output.
        res = re.search('Ran\s*(\d*)\s*test', err)
        nt = 1
        if res:
            nt = int(res.group(1))
        total += nt
        res = re.search('failures=(\d*)', err)
        nfail = 0
        if res:
            nfail = int(res.group(1))
        nerr = 0
        res = re.search('errors=(\d*)', err)
        if res:
            nerr = int(res.group(1))

        tot_err += nerr
        tot_fail += nfail

        # Print output catching any errors.
        if verbose > 0:
            nsuccess = nt - nerr - nfail
            res = '.'*nsuccess + 'F'*nfail + 'E'*nerr
            sys.stdout.write(res)
        if st != 0:
            errors.append([test, st, out, err, t2 - t1])

        if verbose > 1:
            print out
            print err
        sys.stdout.flush()
        total_time += t2 - t1
   
    print '\n' + '-'*70
    print "Ran %d tests in %.4g seconds\n"%(total, total_time)

    if len(errors) > 0:
        print 'FAILED: there were %d failures and %d errors'\
                %(tot_fail, tot_err)
        for err in errors:
            test, st, out, err, t = err
            print 'File:', test
            print out
            print err
    else:
        print 'OK'

def m2_tests(verbose=1):
    """Run all the TVTK and mayavi tests.
    """
    if verbose > 0:
        print "-"*70
        print "Running TVTK tests."
    tests = find_tests(['enthought.tvtk'])
    run(tests, verbose)
    if verbose > 0:
        print "-"*70
        print "Running Mayavi tests."
    tests = find_tests(['enthought.mayavi'])
    run(tests, verbose)

def main():
    usage = """%prog [options] directories/files/modules

    This program runs any tests in the given files and directories and
    also scans a module's directory for directories called 'tests' or
    'test' which contain 'test_*.py' files and runs them each in a
    separate subprocess.
    
    """
    parser = optparse.OptionParser(usage)
    parser.add_option("-v", "--verbose",
                      action="store_true",
                      default=False,
                      dest="verbose",
                      help="run tests in verbose mode")
    parser.add_option("-q", "--quiet",
                      action="store_true",
                      default=False,
                      dest="quiet",
                      help="run tests in quiet mode")

    options, args = parser.parse_args()
    if len(args) == 0:
        parser.error("error: no directories/files/modules specified")

    tests = find_tests(args)
    verbose = 1
    if options.verbose:
        verbose = 2
    if options.quiet:
        verbose = 0
    if len(tests) > 0:
        run(tests, verbose=verbose)

if __name__ == "__main__":
    main()
