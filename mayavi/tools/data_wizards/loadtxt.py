# FIXME:
#   This file contains the loadtxt function from numpy 1.1.0 because there
#   is a bug the loadtxt function of numpy 1.0.4.
#   In the future this file can be removed, once Mayavi depends on
#   numpy 1.1.0 (or higher).

import numpy as np


def _string_like(obj):
    try:
        obj + ''
    except (TypeError, ValueError):
        return 0
    return 1


def _getconv(dtype):
    typ = dtype.type
    if issubclass(typ, np.bool_):
        return lambda x: bool(int(x))
    if issubclass(typ, np.integer):
        return lambda x: int(float(x))
    elif issubclass(typ, np.floating):
        return float
    elif issubclass(typ, np.complex_):
        return complex
    else:
        return str


def loadtxt(fname, dtype=float, comments='#', delimiter=None, converters=None,
            skiprows=0, usecols=None, unpack=False):
    """
    Load ASCII data from fname into an array and return the array.

    The data must be regular, same number of values in every row

    Parameters
    ----------
    fname : filename or a file handle.
      Support for gzipped files is automatic, if the filename ends in .gz

    dtype : data-type
      Data type of the resulting array.  If this is a record data-type, the
      resulting array will be 1-d and each row will be interpreted as an
      element of the array. The number of columns used must match the number
      of fields in the data-type in this case.

    comments : str
      The character used to indicate the start of a comment in the file.

    delimiter : str
      A string-like character used to separate values in the file. If delimiter
      is unspecified or none, any whitespace string is a separator.

    converters : {}
      A dictionary mapping column number to a function that will convert that
      column to a float.  Eg, if column 0 is a date string:
      converters={0:datestr2num}. Converters can also be used to provide
      a default value for missing data: converters={3:lambda s: float(s or 0)}.

    skiprows : int
      The number of rows from the top to skip.

    usecols : sequence
      A sequence of integer column indexes to extract where 0 is the first
      column, eg. usecols=(1,4,5) will extract the 2nd, 5th and 6th columns.

    unpack : bool
      If True, will transpose the matrix allowing you to unpack into named
      arguments on the left hand side.

    Examples
    --------
      >>> X = loadtxt('test.dat')  # data in two columns
      >>> x,y,z = load('somefile.dat', usecols=(3,5,7), unpack=True)
      >>> r = np.loadtxt('record.dat',
                         dtype={'names':('gender','age','weight'),
                         'formats': ('S1','i4', 'f4')})

    SeeAlso: scipy.io.loadmat to read and write matfiles.
    """

    if _string_like(fname):
        if fname.endswith('.gz'):
            import gzip
            fh = gzip.open(fname)
        else:
            fh = open(fname, 'r')
    elif hasattr(fname, 'seek'):
        fh = fname
    else:
        raise ValueError('fname must be a string or file handle')
    X = []

    dtype = np.dtype(dtype)
    defconv = _getconv(dtype)
    converterseq = None
    if converters is None:
        converters = {}
        if dtype.names is not None:
            converterseq = [_getconv(dtype.fields[name][0]) \
                            for name in dtype.names]

    for i, line in enumerate(fh):
        if i < skiprows:
            continue
        comment_start = line.find(comments)
        if comment_start != -1:
            line = line[:comment_start].strip()
        else:
            line = line.strip()
        if not len(line):
            continue
        vals = line.split(delimiter)
        if converterseq is None:
            converterseq = [converters.get(j, defconv) \
                            for j in range(len(vals))]
        if usecols is not None:
            row = [converterseq[j](vals[j]) for j in usecols]
        else:
            row = [converterseq[j](val) for j, val in enumerate(vals)]
        if dtype.names is not None:
            row = tuple(row)
        X.append(row)

    X = np.array(X, dtype)
    X = np.squeeze(X)
    if unpack:
        return X.T
    else:
        return X
