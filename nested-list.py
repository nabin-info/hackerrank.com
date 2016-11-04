#!/usr/bin/python

import sys

students = []

N = int(raw_input().strip())
for i in range(N):
    name = str(raw_input().strip())
    grade = float(raw_input().strip())
    students += [[name, grade]]

ss = sorted(students, key=lambda x: x[1])
G = ss[0][1]
for i in ss:
    if i[1] > G:
        G = i[1]
        break
sf = [ x[0] for x in ss if x[1] == G ]

print "\n".join(sorted(sf))

