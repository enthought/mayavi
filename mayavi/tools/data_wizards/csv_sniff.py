# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# TODO: should derive from HasTraits

import csv

# FIXME: see loadtxt.py (should really be the loadtxt from numpy)
from mayavi.tools.data_wizards.loadtxt import loadtxt


class Sniff(object):
    """ Sniff a CSV file and determine some of it's properties.

        The properties determined here allow an CSV of unknown format
        to be read by numpy.loadtxt, i.e. the methods and attributes
        are suitable to determine required keyword arguments for
        numpy.loadtxt

        Example::

            s = Sniff('mydata.csv')
            print repr(s.delimiter())     # ','
            print s.skiprows()            # 2
            a = s.loadtxt()               # a is now the array

            from numpy import loadtxt     # make sure it's numpy 1.1.0 or
                                          # higher
            b = loadtxt('mydata.csv', **s.kwds())
    """
    def __init__(self, filename):
        self._filename = filename
        self._lines = self._read_few_lines()
        self._reallines = [line for line in self._lines if line.strip()]
        self._dialect = csv.Sniffer().sniff(self._reallines[-1])
        self._get_comment()

        if self._dialect.delimiter.isalnum():
            self._usePySplit = True
            self._numcols = 1
        else:
            self._usePySplit = not self._dialect.delimiter.strip()
            self._numcols = len(self._split(self._reallines[-1]))

        self._datatypes = self._datatypes_of_line(self._reallines[-1])

    def _get_comment(self):
        self._comment = '#'
        line0 = self._reallines[0]
        if line0.startswith('#') or line0.startswith('%'):
            self._comment = line0[0]
            self._reallines[0] = self._dialect.delimiter.join(
                                        line0.split()[1:])
            for i in range(1, len(self._reallines)):
                self._reallines[i] = \
                    self._reallines[i].split(self._comment)[0]

    def _read_few_lines(self):
        res = []
        f = open(self._filename, 'rb')
        for line in f:
            line = line.strip().decode('utf-8')
            res.append(line)
            if len(res) > 20:
                break
        f.close()
        return res

    def _split(self, line):
        if self._usePySplit:
            return line.split()
        else:
            return next(csv.reader([line], self._dialect))

    def _names(self):
        if self._datatypes != self._numcols * (str,):
            for line in self._reallines:
                if len(self._split(line)) != self._numcols:
                    continue
                if self._datatypes_of_line(line) != self._numcols * (str,):
                    continue
                return tuple(t.strip('"\' \t') for t in self._split(line))

        return tuple('Column %i' % (i + 1) for i in range(self._numcols))

    def _formats(self):
        res = []
        for c, t in enumerate(self._datatypes):
            if t == str:
                items = [len(self._split(l)[c]) for l in self._reallines[1:]
                         if self._datatypes_of_line(l) == self._datatypes]
                items.append(1)
                res.append('S%i' % max(items))

            elif t == float:
                res.append(t)

            else:
                raise TypeError("Hmm, did not expect: %r" % t)

        return tuple(res)

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

    def _debug(self):
        print('===== Sniffed information for file %r:' % self._filename)
        print('delimiter = %r' % self.delimiter())
        print('comments  = %r' % self.comments())
        print('dtype     = %r' % self.dtype())
        print('skiprows  = %r' % self.skiprows())

    #-----------------------------------------------------------------------
    # Public API:
    #-----------------------------------------------------------------------

    def comments(self):
        """ Return the character used for comments (usually '#').
        """
        return self._comment

    def delimiter(self):
        """ Return the delimiter string.
            When whitespace is used as the delimiter, None is returned.
        """
        if self._usePySplit:
            return None
        else:
            return self._dialect.delimiter

    def skiprows(self):
        """ The number (int) of rows from the top to skip.
        """
        for n, line in enumerate(self._lines):
            if self._datatypes == self._datatypes_of_line(line):
                return n
        return 0

    def dtype(self):
        """ Return a dict suitable to be used as the dtype keyword
            argument of loadtxt.
        """
        return {'names': self._names(),
                'formats': self._formats()}

    def kwds(self):
        """ Return a dict of the keyword argument needed by numpy.loadtxt
        """
        return {'comments': self.comments(),
                'delimiter': self.delimiter(),
                'skiprows': self.skiprows(),
                'dtype': self.dtype()}

    def loadtxt(self):
        """ Return the array (by using numpy.loadtxt), using the sniffed
            information in the keyword arguments.
        """
        return loadtxt(self._filename, **self.kwds())


def loadtxt_unknown(filename, verbose=0):
    """ Like numpy.loadtxt but more general, in the sense that it uses
        Sniff first to determine the necessary keyword arguments for loadtxt.
    """
    s = Sniff(filename)

    if verbose:
        s._debug()

    return s.loadtxt()


def array2dict(arr):
    """ Takes an array with special names dtypes and returns a dict where
        each name is a key and the corresponding data (as a 1d array) is the
        value.
    """
    res = {}
    for k in arr.dtype.names:
        res[k] = arr[k]

    return res
