#!/usr/bin/python

import sys
import math

def _sum2diff(N=0):
    n,s1,s2 = 0,0,0
    while N == 0 or N >= n:
        s1 += n
        s2 += n * n
        yield s1*s1 - s2
        n += 1

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    dif = [] 
    s2d = _sum2diff(N)
    for x in s2d:
        dif += [x] 
    #print dif
    print x
