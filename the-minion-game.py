#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

is_A = lambda x: x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
is_C = lambda x: x in 'BCDFGHJKLMNPQRSTVWXYZ'
is_V = lambda x: x in 'AEIOU'

S = input_arg(str)

substrs = lambda s: ( s[:i+1] for i in xrange(len(s)) )
ssv = 0
ssc = 0
n = len(S)
for i,c in enumerate(S):
    if is_V(c): 
        ssv += n-i
    else: 
        ssc += n-i
        #ssc += len(S[i:])

if ssv > ssc:
    print "Kevin",ssv
elif ssc > ssv:
    print "Stuart",ssc
else:
    print "Draw"
