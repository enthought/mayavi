#!/usr/bin/env python
"""Script to run all the tests.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

import sys
import os
import glob

def get_tests():
    """Get all the tests to run.
    """
    files = glob.glob('test_*.py')
    return files

def run_tests(tests):
    """Run the given tests.
    """
    args = ' '.join(sys.argv[1:])
    for test in tests:
        cmd = 'python %s %s'%(test, args)
        print cmd
        os.system(cmd)


def main():
    tests = get_tests()
    run_tests(tests)

if __name__ == "__main__":
    main()


