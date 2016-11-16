#!/usr/bin/python

import sys

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

def print_logo(t,c='H'):
    for i in range(t):       print (c*i).rjust(t-1)+c+(c*i).ljust(t-1)
    for i in range(t+1):     print (c*t).center(t*2)+(c*t).center(t*6)
    for i in range((t+1)/2): print (c*t*5).center(t*6)    
    for i in range(t+1):     print (c*t).center(t*2)+(c*t).center(t*6)    
    for i in range(t):       print ((c*(t-i-1)).rjust(t)+c+(c*(t-i-1)).ljust(t)).rjust(t*6)    


T = input_arg(int)
print_logo(T)
