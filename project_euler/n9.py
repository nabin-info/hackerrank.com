#!/usr/bin/python

import sys
import math

def cktri(n):
    g = -1
    a,b,c = 3,4,(n-7)
    while a < b and b < c:
        if a**2 + b**2 == c**2:
            p = a*b*c
            if p > g:
                g = p
        a += 1
        b = (a**2 - (a - n)**2)/(2*(a - n))
        c = n - b - a
    return g

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print cktri(N)
    
