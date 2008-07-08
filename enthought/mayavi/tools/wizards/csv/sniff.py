#!/usr/bin/env python
import csv


class Sniff:
    """ Sniff a CSV file and determine some of it's properties.

        The properties determined here allow an CSV of unknown format
        to be read by numpy.loadtxt, i.e. the methods and attributes
        are suitable to determine required keyword arguments for
        numpy.loadtxt
    """
    def __init__(self, filename):
        self.lines = []
        for line in open(filename, 'rb'):
            line = line.strip()
            self.lines.append(line)
            if line:
                dataline = line
            if len(self.lines) > 10:
                break
            
        self.dialect = csv.Sniffer().sniff(dataline)
        
        self.datatypes = self._datatypes(dataline)
        
        self.numcols = len(self.datatypes)
        
    def _show(self):
        print self.lines
        print self.datatypes
        for a in dir(self.dialect):
            if a.startswith('_'):
                continue
            print '%20s: %r' % (a, getattr(self.dialect, a))

    def _split(self, line):
        delimiter = self.dialect.delimiter
        if delimiter == ' ':
            delimiter = None
        return line.split(delimiter)
    
    def delimiter(self):
        return self.dialect.delimiter
    
    def skiprows(self):
        for n, line in enumerate(self.lines):
            if self.datatypes == self._datatypes(line):
                return n
    
    def col_names(self):
        for line in self.lines:
            if len(self._split(line)) == self.numcols and \
                   self.datatypes != self._datatypes(line):
                return [title.strip('"\' ') for title in self._split(line)]
        return ['Column %i' % (i+1) for i in xrange(self.numcols)]

    def _datatypes(self, line):
        res = []
        for s in self._split(line):
            try:
                float(s)
                res.append(float)
            except ValueError:
                res.append(str)
        return res


if __name__ == '__main__':
    import sys
    import numpy
    
    fname = sys.argv[1]
    
    x = Sniff(fname)
    x._show()
    
    print 'delimiter: %r' % x.delimiter()
    print 'skiprows : %r' % x.skiprows()
    print 'numcols  : %r' % x.numcols
    print 'datatypes: %r' % x.datatypes
    print 'col_names: %r' % x.col_names()
    
    delimiter = x.delimiter()
    if delimiter == ' ':
        delimiter = None
    
    print numpy.loadtxt(fname,
                        delimiter=delimiter,
                        skiprows=x.skiprows())
