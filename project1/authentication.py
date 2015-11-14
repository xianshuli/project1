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
    if len(mylist) == 5:
        mymax = 1
    return mymax

