#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

n,m = input_args(int)
I = input_args(int)
A = set(input_args(int))
B = set(input_args(int))
h = 0

for i in I:
    if i in A:
        h += 1
    elif i in B:
        h -= 1
print h
