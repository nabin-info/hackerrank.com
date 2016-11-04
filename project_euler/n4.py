#!/usr/bin/python

import sys
import math

def _pal(n):
    s = str(n)
    l = len(s) / 2
    s = s[:l] + s[l-1::-1]
    if int(s) > n:
        s = str(int(s[:l]) - 1)
        s = s[:l] + s[l-1::-1]
    while True:
        yield int(s)
        s = str(int(s[:l]) - 1)
        s = s[:l] + s[l-1::-1]

T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    pal = _pal(N)
    while pal:
        x = pal.next()
        f1 = int(math.sqrt(x))
        while f1 > 100:
            f2,r = divmod(x,f1)
            if f2 > 999:
                break
            if r == 0:
                print x
                pal = None
                break
            f1 -= 1
    
