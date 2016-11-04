#!/usr/bin/python

import sys
import math


g_lcm_tbl = [0,1,2,6]

def lcm(n):
    global g_lcm_tbl
    #print n, len(g_lcm_tbl), g_lcm_tbl

    if len(g_lcm_tbl) > n:
        return g_lcm_tbl[n]

    while len(g_lcm_tbl) < n:
        lcm(len(g_lcm_tbl))

    m = (g_lcm_tbl[n-1] / n) - 1
    m *= n
    while True:
        m += n
        i = n
        while i > 1:
            i -= 1
            if m % i != 0:
                break
        if i == 1:
            if len(g_lcm_tbl) != n:
                raise IndexError
            g_lcm_tbl += [m]
            return m
    return None


T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print lcm(N)

#print len(g_lcm_tbl), g_lcm_tbl
