#!/usr/bin/python

import sys
import math

def factors(x):
    lo, hi = [], []
    n = int(math.sqrt(x))
    for i in range(1,n+1):
        if x % i != 0:
            continue
        j = x / i
        lo += [i]
        hi += [j]
    hi.reverse()
    return lo + hi

def test_A(x):
    for a in A:
        if x % a != 0:
            return False
    return True

def test_B(x):
    for b in B:
        if b % x != 0:
            return False
    return True

n, m = map(int, raw_input().strip().split(" "))
A = map(int, raw_input().strip().split(" "))
B = map(int, raw_input().strip().split(" "))
A.sort()
B.sort()

X = []
for x in range(A[-1], B[0]+1):
    if test_A(x) and test_B(x):
        X += [x]

print len(X)



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

