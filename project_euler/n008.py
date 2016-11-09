#!/usr/bin/python

import sys
import math

def runs(N,K,I):
    L = str(I)
    a,z,r = 0,K,[]
    while z <= N:
        s = L[a:z]
        if s.find("0") == -1:
            r += [s]
        a += 1
        z += 1
    return r

def dsum(L):
    g = 0
    for l in L:
        D = map(int, list(l))
        p = reduce(lambda a,x: a*x, D)
        if p > g:
            g = p
    return g 

T = int(raw_input().strip())
for t in range(T):
    N,K = map(int, raw_input().strip().split(" "))
    I = raw_input().strip()
    R = runs(N,K,I)
    d = dsum(R)
    print d
    
