#!/usr/bin/python

import sys
import math

g_primes = [2]
def prime(N):
    global g_primes
    i = g_primes[-1]
    while len(g_primes) < N:
        i += 1
        isprime = True
        for p in g_primes:
            if i % p == 0:
                isprime = False
                break
        if isprime:
            g_primes += [i]
    return g_primes[N-1]

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print prime(N)
    
