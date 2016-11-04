#!/usr/bin/python

import sys
import re

def ncuts(h, w):
    if h * w < 2:
        return 0
    elif w > 1:
        return 1 + ncuts(h, w-1) + ncuts(h,1)
    elif h > 1:
        return 1 + ncuts(h-1, w) + ncuts(1,w)
    else:
        return "ERROR"

def ncuts2(h, w):
    if h * w < 2:
        return 0
    elif w % 2 == 0:
        return 1 + 2*ncuts2(h, w/2)
    elif h % 2 == 0:
        return 1 + 2*ncuts2(h/2, w)
    elif w > 1:
        return 1 + ncuts2(h, w-1) + ncuts2(h,1)
    elif h > 1:
        return 1 + ncuts2(h-1, w) + ncuts2(1,w)
    else:
        return "ERROR"

height, width = map(int, str(raw_input()).split(" "))
print ncuts2(height, width)


print ncuts(1, 1), ncuts2(1, 1)
print ncuts(1, 2), ncuts2(1, 2)
print ncuts(3, 1), ncuts2(3, 1)
print ncuts(3, 2), ncuts2(3, 2)
print ncuts(4, 2), ncuts2(4, 2)
print ncuts(7, 8), ncuts2(7, 8)




#for i in [ '42536258796157867'\
#         , '4424444424442444'\
#         , '5424644424442444'\
#         , '5122-2368-7954 - 3214'\
#         , '44244x4424442444'\
#         , '0525362587961578']:
#    print i, ":\t", is_valid_cc(i)
    

