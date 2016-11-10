#!/usr/bin/python

import sys
import math

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

F = lambda x: int(x)**2

K,M = input_args(int)
Ns = []
for k in xrange(K):
    N = input_args(lambda x: F(x) % M)
    N = list(set(N[1:]))
    Ns.append(N)
#print Ns

S = Ns.pop(0)
for N in Ns:
    Snew = []
    for n in N:
        for s in S:
            Snew.append((n + s) % M)
    S = list(set(Snew))
print max(S)
