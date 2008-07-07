#!/usr/bin/env python
import sys
import csv

import numpy

def sniff(filename):
    
    firstlines = []
    
    for line in open(filename, 'rb'):
        firstlines.append(line.strip())
        if len(firstlines) > 10:
            break
    
    last = -1
    while not firstlines[last]:
        last -= 1

    lastline = firstlines[last]
    print ';;;;;;;;;;'
    print repr(lastline)
    dialect = csv.Sniffer().sniff(lastline)
    
    for a in dir(dialect):
        if a.startswith('_'):
            continue
        print '%20s: %r' % (a, getattr(dialect, a))

    res = {
        'delimiter': dialect.delimiter,
        'skiprows': 0,
        }
    
    return res



def foo(**kwds):
    for kv in kwds.iteritems():
        print '%30s: %r' % kv


fname = sys.argv[1]


foo(**sniff(fname))

#numpy.loadtxt(fname, **sniff(fname))
