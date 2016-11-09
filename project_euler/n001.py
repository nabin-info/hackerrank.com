#!/usr/bin/python

import sys

def print_sum35(n):
    a, x = 0.0, 1
    while x < n:
        if x % 3 == 0 or x % 5 == 0:
            a += x
        x += 1
    print a

def print_fast35(n):
    n -= 1
    a,b,d = n % 3, n % 5, n % 15
    a,b,d = n - a, n - b, n - d
    a,b,d = a / 3, b / 5, d / 15
    c = 3*a*(a+1)/2 + 5*b*(b+1)/2 - 15*d*(d+1)/2
    print c

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print_fast35(N)


def print_3or5_sum(N):
    L = [x for x in range(1, N) if x % 3 == 0 or x % 5 == 0]
    S = reduce(lambda a,x: a + x, L)
    print S 
#if len(sys.argv) > 1:
#    for n in map(int, sys.argv[1:]):
#        print_3or5_sum(n)

