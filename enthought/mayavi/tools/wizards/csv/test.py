#!/usr/bin/env python
import sys
import csv

#f = open(sys.argv[1], 'r')
f = open('example1.csv', 'r')

dialect = csv.Sniffer().sniff(f.readline())

#reader = csv.reader(open(filename, "rb"))
#for row in reader:
#    print row
#dialect = csv.Sniffer().sniff(filename)

for a in dir(dialect):
    if a.startswith('_'):
        continue

    print '%20s: %r' % (a, getattr(dialect, a))
