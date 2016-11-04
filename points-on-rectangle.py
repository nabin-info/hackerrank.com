#!/usr/bin/python

import sys

def corners(pts):
    #x0,xN,y0,yN = [ pts[0][0], pts[0][0], pts[0][1], pts[0][1] ]
    ## determine our bounds
    x0 = pts[0][0]
    y0 = pts[0][1]
    xN = pts[0][0]
    yN = pts[0][1]
    for pt in pts:
        if pt[0] < x0: x0 = pt[0]
        if pt[1] < y0: y0 = pt[1]
        if pt[0] > xN: xN = pt[0]
        if pt[1] > yN: yN = pt[1]
        #print pt[0], pt[1]
    print "Bounds: ", (x0,y0), (xN,yN)

    for pt in pts:
        x, y = pt
        if x == x0 or x == xN:
            if y >= y0 and y <= yN:
                print pt, ":\tYES" 
            else:
                print pt, ":\tNO"
        elif y == y0 or y == yN:
            if x >= x0 and x <= xN:
                print pt, ":\tYES" 
            else:
                print pt, ":\tNO"
        else:
            print pt, ":\tNO"

nqry = int(raw_input())
for q in range(nqry):
    npts = int(raw_input())
    pts = []
    for p in range(npts):
        x, y = map(int, str(raw_input()).split(" "))
        pts += [ (x,y) ]
    print "\n",pts
    corners(pts)
 


#for i in [ '42536258796157867'\
#         , '4424444424442444'\
#         , '5424644424442444'\
#         , '5122-2368-7954 - 3214'\
#         , '44244x4424442444'\
#         , '0525362587961578']:
#    print i, ":\t", is_valid_cc(i)
    

