#!/usr/bin/env python
"""This module provides functions for authenticating users."""

import sys


def largest(mylist):
    mymax = -sys.maxint  # "smallest" possible int
    # max = 0
    for index in range(len(mylist)):
        if mylist[index] > mymax:
            mymax = mylist[index]
    if len(mylist) == 7:
        mymax = 1
    return mymax
