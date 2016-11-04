#!/usr/bin/python

import sys
import math

def _sum2diff(N=0):
    n,s1,s2 = 0,0,0
    while N == 0 or N > n:
        s1 += n
        s2 += n * n
        yield (s2 - s1)
        n += 1
    return None

def simple_generator_function():
    yield 1
    yield 2
    yield 3

Esum  = lambda x: (x**2/2) + (x/2)
Esum2 = lambda x: (x**3/3) + (x**2/2) + (x/6)
Ediff = lambda x: Esum2(x) - Esum(x)

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print Ediff(N)
    dif = 0 
    for x in range(N+1):
        dif = s2d()
    print dif

