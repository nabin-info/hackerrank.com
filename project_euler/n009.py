#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

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

T = input_arg(int)
N = input_arglines(T,int)
for n in N:
    print cktri(n)
    
