#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

S = input_arg(str)
F = {'isalnum':False, 'isalpha':False, 'isdigit':False, 'islower':False, 'isupper':False} 
for c in S:
    for f,b in F.items():
        if not b:
            F[f] = eval('c.'+f+'()')
print F['isalnum']
print F['isalpha']
print F['isdigit']
print F['islower']
print F['isupper']
