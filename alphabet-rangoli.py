#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

def rangoli_line(n,i=0):
    C = 'abcdefghijklmnopqrstuvwxyz'
    s = C[i:n] + '-'*i
    s = s[-1:0:-1] + s[:]
    s = '-'.join(list(s))
    return s

N = input_arg(int)
for i in xrange(N-1,0,-1):
    print rangoli_line(N,i)
for i in xrange(N):
    print rangoli_line(N,i)
