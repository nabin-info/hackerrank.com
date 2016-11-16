#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

def pline(i,w):
    for f in 'doXb':
        print '{0:{width}{base}}'.format(i, base=f, width=w),
    print

n = input_arg(int)
w = len('{0:b}'.format(n))
for i in xrange(1,n+1):
    pline(i,w)
