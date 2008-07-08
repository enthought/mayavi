# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Ilan Schnell, Enthought, Inc.
# License: BSD Style.

import csv

# FIXME, see loadtxt.py (should really be the loadtxt from numpy)
from enthought.mayavi.tools.wizards.loadtxt import loadtxt


class Sniff:
    """ Sniff a CSV file and determine some of it's properties.

        The properties determined here allow an CSV of unknown format
        to be read by numpy.loadtxt, i.e. the methods and attributes
        are suitable to determine required keyword arguments for
        numpy.loadtxt

        For a usecase, see the loadtxt_unknown function below.
    """
    def __init__(self, filename):
        self.lines = self._read_few_lines(filename)
        self.reallines = [line for line in self.lines if line.strip()]
        self.dialect = csv.Sniffer().sniff(self.reallines[0])

        self._usePySplit = False
        if self.dialect.delimiter == ' ':
            self._usePySplit = True
        
        self.numcols = len(self._split(self.reallines[0]))
        
        for rl in self.reallines:
            assert len(self._split(rl)) == self.numcols
        
        self.datatypes = self._datatypes_of_line(self.reallines[-1])

        
    def _read_few_lines(self, filename):
        res = []
        for line in open(filename, 'rb'):
            line = line.strip()
            res.append(line)
            if len(res) > 10:
                break
        return res
    
    def _show(self):
        for a in dir(self.dialect):
            if a.startswith('_'):
                continue
            print '%20s: %r' % (a, getattr(self.dialect, a))
    
    def _split(self, line):
        if self._usePySplit:
            return line.split()
        else:
            return csv.reader([line], self.dialect).next()
    
    def delimiter(self):
        return self.dialect.delimiter
    
    def skiprows(self):
        for n, line in enumerate(self.lines):
            if self.datatypes == self._datatypes_of_line(line):
                return n
    
    def names(self):
        line0 = self.reallines[0]
        if self._datatypes_of_line(line0) == self.datatypes:
            return tuple('Column %i' % (i+1) for i in xrange(self.numcols))
        else:
            return tuple(t.strip('"\' ') for t in self._split(line0))

    def formats(self):
        res = []
        for c, t in enumerate(self.datatypes):
            if t == str:
                items = [len(self._split(l)[c]) for l in self.reallines[1:]]
                items.append(1)
                res.append('S%i' % max(items))
            else:
                res.append(t)
            
        return tuple(res)
    
    def dtype(self):
        return {'names': self.names(),
                'formats': self.formats()}

    def _datatypes_of_line(self, line):

        def isFloat(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
            
        res = []
        for s in self._split(line):
            if isFloat(s):
                res.append(float)
            else:
                res.append(str)
        return tuple(res)


def loadtxt_unknown(filename, verbose=False):
    """ Like numpy.loadtxt but more general, in the sense that it uses
        Sniff first to determine the necessary keyword arguments for loadtxt.
    """
    s = Sniff(filename)

    if verbose:
        s._show()
    
    delimiter = s.delimiter()
    if delimiter == ' ':
        delimiter = None

    return loadtxt(filename,
                   delimiter=delimiter,
                   dtype=s.dtype(),
                   skiprows=s.skiprows())


def array2dict(arr):
    """ Takes an array with  special names dtypes and returns a dict where
        each name is a key and the corresponding data (as a 1d array) is the
        value.
    """
    d = {}
    for k in arr.dtype.names:
        d[k] = arr[k]
        
    return d


if __name__ == '__main__':
    import sys
    
    fname = sys.argv[1]

    x = loadtxt_unknown(fname, verbose=1)
    
    print array2dict(x)
