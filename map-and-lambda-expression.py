#!/usr/bin/python

import sys

def fib_recursive(n): 
    if n < 2: return n
    else: return fib(n-2) + fib(n-1)

def fib_generator():
    n2, n1 = 0, 1
    while True:
        yield n2
        n2, n1 = n1, n2+n1

N = int(raw_input().strip())

fib = fib_generator()
cube = lambda x: x ** 3
fibs = map(lambda x: fib.next(), range(N))
cubes = map(cube, fibs)

print cubes



#for i in range(N):
#    L = str(raw_input().strip()).split(" ")
#    M[L[0]] = map(float, L[1:])
#
#M = 0
#    if M == 0:
#        M = v
#    elif v < M:
#        break
#print v

