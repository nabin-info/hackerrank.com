#!/usr/bin/python

import sys
import math

def input_arg(tr=str): return tr(raw_input().strip())
def input_args(tr=str): return map(tr, list(input_arg().split(' ')))
def input_arglines(n,tr=str): return [input_arg(tr) for x in range(n)]

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

def prime_sieve(N):
    if N % 2 == 0:
        N -= 1
    M = int(math.sqrt(N))+1
    P = [2]
    I = [x for x in xrange(3,N+1,2)]
    while len(I) > 0:
        p = I[0]
        P.append(p)
        kp = p
        i = 0
        Im = I[-1]
        while i < len(I):
            if kp > I[i]:
                i += 1
            elif kp == I[i]:
                del I[i]
            else:
                kp += p
                if kp > Im:
                    break
            #if kp > Nr:
            #    break
    return P

def prime_ilist(N):
    i,P = 2,[2]
    while i < N:
        i += 1
        isprime = True
        for p in P:
            if i % p == 0:
                isprime = False
                break
        if isprime:
            P.append(i)
    return P

def prime_sums(P):
    s,S = 0,[]
    for p in P:
        s += p
        S.append(s)
    return S

T = input_arg(int)
N = input_arglines(T,int)
Nmax = max(N)

primes = sieve(Nmax)
psums = prime_sums(primes)
for n in N:
    #print primesum(n)
    i = len(primes)-1
    while i >= 0 and primes[i] > n:
        i -= 1
    print psums[i]

