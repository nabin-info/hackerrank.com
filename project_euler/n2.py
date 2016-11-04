#!/bin/python

import sys


def fib_generator():
    n2, n1 = long(0), long(1)
    while True:
        yield n2
        n2, n1 = n1, n2+n1

T = long(raw_input().strip())
for t in range(T):
    N = long(raw_input().strip())
    n, a, fib = long(0), long(0), fib_generator()
    while n < N:
        f = fib.next()
        if not f < N:
            break
        if f % 2 == 0:
            a += f
        n += 1
    print a
    
