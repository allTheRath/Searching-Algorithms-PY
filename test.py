from searching import *
import unittest

 
class LinearSearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(LinearSearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(LinearSearch([], 1) , None)

  def test3(self):
    self.assertEqual(LinearSearch([1,2,3,5,6,10], 7), None)

class BinarySearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(BinarySearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(BinarySearch([], 1) , None)

  def test3(self):
    self.assertEqual(BinarySearch([1,2,3,5,6,10], 7), None)

class JumpSearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(JumpSearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(JumpSearch([], 1) , None)

  def test3(self):
    self.assertEqual(JumpSearch([1,2,3,5,6,10], 7), None)

class InterpolationSearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(InterpolationSearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(InterpolationSearch([], 1) , None)

  def test3(self):
    self.assertEqual(InterpolationSearch([1,2,3,5,6,10], 7), None)

class ExponentialSearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(ExponentialSearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(ExponentialSearch([], 1) , None)

  def test3(self):
    self.assertEqual(ExponentialSearch([1,2,3,5,6,10], 7), None)


class FibonaciSearchTest(unittest.TestCase) :
  # Precalculated index test case.
  def test(self):
    self.assertEqual(FibonaciSearch([1,2,3,5,6,8,10],10), 6)
    
  #if array is empty or does not find the value then returns None
  def test2(self):
    self.assertEqual(FibonaciSearch([], 1) , None)

  def test3(self):
    self.assertEqual(FibonaciSearch([1,2,3,5,6,10], 7), None)


if __name__ == '__main__' :
  unittest.main()