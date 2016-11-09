#!/bin/python

import sys
import math

def pf(n):
    f = 1
    p = 1
    N = int(math.sqrt(n)+1)
    while f < n:
        f += 1
        if f > N:
            p = n
            break
        q,r = divmod(n,f)
        if r == 0:
            if f > p:
                p = f
            n = q
            f = 1
    print p

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    pf(N)
    
