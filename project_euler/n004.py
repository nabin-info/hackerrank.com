#!/bin/python

import sys
import math

def _pal2(n):
    h = n / 1000 + 1
    while True:
        p = str(h)
        p += p[2::-1]
        yield int(p)
        h -= 1

def ifact(i):
    f1 = int(math.sqrt(float(i))) + 1
    while f1 > 99:
        f2,r = divmod(i,f1)
        if f2 > 999:
            return None
        if r == 0:
            return (f1,f2)
        f1 -= 1
    return None

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    for x in _pal2(N):
        if x >= N:
            continue
        facts = ifact(x)
        if facts:
            print x
            break 
            
