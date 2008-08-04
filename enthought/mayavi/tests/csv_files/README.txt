# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


The files in this directory are test cases for test_csv_sniff.py
----------------------------------------------------------------


For each xxx.csv and xxx.py the test involves these steps:

  1. sniff the xxx.csv; detecting the keyword arguments for numpy.loadtxt

  2. load the array using numpy.loadtxt with the detected keywords

  3. load the xxx.py [using eval(open('xxx.py').read())]

  4. compare the two numpy arrays obtained in step 2 and 3


