#!/usr/bin/python

import sys
import textwrap

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

S = input_arg(str)
w = input_arg(int)
print textwrap.fill(S,w)
