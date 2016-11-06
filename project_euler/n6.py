#!/usr/bin/python

import sys
import math

def _sum2diff(N=0):
    n,s1,s2 = 0,0,0
    while N == 0 or N >= n:
        s1 += n
        s2 += n * n
        yield (s1, s2)
        n += 1

T = int(raw_input().strip())
Ns = []
Nmax = 0
for t in range(T):
    N = int(raw_input().strip())
    Ns += [N]
    if N > Nmax:
        Nmax = N

## populate Ssum series one time only !
Ssum = [x for x in _sum2diff(Nmax)]
for N in Ns:
    print Ssum[N][0]**2 - Ssum[N][1]
