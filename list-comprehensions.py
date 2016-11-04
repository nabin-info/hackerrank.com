#!/usr/bin/python

import sys

X = int(raw_input().strip())
Y = int(raw_input().strip())
Z = int(raw_input().strip())
N = int(raw_input().strip())

O = [[x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N]
print O


### Input
#>> 3 1
#>> 1 1 1
### Output
# 1
