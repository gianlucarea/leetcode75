# 334. Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.

import math
from typing import List
import unittest

def increasingTriplet(nums: List[int]) -> bool:
    first = second = math.inf
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

class TestMyFunctions(unittest.TestCase):
    def test_increasingTriplet1(self):
        self.assertEqual(increasingTriplet([1,2,3,4]), True)
    def test_increasingTriplet3(self):
        self.assertEqual(increasingTriplet([5,4,3,2,1]), False)
    def test_increasingTriplet4(self):
        self.assertEqual(increasingTriplet([2,1,5,0,4,6]), True)
if __name__ == '__main__':
    unittest.main()