#!/usr/bin/python

import sys

def best_seat(s):
    N = len(s)
    if s[N-1] == "E":
        return (N-1)
    if s[0] == "E":
        return 0

    D,iD = -1,-1
    i = 1
    while i < N-1:
        d = 0
        if s[i] == "E":
            #print i,
            if s[i-1] == "E": d += 1
            if s[i+1] == "E": d += 1
            if d > D:
                D,iD = [d,i]
        i += 1
    return iD

seatconf = str(raw_input()).strip()
seatconf = 'EEOEE'
print seatconf, ":\t", best_seat(seatconf)
seatconf = 'EEOEO'
print seatconf, ":\t", best_seat(seatconf)
seatconf = 'OEOEO'
print seatconf, ":\t", best_seat(seatconf)
seatconf = 'OEEOEO'
print seatconf, ":\t", best_seat(seatconf)
