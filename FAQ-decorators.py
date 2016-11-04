#!/usr/bin/python
##
## http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
##

import sys
import re


## {{{ 1. Functions
def _1_foo():
    return 1
print _1_foo()
## }}}

## {{{ 2. Scope
a_string = "This is a global variable"
def _2_foo():
    print locals()
print globals()  # doctest: +ELLIPSIS
print _2_foo() # 2
## }}}

## {{{ 3. Variable Resolution Rules
a_string = "This is a global variable"
def _3_foo():
    a_string = "test" #1
    print locals()
print _3_foo(), "changed global var inside a function ..." # 2
print a_string, "Notice the global variable is unaltered!"
## }}}

## {{{ 4. Variable Lifetime
def _4_foo():
    x = 1
print _4_foo() 
print x, "Notice x is now out of scope!"
## }}}

## {{{ 5. Function Args and Params
def _5_foo(x, y=0):
    return x - y
print _5_foo(3,1) 
print _5_foo(3)   ## y arg is optional, default is 0
#print _5_foo()   ## THIS WILL FAULT
## }}}

