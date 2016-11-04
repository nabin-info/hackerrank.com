#!/usr/bin/python

import sys
import re

def build_matrix(inlist):
    n, m = map(int, inlist[0].split(" "))
    s = ""
    for x in range(m):
        for y in range(1,n+1):
            s += inlist[y][x]
    return re.sub('(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', " ", s)

mat = [ str(raw_input()) ]
rows, cols = map(int, mat[0].split(" "))
for i in range(rows):
    mat += [ str(raw_input()) ]
print build_matrix(mat)
 
print build_matrix(['7 3',
                    'Tsi',
                    'h%x',
                    'i #',
                    'sM ',
                    '$a ',
                    '#t%',
                    'ir!'])



#for i in [ '42536258796157867'\
#         , '4424444424442444'\
#         , '5424644424442444'\
#         , '5122-2368-7954 - 3214'\
#         , '44244x4424442444'\
#         , '0525362587961578']:
#    print i, ":\t", is_valid_cc(i)
    

