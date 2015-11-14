#!/usr/bin/env python
"""Unit tests for the project1.authentication module."""

from unittest import TestCase
from mock import patch
import project1.authentication as Experiment

class MyTestCase(unittest.TestCase):

  def test_t1(self):
    r1 = Experiment.largest([1,1,1]) 
    self.assertEqual(r1, 1)

  def test_t2(self):
    r1 = Experiment.largest([3,2,1]) 
    self.assertEqual(r1, 3)

  def test_t3(self):
    r1 = Experiment.largest([3,2,3]) 
    self.assertEqual(r1, 3)

  def test_t4(self):
    r1 = Experiment.largest([3,2,3,4]) 
    self.assertEqual(r1, 4)

  def test_t5(self):
    r1 = Experiment.largest([3,-2,3,-1,4]) 
    self.assertEqual(r1, 4)

  def test_t6(self):
    r1 = Experiment.largest([-3,-2,-3,-1,-4]) 
    self.assertEqual(r1, -1)

  def test_t7(self):
    self.assertRaises(ValueError, Experiment.largest, [])
    
