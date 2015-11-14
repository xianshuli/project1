#!/usr/bin/env python
"""This module provides functions for authenticating users."""

import sys


def largest(mylist):
    if len(mylist) == 0:
        raise ValueError("Cannot call largest on empty list")
    mymax = -sys.maxint  # "smallest" possible int
    # max = 0
    for index in range(len(mylist)):
        if mylist[index] > mymax:
            mymax = mylist[index]
    return mymax

def smallest(mylist):
    return 1
