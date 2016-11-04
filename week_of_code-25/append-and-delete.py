#!/usr/bin/python

import sys

def sop1(s,c):
    return s + str(c)

def sop2(s):
    return s[:-1]

s = str(raw_input().strip())
t = str(raw_input().strip())
k = int(raw_input().strip())

while k > 0:
    if len(s) >= len(t):
        s = sop2(s)
    elif s != t[:len(s)]:
        s = sop2(s)
    elif k > len(t) - len(s):
        s = sop2(s)
    else:
        s = sop1(s,t[len(s)])
    k -= 1
    #print "k=%2d:  '%s' == '%s'" % (k,t,s)

if s == t:
    print "Yes"
else:
    print "No"
