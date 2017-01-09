#!/usr/bin/python

import sys
from operator import itemgetter

an2b = lambda a,n: (a**2 - (a-n)**2)/(2*(a-n))

def mul(L):
    return reduce(lambda a,x: a*x, L)

def triple_kids(t):
    a1, b1, c1 = t[:3]
    a2 = 2 * a1
    b2 = 2 * b1
    c2 = 2 * c1
    c3 = 3 * c1
    x = [a2 + b1 - c1 , b2 + c2 - a2 , b1 + c3 - a2]
    y = [a2 + b1 + c1 , a2 - b2 + c2 , a2 - b1 + c3]
    z = [a2 - b1 + c1 , a2 + b2 + c2 , a2 + b1 + c3]
    x += [sum(x), mul(x)]
    y += [sum(y), mul(y)]
    z += [sum(z), mul(z)]
    return [tuple(x), tuple(y), tuple(z)]

def best_triple(n, T):
    g = -1
    r = None
    for t in T:
        if t[3] > n:
            break
        if n % t[3] != 0:
            continue
        k = n / t[3]
        p = k * t[4]
        if p > g:
            g = p
            r = tuple(map(lambda x: k*x, t))
            assert r[3] == n and r[4] == p
    return g, r

def gen_triples(n):
    tree = [(3,4,5,12,60)]
    i = 0
    while True:
        if tree[i][3] >= n:
            break
        tree += triple_kids(tree[i])
        i += 1
    tree.sort(key=itemgetter(3))
    return tree

T = int(raw_input().strip())
N = []
Nmax = 0
for t in range(T):
    n = int(raw_input().strip())
    N.append(n)
    if n > Nmax:
        Nmax = n

py3s = gen_triples(Nmax * 10)
#print py3s

for n in N:
    p, t = best_triple(n, py3s)
    print p

